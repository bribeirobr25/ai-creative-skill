"""Objective convergence descriptors for DQB-02 sites (coordinator tooling).

Not an aesthetic score. Measures how similar deliveries are, within and across
conditions/briefs: font families actually rendered, hero image chosen, background
color, and perceptual distance of the 1440 home opening.

usage: python3 convergence.py <frozen_root> <evidence_root> <condition_map> <round> <out.json>
"""
import json, sys, pathlib, itertools
from PIL import Image
from playwright.sync_api import sync_playwright

FROZEN, EV, MAP, RND, OUT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4], pathlib.Path(sys.argv[5])
runs = json.loads(MAP.read_text())

def dhash(path, size=16):
    im = Image.open(path).convert("L").resize((size + 1, size))
    px = list(im.getdata())
    return [px[r * (size + 1) + c] > px[r * (size + 1) + c + 1] for r in range(size) for c in range(size)]

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b)) / len(a)

desc = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    for r in runs:
        site = FROZEN / f"{r['run']}-{RND}" / "index.html"
        pg = b.new_page(viewport={"width": 1440, "height": 900})
        pg.route("http*://**", lambda route: route.abort())
        pg.goto(site.as_uri()); pg.wait_for_timeout(800)
        d = pg.evaluate("""() => {
          const fam = s => (s||'').split(',')[0].replace(/["']/g,'').trim();
          const h1 = document.querySelector('h1'); const body = document.body;
          const fams = new Set([...document.querySelectorAll('body *')].filter(e=>e.childNodes.length && [...e.childNodes].some(n=>n.nodeType===3 && n.textContent.trim())).map(e=>fam(getComputedStyle(e).fontFamily)));
          const vis = [...document.images].filter(i=>{const r=i.getBoundingClientRect(); return r.top<900 && r.bottom>0 && r.width*r.height>40000});
          return {h1_font: h1?fam(getComputedStyle(h1).fontFamily):null, body_font: fam(getComputedStyle(body).fontFamily),
                  families: [...fams].sort(), body_bg: getComputedStyle(body).backgroundColor,
                  hero_images: vis.map(i=>i.getAttribute('src').split('/').pop())};
        }""")
        desc[r["run"]] = {**d, "brief": r["brief"], "condition": r["condition"], "repetition": r["repetition"]}
        pg.close()
    b.close()

hashes = {r["run"]: dhash(EV / f"{r['run']}-{RND}" / f"{r['run']}-{RND}-1440-home.jpg") for r in runs}
pairs = []
for a, c in itertools.combinations(runs, 2):
    kind = ("same-brief" if a["brief"] == c["brief"] else "cross-brief") + "/" + (("within-" + a["condition"]) if a["condition"] == c["condition"] else "cross-condition")
    pairs.append({"a": a["run"], "b": c["run"], "kind": kind, "home_dhash_distance": round(hamming(hashes[a["run"]], hashes[c["run"]]), 3)})
summary = {}
for k in sorted({p["kind"] for p in pairs}):
    v = [p["home_dhash_distance"] for p in pairs if p["kind"] == k]
    summary[k] = {"n": len(v), "mean": round(sum(v) / len(v), 3), "values": v}
trio = {r: tuple(sorted(set(d["families"]) - {"system-ui", "-apple-system", "ui-monospace", "monospace", "sans-serif", "serif"})) for r, d in desc.items()}
out = {"round": RND, "note": "Descriptors of similarity, not quality. dHash distance: 0 identical, ~0.5 unrelated.",
       "sites": desc, "font_sets": {r: list(t) for r, t in trio.items()}, "distinct_font_sets": len(set(trio.values())),
       "home_pairs": pairs, "home_distance_by_kind": summary}
OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(json.dumps({"distinct_font_sets": out["distinct_font_sets"], "font_sets": out["font_sets"],
                  "h1": {r: d["h1_font"] for r, d in desc.items()}, "hero": {r: d["hero_images"] for r, d in desc.items()},
                  "bg": {r: d["body_bg"] for r, d in desc.items()},
                  "distance": {k: v["mean"] for k, v in summary.items()}}, indent=1, ensure_ascii=False))
