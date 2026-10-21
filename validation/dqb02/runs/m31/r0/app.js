/* Miolo — protótipo demonstrativo. Sem rede, sem envio, sem dados pessoais. */
(function () {
  'use strict';
  var PRODUCTS = window.MIOLO_PRODUCTS || [];
  var CREDITS = window.MIOLO_CREDITS || [];
  var SLOTS = ['08:00–09:00', '09:00–10:00', '10:00–11:00', '11:00–12:00'];
  var MAX = 12;
  var STORE_KEY = 'miolo-demo-order-v1';
  var view = document.getElementById('view');
  var main = document.getElementById('conteudo');
  var announcer = document.getElementById('route-announcer');
  var firstRender = true;

  /* ---------- estado da encomenda (local, demonstrativo) ---------- */
  var state = { items: [], slot: null, reviewed: false };
  try {
    var saved = JSON.parse(sessionStorage.getItem(STORE_KEY) || 'null');
    if (saved && Array.isArray(saved.items)) {
      state.items = saved.items.filter(function (i) { return byId(i.id); }).map(function (i) { return { id: i.id, qty: clampQty(i.qty) }; });
      state.slot = SLOTS.indexOf(saved.slot) >= 0 ? saved.slot : null;
    }
  } catch (e) { /* armazenamento indisponível: segue só em memória */ }

  function persist() {
    try { sessionStorage.setItem(STORE_KEY, JSON.stringify({ items: state.items, slot: state.slot })); } catch (e) {}
    updateBadge();
  }
  function byId(id) { for (var i = 0; i < PRODUCTS.length; i++) if (PRODUCTS[i].id === id) return PRODUCTS[i]; return null; }
  function clampQty(v) {
    var n = parseInt(v, 10);
    if (!isFinite(n) || isNaN(n)) return 1;
    return Math.min(MAX, Math.max(1, n));
  }
  function money(cents) {
    var c = Math.max(0, Math.round(Number(cents) || 0));
    return '€' + (c / 100).toFixed(2).replace('.', ',');
  }
  function total() {
    return state.items.reduce(function (s, i) { var p = byId(i.id); return s + (p ? p.price * i.qty : 0); }, 0);
  }
  function countItems() { return state.items.reduce(function (s, i) { return s + i.qty; }, 0); }
  function updateBadge() {
    var b = document.getElementById('order-count');
    var n = countItems();
    b.textContent = n;
    b.setAttribute('aria-label', n === 1 ? '1 item' : n + ' itens');
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function img(p, i) { var ph = p.photos[i || 0]; return 'assets/' + ph.file; }
  function catLabel(c) { return c === 'salgado' ? 'Salgado' : 'Doce'; }

  /* ---------- rotas ---------- */
  function parse() {
    var h = (location.hash || '#/').replace(/^#/, '');
    var parts = h.split('/').filter(Boolean);
    return parts;
  }
  function setNav(key) {
    document.querySelectorAll('.main-nav a').forEach(function (a) {
      if (a.getAttribute('data-nav') === key) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
  }
  function render() {
    var parts = parse();
    var r = parts[0] || '';
    var title = 'Miolo · Fornada de sábado';
    if (r === '') { view.innerHTML = homeView(); setNav('home'); }
    else if (r === 'fornada') { view.innerHTML = catalogView(parts[1]); setNav('fornada'); bindCatalog(); title = 'A fornada · Miolo'; }
    else if (r === 'produto' && byId(parts[1])) { var p = byId(parts[1]); view.innerHTML = detailView(p); setNav('fornada'); bindDetail(p); title = p.name + ' · Miolo'; }
    else if (r === 'encomenda') { view.innerHTML = orderView(); setNav('encomenda'); bindOrder(); title = 'Encomenda · Miolo'; }
    else if (r === 'creditos') { view.innerHTML = creditsView(); setNav(''); title = 'Créditos das fotografias · Miolo'; }
    else { view.innerHTML = '<section class="wrap not-found"><h1>Página não encontrada</h1><p><a class="link" href="#/">Voltar ao início</a> ou <a class="link" href="#/fornada">ver a fornada</a>.</p></section>'; setNav(''); title = 'Página não encontrada · Miolo'; }
    document.title = title;
    view.style.animation = 'none'; void view.offsetWidth; view.style.animation = '';
    if (!firstRender) {
      window.scrollTo(0, 0);
      main.focus({ preventScroll: true });
      announcer.textContent = title;
    }
    firstRender = false;
    updateBadge();
  }

  /* ---------- views ---------- */
  function homeView() {
    var feat = byId('no-cardamomo');
    return '' +
      '<section class="hero"><div class="wrap hero-grid">' +
        '<div class="hero-copy">' +
          '<p class="kicker">Micro-padaria · bairro Vale</p>' +
          '<h1>O pão de sábado <em>começa na sexta.</em></h1>' +
          '<p class="hero-lede">Encomende até sexta, 18h. Retire no sábado entre 8h e 12h, ainda morno.</p>' +
          '<div class="hero-actions"><a class="btn btn-primary" href="#/fornada">Ver a fornada <span class="arrow" aria-hidden="true">→</span></a>' +
          '<a class="link" href="#como-funciona" data-scroll="como-funciona">Como funciona</a></div>' +
        '</div>' +
        '<figure class="hero-photo"><img src="assets/cardamom-buns-on-grate-under-towel.jpg" alt="Nós de cardamomo recém-assados sobre uma grade, parcialmente cobertos por um pano de prato" width="1920" height="1280">' +
        '<figcaption>Foto ilustrativa</figcaption></figure>' +
      '</div></section>' +
      '<section class="ruler" id="como-funciona" aria-labelledby="como-title" tabindex="-1">' +
        '<div class="wrap how-title"><p class="eyebrow">Como funciona</p><h2 id="como-title">Uma fornada por semana, em três tempos.</h2></div>' +
        '<div class="wrap"><ol>' +
          '<li><p class="when"><span class="dot" aria-hidden="true"></span>Até sexta, 18h</p><h3>Escolha até sexta, 18h</h3><p>Veja a fornada da semana e monte a sua encomenda. A massa é preparada na sexta à noite.</p></li>' +
          '<li><p class="when"><span class="dot" aria-hidden="true"></span>Madrugada de sábado</p><h3>Assamos na madrugada de sábado</h3><p>Uma única fornada, assada para as encomendas da semana.</p></li>' +
          '<li><p class="when"><span class="dot" aria-hidden="true"></span>Sábado, 8h–12h</p><h3>Retire entre 8h e 12h</h3><p>Escolha uma faixa de horário e passe para buscar, ainda morno.</p></li>' +
        '</ol></div>' +
      '</section>' +
      '<section class="section" aria-labelledby="destaque-title"><div class="wrap">' +
        '<div class="section-head"><div><p class="eyebrow">Nesta fornada</p><h2 id="destaque-title">Cinco itens, todos de sábado.</h2></div>' +
        '<a class="link" href="#/fornada">Ver a fornada completa →</a></div>' +
        '<div class="feature">' +
          '<a class="feature-photo" href="#/produto/' + feat.id + '" tabindex="-1" aria-hidden="true"><img src="' + img(feat, 0) + '" alt="" style="object-position:' + feat.photos[0].pos + '"></a>' +
          '<div><span class="tag">' + catLabel(feat.cat) + '</span><h3>' + esc(feat.name) + '</h3><p class="desc">' + esc(feat.desc) + '</p>' +
          '<p class="price-line"><span class="price-big">' + money(feat.price) + '</span><span class="mono">/ ' + esc(feat.unit) + '</span></p>' +
          '<a class="btn" href="#/produto/' + feat.id + '">Ver o nó de cardamomo <span class="arrow" aria-hidden="true">→</span></a></div>' +
        '</div>' +
        '<ul class="mini-list" aria-label="Itens da fornada">' + PRODUCTS.map(function (p) {
          return '<li><a href="#/produto/' + p.id + '"><span class="n">' + esc(p.name) + '</span><span class="u">' + catLabel(p.cat) + ' · ' + esc(p.unit) + '</span><span class="price">' + money(p.price) + '</span></a></li>';
        }).join('') + '</ul>' +
      '</div></section>';
  }

  var FILTERS = { todos: { label: 'Todos', test: 'filter-all' }, doces: { label: 'Doces', test: 'filter-sweet' }, salgados: { label: 'Salgados', test: 'filter-savory' } };
  function catalogView(f) {
    var key = FILTERS[f] ? f : 'todos';
    return '' +
      '<section class="wrap"><div class="cat-head"><div><p class="eyebrow">Sábado · retirada 8h–12h</p><h1>A fornada</h1>' +
      '<p>Tudo o que sai do forno neste sábado. Abra um item para ver detalhes e adicionar à encomenda.</p></div>' +
      '<div class="filters" role="group" aria-label="Filtrar a fornada">' + Object.keys(FILTERS).map(function (k) {
        return '<button type="button" data-filter="' + k + '" data-testid="' + FILTERS[k].test + '" aria-pressed="' + (k === key) + '">' + FILTERS[k].label + '</button>';
      }).join('') + '</div></div>' +
      '<p class="count" id="cat-count" aria-live="polite"></p>' +
      '<ul class="grid" id="grid">' + PRODUCTS.map(function (p) {
        return '<li data-cat="' + p.cat + '"><a class="card" href="#/produto/' + p.id + '" data-testid="product-' + p.id + '">' +
          '<div class="card-img"><img src="' + img(p, 0) + '" alt="' + esc(p.photos[0].alt) + '" style="object-position:' + p.photos[0].pos + '" loading="lazy"></div>' +
          '<div class="card-body"><h2>' + esc(p.name) + '</h2><span class="price">' + money(p.price) + '</span>' +
          '<span class="meta"><span class="tag">' + catLabel(p.cat) + '</span><span>' + esc(p.unit) + '</span></span>' +
          (p.note ? '<span class="photo-note">Sorvete da foto não acompanha.</span>' : '') +
          '</div></a></li>';
      }).join('') + '</ul></section><div class="section" style="padding-top:48px"></div>';
  }
  function applyFilter(key) {
    var grid = document.getElementById('grid');
    var shown = 0;
    grid.querySelectorAll('li').forEach(function (li) {
      var cat = li.getAttribute('data-cat');
      var ok = key === 'todos' || (key === 'doces' && cat === 'doce') || (key === 'salgados' && cat === 'salgado');
      li.hidden = !ok; if (ok) shown++;
    });
    grid.classList.toggle('is-all', key === 'todos');
    document.querySelectorAll('[data-filter]').forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === key)); });
    document.getElementById('cat-count').textContent = shown + (shown === 1 ? ' item' : ' itens') + (key === 'todos' ? ' nesta fornada' : ' · ' + FILTERS[key].label.toLowerCase());
  }
  function bindCatalog() {
    var parts = parse();
    var key = FILTERS[parts[1]] ? parts[1] : 'todos';
    applyFilter(key);
    document.querySelectorAll('[data-filter]').forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.getAttribute('data-filter');
        applyFilter(k);
        var target = k === 'todos' ? '#/fornada' : '#/fornada/' + k;
        try { history.replaceState(null, '', target); } catch (e) {}
      });
    });
  }

  function detailView(p) {
    var thumbs = p.photos.length > 1 ? '<div class="thumbs" role="group" aria-label="Outras fotos">' + p.photos.map(function (ph, i) {
      return '<button type="button" data-photo="' + i + '" aria-pressed="' + (i === 0) + '" aria-label="Foto ' + (i + 1) + ' de ' + p.photos.length + '"><img src="assets/' + ph.file + '" alt=""></button>';
    }).join('') + '</div>' : '';
    return '' +
      '<div class="wrap"><nav class="crumbs" aria-label="Trilha"><a href="#/fornada">← Voltar à fornada</a></nav>' +
      '<article class="detail">' +
        '<div><figure class="gallery-main"><img id="main-photo" src="' + img(p, 0) + '" alt="' + esc(p.photos[0].alt) + '" style="object-position:' + p.photos[0].pos + '"></figure>' +
        (p.note ? '<p class="gallery-note">' + esc(p.note) + '</p>' : '') + thumbs + '</div>' +
        '<div class="detail-info"><span class="tag">' + catLabel(p.cat) + '</span><h1>' + esc(p.name) + '</h1>' +
          '<p class="desc">' + esc(p.desc) + '</p>' +
          '<dl class="spec"><div><dt>Preço</dt><dd class="price">' + money(p.price) + '</dd></div><div><dt>Unidade</dt><dd>' + esc(p.unit) + '</dd></div><div><dt>Retirada</dt><dd>Sábado, 8h–12h</dd></div></dl>' +
          '<p class="allergen">Informações sobre alérgenos não disponíveis neste protótipo.</p>' +
          '<div class="add-row"><div class="qty-field"><label for="qty">Quantidade</label>' +
            '<div class="stepper"><button type="button" data-step="-1" aria-label="Diminuir quantidade">−</button>' +
            '<input id="qty" type="number" inputmode="numeric" min="1" max="12" step="1" value="1">' +
            '<button type="button" data-step="1" aria-label="Aumentar quantidade">+</button></div></div>' +
            '<button type="button" class="btn btn-primary" id="add" data-testid="add-order">Adicionar à encomenda</button></div>' +
          '<p class="added" id="added" role="status" aria-live="polite"></p>' +
        '</div>' +
      '</article></div>';
  }
  function bindDetail(p) {
    var qty = document.getElementById('qty');
    var minus = view.querySelector('[data-step="-1"]'), plus = view.querySelector('[data-step="1"]');
    function sync() { var v = clampQty(qty.value); qty.value = v; minus.disabled = v <= 1; plus.disabled = v >= MAX; }
    sync();
    qty.addEventListener('change', sync);
    qty.addEventListener('blur', sync);
    [minus, plus].forEach(function (b) { b.addEventListener('click', function () { qty.value = clampQty(clampQty(qty.value) + Number(b.getAttribute('data-step'))); sync(); }); });
    view.querySelectorAll('[data-photo]').forEach(function (b) {
      b.addEventListener('click', function () {
        var i = Number(b.getAttribute('data-photo')), ph = p.photos[i], m = document.getElementById('main-photo');
        m.src = 'assets/' + ph.file; m.alt = ph.alt; m.style.objectPosition = ph.pos;
        view.querySelectorAll('[data-photo]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      });
    });
    document.getElementById('add').addEventListener('click', function () {
      sync();
      var n = clampQty(qty.value);
      var line = state.items.filter(function (i) { return i.id === p.id; })[0];
      var capped = false;
      if (line) { var nv = line.qty + n; if (nv > MAX) { capped = true; nv = MAX; } line.qty = nv; }
      else state.items.push({ id: p.id, qty: n });
      state.reviewed = false;
      persist();
      var now = line ? line.qty : n;
      document.getElementById('added').innerHTML = (capped ? 'Limite de 12 por item. ' : 'Adicionado. ') + 'Na encomenda: ' + now + ' × ' + esc(p.name) + '. <a href="#/encomenda">Ver encomenda →</a>';
    });
  }

  function orderView() {
    var head = '<section class="wrap"><div class="order-head"><p class="eyebrow">Retirada no sábado, 8h–12h</p><h1>Sua encomenda</h1>' +
      '<p>Encomenda demonstrativa: ajuste as quantidades, escolha um horário de retirada e revise o resumo. Nada é enviado.</p></div>';
    if (!state.items.length) {
      return head + '<div class="order-layout"><div class="empty" data-testid="order-empty"><h2>Sua encomenda está vazia.</h2>' +
        '<p>Escolha itens da fornada de sábado até sexta, 18h.</p><a class="btn btn-primary" href="#/fornada">Ver a fornada <span class="arrow" aria-hidden="true">→</span></a>' +
        '<p class="notice-box">Protótipo demonstrativo. Marca, produtos e preços fictícios. Nenhuma encomenda é enviada.</p></div></div></section>';
    }
    var lines = state.items.map(function (i) {
      var p = byId(i.id);
      return '<li class="line" data-line="' + p.id + '"><img src="' + img(p, 0) + '" alt="" style="object-position:' + p.photos[0].pos + '">' +
        '<div><h2><a href="#/produto/' + p.id + '" style="text-decoration:none">' + esc(p.name) + '</a></h2><p class="unit"><span class="price">' + money(p.price) + '</span> / ' + esc(p.unit) + '</p>' +
        '<div class="line-controls"><label class="sr-only" for="q-' + p.id + '">Quantidade de ' + esc(p.name) + '</label>' +
        '<div class="stepper"><button type="button" data-dec="' + p.id + '" aria-label="Diminuir ' + esc(p.name) + '"' + (i.qty <= 1 ? ' disabled' : '') + '>−</button>' +
        '<input id="q-' + p.id + '" type="number" inputmode="numeric" min="1" max="12" step="1" value="' + i.qty + '" data-testid="order-quantity" data-qty="' + p.id + '">' +
        '<button type="button" data-inc="' + p.id + '" aria-label="Aumentar ' + esc(p.name) + '"' + (i.qty >= MAX ? ' disabled' : '') + '>+</button></div>' +
        '<button type="button" class="remove" data-remove="' + p.id + '" data-testid="order-remove" aria-label="Remover ' + esc(p.name) + '">Remover</button></div></div>' +
        '<div class="line-total"><span class="sr-only">Valor da linha: </span><span class="price" data-linetotal="' + p.id + '">' + money(p.price * i.qty) + '</span></div></li>';
    }).join('');
    var slots = SLOTS.map(function (s, k) {
      var a = s.split('–');
      return '<label class="slot"><input type="radio" name="pickup" value="' + s + '" data-testid="pickup-slot"' + (state.slot === s ? ' checked' : '') + ' aria-label="Sábado, das ' + a[0] + ' às ' + a[1] + '"><span><b>' + a[0] + '</b>até ' + a[1] + '</span></label>';
    }).join('');
    return head + '<div class="order-layout">' +
      '<div><ul class="lines" aria-label="Itens da encomenda">' + lines + '</ul>' +
      '<p style="margin-top:20px"><a class="link" href="#/fornada">+ Adicionar mais itens da fornada</a></p></div>' +
      '<aside class="panel" aria-labelledby="ret-title"><h2 id="ret-title">Retirada</h2><p class="hint" style="margin:0">Sábado, no Vale. Escolha uma faixa de horário.</p>' +
      '<fieldset id="slot-field" aria-describedby="slot-hint"><legend>Horário de retirada <span aria-hidden="true">*</span><span class="sr-only">(obrigatório)</span></legend>' +
      '<p class="hint" id="slot-hint">Obrigatório. Uma faixa entre 8h e 12h.</p><div class="slots">' + slots + '</div>' +
      '<div class="slot-scale" aria-hidden="true"><span>8h</span><span>9h</span><span>10h</span><span>11h</span><span>12h</span></div></fieldset>' +
      '<div class="totals"><span>Subtotal</span><span class="price-big" data-testid="order-subtotal" id="subtotal" aria-live="polite">' + money(total()) + '</span></div>' +
      '<button type="button" class="btn btn-primary" id="review" data-testid="order-review">Revisar encomenda</button>' +
      '<p class="error" id="review-error" role="alert"></p>' +
      '<p class="notice-box">Protótipo demonstrativo. Marca, produtos e preços fictícios. Nenhuma encomenda é enviada.</p>' +
      '</aside></div><div id="summary-slot"></div></section>';
  }
  function refreshOrderNumbers() {
    state.items.forEach(function (i) {
      var p = byId(i.id), el = view.querySelector('[data-linetotal="' + i.id + '"]');
      if (el) el.textContent = money(p.price * i.qty);
      var dec = view.querySelector('[data-dec="' + i.id + '"]'), inc = view.querySelector('[data-inc="' + i.id + '"]');
      if (dec) dec.disabled = i.qty <= 1; if (inc) inc.disabled = i.qty >= MAX;
    });
    document.getElementById('subtotal').textContent = money(total());
    invalidateSummary();
  }
  function invalidateSummary() {
    var s = document.getElementById('summary-slot');
    if (s && s.innerHTML) { s.innerHTML = ''; }
    state.reviewed = false;
  }
  function setQty(id, v) {
    var line = state.items.filter(function (i) { return i.id === id; })[0];
    if (!line) return;
    line.qty = clampQty(v);
    var input = view.querySelector('[data-qty="' + id + '"]'); if (input) input.value = line.qty;
    persist(); refreshOrderNumbers();
  }
  function bindOrder() {
    if (!state.items.length) return;
    view.querySelectorAll('[data-qty]').forEach(function (inp) {
      var id = inp.getAttribute('data-qty');
      inp.addEventListener('input', function () {
        var n = parseInt(inp.value, 10);
        if (!isNaN(n) && n >= 1 && n <= MAX) { var line = state.items.filter(function (i) { return i.id === id; })[0]; line.qty = n; persist(); refreshOrderNumbers(); }
      });
      inp.addEventListener('change', function () { setQty(id, inp.value); });
      inp.addEventListener('blur', function () { setQty(id, inp.value); });
    });
    view.querySelectorAll('[data-dec]').forEach(function (b) { b.addEventListener('click', function () { var id = b.getAttribute('data-dec'); var l = state.items.filter(function (i) { return i.id === id; })[0]; setQty(id, l.qty - 1); }); });
    view.querySelectorAll('[data-inc]').forEach(function (b) { b.addEventListener('click', function () { var id = b.getAttribute('data-inc'); var l = state.items.filter(function (i) { return i.id === id; })[0]; setQty(id, l.qty + 1); }); });
    view.querySelectorAll('[data-remove]').forEach(function (b) {
      b.addEventListener('click', function () {
        var id = b.getAttribute('data-remove'), name = byId(id).name;
        state.items = state.items.filter(function (i) { return i.id !== id; });
        persist();
        view.innerHTML = orderView(); bindOrder();
        announcer.textContent = name + ' removido da encomenda.';
        var next = view.querySelector('[data-remove]') || view.querySelector('[data-testid="order-empty"] .btn');
        if (next) next.focus();
      });
    });
    view.querySelectorAll('input[name="pickup"]').forEach(function (r) {
      r.addEventListener('change', function () { state.slot = r.value; persist(); document.getElementById('review-error').textContent = ''; invalidateSummary(); });
    });
    document.getElementById('review').addEventListener('click', function () {
      var err = document.getElementById('review-error');
      if (!state.slot) {
        err.textContent = 'Escolha um horário de retirada para revisar a encomenda.';
        var first = view.querySelector('input[name="pickup"]'); if (first) first.focus();
        return;
      }
      err.textContent = '';
      var rows = state.items.map(function (i) { var p = byId(i.id); return '<tr><td>' + esc(p.name) + '<br><span style="opacity:.75;font-size:.88em">' + money(p.price) + ' / ' + esc(p.unit) + '</span></td><td class="r">' + i.qty + '</td><td class="r">' + money(p.price * i.qty) + '</td></tr>'; }).join('');
      var s = document.getElementById('summary-slot');
      s.innerHTML = '<section class="summary" data-testid="order-summary" tabindex="-1" aria-labelledby="sum-title">' +
        '<h2 id="sum-title">Resumo da encomenda</h2><p class="sub">Revise antes de sexta, 18h. Este resumo fica apenas neste navegador.</p>' +
        '<table><thead><tr><th>Item</th><th class="r">Qtd.</th><th class="r">Valor</th></tr></thead><tbody>' + rows + '</tbody>' +
        '<tfoot><tr><td colspan="2">Total</td><td class="r">' + money(total()) + '</td></tr></tfoot></table>' +
        '<p class="pick">Retirada: sábado, ' + esc(state.slot.replace('–', ' às ')) + ' · Vale</p>' +
        '<p class="notice">Protótipo demonstrativo. Marca, produtos e preços fictícios. Nenhuma encomenda é enviada.</p></section>';
      state.reviewed = true;
      var sec = s.firstChild;
      var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      sec.focus({ preventScroll: true });
      sec.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    });
  }

  function creditsView() {
    return '<section class="wrap"><div class="credits-head"><p class="eyebrow">Créditos</p><h1>Fotografias</h1>' +
      '<p>Fotografias ilustrativas de terceiros, sob licenças CC0, CC BY 4.0 e CC BY-SA 4.0. Usadas sem alteração de pixels, apenas enquadradas na página. Não mostram produtos ou locais da Miolo, que é uma marca fictícia.</p></div>' +
      '<ul class="credits">' + CREDITS.map(function (c) {
        return '<li><img src="assets/' + esc(c.file) + '" alt="" loading="lazy"><div><p class="t">' + esc(c.title) + '</p>' +
          '<p class="m">Autor: ' + esc(c.author) + ' · Licença: <a href="' + esc(c.license_url) + '" rel="noopener license">' + esc(c.license) + '</a></p>' +
          '<p class="m">Fonte: <a href="' + esc(c.source) + '" rel="noopener">' + esc(c.source) + '</a></p></div></li>';
      }).join('') + '</ul></section>';
  }

  /* rolagem para âncora interna sem quebrar o roteamento por hash */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-scroll]');
    if (!a) return;
    e.preventDefault();
    var t = document.getElementById(a.getAttribute('data-scroll'));
    if (t) { var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' }); t.focus({ preventScroll: true }); }
  });

  window.addEventListener('hashchange', render);
  render();
})();
