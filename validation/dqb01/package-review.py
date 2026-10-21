"""Package neutral reviewer copies; never synthesize human responses."""
import argparse, hashlib, json, shutil, zipfile
from pathlib import Path

parser=argparse.ArgumentParser()
parser.add_argument('destination',type=Path)
args=parser.parse_args()
root=Path(__file__).resolve().parents[2]
runs=root/'validation/dqb01/runs'
dest=args.destination.resolve()
dest.mkdir(parents=True,exist_ok=True)
key={}
for packet,mapping in [('R1',{'X':'A','Y':'B'}),('R2',{'X':'B','Y':'A'})]:
    key[packet]=mapping
    for stage in ['r0','r1']:
        out=dest/f'{packet}-{stage}'
        out.mkdir()
        hashes={}
        for label,condition in mapping.items():
            source=runs/condition/stage
            shutil.copytree(source,out/label,ignore=shutil.ignore_patterns('evidence','qa'))
            for p in sorted((out/label).rglob('*')):
                if p.is_file():
                    rel=p.relative_to(out/label)
                    digest=hashlib.sha256((source/rel).read_bytes()).hexdigest()
                    assert hashlib.sha256((out/label/rel).read_bytes()).hexdigest()==digest
                    hashes[f'{label}/{rel}']=digest
        brief=(root/'docs/research/dqb01/briefing.md').read_text().split('## Entrega do executor')[0]
        (out/'briefing.md').write_text(brief)
        rubric=(root/'docs/research/dqb01/protocolo.md').read_text()
        rubric=rubric.split('## Rubrica de qualidade')[1].split('## Integridade')[0]
        # Remove experimental/coordinator interpretation from reviewer material.
        rubric=rubric.split('## Avaliação humana e decisão')[0]
        (out/'rubrica.md').write_text('# Rubrica de qualidade\n'+rubric)
        form=(root/'docs/research/dqb01/avaliacao-humana.md').read_text()
        form=form.split('## Ficha entregue ao revisor')[1].split('## Síntese após recebimento')[0]
        (out/'resposta.md').write_text('# Ficha do revisor\n'+form)
        first='desktop, depois mobile' if packet=='R1' else 'mobile, depois desktop'
        stage_name='Primeira entrega' if stage=='r0' else 'Rodada revisada'
        dims=['Direção de arte/identidade','Tipografia/hierarquia','Composição/espaçamento','Integração das imagens','Consistência de componentes','UI/interações','Responsividade','Clareza/usabilidade','Fidelidade']
        sections=''
        for viewport in ['desktop','mobile']:
            sections+=f'<fieldset><legend>{viewport.title()}</legend>'
            for i,dim in enumerate(dims):
                sections+=f'<p>{dim}</p>'
                for label in ['X','Y']:
                    sections+=f'<label>{label} <select required name="{viewport}_{i}_{label}"><option value="">Escolha</option>'+''.join(f'<option>{v}</option>' for v in ['1','2','3','4','5','N/A'])+'</select></label> '
                sections+=f'<label class="block">Justificativa e tela/estado <textarea required name="{viewport}_{i}_reason"></textarea></label>'
            for label in ['X','Y']:
                sections+=f'<label class="block">Classificação {label} <select required name="{viewport}_{label}_overall"><option value="">Escolha</option>'+''.join(f'<option>{v}</option>' for v in ['protótipo','adequado','profissional','evidência insuficiente'])+'</select></label>'
            sections+=f'<label class="block">Tarefas: sucesso, ajuda ou falha; tempo somente se medido. Identifique X/Y e cada tarefa da rubrica.<textarea required name="{viewport}_tasks"></textarea></label><label class="block">Preferência <select required name="{viewport}_preference"><option value="">Escolha</option><option>X</option><option>Y</option><option>empate</option><option>evidência insuficiente</option></select></label></fieldset>'
        html=f'''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Avaliação independente</title><style>body{{font:17px/1.6 system-ui;max-width:820px;margin:40px auto;padding:24px;color:#202724}}a{{color:#23543d}}.links{{display:flex;gap:24px}}h1{{font-size:36px}}input,textarea,select,button{{font:inherit;padding:8px;max-width:100%;box-sizing:border-box}}textarea{{display:block;width:100%;min-height:76px}}fieldset{{margin:32px 0;padding:20px}}.block{{display:block;margin:16px 0}}button{{background:#23543d;color:white;border:0;padding:14px 24px}}</style><h1>{stage_name}</h1><p>Ordem de formatos: {first}. Use o briefing e a rubrica fornecidos. Avalie X e Y sem consultar o outro participante. Registre empate ou evidência insuficiente quando necessário.</p><div class="links"><a target="_blank" onclick="resetDemo()" href="X/index.html">Abrir versão X</a><a target="_blank" onclick="resetDemo()" href="Y/index.html">Abrir versão Y</a></div><p>Desktop: 1440 × 900. Mobile: 390 × 844. Use zoom de 100% e anote qualquer diferença. Os links reiniciam somente os carrinhos demonstrativos; avalie uma versão de cada vez. Nada é transmitido automaticamente.</p><p>Leia briefing.md e rubrica.md antes da avaliação. Não leia código-fonte ou relatórios externos. Feche a rodada inicial antes de abrir a revisada. As respostas só são salvas ao baixar o arquivo.</p><form id="review"><label class="block">Seu identificador <input required name="reviewer_id"></label><label class="block">Experiência em design <input required name="experience"></label><label class="block">Dispositivo, navegador, tamanhos e zoom <textarea required name="viewing_context"></textarea></label><label class="block">Conhecimento anterior e conflitos de interesse <textarea required name="prior_exposure"></textarea></label><label><input type="checkbox" required name="human_independent"> Sou uma pessoa real e respondo independentemente.</label>{sections}<label class="block">O site mais atraente também foi o mais fácil de usar? Por quê?<textarea required name="conclusion"></textarea></label><button>Baixar respostas</button><p role="status" id="status"></p></form><script>function resetDemo(){{try{{localStorage.removeItem('noma-demo-cart');sessionStorage.removeItem('noma-cart');}}catch(e){{}}}}document.querySelector('form').addEventListener('submit',e=>{{e.preventDefault();const result={{packet:'{packet}',stage:'{stage}',provenance:'SELF_REPORTED_HUMAN_UNVERIFIED',values:Object.fromEntries(new FormData(e.target))}};const url=URL.createObjectURL(new Blob([JSON.stringify(result,null,2)],{{type:'application/json'}}));const a=document.createElement('a');a.href=url;a.download='resposta-{packet}-{stage}.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);document.querySelector('#status').textContent='Arquivo preparado para download. Envie-o ao coordenador; nada foi enviado automaticamente.';}});</script></html>'''
        (out/'index.html').write_text(html)
        (out/'hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
        (out/'LEIA-ME.txt').write_text('Abra index.html no navegador. Se o navegador bloquear recursos locais, execute nesta pasta: python3 -m http.server 8900 --bind 127.0.0.1\nEntão abra http://127.0.0.1:8900/ . Não é publicação na internet.\nPreencha resposta.md com observações reais; não invente tempos.\n')
        with zipfile.ZipFile(dest/f'{packet}-{stage}.zip','w',zipfile.ZIP_DEFLATED) as z:
            for p in sorted(out.rglob('*')):
                if p.is_file():z.write(p,p.relative_to(out))
(dest/'COORDINATOR-KEY.json').write_text(json.dumps(key,indent=2)+'\n')
receipt={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in dest.glob('*.zip')}
(dest/'receipt.json').write_text(json.dumps({'human_responses':0,'status':'AWAITING_HUMAN_REVIEW','packets':receipt},indent=2)+'\n')
print(json.dumps(receipt,indent=2))
