"""Prepare fictional A/B and separate synthetic mutation; immutable local copies."""
import hashlib,json,shutil,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
out=Path(sys.argv[1]).resolve()
out.mkdir(parents=True,exist_ok=False)
manifest={}
for variant,patches in [('A',[]),('B',['direction-b.css']),('S',['direction-b.css','sabotage.css'])]:
    target=out/variant;shutil.copytree(HERE/'fixture',target)
    with (target/'styles.css').open('a') as f:
        for patch in patches:f.write('\n'+(HERE/patch).read_text())
    manifest[variant]={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(target.iterdir()) if p.is_file()}
for variant in ['B','S']:
    assert {k for k in manifest['A'] if manifest['A'][k]!=manifest[variant][k]}=={'styles.css'}
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(out)
