"""DQB-03 common evidence collector (coordinator tooling, not part of the skill).

Same checks and captures for every run and round. Functional assertions confirm
brief tasks; they are NOT aesthetic scores.

usage: python3 check_site.py <brief:D1|D2> <site_dir> <out_dir> <label>
"""
import json, re, sys, time, hashlib, pathlib
from playwright.sync_api import sync_playwright

BRIEF, SITE, OUT, LABEL = sys.argv[1], pathlib.Path(sys.argv[2]).resolve(), pathlib.Path(sys.argv[3]), sys.argv[4]
OUT.mkdir(parents=True, exist_ok=True)
URL = (SITE / "index.html").as_uri()
results, shots = [], []

def rec(check, ok, detail="", viewport=None):
    results.append({"check": check, "viewport": viewport, "result": "PASS" if ok is True else ("FAIL" if ok is False else str(ok)), "detail": str(detail)[:300]})

def money(s):
    s = s.replace("\xa0", " ")
    m = re.findall(r"(\d+(?:[.,]\d{1,2})?)", s.replace(".", "") if re.search(r"\d\.\d{3}", s) else s)
    return [float(x.replace(",", ".")) for x in m]

def norm(s):
    """Amendment E4: collapse whitespace (inline SVG or spans inside a heading split innerText) and curly apostrophes."""
    return re.sub(r"\s+([.,!?])", r"\1", " ".join(s.replace("\u2019", "'").split()))

def tid(page, name):
    return page.locator(f'[data-testid="{name}"]')

def visible_tid(page, name):
    loc = tid(page, name)
    return [loc.nth(i) for i in range(loc.count()) if loc.nth(i).is_visible()]

def open_menu(page):
    """Amendment E1: open a collapsed mobile menu (aria-expanded toggle or a button named menu) before navigating."""
    for sel in ['[aria-expanded="false"][aria-controls]', 'button[aria-label*="menu" i]', 'button:has-text("Menu")']:
        loc = page.locator(sel)
        for i in range(loc.count()):
            if loc.nth(i).is_visible():
                loc.nth(i).click(); page.wait_for_timeout(400); return True
    return False

def click(page, name):
    loc = visible_tid(page, name)
    if not loc and name.startswith("nav-") and open_menu(page):
        loc = visible_tid(page, name)
    if not loc:
        raise AssertionError(f"no visible {name}")
    loc[0].scroll_into_view_if_needed(); loc[0].click(); page.wait_for_timeout(450)

def settle(page):
    page.wait_for_timeout(500)
    h = page.evaluate("document.documentElement.scrollHeight")
    for y in range(0, h, 500):
        page.evaluate(f"window.scrollTo({{top:{y},behavior:'instant'}})"); page.wait_for_timeout(60)
    page.evaluate("window.scrollTo({top:0,behavior:'instant'})"); page.wait_for_timeout(350)

def shot(page, name, full=False):
    f = OUT / f"{LABEL}-{name}.jpg"
    if full:
        settle(page)
    page.screenshot(path=str(f), type="jpeg", quality=80, full_page=full)
    shots.append({"state": name, "file": f.name, "sha256": hashlib.sha256(f.read_bytes()).hexdigest()})

def images_ok(page):
    settle(page)
    return page.evaluate("""() => {const im=[...document.images];
      const broken=im.filter(i=>i.complete && i.naturalWidth===0).map(i=>i.getAttribute('src'));
      const tiny=im.filter(i=>{if(/logo|wordmark/i.test(i.getAttribute('src')||'')) return false; const r=i.getBoundingClientRect(); const cs=getComputedStyle(i);
         return i.naturalWidth>0 && cs.display!=='none' && cs.visibility!=='hidden' && r.width>0 && (r.width<24||r.height<24)}).map(i=>i.getAttribute('src'));
      const noalt=im.filter(i=>!i.hasAttribute('alt')).map(i=>i.getAttribute('src'));
      return {count:im.length, broken, tiny, noalt}}""")

def overflow(page):
    return page.evaluate("document.documentElement.scrollWidth - window.innerWidth")

def new_page(b, w, h, reduce=False):
    ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1, reduced_motion="reduce" if reduce else "no-preference")
    page = ctx.new_page()
    page._errors, page._external = [], []
    page.on("pageerror", lambda e: page._errors.append(str(e)))
    page.on("console", lambda m: page._errors.append("console:" + m.text) if m.type == "error" else None)
    page.on("request", lambda r: page._external.append(r.url) if not r.url.startswith(("file:", "data:", "blob:", "about:")) else None)
    ctx.route(re.compile(r"^https?://"), lambda route: route.abort())
    page.goto(URL); page.wait_for_timeout(700)
    return ctx, page

HERO = {"D1": "It's in the little details.", "D2": "Practice money decisions before they're real."}
NOTICE = {"D1": "Preview website.", "D2": "Practice is a simulation. No real money moves."}

def d1_tasks(page, vp):
    ids = ["croissant", "ursinho", "limao", "branca", "azul", "rosa"]
    click(page, "nav-collection"); rec("nav-collection opens collection", len(visible_tid(page, "filter-all")) > 0, viewport=vp)
    def vis():
        return [i for i in ids if visible_tid(page, f"product-{i}")]
    click(page, "filter-print"); v = vis(); rec("filter Print -> croissant, ursinho, limao", sorted(v) == ["croissant", "limao", "ursinho"], v, vp)
    click(page, "filter-terry"); v = vis(); rec("filter Terry -> rosa only", v == ["rosa"], v, vp)
    click(page, "filter-embroidered"); v = vis(); rec("filter Embroidered -> branca, azul", sorted(v) == ["azul", "branca"], v, vp)
    click(page, "filter-all"); v = vis(); rec("filter All -> 6", len(v) == 6, v, vp)
    page.evaluate("window.scrollTo(0,0)"); page.wait_for_timeout(250); shot(page, "collection")  # E3
    body_all = []
    for pid in ids:
        if not visible_tid(page, f"product-{pid}"):
            click(page, "nav-collection"); click(page, "filter-all")
        click(page, f"product-{pid}"); body = page.inner_text("body"); body_all.append(body)
        low = body.lower()
        rec(f"{pid}: price to be announced, no numeric price", "price to be announced" in low and not re.search(r"[€$£]\s?\d|\d\s?(€|eur)\b", low), viewport=vp)
        rec(f"{pid}: props note", "styling props" in low and "not included" in low, viewport=vp)
        th = visible_tid(page, "gallery-thumb"); rec(f"{pid}: >=2 gallery thumbs", len(th) >= 2, len(th), vp)
        if pid == "croissant":
            if len(th) >= 2:
                before = page.evaluate("[...document.images].filter(i=>i.getBoundingClientRect().width>200).map(i=>i.currentSrc).join('|')")
                th[1].click(); page.wait_for_timeout(400)
                after = page.evaluate("[...document.images].filter(i=>i.getBoundingClientRect().width>200).map(i=>i.currentSrc).join('|')")
                rec("croissant: thumbnail changes main image", before != after, viewport=vp)
                if len(th) >= 3:
                    tops = sorted(round(t.bounding_box()["y"]) for t in th if t.bounding_box())
                    rec("croissant: thumbnails in one row", bool(tops) and tops[-1] - tops[0] <= 8, tops, vp)  # E2: 8 px tolerance
            rec("croissant: sticker sheet mentioned", "sticker" in low, viewport=vp)
            page.evaluate("window.scrollTo(0,0)"); page.wait_for_timeout(250); shot(page, "product")  # E3
        if pid == "limao":
            rec("limao: flower, not bow", "flower" in low, viewport=vp)
        page.go_back(); page.wait_for_timeout(400)
    joined = " ".join(body_all).lower()
    rec("no sticker sheet outside croissant", all("sticker" not in b.lower() for b in body_all[1:]), viewport=vp)
    rec("no 'made in berlin' claim", "made in berlin" not in joined and "handmade in berlin" not in joined, viewport=vp)
    for pid in ["croissant", "rosa"]:
        click(page, "nav-collection"); click(page, "filter-all"); click(page, f"product-{pid}"); click(page, "add-interest")
    click(page, "nav-interest")
    items = visible_tid(page, "interest-item"); rec("interest list has 2 items", len(items) == 2, len(items), vp)
    em = visible_tid(page, "interest-email")[0]
    em.fill("hello@"); click(page, "interest-submit")
    err = visible_tid(page, "interest-error"); conf = visible_tid(page, "interest-confirmation")
    rec("invalid email -> error, no confirmation", bool(err and err[0].inner_text().strip()) and not conf, viewport=vp)
    err and err[0].scroll_into_view_if_needed(); page.evaluate("window.scrollBy(0, -window.innerHeight/3)"); page.wait_for_timeout(200); shot(page, "interest-error")  # E3
    em = visible_tid(page, "interest-email")
    if em: em[0].fill("hello@example.com")
    click(page, "interest-submit")
    conf = visible_tid(page, "interest-confirmation"); txt = conf[0].inner_text().lower() if conf else ""
    rec("valid email -> confirmation names croissant and rosa", "croissant" in txt and "rosa" in txt, txt[:160], vp)
    conf and conf[0].scroll_into_view_if_needed(); page.evaluate("window.scrollBy(0, -window.innerHeight/3)"); page.wait_for_timeout(200); shot(page, "interest-confirmation")  # E3
    body = page.inner_text("body")
    rec("no-data-sent notice", "No data is sent" in body, viewport=vp)
    click(page, "nav-interest")
    for _ in range(3):
        r = visible_tid(page, "interest-remove")
        if not r: break
        r[0].click(); page.wait_for_timeout(300)
    rec("remove all -> empty state", len(visible_tid(page, "interest-empty")) > 0, viewport=vp)

def d2_tasks(page, vp):
    ctas = page.locator('[data-testid="cta-practice"]')
    hrefs = [ctas.nth(i).get_attribute("href") for i in range(ctas.count())]
    rec("cta-practice links to app.diboas.com", bool(hrefs) and all(h and h.rstrip("/") == "https://app.diboas.com" for h in hrefs), hrefs, vp)
    click(page, "nav-how")
    steps = visible_tid(page, "how-step"); rec("how it works shows 8 steps", len(steps) == 8, len(steps), vp)
    body = page.inner_text("body"); low = body.lower()
    rec("how: 10,000 credits, 1,000 weekly, 20,000 pause, 1,500 event", all(x in body for x in ["10,000", "1,000", "20,000", "1,500"]), viewport=vp)
    rec("how: reference cost 0.39% / 0.25 not charged", "0.39%" in body and "0.25" in body and "not charged" in low, viewport=vp)
    page.evaluate("window.scrollTo(0,0)"); page.wait_for_timeout(250); shot(page, "how")  # E3
    click(page, "nav-system")
    def setp(e, t, l):
        for k, v in (("emergency", e), ("trip", t), ("laptop", l)):
            el = visible_tid(page, f"system-pct-{k}")[0]; el.fill(str(v)); el.dispatch_event("input"); el.dispatch_event("change")
        page.wait_for_timeout(350)
        get = lambda k: " ".join(x.inner_text() for x in visible_tid(page, k))
        return {k: get(f"system-amount-{k}") for k in ("emergency", "trip", "laptop")}, get("system-available"), visible_tid(page, "system-error")
    a, av, err = setp(40, 30, 0)
    ok = 400 in money(a["emergency"].replace(",", "")) and 300 in money(a["trip"].replace(",", "")) and 0 in money(a["laptop"].replace(",", "")) and 300 in money(av.replace(",", ""))
    rec("system 40/30/0 -> 400/300/0, 300 available", ok and not any(e.inner_text().strip() for e in err), f"{a} | {av}", vp)
    shot(page, "system")
    a, av, err = setp(70, 50, 0)
    txt = " ".join(a.values()) + " " + av
    rec("system 70/50 -> error, no negative/NaN", bool(err and err[0].inner_text().strip()) and "NaN" not in txt and not re.search(r"-\s?\d", txt), f"err={bool(err)} '{txt[:120]}'", vp)
    shot(page, "system-error")
    click(page, "nav-waitlist")
    em = visible_tid(page, "waitlist-email")[0]; em.fill("hello@"); click(page, "waitlist-submit")
    err = visible_tid(page, "waitlist-error"); conf = visible_tid(page, "waitlist-confirmation")
    rec("invalid email -> error, no confirmation", bool(err and err[0].inner_text().strip()) and not conf, viewport=vp)
    em = visible_tid(page, "waitlist-email")
    if em: em[0].fill("hello@example.com")
    click(page, "waitlist-submit")
    conf = visible_tid(page, "waitlist-confirmation"); t = conf[0].inner_text().lower() if conf else ""
    rec("valid email -> local confirmation, nothing sent", bool(conf) and ("not sent" in t or "nothing was sent" in t or "no data" in t or "wasn't sent" in t or "was not sent" in t), t[:160], vp)
    conf and conf[0].scroll_into_view_if_needed(); page.evaluate("window.scrollBy(0, -window.innerHeight/3)"); page.wait_for_timeout(200); shot(page, "waitlist")  # E3
    body = page.inner_text("body").lower()
    banned = [w for w in ["risk-free", "guaranteed return", "passive income", " apy", "defi", "stablecoin", "blockchain", "sandbox", "limited-time"] if w in body]
    rec("no banned words on page", not banned, banned, vp)
    click(page, "nav-home")
    faq = visible_tid(page, "faq-item")
    if not faq:
        for nav in ("nav-how", "nav-waitlist", "nav-system"):
            click(page, nav); faq = visible_tid(page, "faq-item")
            if faq: break
    rec("FAQ has >= 4 items", len(faq) >= 4, len(faq), vp)
    if faq:
        before = page.inner_text("body"); faq[0].click(); page.wait_for_timeout(350); after = page.inner_text("body")
        rec("FAQ item expands", "never convert" in after.lower() or len(after) > len(before), viewport=vp)

with sync_playwright() as p:
    b = p.chromium.launch()
    for (w, h) in [(1440, 900), (390, 844)]:
        vp = f"{w}x{h}"
        ctx, page = new_page(b, w, h)
        shot(page, f"{w}-home")
        shot(page, f"{w}-home-full", full=True)
        img = images_ok(page)
        rec("images decoded, none broken", not img["broken"], img, vp)
        rec("no collapsed/tiny visible images", not img["tiny"], img["tiny"], vp)
        rec("all images have alt attribute", not img["noalt"], img["noalt"], vp)
        rec("no horizontal overflow (home)", overflow(page) <= 1, overflow(page), vp)
        body = page.inner_text("body")
        rec("hero copy preserved", HERO[BRIEF] in norm(body), viewport=vp)  # E4: whitespace-normalised
        rec("footer preview notice", NOTICE[BRIEF] in body, viewport=vp)
        LABEL_ORIG = LABEL
        globals()["LABEL"] = f"{LABEL_ORIG}-{w}"
        try:
            (d1_tasks if BRIEF == "D1" else d2_tasks)(page, vp)
        except Exception as e:
            rec("task sequence completed", f"ERROR", repr(e)[:250], vp)
        globals()["LABEL"] = LABEL_ORIG
        rec("no script/console errors", not page._errors, page._errors[:5], vp)
        rec("no external network requests", not page._external, page._external[:5], vp)
        ctx.close()
    for (w, h) in [(768, 1024), (320, 740)]:
        ctx, page = new_page(b, w, h)
        rec("no horizontal overflow (home)", overflow(page) <= 1, overflow(page), f"{w}x{h}")
        shot(page, f"{w}-home")
        ctx.close()
    ctx, page = new_page(b, 1440, 900, reduce=True)
    page.wait_for_timeout(800)
    running = page.evaluate("document.getAnimations().filter(a=>a.playState==='running' && (a.effect?.getTiming().iterations===Infinity || (a.effect?.getComputedTiming().duration||0)>50)).length")
    rec("reduced motion: no running animations", running == 0, running, "1440x900/reduce")
    ctx.close()
    ctx, page = new_page(b, 1440, 900)
    focus = []
    for _ in range(6):
        page.keyboard.press("Tab"); page.wait_for_timeout(80)
        focus.append(page.evaluate("""() => {const e=document.activeElement; if(!e||e===document.body) return null;
          const cs=getComputedStyle(e); return {tag:e.tagName, visible: (cs.outlineStyle!=='none' && parseFloat(cs.outlineWidth)>0) || cs.boxShadow!=='none' || cs.textDecorationLine.includes('underline')}}"""))
    focused = [f for f in focus if f]  # Tab may leave the document (body) between controls; skip those steps
    rec("keyboard Tab reaches controls with visible focus", len(focused) >= 3 and all(f["visible"] for f in focused), focus, "1440x900")
    ctx.close()
    b.close()

summary = {"label": LABEL, "brief": BRIEF, "site": str(SITE), "collected_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "pass": sum(r["result"] == "PASS" for r in results), "total": len(results), "checks": results, "screenshots": shots}
(OUT / f"{LABEL}-checks.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))
print(f"{LABEL}: {summary['pass']}/{summary['total']} PASS")
for r in results:
    if r["result"] != "PASS": print("  ", r["result"], r["viewport"], r["check"], "|", r["detail"][:160])
