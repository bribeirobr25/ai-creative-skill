"""Freeze one delivery: copy <run>/<round> to <frozen>/<run>-<round> and write per-file SHA-256.
usage: python3 freeze.py <runs_root> <frozen_root> <run> <round>"""
import hashlib,json,shutil,sys,pathlib
runs,fz,run,rnd=pathlib.Path(sys.argv[1]),pathlib.Path(sys.argv[2]),sys.argv[3],sys.argv[4]
src=runs/run/rnd;dst=fz/f"{run}-{rnd}"
if dst.exists():raise SystemExit(f"{dst} already frozen")
shutil.copytree(src,dst)
h={str(p.relative_to(dst)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dst.rglob('*')) if p.is_file()}
(fz/f"{run}-{rnd}.hashes.json").write_text(json.dumps(h,indent=1))
for extra in ("execution.md","execution-r1.md",f"web-delivery-{rnd}.json"):
    if (runs/run/extra).exists():shutil.copy(runs/run/extra,fz/f"{run}-{rnd}-{extra}")
print(dst,len(h),'files')
