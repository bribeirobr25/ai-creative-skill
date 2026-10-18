#!/usr/bin/env python3
"""Installation integrity & cheap functional smoke; no network, paid calls or model download."""
import sys,json,hashlib,subprocess,tempfile,os
from pathlib import Path
from PIL import Image
BASE=Path(__file__).resolve().parents[1]
checks={}
manifest=json.loads((BASE/'MANIFEST_SHA256.json').read_text())
checks['manifest'] = all((BASE/f).is_file() and hashlib.sha256((BASE/f).read_bytes()).hexdigest()==d for f,d in manifest['sha256'].items())
for name,argv in [('web_route',[sys.executable,str(BASE/'scripts/creative_web.py'),'route','crie uma landing para meu produto']),('media_routes',[sys.executable,str(BASE/'scripts/creative_media.py'),'routes'])]:
 try:
  z=subprocess.run(argv,text=True,capture_output=True,timeout=25)
  checks[name]=(z.returncode==0 and z.stdout.strip().startswith('{'))
 except Exception:checks[name]=False
try:
 from PIL import Image
except ImportError:
 Image=None
if Image is None:
 checks['image_lanczos']='SKIPPED_PILLOW_NOT_INSTALLED'
else:
 with tempfile.TemporaryDirectory() as d:
  p=Path(d); src=p/'a.png';Image.new('RGB',(24,24),'white').save(src)
  argv=[sys.executable,str(BASE/'scripts/creative_media.py'),'run','--kind','IMAGE','--route','local.pillow.lanczos.image.v0.2','--source',str(src),'--width','48','--height','48','--output-dir',str(p/'out')]
  try:
   z=subprocess.run(argv,text=True,capture_output=True,timeout=40)
   checks['image_lanczos']=(z.returncode==0 and 'TECHNICAL_QA_PASS' in z.stdout)
  except Exception:checks['image_lanczos']=False
print(json.dumps({'release':'2.5.0','checks':checks,'all_pass':all(x is True or x=='SKIPPED_PILLOW_NOT_INSTALLED' for x in checks.values()),'not_tested':['real browser','auto-agent invocation','neural fidelity','commercial adapters']},indent=2))
sys.exit(0 if all(x is True or x=='SKIPPED_PILLOW_NOT_INSTALLED' for x in checks.values()) else 1)
