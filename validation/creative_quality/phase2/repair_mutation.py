"""Undo only the declared mutation in an isolated R copy; R is not design C."""
import hashlib,shutil,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
root=Path(sys.argv[1]).resolve();source=root/'S';target=root/'R'
patch='\n'+(HERE/'sabotage.css').read_text();css=(source/'styles.css').read_text()
if not css.endswith(patch):raise ValueError('Declared mutation suffix not found')
shutil.copytree(source,target)
(target/'styles.css').write_text(css[:-len(patch)])
for f in (root/'B').iterdir():
    if f.is_file():assert f.read_bytes()==(target/f.name).read_bytes(),f.name
print('R exactly restores B; S retained; no new creative candidate C')
