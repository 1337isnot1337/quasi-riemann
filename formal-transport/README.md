# Transport fork for the conditional 0.87 geometry

This is a fork of nine modules from tracker commit
`fc2f46afbfda62351055d3c12fcacd4f6916cc63`, with inherited authorship and
Apache-2.0 notices retained in `source.patch`. It admits the rational geometry in
`Geometry.lean` and broadens the generic analytic transport. It does not supply
the improved row count, or prove a new zero-free half-plane.

The patch makes these changes:

- Broaden `BoundsN` to theta>0.869, h>0.781, y>0.408, ell<0.187 and
  smallSaving>6/125. The 0.87 instance proves every field, including the floor
  margin, without adding an axiom.
- Reduce the geometric loss allowance from 1/20 to 1/25. The smaller allowance
  preserves the positive saving after lowering the smallSaving cutoff.
- Relax the schedule's lower switch restriction from 3/4 to 2/3. The exact
  conditional exponent certificate uses switch 7/10; source-selection helpers
  still operate above d=1/2.
- Weaken two internal local Euler-factor estimates from Q^(-2.19) to Q^(-2.17)
  and from Q^(-0.77) to Q^(-0.76). Their products still give the existing final
  defect estimate 240 Q^(-1.7).
- Use the broader lower bound for y in the two high-transport signal checks.

The inherited comments describe earlier forks. The current changes are the
nine-file patch above; no upstream checkout is modified by this repository.

The recorded replay passes the high-transport target over 3,078 modules, of
which 2,923 match the signed cache. All remaining modules were compiled locally;
`results/transport-087-lean.json` distinguishes fresh and reused local products.
The three geometry declarations, three transport statements and three inherited
analytic inputs in `Audit.lean` report only `propext`, `Classical.choice` and `Quot.sound`.

## Reproduction

Use an isolated project directory. Python 3.11+, Node, Git, patch, OpenSSL and
Lean 4.34.1 are required. The commands below assume shell variables `tracker`
(the exact tracker checkout), `project` (a new directory), `research` (this
repository), and `lake` (the absolute Lean 4.34.1 Lake executable). Do not point
`project` at an existing checkout.

Prepare immutable source using the official tracker collector:

```sh
mkdir "$project"
printf '{}\n' > "$project/empty-libraries.json"
node "$tracker/verifier/standard/prepare.mjs" \
  --checkout "$tracker" --head fc2f46afbfda62351055d3c12fcacd4f6916cc63 \
  --repository GTimG/QuasiRiemannTracker --id positive-reserve-selected-gap \
  --source-commit fc2f46afbfda62351055d3c12fcacd4f6916cc63 \
  --bound 8733819666133/10000000000000 \
  --libraries "$project/empty-libraries.json" --out "$project/prepared"
cp -a "$project/prepared/submission/src/Candidate" "$project/Candidate"
chmod -R u+w "$project/Candidate"
ln -s "$project/prepared/submission/src/Submissions" "$project/Submissions"
(cd "$project" && patch --batch -p1 -i "$research/formal-transport/source.patch")
cp "$tracker/verifier/standard/lakefile.lean" "$project/lakefile.lean"
printf '\nlean_lib Transport087\n' >> "$project/lakefile.lean"
cp "$tracker/verifier/standard/lake-manifest.json" "$project/lake-manifest.json"
printf 'leanprover/lean4:v4.34.1\n' > "$project/lean-toolchain"
```

Provision only the Lean source dependencies, following the dependency part of
`verifier/actions/setup.py`. This avoids installing the separate leaderboard
judging environment. The following code clones each manifest revision and
applies the two official Lean 4.34.1 compatibility patches:

```sh
python - "$tracker" "$project" <<'PY'
import json, subprocess, sys
from pathlib import Path
tracker, project = map(Path, sys.argv[1:])
for package in json.loads((project/'lake-manifest.json').read_text())['packages']:
    name = package['name'].strip('«»')
    path = project/'.lake/packages'/name
    subprocess.run(['git', 'init', str(path)], check=True)
    subprocess.run(['git', '-C', str(path), 'fetch', '--depth=1', package['url'], package['rev']], check=True)
    subprocess.run(['git', '-C', str(path), 'checkout', '--detach', 'FETCH_HEAD'], check=True)
    if name in ['rellich-kondrachov', 'PrimeNumberTheoremAnd']:
        patch = tracker/'verifier/actions/patches'/(name+'-lean4341.patch')
        subprocess.run(['git', '-C', str(path), 'apply', str(patch)], check=True)
PY
(cd "$project" && "$lake" exe cache get)
(cd "$project" && "$lake" build PrimeNumberTheoremAnd.Wiener \
  RellichKondrachov.Analysis.FunctionalSpaces.Sobolev.Euclidean.Rellich)
python "$research/formal-transport/replay.py" --tracker "$tracker" \
  --work "$project" --lean "$(dirname "$lake")/lean" --jobs 4
```

The replay validates the pristine collector output, reconstructs the published
patch, rejects undocumented source changes, checks the compiler pin, hashes the
actual library products, then builds the target's source dependency closure.
It also checks `Geometry.lean` and prints its axiom dependencies. Logs and a
scoped JSON receipt stay in the isolated project. Incremental outputs are reused
only when their source/dependency key and all compiler-product hashes match.

An optional `--cache DIR` accepts the official signed build archive plus
`cache.json` and `cache.sig` obtained from the tracker's
`submission-build-cache-v1` release. The signature, archive digest and
compiler/library environment are checked before selecting matching modules.
This is only a Lean compilation optimization. No Comparator, NanoDa, con-ron or
leaderboard verifier is invoked by this replay.
