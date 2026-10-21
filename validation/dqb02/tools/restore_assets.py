"""Restore the shared photos and fonts into each preserved DQB-02 site so it opens locally.

Sites were committed without their byte-identical copies of shared/assets-* and
shared/fonts (verified by SHA-256 against each run's rN.hashes.json).
usage: python3 validation/dqb02/tools/restore_assets.py
"""
import hashlib, json, pathlib, shutil
ROOT = pathlib.Path(__file__).resolve().parents[1]
for hfile in sorted(ROOT.glob("runs/*/r?.hashes.json")):
    rec = json.loads(hfile.read_text()); site = hfile.with_suffix("").with_suffix("")
    assets = ROOT / "shared" / ("assets-b1" if rec["run"].startswith("m") else "assets-b2")
    for rel, digest in rec["file_hashes"].items():
        if rel.split("/")[0] not in ("assets", "fonts"):
            continue
        src = (assets / rel.split("/", 1)[1]) if rel.startswith("assets/") else (ROOT / "shared" / rel)
        dst = site / rel; dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        assert hashlib.sha256(dst.read_bytes()).hexdigest() == digest, rel
    print("restored", site.relative_to(ROOT))
