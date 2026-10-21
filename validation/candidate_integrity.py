"""Candidate content inventory, separate from the immutable V2.5 release attestation."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RELEASE_REF='39a0bfa39270ea4b685b0f862e7dbf647cf81d77'
HARNESS_REF='b70b8839022372cd71a26c6d48f9e342468a7318'
CANDIDATE=ROOT/'validation/candidates/boundary-hardening-v1'
ALLOWED_CHANGES={
 'scripts/validate_deliverable.py','web/runtime/preview.py','web/runtime/router.py',
 'web/runtime/revision.py','web/runtime/validate.py','web/schemas/web_delivery_v0.2.schema.json'}

def git_bytes(ref,path):
    return subprocess.check_output(['git','show',f'{ref}:{path}'],cwd=ROOT)

def sha(data):return hashlib.sha256(data).hexdigest()

def inventory(root):
    result={}
    for p in sorted(root.rglob('*')):
        if '__pycache__' in p.parts or p.suffix in ('.pyc','.pyo'):continue
        if p.is_symlink():raise ValueError('Symlink in candidate source')
        if p.is_file():result[p.relative_to(root).as_posix()]=sha(p.read_bytes())
    return result

def preserved_history(root=ROOT):
    # Compare historical evidence to its actual committed bytes, not mutable expectations.
    fixed={RELEASE_REF:['docs/migration/v2.5.0-source-attestation.json','src/ai-creative-skill/MANIFEST_SHA256.json','packaging/build.py','packaging/plugin.json','tests/test_packaging.py'],
      HARNESS_REF:['validation/known_findings.json','validation/reports/2026-10-20-baseline.json','validation/reports/2026-10-20-baseline-economics.json','validation/reports/2026-10-20-checks.json','validation/reports/2026-10-20-findings.md']}
    for ref,paths in fixed.items():
        for path in paths:
            if (root/path).read_bytes()!=git_bytes(ref,path):raise ValueError('Historical artifact changed: '+path)
    return True

def check(root=ROOT,manifest=None):
    preserved_history(root)
    spec=manifest or json.loads((CANDIDATE/'source-manifest.json').read_text())
    if spec['candidate_id']!='boundary-hardening-v1' or spec['release_ref']!=RELEASE_REF or spec['release_approved'] is not False:
        raise ValueError('Invalid candidate identity')
    actual=inventory(root/'src/ai-creative-skill')
    if actual!=spec['files_sha256']:raise ValueError('Candidate content differs from reviewed inventory')
    release=json.loads(git_bytes(RELEASE_REF,'docs/migration/v2.5.0-source-attestation.json'))['files_sha256']
    if set(actual)!=set(release):raise ValueError('Unexpected candidate file addition/removal')
    changed={path for path in actual if actual[path]!=release[path]}
    if changed!=ALLOWED_CHANGES or sorted(changed)!=spec['changed_from_release']:
        raise ValueError('Changes exceed reviewed remediation scope')
    return {'candidate_id':spec['candidate_id'],'status':'CANDIDATE_CONTENT_VERIFIED_NOT_RELEASE_APPROVED','source_files':len(actual),
            'release_ref':RELEASE_REF,'release_history_preserved':True,'changed_from_release':sorted(changed),
            'candidate_tree_sha256':sha(json.dumps(actual,sort_keys=True).encode()),'release_approved':False}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output');args=p.parse_args();report=check()
    report['git_head']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    text=json.dumps(report,indent=2)+'\n'
    if args.output:
        path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
    print(text)
if __name__=='__main__':main()
