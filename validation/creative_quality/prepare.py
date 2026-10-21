"""Create isolated B/C copies. Never overwrite input/output or copy into public Git."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent

def manifest(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("original", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    original, destination = args.original.resolve(), args.destination.resolve()
    repository = HERE.parents[1]
    if destination == repository or repository in destination.parents:
        raise ValueError("Private experiments must remain outside the public checkout")
    if original == destination or original in destination.parents:
        raise ValueError("Output cannot be inside original")
    for p in original.rglob("*"):
        if p.is_symlink():
            raise ValueError("Resolve/review source symlinks before experiment")
    before = manifest(original)
    destination.mkdir(parents=True, exist_ok=False)
    records = {}
    for name, patches in (("B", ["direction-b.css"]), ("C", ["direction-b.css", "repair-c.css"])):
        target = destination / name
        shutil.copytree(original, target)
        with (target / "styles.css").open("a") as f:
            for patch in patches:
                f.write("\n" + (HERE / patch).read_text())
        after = manifest(target)
        changed = sorted(k for k in before if before[k] != after[k])
        assert changed == ["styles.css"], changed
        records[name] = {"files": after, "changed": changed,
                         "patches": {p: hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in patches}}
    assert manifest(original) == before
    (destination / "experiment-manifest.json").write_text(json.dumps({
        "original": before, "versions": records, "paid_generation_calls": 0,
        "preservation": "all source bytes except isolated stylesheet unchanged",
        "quality_approval": "UNVERIFIED"
    }, indent=2))

if __name__ == "__main__":
    main()
