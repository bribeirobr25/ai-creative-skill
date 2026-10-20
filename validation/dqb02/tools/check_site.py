"""DQB-02 common evidence collector (coordinator tooling, not part of the skill).

Same checks and captures for every run and round. Functional assertions confirm
brief tasks; they are NOT aesthetic scores.

usage: python3 check_site.py <brief:B1|B2> <site_dir> <out_dir> <label>
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

def tid(page, name):
    return page.locator(f'[data-testid="{name}"]')

def visible_tid(page, name):
    loc = tid(page, name)
    return [loc.nth(i) for i in range(loc.count()) if loc.nth(i).is_visible()]

def click(page, name):
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
      const tiny=im.filter(i=>{const r=i.getBoundingClientRect(); const cs=getComputedStyle(i);
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

def b1_tasks(page, vp):
    click(page, "nav-catalog"); rec("nav-catalog opens catalog", len(visible_tid(page, "filter-all")) > 0, viewport=vp)
    ids = ["no-cardamomo", "muffin-baunilha", "torta-morango", "bolo-maca", "scone-queijo"]
    def vis_products():
        return [i for i in ids if visible_tid(page, f"product-{i}")]
    click(page, "filter-savory"); v = vis_products(); rec("filter Salgados -> only scone", v == ["scone-queijo"], v, vp)
    click(page, "filter-sweet"); v = vis_products(); rec("filter Doces -> 4 sweet", sorted(v) == sorted(ids[:4]), v, vp)
    click(page, "filter-all"); v = vis_products(); rec("filter Todos -> 5", len(v) == 5, v, vp)
    if vp == "1440x900": shot(page, "catalog")
    else: shot(page, "catalog")
    click(page, "product-bolo-maca"); body = page.inner_text("body").lower()
    rec("bolo-maca states ice cream not included", "sorvete" in body and ("não acompanha" in body or "nao acompanha" in body), viewport=vp)
    rec("allergen notice on detail", "alérgenos" in body, viewport=vp)
    page.go_back(); page.wait_for_timeout(400)
    rec("browser back returns from detail", len(visible_tid(page, "product-no-cardamomo")) > 0 or len(visible_tid(page, "filter-all")) > 0, viewport=vp)
    click(page, "nav-catalog"); click(page, "filter-all"); click(page, "product-no-cardamomo")
    shot(page, "product")
    click(page, "add-order"); click(page, "nav-order")
    q = visible_tid(page, "order-quantity")
    rec("order line has quantity control", len(q) == 1, len(q), vp)
    q[0].fill("2") if q[0].evaluate("e=>e.tagName") == "INPUT" else q[0].select_option("2")
    q[0].dispatch_event("change"); q[0].dispatch_event("input"); page.wait_for_timeout(400)
    sub = " ".join(x.inner_text() for x in visible_tid(page, "order-subtotal"))
    rec("2 x Nó de cardamomo = 5,60", 5.6 in money(sub), sub, vp)
    q[0].fill("0") if q[0].evaluate("e=>e.tagName") == "INPUT" else None
    q[0].dispatch_event("change"); page.wait_for_timeout(300)
    sub0 = " ".join(x.inner_text() for x in visible_tid(page, "order-subtotal"))
    rec("invalid quantity never negative/NaN", "NaN" not in sub0 and "-" not in sub0, sub0, vp)
    q = visible_tid(page, "order-quantity")
    if q:
        q[0].fill("2") if q[0].evaluate("e=>e.tagName") == "INPUT" else q[0].select_option("2")
        q[0].dispatch_event("change"); page.wait_for_timeout(300)
    slots = visible_tid(page, "pickup-slot")
    if slots and slots[0].evaluate("e=>e.tagName") == "SELECT":
        opts = slots[0].evaluate("e=>[...e.options].map(o=>o.value).filter(v=>v)"); slots[0].select_option(opts[0])
    elif slots:
        slots[0].check(force=True) if slots[0].evaluate("e=>e.type") == "radio" else slots[0].click()
    else:
        lab = page.locator('[data-testid="pickup-slot"]')
        lab.first.check(force=True) if lab.count() else None
    rec("pickup slot control present", page.locator('[data-testid="pickup-slot"]').count() > 0, page.locator('[data-testid="pickup-slot"]').count(), vp)
    shot(page, "order-filled")
    click(page, "order-review")
    summ = visible_tid(page, "order-summary")
    rec("review shows local summary", len(summ) > 0 and "5" in summ[0].inner_text(), summ[0].inner_text()[:120] if summ else "none", vp)
    shot(page, "order-review")
    body = page.inner_text("body")
    rec("prototype disclaimer in order", "Nenhuma encomenda é enviada" in body, viewport=vp)
    if not visible_tid(page, "order-remove"):
        click(page, "nav-order")
    click(page, "order-remove")
    rec("remove -> empty state", len(visible_tid(page, "order-empty")) > 0, viewport=vp)

def plan(page, session, people):
    sel = page.locator('[data-testid="plan-session"]')
    if sel.first.evaluate("e=>e.tagName") == "SELECT":
        opts = sel.first.evaluate("e=>[...e.options].map(o=>[o.value,o.textContent])")
        val = next((v for v, t in opts if session in v or session.replace('-', ' ') in t.lower()), None)
        if val is None:
            label = {"aberta": "aberta", "nascer-sol": "nascer", "privativa": "privativa"}[session]
            val = next(v for v, t in opts if label in t.lower())
        sel.first.select_option(val)
    else:
        target = page.locator(f'[data-testid="plan-session"][value*="{session}"]')
        if target.count() == 0:
            target = page.locator('[data-testid="plan-session"]').filter(has_text=re.compile(session.split('-')[0], re.I))
        target.first.check(force=True) if target.first.evaluate("e=>e.type") == "radio" else target.first.click()
    pp = visible_tid(page, "plan-people")[0]
    pp.fill(str(people)); pp.dispatch_event("input"); pp.dispatch_event("change"); page.wait_for_timeout(400)
    tot = " ".join(x.inner_text() for x in visible_tid(page, "plan-total"))
    err = visible_tid(page, "plan-error")
    return tot, bool(err and err[0].inner_text().strip())

def b2_tasks(page, vp):
    click(page, "nav-schedule")
    def slots():
        return [s.get_attribute("data-session") for s in visible_tid(page, "schedule-slot")]
    click(page, "schedule-filter-all"); s_all = slots(); rec("schedule Todas shows 16 slots", len(s_all) == 16, f"{len(s_all)} {sorted(set(s_all))}", vp)
    click(page, "schedule-filter-sunrise"); s = slots(); rec("filter Nascer do sol -> 2 sunrise only", len(s) == 2 and set(s) == {"nascer-sol"}, s, vp)
    click(page, "schedule-filter-all")
    shot(page, "schedule")
    for sid in ["aberta", "nascer-sol", "privativa"]:
        if not visible_tid(page, f"session-{sid}"):
            click(page, "nav-schedule")
        click(page, f"session-{sid}")
        body = page.inner_text("body")
        price = {"aberta": "18", "nascer-sol": "22", "privativa": "120"}[sid]
        rec(f"session {sid} detail shows price", price in body, viewport=vp)
        if sid == "aberta": shot(page, "session")
        page.go_back(); page.wait_for_timeout(400)
    click(page, "nav-plan")
    for sess, n, exp in [("aberta", 3, 54), ("nascer-sol", 2, 44), ("privativa", 4, 120)]:
        tot, err = plan(page, sess, n); rec(f"plan {sess} x{n} = {exp}", (exp in money(tot)) and not err, tot, vp)
    shot(page, "plan")
    for sess, n in [("aberta", 9), ("privativa", 7)]:
        tot, err = plan(page, sess, n); rec(f"plan {sess} x{n} -> error, no misleading total", err and not any(v > 0 and v not in (8, 6, 1, 7, 9) for v in money(tot)), f"err={err} total='{tot}'", vp)
    shot(page, "plan-error")
    body = page.inner_text("body"); rec("prototype disclaimer in planner", "Nada é reservado" in body, viewport=vp)

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
        rec("hero copy preserved", ("O pão de sábado começa na sexta." if BRIEF == "B1" else "Aqueça. Mergulhe. Descanse.") in body.replace("\n", " "), viewport=vp)
        rec("footer prototype disclaimer", "Protótipo demonstrativo" in body, viewport=vp)
        LABEL_ORIG = LABEL
        globals()["LABEL"] = f"{LABEL_ORIG}-{w}"
        try:
            (b1_tasks if BRIEF == "B1" else b2_tasks)(page, vp)
        except Exception as e:
            rec("task sequence completed", f"ERROR", repr(e)[:250], vp)
        globals()["LABEL"] = LABEL_ORIG
        rec("no script/console errors", not page._errors, page._errors[:5], vp)
        rec("no external network requests", not page._external, page._external[:5], vp)
        ctx.close()
    for (w, h) in [(768, 1024), (320, 740)]:
        ctx, page = new_page(b, w, h)
        rec("no horizontal overflow (home)", overflow(page) <= 1, overflow(page), f"{w}x{h}")
        if w == 768: shot(page, "768-home")
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
