"""Run original release checks on a pinned, exported release; never rewrite its hashes."""
import argparse,io,json,subprocess,sys,tarfile,tempfile
from pathlib import Path
from validation.candidate_integrity import ROOT,RELEASE_REF,preserved_history

def verify(output=None):
    preserved_history()
    report={'release_ref':RELEASE_REF,'historical_bytes_unchanged':True,'checks':[],'release_promotion':False}
    data=subprocess.check_output(['git','archive','--format=tar',RELEASE_REF],cwd=ROOT)
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)
        with tarfile.open(fileobj=io.BytesIO(data)) as archive:
            for member in archive.getmembers():
                if member.isdir():continue
                if not member.isfile() or '..' in Path(member.name).parts or Path(member.name).is_absolute():raise ValueError('Unsafe release archive')
                target=root/member.name;target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(archive.extractfile(member).read())
        commands=[['-m','unittest','discover','-s','tests','-p','test_*.py','-v'],
          ['-m','unittest','discover','-s','src/ai-creative-skill/web/tests','-p','test_*.py','-v'],
          ['src/ai-creative-skill/scripts/smoke_install.py'],['packaging/build.py','--output-dir','dist']]
        for args in commands:
            run=subprocess.run([sys.executable,*args],cwd=root,capture_output=True,text=True,timeout=120)
            text=run.stdout+run.stderr
            if 'unittest' in args:text='\n'.join(text.strip().splitlines()[-4:])
            report['checks'].append({'command':['python',*args],'exit_code':run.returncode,'output':text.strip()})
    report['status']='PASS' if all(c['exit_code']==0 for c in report['checks']) else 'FAIL'
    report['verification_checkout']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    if output:
        path=Path(output);path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(report,indent=2)+'\n')
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();result=verify(a.output)
    print(json.dumps(result,indent=2));sys.exit(0 if result['status']=='PASS' else 1)
