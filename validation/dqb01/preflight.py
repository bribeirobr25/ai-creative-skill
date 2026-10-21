from pathlib import Path
from PIL import Image
import hashlib, json, datetime, subprocess
root=Path(__file__).resolve().parents[2]
base=root/'validation/dqb01'; manifest=json.loads((base/'results/input-manifest.json').read_text())
checks=[]
for name,digest in manifest['files'].items():
 p=base/name
 checks.append({'id':'input:'+name,'pass':hashlib.sha256(p.read_bytes()).hexdigest()==digest})
for name in ('arco.jpg','trama.jpg','editorial.jpg'):
 p=base/'shared/assets'/name
 with Image.open(p) as im:
  im.load();checks.append({'id':'image:'+name,'pass':min(im.size)>=1000,'size':list(im.size),'mode':im.mode})
for name in ('briefing.md','protocolo.md'):
 checks.append({'id':'shared-document:'+name,'pass':(base/'shared'/name).read_bytes()==(root/'docs/research/dqb01'/name).read_bytes()})
changed=subprocess.check_output(['git','diff','--name-only','39a0bfa','HEAD'],cwd=root,text=True).splitlines()
checks.append({'id':'research-only-change','pass':all(p.startswith(('docs/research/dqb01/','validation/dqb01/')) for p in changed)})
checks.append({'id':'independent-main-base','pass':subprocess.check_output(['git','merge-base','HEAD','main'],cwd=root,text=True).strip()=='39a0bfa39270ea4b685b0f862e7dbf647cf81d77'})
result={'run_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'INPUT_PREFLIGHT_ONLY','checks':checks,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'does_not_establish':['website implementation','professional design quality','human review','C execution']}
(base/'results/preflight-checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
