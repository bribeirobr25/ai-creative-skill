"""Create two counterbalanced private packets. Never fabricate human responses."""
import argparse,hashlib,html,json,secrets,shutil,zipfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--captures',type=Path,required=True);p.add_argument('--videos',type=Path,required=True);p.add_argument('--brief',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
out=a.output.resolve();repo=HERE.parents[2]
if out==repo or repo in out.parents:raise ValueError('Private review must stay outside public checkout')
out.mkdir(parents=True,exist_ok=False);order=['a','c'];secrets.SystemRandom().shuffle(order);key={}
for n,variants in [(1,order),(2,list(reversed(order)))]:
    name=f'R{n}';folder=out/name;folder.mkdir();key[name]={}
    for label,variant in zip(['X','Y'],variants):
        key[name][label]=variant.upper()
        for width in [1440,390]:
            for kind in ['hero','full']:
                shutil.copy2(a.captures/f'web-{variant}-{width}-{kind}.png',folder/f'{label}-{width}-{kind}.png')
            shutil.copy2(a.videos/f'{variant}-{width}.webm',folder/f'{label}-{width}.webm')
    text=(HERE/'review-template.html').read_text().replace('@@PACKET@@',name).replace('@@BRIEF@@',html.escape(a.brief.read_text().strip()))
    (folder/'index.html').write_text(text)
    (folder/'LEIA-ME.txt').write_text('Extraia todo o pacote. Abra index.html no navegador. A resposta e baixada localmente como JSON. Envie somente pelo canal privado combinado. Nao existe envio automatico. Assista aos videos e veja as capturas completas antes de responder.\n')
    with zipfile.ZipFile(out/f'{name}.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in folder.iterdir():z.write(f,f'{name}/{f.name}')
(out/'COORDINATOR-KEY.json').write_text(json.dumps(key,indent=2))
(out/'review-status.json').write_text(json.dumps({'gate':'AWAITING_HUMAN_REVIEW','human_responses_received':0,'independent_human_reviews_verified':0,'owner_acceptance':'NOT_GIVEN'},indent=2))
(out/'packet-hashes.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in out.glob('*.zip')},indent=2))
print('Two private packets prepared. Zero human responses. Gate AWAITING_HUMAN_REVIEW.')
