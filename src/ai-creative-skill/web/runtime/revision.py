"""PRESERVE/VARY regression check. Source stability, not pixel-perfect browser assurance."""
from pathlib import Path
import hashlib,json
from bs4 import BeautifulSoup

def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def snapshot(root,regions):
    root=Path(root);html=(root/'index.html').read_text();soup=BeautifulSoup(html,'html.parser')
    result={'sections':{},'global_files':{}}
    for name in regions:
        if name=='hero':element=soup.select_one('section.hero')
        else:element=soup.find(id=name)
        if element is None:raise ValueError('Region not found '+name)
        result['sections'][name]=digest(str(element))
    for file in ['styles.css','app.js']:
        p=root/file
        if p.is_file():result['global_files'][file]=hashlib.sha256(p.read_bytes()).hexdigest()
    return result

def compare(before_root,after_root,preserved,changed):
    b=snapshot(before_root,preserved+changed);a=snapshot(after_root,preserved+changed)
    preserved_diffs=[r for r in preserved if b['sections'][r]!=a['sections'][r]]
    changed_missing=[r for r in changed if b['sections'][r]==a['sections'][r]]
    globals_changed=[f for f in sorted(set(b['global_files']) | set(a['global_files'])) if b['global_files'].get(f)!=a['global_files'].get(f)]
    return {'protected_regions_unchanged':not preserved_diffs,'preservation_failures':preserved_diffs,'target_regions_unchanged':changed_missing,'shared_css_js_changed':globals_changed,'browser_retest_required':bool(globals_changed),'human_approval_not_inferred':True,'status':'FAIL' if preserved_diffs or changed_missing else ('PARTIAL' if globals_changed else 'SOURCE_PRESERVATION_PASS')}
