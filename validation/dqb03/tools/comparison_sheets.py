"""Owner comparison sheets: per brief and round, one row per state, columns A1 A2 B1 B2 (labels shown).
usage: python3 comparison_sheets.py <evidence_root> <condition_map.json> <out_dir> <round>"""
import json, sys, pathlib
from PIL import Image, ImageDraw, ImageFont

EV, MAP, OUT, RND = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
OUT.mkdir(parents=True, exist_ok=True)
runs = json.loads(MAP.read_text())
SHEETS = {
 "D1": {"desk1": ["1440-home", "1440-collection"], "desk2": ["1440-product", "1440-interest-confirmation"],
        "mob": ["390-home", "390-collection", "390-product", "390-interest-confirmation"], "narrow": ["320-home", "768-home"],
        "full": ["1440-home-full"], "mobfull": ["390-home-full"]},
 "D2": {"desk1": ["1440-home", "1440-how"], "desk2": ["1440-system", "1440-waitlist"],
        "mob": ["390-home", "390-how", "390-system", "390-waitlist"], "narrow": ["320-home", "768-home"],
        "full": ["1440-home-full"], "mobfull": ["390-home-full"]}}
try:
    FONT = ImageFont.truetype("DejaVuSans-Bold.ttf", 22); SMALL = ImageFont.truetype("DejaVuSans.ttf", 16)
except OSError:
    FONT = SMALL = ImageFont.load_default()

def cols(brief):
    out = []
    for cond in "AB":
        for rep in (1, 2):
            r = next(x for x in runs if x["brief"] == brief and x["condition"] == cond and x["repetition"] == rep)
            out.append((f"{cond}{rep}", r["run"]))
    return out

for brief, sheets in SHEETS.items():
    cs = cols(brief)
    for name, states in sheets.items():
        width = {"mob": 390, "mobfull": 390, "narrow": 420}.get(name, 900)
        rows = []
        for st in states:
            ims = []
            for lab, run in cs:
                f = EV / f"{run}-{RND}" / f"{run}-{RND}-{st}.jpg"
                if f.exists():
                    im = Image.open(f).convert("RGB")
                    if name == "full": im = im.resize((width, int(im.height * width / im.width)))
                    elif im.width != width: im = im.resize((width, int(im.height * width / im.width)))
                    if name in ("full", "mobfull") and im.height > 4200: im = im.crop((0, 0, im.width, 4200))
                else:
                    im = Image.new("RGB", (width, 200), "#ddd")
                ims.append((lab, im))
            h = max(i.height for _, i in ims)
            rows.append((st, ims, h))
        gap, head = 16, 40
        W = gap + len(cs) * (width + gap)
        H = sum(head + h + gap for _, _, h in rows) + gap
        sheet = Image.new("RGB", (W, H), "#f2f1ee"); d = ImageDraw.Draw(sheet)
        y = gap
        for st, ims, h in rows:
            for i, (lab, im) in enumerate(ims):
                x = gap + i * (width + gap)
                d.text((x, y + 8), f"{lab}", fill="#111", font=FONT)
                d.text((x + 60, y + 12), st, fill="#555", font=SMALL)
                sheet.paste(im, (x, y + head))
            y += head + h + gap
        p = OUT / f"{brief.lower()}{RND}_{name}.jpg"
        sheet.save(p, quality=82, optimize=True)
        print(p, sheet.size)
