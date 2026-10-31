#!/usr/bin/env python3
"""Fetch only hash-pinned public sources; never execute downloaded content."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkout", type=Path,
                        help="verify a local upstream checkout instead of downloading")
    args = parser.parse_args()
    lock = json.loads((ROOT / "sources.lock.json").read_text())
    for item in lock["files"]:
        rel = Path(item["path"])
        if rel.is_absolute() or ".." in rel.parts:
            raise ValueError("unsafe path in source lock")
        path = (args.checkout if args.checkout else ROOT / ".sources") / rel
        if args.checkout:
            data = path.read_bytes()
        elif path.exists():
            data = path.read_bytes()
        else:
            url = ("https://raw.githubusercontent.com/" + lock["repository"]
                   + "/" + lock["commit"] + "/" + rel.as_posix())
            with urllib.request.urlopen(url, timeout=45) as response:
                data = response.read()
            if hashlib.sha256(data).hexdigest() != item["sha256"]:
                raise ValueError(f"source hash mismatch: {rel}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            raise ValueError(f"source hash mismatch: {rel}")
    print(f"Verified {len(lock['files'])} source hashes at {lock['commit']}.")


if __name__ == "__main__":
    main()
