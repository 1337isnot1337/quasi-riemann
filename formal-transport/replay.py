#!/usr/bin/env python3
"""Replay the documented transport fork in an already provisioned Lean project."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import threading

PIN = 'fc2f46afbfda62351055d3c12fcacd4f6916cc63'
TARGET = 'Candidate.Local.Qrh.JointDetector.BoundaryPhysical.Transport.FinalFixedHigh'
HERE = Path(__file__).resolve().parent


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def run(*args, **kwargs):
    return subprocess.run(list(map(str, args)), check=True, **kwargs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tracker', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--lean', type=Path, required=True)
    parser.add_argument('--target', default=TARGET)
    parser.add_argument('--jobs', type=int, default=4)
    parser.add_argument('--cache', type=Path, help='Directory containing the upstream signed cache index, signature and archive')
    args = parser.parse_args()
    tracker, work, lean = args.tracker.resolve(), args.work.resolve(), args.lean.resolve()
    head = subprocess.check_output(['git', '-C', str(tracker), 'rev-parse', 'HEAD'], text=True).strip()
    if head != PIN or not 1 <= args.jobs <= 16:
        raise ValueError('Wrong tracker revision or invalid job count')
    run('git', '-C', tracker, 'diff', '--quiet', 'HEAD', '--', 'verifier', 'core')
    sys.path.insert(0, str(tracker/'verifier'))
    from standard.build_cache import build_inputs, compatibility_error, restore_cache
    from standard.compile import compile_modules

    contract = json.loads((work/'prepared/contract.json').read_text())
    if contract['source_commit'] != PIN:
        raise ValueError('Prepared source pin differs')
    original = work/'prepared/submission/src'
    patch = HERE/'source.patch'
    changed = [line[6:] for line in patch.read_text().splitlines() if line.startswith('--- a/')]
    # Reconstruct the published patch independently before accepting the working fork.
    with tempfile.TemporaryDirectory(prefix='transport-patch-') as tmp:
        stage = Path(tmp)
        for name in changed:
            destination = stage/name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original/name, destination)
        run('patch', '--batch', '-p1', '-i', patch, cwd=stage, stdout=subprocess.DEVNULL)
        for name in changed:
            if (stage/name).read_bytes() != (work/name).read_bytes():
                raise ValueError('Working source differs from published patch: '+name)
    changed = set(changed)
    for name, digest in contract['source_files'].items():
        if not name.startswith('src/'):
            continue
        relative = name[4:]
        if sha(original/relative) != digest:
            raise ValueError('Prepared source changed: '+relative)
        if relative not in changed and sha(work/relative) != digest:
            raise ValueError('Undocumented working source change: '+relative)

    dependencies = contract['module_dependencies']
    closure = set()
    def visit(module):
        if module not in closure:
            closure.add(module)
            for dependency in dependencies[module]:
                visit(dependency)
    visit(args.target)
    contract['build_order'] = [m for m in contract['build_order'] if m in closure]
    contract['module_dependencies'] = {m: dependencies[m] for m in contract['build_order']}
    for module in closure:
        relative = module.replace('.', '/')+'.lean'
        contract['source_files']['src/'+relative] = sha(work/relative)
    libraries = sorted(p.resolve() for p in (work/'.lake/packages').glob('*/.lake/build/lib/lean') if p.is_dir())
    inventory = {str(p): sha(p) for library in libraries for p in library.rglob('*')
                 if p.is_file() and p.name.endswith(('.olean', '.olean.private', '.olean.server', '.so', '.ir', '.ir.sig'))}
    pinned_tools = json.loads((tracker/'verifier/standard/tool-pins.json').read_text())
    if sha(lean) != pinned_tools['source_lean']:
        raise ValueError('Lean compiler differs from the pinned binary')
    inputs = build_inputs(contract, {'libraries': list(map(str, libraries))}, inventory,
                          {'source_lean': sha(lean)})
    output = work/'replay-lib'
    output.mkdir(exist_ok=True)
    selected = set()
    if args.cache:
        cache = args.cache.resolve()
        run('openssl', 'pkeyutl', '-verify', '-pubin', '-inkey',
            tracker/'verifier/standard/build-cache-public.pem', '-rawin',
            '-in', cache/'cache.json', '-sigfile', cache/'cache.sig')
        index = json.loads((cache/'cache.json').read_text())
        if (index.get('archive') != index.get('sha256', '')+'.tar.gz'
                or len(index.get('sha256', '')) != 64):
            raise ValueError('Invalid signed archive name')
        archive = cache/index['archive']
        if sha(archive) != index['sha256'] or archive.stat().st_size != index['size']:
            raise ValueError('Signed cache archive checksum differs')
        if error := compatibility_error(index, inputs):
            raise ValueError(error)
        with tempfile.TemporaryDirectory(dir=work, prefix='replay-cache-') as tmp:
            stage = Path(tmp)/'lib'
            selected = restore_cache(archive, stage, inputs)
            for source in stage.rglob('*'):
                if source.is_file():
                    destination = output/source.relative_to(stage)
                    if destination.exists():
                        if sha(destination) != sha(source):
                            raise ValueError('Conflicting authenticated output: '+str(destination))
                    else:
                        destination.parent.mkdir(parents=True, exist_ok=True)
                        source.rename(destination)
        print('Authenticated cached modules:', len(selected), flush=True)
    logs = work/'replay-logs'
    logs.mkdir(exist_ok=True)
    environment = {**os.environ, 'LEAN_PATH': ':'.join(map(str, [output, *libraries]))}
    record_path = work/'replay-modules.json'
    records = json.loads(record_path.read_text()) if record_path.exists() else {}
    lock = threading.Lock()
    compiled = []
    reused = []
    def products(module):
        base = output/(module.replace('.', '/')+'.olean')
        return {str(p.relative_to(output)): sha(p) for p in
                [base, Path(str(base)+'.private'), Path(str(base)+'.server')] if p.is_file()}
    def compile_one(module, threads):
        if module in selected:
            return
        if (module in records and records[module]['key'] == inputs['modules'][module]
                and records[module]['products'] == products(module)):
            reused.append(module)
            return
        relative = module.replace('.', '/')
        destination = output/(relative+'.olean')
        destination.parent.mkdir(parents=True, exist_ok=True)
        print('Compile', module, flush=True)
        result = subprocess.run([str(lean), f'-j{threads}', '-o', str(destination), relative+'.lean'],
                                cwd=work, env=environment, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        (logs/(module+'.log')).write_text(result.stdout)
        if result.returncode:
            raise RuntimeError(module+' failed:\n'+result.stdout[-5000:])
        with lock:
            records[module] = {'key': inputs['modules'][module], 'products': products(module)}
            compiled.append(module)
            record_path.write_text(json.dumps(records, sort_keys=True)+'\n')
    compile_modules(contract['build_order'], contract['module_dependencies'], compile_one, jobs=args.jobs)
    geometry_dir = work/'Transport087'
    geometry_dir.mkdir(exist_ok=True)
    shutil.copyfile(HERE/'Geometry.lean', geometry_dir/'Geometry.lean')
    geometry_output = output/'Transport087/Geometry.olean'
    geometry_output.parent.mkdir(parents=True, exist_ok=True)
    run(lean, '-o', geometry_output, 'Transport087/Geometry.lean', cwd=work, env=environment)
    if args.target == TARGET:
        shutil.copyfile(HERE/'GaussianLog.lean', geometry_dir/'GaussianLog.lean')
        gaussian_output = output/'Transport087/GaussianLog.olean'
        gaussian = subprocess.check_output([str(lean), '-o', str(gaussian_output),
                                           'Transport087/GaussianLog.lean'],
                                          cwd=work, env=environment, text=True)
        (work/'replay-gaussian-axioms.txt').write_text(gaussian)
        print(gaussian)
        if 'sorryAx' in gaussian:
            raise ValueError('Gaussian profile proof contains sorryAx')
        shutil.copyfile(HERE/'Audit.lean', geometry_dir/'Audit.lean')
        audit = subprocess.check_output([str(lean), 'Transport087/Audit.lean'], cwd=work,
                                        env=environment, text=True)
        (work/'replay-axioms.txt').write_text(audit)
        print(audit)
        if 'sorryAx' in audit:
            raise ValueError('Axiom audit contains sorryAx')
    receipt = {'upstream_source': PIN, 'target': args.target, 'source_closure': len(closure),
               'environment': inputs['environment'], 'patch_sha256': sha(patch),
               'geometry_sha256': sha(HERE/'Geometry.lean'),
               'gaussian_log_sha256': sha(HERE/'GaussianLog.lean'),
               'gaussian_log_checked': args.target == TARGET, 'source_compiled_this_run': compiled, 'source_reused_modules': sorted(reused),
               'authenticated_cached_modules': len(selected),
               'scope': 'Lean source build and geometry admission; no improved bound theorem; independent kernels not run'}
    (work/'replay-receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
