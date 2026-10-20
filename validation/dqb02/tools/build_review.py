"""Build (1) the coordinator gallery (conditions revealed) and (2) blind reviewer packets.

usage: python3 build_review.py <evidence_root> <condition_map.json> <out_root> <round:r0|r1> [seed]

Packets: one per brief×repetition pair, labels X/Y; X/Y↔A/B mapping and side order are
counterbalanced and stored ONLY in the coordinator key file (never inside packets).
"""
import json, sys, shutil, random, pathlib, html

EV, MAP, OUT, RND = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
SEED = int(sys.argv[5]) if len(sys.argv) > 5 else 20261021
runs = json.loads(MAP.read_text())
STATES = {"B1": ["1440-home", "1440-home-full", "1440-catalog", "1440-product", "1440-order-filled", "1440-order-review",
                 "390-home", "390-home-full", "390-catalog", "390-product", "390-order-filled", "768-home"],
          "B2": ["1440-home", "1440-home-full", "1440-schedule", "1440-session", "1440-plan", "1440-plan-error",
                 "390-home", "390-home-full", "390-schedule", "390-session", "390-plan", "768-home"]}
DIMS = ["Direção de arte/identidade", "Tipografia/hierarquia", "Composição/espaçamento", "Imagens", "Componentes",
        "UI/interações", "Responsividade", "Clareza/usabilidade", "Fidelidade"]

def img(label, state):
    return f"{label}-{state}.jpg"

def css():
    return """<style>:root{color-scheme:light dark;--bg:#f6f5f2;--fg:#1d1d1b;--mut:#6b6a66;--line:#d9d6cf;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--fg:#ecebe7;--mut:#a3a29d;--line:#34332f;--card:#1f1f1d}}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif}main{max-width:1500px;margin:auto;padding:24px 16px}
h1{font-size:26px;margin:0 0 4px}h2{font-size:20px;margin:40px 0 8px;border-top:1px solid var(--line);padding-top:24px}h3{font-size:15px;margin:18px 0 6px;color:var(--mut)}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px}.pair figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px}
figcaption{font-size:13px;color:var(--mut);margin:0 0 6px}img{width:100%;height:auto;display:block;border-radius:4px}
.mob img{max-width:300px;margin:auto}a{color:inherit}.note{color:var(--mut);font-size:14px;max-width:80ch}
table{border-collapse:collapse;width:100%;font-size:14px}td,th{border:1px solid var(--line);padding:6px;text-align:left;vertical-align:top}
select,textarea{font:inherit;width:100%;box-sizing:border-box}textarea{min-height:56px}button{font:inherit;padding:8px 14px}
@media(max-width:700px){.pair{grid-template-columns:1fr}}</style>"""

def build_gallery():
    out = OUT / f"gallery-{RND}"; out.mkdir(parents=True, exist_ok=True)
    parts = [f"<!doctype html><html lang='pt-BR'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>DQB-02 galeria {RND}</title>{css()}<main>",
             f"<h1>DQB-02 · galeria da coordenação · {RND.upper()}</h1><p class='note'>Condições reveladas: uso exclusivo da coordenação. Revisores devem usar os pacotes cegos, nunca esta página.</p>"]
    for brief in ["B1", "B2"]:
        for rep in [1, 2]:
            pr = {r["condition"]: r for r in runs if r["brief"] == brief and r["repetition"] == rep}
            if not all((EV / f"{pr[c]['run']}-{RND}").exists() for c in "AB"):
                continue
            parts.append(f"<h2>{brief} · repetição {rep} · A = {pr['A']['run']} · B = {pr['B']['run']}</h2>")
            for st in STATES[brief]:
                cls = " mob" if st.startswith("390") else ""
                parts.append(f"<h3>{st}</h3><div class='pair{cls}'>")
                for c in "AB":
                    lab = f"{pr[c]['run']}-{RND}"; src = EV / lab / img(lab, st)
                    if src.exists():
                        shutil.copy(src, out / src.name)
                        parts.append(f"<figure><figcaption>{c} · {pr[c]['run']}</figcaption><a href='{src.name}'><img loading='lazy' src='{src.name}' alt='{c} {st}'></a></figure>")
                    else:
                        parts.append(f"<figure><figcaption>{c} · {pr[c]['run']} · captura ausente</figcaption></figure>")
                parts.append("</div>")
    parts.append("</main></html>")
    (out / "index.html").write_text("\n".join(parts))
    return out

def build_packets():
    rng = random.Random(SEED); key = []
    root = OUT / f"packets-{RND}"; root.mkdir(parents=True, exist_ok=True)
    for brief in ["B1", "B2"]:
        for rep in [1, 2]:
            pr = {r["condition"]: r for r in runs if r["brief"] == brief and r["repetition"] == rep}
            if not all((EV / f"{pr[c]['run']}-{RND}").exists() for c in "AB"):
                continue
            pid = f"{brief}-par{rep}"
            order = ["A", "B"]; rng.shuffle(order)  # order[0] -> X (shown left)
            key.append({"packet": pid, "round": RND, "X": order[0], "Y": order[1], "X_run": pr[order[0]]["run"], "Y_run": pr[order[1]]["run"]})
            d = root / pid; d.mkdir(exist_ok=True)
            for lbl, cond in zip("XY", order):
                site_src = pathlib.Path(pr[cond]["dir"]) / RND
                if (d / f"site-{lbl}").exists(): shutil.rmtree(d / f"site-{lbl}")
                shutil.copytree(site_src, d / f"site-{lbl}", ignore=shutil.ignore_patterns(".*"))
                for f in (d / f"site-{lbl}").rglob("*"):
                    if f.is_file() and f.suffix in (".html", ".js", ".css"):
                        t = f.read_text(errors="ignore")
                        for w in (pr["A"]["run"], pr["B"]["run"]):
                            t = t.replace(w, "")
                        f.write_text(t)
            rows = "".join(f"<tr><td>{html.escape(dm)}</td><td><select name='pref::{i}'><option value=''>—</option><option>X</option><option>Y</option><option>Empate</option></select></td>"
                           f"<td><select name='x::{i}'><option value=''>—</option>{''.join(f'<option>{n}</option>' for n in ['1','2','3','4','5','N/A'])}</select></td>"
                           f"<td><select name='y::{i}'><option value=''>—</option>{''.join(f'<option>{n}</option>' for n in ['1','2','3','4','5','N/A'])}</select></td>"
                           f"<td><textarea name='why::{i}' placeholder='Tela/estado e motivo'></textarea></td></tr>" for i, dm in enumerate(DIMS))
            shots = []
            for st in STATES[brief]:
                cls = " mob" if st.startswith("390") else ""
                cells = []
                for lbl, cond in zip("XY", order):
                    lab = f"{pr[cond]['run']}-{RND}"; src = EV / lab / img(lab, st)
                    if src.exists():
                        dst = f"{lbl}-{st}.jpg"; shutil.copy(src, d / dst)
                        cells.append(f"<figure><figcaption>{lbl}</figcaption><a href='{dst}'><img loading='lazy' src='{dst}' alt='{lbl} {st}'></a></figure>")
                shots.append(f"<h3>{st}</h3><div class='pair{cls}'>{''.join(cells)}</div>")
            page = f"""<!doctype html><html lang='pt-BR'><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Avaliação {pid}</title>{css()}<main>
<h1>Avaliação cega · {pid}</h1>
<p class='note'>Dois websites fictícios feitos a partir do mesmo briefing, materiais e regras. Abra e use cada um antes de responder:
<a href='site-X/index.html'>abrir X</a> · <a href='site-Y/index.html'>abrir Y</a>. Teste no desktop e, se possível, no celular ou janela estreita (~390 px).
Não leia relatórios do estudo antes de responder. Não há resposta certa; empate é válido.</p>
<form id='f'><table><tr><th>Dimensão</th><th>Preferência</th><th>Nota X (1–5)</th><th>Nota Y (1–5)</th><th>Justificativa (cite tela/estado)</th></tr>{rows}</table>
<p><label>Classificação geral de X <select name='overall::X'><option value=''>—</option><option>protótipo</option><option>adequado</option><option>profissional</option><option>evidência insuficiente</option></select></label></p>
<p><label>Classificação geral de Y <select name='overall::Y'><option value=''>—</option><option>protótipo</option><option>adequado</option><option>profissional</option><option>evidência insuficiente</option></select></label></p>
<p><label>Você já tinha visto algum destes sites ou relatórios do estudo? <select name='prior_exposure'><option value=''>—</option><option>não</option><option>sim</option></select></label></p>
<p><label>Experiência com UI/design visual <select name='design_experience'><option value=''>—</option><option>profissional</option><option>alguma</option><option>nenhuma</option></select></label></p>
<p><label>Identificação do revisor (iniciais) <input name='reviewer' style='font:inherit'></label></p>
<button type='button' id='save'>Baixar respostas (JSON)</button></form>
<p class='note'>As respostas ficam apenas neste navegador até você baixar o arquivo e enviá-lo à coordenação.</p>
<h2>Capturas de referência (mesmos estados, mesmo tamanho)</h2>{''.join(shots)}
<script>
const f=document.getElementById('f'),K='dqb02-{pid}-{RND}';
try{{const s=JSON.parse(localStorage.getItem(K)||'{{}}');for(const[k,v]of Object.entries(s)){{const e=f.elements[k];if(e)e.value=v}}}}catch(e){{}}
f.addEventListener('input',()=>{{const o={{}};for(const e of f.elements)if(e.name)o[e.name]=e.value;try{{localStorage.setItem(K,JSON.stringify(o))}}catch(e){{}}}});
document.getElementById('save').onclick=()=>{{const o={{packet:'{pid}',round:'{RND}',saved_utc:new Date().toISOString()}};for(const e of f.elements)if(e.name)o[e.name]=e.value;
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(o,null,1)],{{type:'application/json'}}));a.download='dqb02-{pid}-{RND}-'+(o.reviewer||'revisor')+'.json';a.click()}};
</script></main></html>"""
            (d / "index.html").write_text(page)
    (OUT / f"KEY-{RND}-coordinator-only.json").write_text(json.dumps({"seed": SEED, "pairs": key}, indent=1))
    return root

if __name__ == "__main__":
    print(build_gallery()); print(build_packets())
