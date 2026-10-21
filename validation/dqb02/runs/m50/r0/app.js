(function () {
  'use strict';

  var A = 'assets/';
  var PRODUCTS = [
    {
      id: 'no-cardamomo', name: 'Nó de cardamomo', cat: 'doce', price: 280, unit: 'unidade',
      desc: 'Massa enriquecida, enrolada em nó, com açúcar e cardamomo.',
      photos: [
        { f: 'cardamom-buns.jpg', alt: 'Tigela de madeira com nós de cardamomo dourados sobre pano xadrez vermelho e branco.', pos: '50% 45%' },
        { f: 'two-layers-of-cardamom-buns-on-grate.jpg', alt: 'Grade de metal coberta por duas camadas de nós de cardamomo polvilhados com açúcar.', pos: '50% 50%' },
        { f: 'one-layer-of-cardamom-buns-on-grate.jpg', alt: 'Uma camada de nós de cardamomo enfileirados sobre grade de metal.', pos: '50% 50%' },
        { f: 'cardamom-buns-on-grate-under-towel.jpg', alt: 'Nós de cardamomo em grade de metal, parcialmente cobertos por um pano claro.', pos: '55% 60%' }
      ]
    },
    {
      id: 'muffin-baunilha', name: 'Muffin de baunilha', cat: 'doce', price: 250, unit: 'unidade',
      desc: 'Massa simples de baunilha, assada em forminha de papel.',
      photos: [
        { f: 'plain-vanilla-muffin.jpg', alt: 'Um muffin de baunilha em forminha de papel pregueada sobre papel amassado.', pos: '50% 50%' },
        { f: 'plain-vanilla-muffins-1.jpg', alt: 'Três muffins de baunilha em forminhas de papel.', pos: '50% 50%' },
        { f: 'plain-vanilla-muffins-2.jpg', alt: 'Três muffins de baunilha vistos de perto, com o topo rachado.', pos: '50% 50%' },
        { f: 'plain-vanilla-muffins-3.jpg', alt: 'Três muffins de baunilha em forminhas sobre papel claro.', pos: '50% 50%' }
      ]
    },
    {
      id: 'torta-morango', name: 'Torta de morango', cat: 'doce', price: 2400, unit: 'inteira, 8 fatias',
      desc: 'Base amanteigada coberta de morangos.',
      photos: [
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-3.jpg', alt: 'Torta de morango inteira sobre a base de uma forma de aro removível, morangos fatiados e brilhantes por cima.', pos: '50% 55%' },
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-1.jpg', alt: 'Torta de morango ainda dentro da forma de aro removível, vista de cima e de lado.', pos: '50% 50%' },
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-2.jpg', alt: 'Forma de aro removível com a torta de morango, vista lateral com a trava da forma.', pos: '50% 50%' }
      ]
    },
    {
      id: 'bolo-maca', name: 'Bolo de maçã', cat: 'doce', price: 420, unit: 'fatia',
      desc: 'Bolo de maçã com canela.',
      iceCream: true,
      photos: [
        { f: 'apple-cake-with-vanilla-ice-cream-2.jpg', alt: 'Fatia de bolo de maçã com canela num prato branco, servida com uma bola de sorvete que não acompanha o produto.', pos: '45% 50%' },
        { f: 'apple-cake-with-vanilla-ice-cream-1.jpg', alt: 'Fatia de bolo de maçã vista de lado, com uma bola de sorvete por cima que não acompanha o produto.', pos: '45% 50%' }
      ]
    },
    {
      id: 'scone-queijo', name: 'Scone de queijo', cat: 'salgado', price: 300, unit: 'unidade',
      desc: 'Scone salgado com queijo.',
      photos: [
        { f: 'swedish-cheese-scones.jpg', alt: 'Scones de queijo dourados e irregulares sobre papel manteiga.', pos: '40% 60%' }
      ]
    }
  ];
  var BY_ID = {};
  PRODUCTS.forEach(function (p) { BY_ID[p.id] = p; });

  var SLOTS = ['08:00–09:00', '09:00–10:00', '10:00–11:00', '11:00–12:00'];
  var MAX = 12, MIN = 1;
  var NOTICE = 'Protótipo demonstrativo. Marca, produtos e preços fictícios. Nenhuma encomenda é enviada.';
  var ICE = 'A bola de sorvete aparece só na foto: o sorvete não acompanha o bolo.';
  var ALLERGEN = 'Informações sobre alérgenos não disponíveis neste protótipo.';

  /* ---------- state ---------- */
  var STORE_KEY = 'miolo-encomenda-v1';
  var state = { items: [], slot: '', reviewed: false };
  try {
    var saved = JSON.parse(localStorage.getItem(STORE_KEY) || 'null');
    if (saved && Array.isArray(saved.items)) {
      state.items = saved.items.filter(function (it) { return BY_ID[it.id]; }).map(function (it) { return { id: it.id, qty: clamp(it.qty) }; });
      state.slot = SLOTS.indexOf(saved.slot) >= 0 ? saved.slot : '';
    }
  } catch (e) { /* armazenamento indisponível: segue só em memória */ }
  function persist() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify({ items: state.items, slot: state.slot })); } catch (e) {}
  }
  var catalogFilter = 'todos';

  function clamp(n) {
    n = parseInt(n, 10);
    if (!isFinite(n) || isNaN(n)) return MIN;
    return Math.max(MIN, Math.min(MAX, n));
  }
  function eur(cents) {
    cents = Math.max(0, Math.round(Number(cents) || 0));
    return '€' + Math.floor(cents / 100) + ',' + String(cents % 100).padStart(2, '0');
  }
  function totalCents() {
    return state.items.reduce(function (s, it) { return s + BY_ID[it.id].price * clamp(it.qty); }, 0);
  }
  function itemCount() {
    return state.items.reduce(function (s, it) { return s + clamp(it.qty); }, 0);
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; });
  }
  function catLabel(c) { return c === 'salgado' ? 'Salgado' : 'Doce'; }

  /* ---------- icons (SVG simples, feitos à mão) ---------- */
  var ICON = {
    moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M19 14.5A7.5 7.5 0 0 1 9.5 5a7.5 7.5 0 1 0 9.5 9.5Z"/></svg>',
    oven: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3.5" y="4.5" width="17" height="15" rx="2"/><path d="M3.5 9h17"/><rect x="7" y="12" width="10" height="4.5" rx="1"/><path d="M7 6.8h.01M10 6.8h.01"/></svg>',
    sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/></svg>',
    info: '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="8" cy="8" r="6.5"/><path d="M8 7.2v4M8 4.8h.01"/></svg>',
    basket: '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M10 26h44l-5 26a3 3 0 0 1-3 2.5H18a3 3 0 0 1-3-2.5L10 26Z"/><path d="M22 26l8-14M42 26l-8-14"/><path d="M24 36v10M32 36v10M40 36v10" stroke-dasharray="2 4"/></svg>',
    back: '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M10 3 5 8l5 5"/></svg>',
    check: '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m4 9.5 3.2 3L14 5.5"/></svg>'
  };

  /* ---------- components ---------- */
  function card(p, headingTag) {
    var ph = p.photos[0];
    var h = headingTag || 'h3';
    return '<a class="card" href="#/produto/' + p.id + '" data-testid="product-' + p.id + '">' +
      '<div class="card__img"><img src="' + A + ph.f + '" alt="' + esc(ph.alt) + '" style="object-position:' + ph.pos + '" loading="lazy" width="640" height="480"></div>' +
      '<div class="card__body">' +
        '<span class="tag' + (p.cat === 'salgado' ? ' tag--savory' : '') + '">' + catLabel(p.cat) + '</span>' +
        '<div class="card__top"><' + h + '>' + esc(p.name) + '</' + h + '><span class="price">' + eur(p.price) + '</span></div>' +
        '<p class="card__unit">por ' + esc(p.unit) + '</p>' +
        '<p class="card__desc">' + esc(p.desc) + '</p>' +
        (p.iceCream ? '<p class="note">' + ICON.info + '<span>' + ICE + '</span></p>' : '') +
        '<span class="card__more">Ver detalhes <span class="arrow" aria-hidden="true">→</span></span>' +
      '</div></a>';
  }
  function stepperHTML(id, val, label, testid) {
    return '<div class="stepper" role="group" aria-label="' + esc(label) + '">' +
      '<button type="button" data-step="-1" data-for="' + id + '" aria-label="Diminuir quantidade"' + (val <= MIN ? ' disabled' : '') + '>−</button>' +
      '<input id="' + id + '" type="number" inputmode="numeric" min="1" max="12" step="1" value="' + val + '" aria-label="' + esc(label) + '"' + (testid ? ' data-testid="' + testid + '"' : '') + '>' +
      '<button type="button" data-step="1" data-for="' + id + '" aria-label="Aumentar quantidade"' + (val >= MAX ? ' disabled' : '') + '>+</button>' +
    '</div>';
  }
  function syncStepper(input) {
    var v = clamp(input.value);
    input.value = v;
    var g = input.parentNode;
    g.querySelector('[data-step="-1"]').disabled = v <= MIN;
    g.querySelector('[data-step="1"]').disabled = v >= MAX;
    return v;
  }

  /* ---------- views ---------- */
  function viewHome() {
    var featured = ['no-cardamomo', 'torta-morango', 'scone-queijo'].map(function (id) { return card(BY_ID[id]); }).join('');
    return '<div class="view">' +
      '<section class="hero" aria-labelledby="hero-t"><div class="wrap hero__grid">' +
        '<div>' +
          '<p class="eyebrow">Micro-padaria no Vale · uma fornada por semana</p>' +
          '<h1 id="hero-t">O pão de sábado começa <em>na sexta.</em></h1>' +
          '<p class="hero__lede">Encomende até sexta, 18h. Retire no sábado entre 8h e 12h, ainda morno.</p>' +
          '<div class="hero__actions"><a class="btn btn--primary" href="#/fornada">Ver a fornada <span class="arrow" aria-hidden="true">→</span></a>' +
          '<a class="textlink" href="#como-funciona" data-scroll="como-funciona">Como funciona</a></div>' +
          '<div class="ticket" aria-label="Prazos da semana"><div><b>Encomendas</b>até sexta, 18h</div><div><b>Retirada</b>sábado, 8h–12h</div></div>' +
        '</div>' +
        '<figure class="hero__photo" style="margin:0"><div class="arch"><img src="' + A + 'cardamom-buns-on-grate-under-towel.jpg" alt="Nós de cardamomo em grade de metal, parcialmente cobertos por um pano claro, sobre toalha xadrez." width="960" height="1200"></div>' +
        '<figcaption class="photo-note">Foto ilustrativa: nós de cardamomo descansando sob o pano.</figcaption></figure>' +
      '</div></section>' +

      '<section class="night" id="como-funciona" aria-labelledby="how-t" tabindex="-1"><div class="wrap how">' +
        '<div class="how__head"><div><p class="eyebrow">Como funciona</p><h2 id="how-t">Da noite de sexta à manhã de sábado.</h2></div>' +
        '<p class="how__aside">Assamos uma vez por semana, só o que foi encomendado. Por isso a encomenda fecha na sexta.</p></div>' +
        '<ol class="steps">' +
          '<li class="step"><div class="step__dot">' + ICON.moon + '</div><p class="step__when">1 · Até sexta</p><h3>Escolha até sexta, 18h</h3><p>Veja a fornada, monte a encomenda e escolha um horário de retirada.</p></li>' +
          '<li class="step"><div class="step__dot">' + ICON.oven + '</div><p class="step__when">2 · Madrugada</p><h3>Assamos na madrugada de sábado</h3><p>A massa preparada na sexta à noite vai ao forno antes de o bairro acordar.</p></li>' +
          '<li class="step"><div class="step__dot">' + ICON.sun + '</div><p class="step__when">3 · Sábado de manhã</p><h3>Retire entre 8h e 12h</h3><p>Escolha uma janela de uma hora. A encomenda espera por você, ainda morna.</p></li>' +
        '</ol>' +
      '</div></section>' +

      '<section class="about" aria-labelledby="about-t"><div class="wrap about__grid">' +
        '<figure style="margin:0"><div class="about__photo"><img src="' + A + 'two-layers-of-cardamom-buns-on-grate.jpg" alt="Grade de metal com duas camadas de nós de cardamomo polvilhados com açúcar." loading="lazy" width="960" height="640"></div>' +
        '<figcaption class="photo-note">Foto ilustrativa.</figcaption></figure>' +
        '<div><p class="eyebrow">A padaria</p><h2 id="about-t">Uma fornada só, feita para quem encomendou.</h2>' +
        '<p>Miolo é uma micro-padaria de bairro no Vale. Preparamos a massa na sexta à noite e assamos uma única fornada no sábado de manhã.</p>' +
        '<p>São cinco itens nesta semana, quatro doces e um salgado. Escolha com calma até sexta, 18h, e passe para buscar no horário que reservou.</p></div>' +
      '</div></section>' +

      '<section class="featured" aria-labelledby="feat-t"><div class="wrap">' +
        '<div class="section-head"><div><p class="eyebrow">Destaques da fornada</p><h2 id="feat-t">Neste sábado sai do forno</h2></div>' +
        '<a class="btn btn--ghost" href="#/fornada">Ver os cinco itens <span class="arrow" aria-hidden="true">→</span></a></div>' +
        '<div class="grid">' + featured + '</div>' +
      '</div></section>' +
    '</div>';
  }

  function viewCatalog() {
    var counts = { todos: PRODUCTS.length, doce: 0, salgado: 0 };
    PRODUCTS.forEach(function (p) { counts[p.cat]++; });
    function chip(key, label, testid) {
      return '<button type="button" class="chip" data-filter="' + key + '" data-testid="' + testid + '" aria-pressed="' + (catalogFilter === key) + '">' + label + ' <span class="n">' + counts[key] + '</span></button>';
    }
    return '<div class="view"><div class="wrap catalog">' +
      '<div class="pagehead"><p class="eyebrow">Fornada de sábado</p><h1>A fornada</h1>' +
      '<p>Tudo o que vai ao forno neste sábado. Abra um item para ver fotos e escolher a quantidade. Encomendas até sexta, 18h.</p></div>' +
      '<div class="filters" role="group" aria-label="Filtrar por categoria">' +
        chip('todos', 'Todos', 'filter-all') + chip('doce', 'Doces', 'filter-sweet') + chip('salgado', 'Salgados', 'filter-savory') +
      '</div>' +
      '<p class="result-line" id="resultLine" aria-live="polite"></p>' +
      '<div class="grid" id="catalogGrid"></div>' +
    '</div></div>';
  }
  function renderCatalogGrid() {
    var list = PRODUCTS.filter(function (p) { return catalogFilter === 'todos' || p.cat === catalogFilter; });
    var grid = document.getElementById('catalogGrid');
    if (!grid) return;
    grid.innerHTML = list.map(function (p) { return card(p, 'h2'); }).join('');
    var label = { todos: 'Todos os itens', doce: 'Doces', salgado: 'Salgados' }[catalogFilter];
    document.getElementById('resultLine').textContent = label + ' · ' + list.length + (list.length === 1 ? ' item' : ' itens');
    document.querySelectorAll('[data-filter]').forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === catalogFilter)); });
  }

  function viewProduct(p) {
    var thumbs = p.photos.length > 1 ? '<div class="thumbs" role="group" aria-label="Escolher foto">' + p.photos.map(function (ph, i) {
      return '<button type="button" class="thumb" data-photo="' + i + '" aria-pressed="' + (i === 0) + '" aria-label="Foto ' + (i + 1) + ' de ' + p.photos.length + '"><img src="' + A + ph.f + '" alt="" style="object-position:' + ph.pos + '" loading="lazy"></button>';
    }).join('') + '</div>' : '';
    var ph = p.photos[0];
    return '<div class="view"><div class="wrap">' +
      '<nav class="crumbs" aria-label="Voltar"><a href="#/fornada">' + ICON.back + ' Voltar para a fornada</a></nav>' +
      '<article class="detail">' +
        '<div class="gallery"><figure style="margin:0"><div class="gallery__main"><img id="mainPhoto" src="' + A + ph.f + '" alt="' + esc(ph.alt) + '" style="object-position:' + ph.pos + '" width="960" height="768"></div>' +
        (p.iceCream ? '<figcaption class="note" style="margin-top:10px">' + ICON.info + '<span><strong>Sobre a foto:</strong> ' + ICE + '</span></figcaption>' : '<figcaption class="photo-note">Foto ilustrativa.</figcaption>') +
        '</figure>' + thumbs + '</div>' +
        '<div class="detail__info">' +
          '<span class="tag' + (p.cat === 'salgado' ? ' tag--savory' : '') + '">' + catLabel(p.cat) + '</span>' +
          '<h1>' + esc(p.name) + '</h1>' +
          '<p class="detail__price"><span class="price">' + eur(p.price) + '</span><span>por ' + esc(p.unit) + '</span></p>' +
          '<p class="detail__desc">' + esc(p.desc) + '</p>' +
          (p.iceCream ? '<p class="callout">' + ICE + ' Vendemos só a fatia de bolo.</p>' : '') +
          '<p class="callout callout--muted">' + ALLERGEN + '</p>' +
          '<div class="buy">' +
            '<div class="qty"><label for="qty-detail">Quantidade</label>' + stepperHTML('qty-detail', 1, 'Quantidade de ' + p.name) + '</div>' +
            '<button type="button" class="btn btn--primary" id="addBtn" data-testid="add-order">Adicionar à encomenda</button>' +
          '</div>' +
          '<p class="added" id="addedMsg" role="status" hidden></p>' +
        '</div>' +
      '</article>' +
    '</div></div>';
  }

  function viewOrder() {
    return '<div class="view"><div class="wrap">' +
      '<div class="pagehead"><p class="eyebrow">Encomenda demonstrativa</p><h1>Sua encomenda</h1>' +
      '<p>Ajuste as quantidades, escolha uma janela de retirada no sábado e revise. Nada é enviado.</p></div>' +
      '<div class="order">' +
        '<section class="slip" aria-labelledby="slip-t"><h2 id="slip-t">Itens</h2><div id="lines"></div></section>' +
        '<aside class="side" aria-label="Retirada e total">' +
          '<div class="slip">' +
            '<fieldset><legend>Horário de retirada</legend><p class="legend-hint">Sábado. Escolha uma janela (obrigatório).</p>' +
            '<div class="slots">' + SLOTS.map(function (s, i) {
              return '<label class="slot"><input type="radio" name="slot" value="' + s + '" data-testid="pickup-slot"' + (state.slot === s ? ' checked' : '') + ' aria-describedby="slotErr"><span>' + s + '</span></label>';
            }).join('') + '</div></fieldset>' +
            '<div class="totals" style="margin-top:20px"><span>Total</span><output id="subtotal" data-testid="order-subtotal" aria-live="polite">' + eur(totalCents()) + '</output></div>' +
            '<p class="error" id="slotErr" role="alert"></p>' +
            '<button type="button" class="btn btn--dark" id="reviewBtn" data-testid="order-review">Revisar encomenda</button>' +
          '</div>' +
          '<p class="notice-box"><strong>Protótipo demonstrativo.</strong> Marca, produtos e preços fictícios. Nenhuma encomenda é enviada.</p>' +
        '</aside>' +
      '</div>' +
      '<div id="summaryHost"></div>' +
    '</div></div>';
  }
  function renderLines() {
    var host = document.getElementById('lines');
    if (!host) return;
    if (!state.items.length) {
      host.innerHTML = '<div class="empty" data-testid="order-empty">' + ICON.basket + '<h2>Sua encomenda está vazia</h2><p>Escolha itens da fornada de sábado. Você pode encomendar até sexta, 18h.</p><a class="btn btn--primary" href="#/fornada">Ver a fornada <span class="arrow" aria-hidden="true">→</span></a></div>';
    } else {
      host.innerHTML = '<ul class="lines">' + state.items.map(function (it) {
        var p = BY_ID[it.id], q = clamp(it.qty), ph = p.photos[0];
        return '<li class="line" data-line="' + p.id + '">' +
          '<div class="line__img"><img src="' + A + ph.f + '" alt="" style="object-position:' + ph.pos + '"></div>' +
          '<div><p class="line__name"><a href="#/produto/' + p.id + '">' + esc(p.name) + '</a></p><p class="line__unit">' + eur(p.price) + ' / ' + esc(p.unit) + '</p></div>' +
          '<div class="line__total" data-line-total>' + eur(p.price * q) + '</div>' +
          '<div class="line__ctrl">' + stepperHTML('qty-' + p.id, q, 'Quantidade de ' + p.name + ' (1 a 12)', 'order-quantity') +
          '<button type="button" class="remove" data-remove="' + p.id + '" data-testid="order-remove" aria-label="Remover ' + esc(p.name) + ' da encomenda">Remover</button></div>' +
        '</li>';
      }).join('') + '</ul>';
    }
    updateTotals();
  }
  function updateTotals() {
    var st = document.getElementById('subtotal');
    if (st) st.textContent = eur(totalCents());
    var n = itemCount();
    var c = document.getElementById('navCount');
    c.textContent = n;
    c.setAttribute('data-zero', String(n === 0));
    c.setAttribute('aria-label', n === 1 ? '1 item' : n + ' itens');
  }
  function clearSummary() {
    var h = document.getElementById('summaryHost');
    if (h && h.innerHTML) { h.innerHTML = ''; }
    state.reviewed = false;
  }
  function review() {
    var err = document.getElementById('slotErr');
    err.textContent = '';
    if (!state.items.length) { err.textContent = 'Adicione pelo menos um item da fornada antes de revisar.'; return; }
    if (!state.slot) {
      err.textContent = 'Escolha um horário de retirada para revisar a encomenda.';
      var first = document.querySelector('input[name="slot"]');
      if (first) first.focus();
      return;
    }
    var rows = state.items.map(function (it) {
      var p = BY_ID[it.id], q = clamp(it.qty);
      return '<dt>' + q + ' × ' + esc(p.name) + ' <span class="mono" style="color:var(--crust-2);font-size:14px">(' + eur(p.price) + ' / ' + esc(p.unit) + ')</span></dt><dd>' + eur(p.price * q) + '</dd>';
    }).join('');
    var host = document.getElementById('summaryHost');
    host.innerHTML = '<section class="summary" data-testid="order-summary" tabindex="-1" id="summary" aria-labelledby="sum-t">' +
      '<p class="eyebrow">Resumo local</p><h2 id="sum-t">Resumo da encomenda</h2>' +
      '<p class="slotline">Retirada: sábado, ' + esc(state.slot) + '</p>' +
      '<dl>' + rows + '<dt class="sum-total">Total</dt><dd class="sum-total">' + eur(totalCents()) + '</dd></dl>' +
      '<p class="notice-box">' + NOTICE + ' Este resumo existe só nesta página.</p>' +
      '<div class="actions"><button type="button" class="btn btn--ghost" id="editBtn">Alterar encomenda</button><a class="btn btn--ghost" href="#/fornada">Voltar para a fornada</a></div>' +
    '</section>';
    state.reviewed = true;
    var s = document.getElementById('summary');
    s.focus({ preventScroll: true });
    s.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth', block: 'start' });
  }

  function viewCredits() {
    var used = {};
    PRODUCTS.forEach(function (p) { p.photos.forEach(function (ph) { used[ph.f] = true; }); });
    var list = (window.MIOLO_CREDITS || []).filter(function (c) { return used[c.file]; });
    return '<div class="view"><div class="wrap credits">' +
      '<div class="pagehead"><p class="eyebrow">Créditos</p><h1>Fotografias</h1>' +
      '<p>Fotografias ilustrativas de terceiros, sob licenças CC0, CC BY 4.0 e CC BY-SA 4.0. Elas não mostram produtos nem o local da Miolo, que é uma marca fictícia. As imagens foram usadas sem alteração de pixels; apenas o enquadramento é feito na página.</p></div>' +
      '<ul class="credit-list">' + list.map(function (c) {
        return '<li class="credit"><img src="' + A + c.file + '" alt="" loading="lazy"><p><span class="t">' + esc(c.title) + '</span><br>Autor: ' + esc(c.author) + ' · Licença: <a href="' + esc(c.license_url) + '" rel="noopener noreferrer" target="_blank">' + esc(c.license) + '</a><br><a href="' + esc(c.source) + '" rel="noopener noreferrer" target="_blank">Fonte no Wikimedia Commons</a></p></li>';
      }).join('') + '</ul>' +
    '</div></div>';
  }

  function viewNotFound() {
    return '<div class="view"><div class="wrap pagehead"><h1>Página não encontrada</h1><p>Esse endereço não existe neste protótipo.</p><p style="margin-top:20px"><a class="btn btn--primary" href="#/fornada">Ver a fornada</a></p></div></div>';
  }

  /* ---------- router ---------- */
  var main = document.getElementById('main');
  var live = document.getElementById('live');
  function reduceMotion() { return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches; }

  function route() {
    var h = location.hash || '#/';
    if (h.indexOf('#/') !== 0) return; // âncora interna
    var parts = h.slice(2).split('/');
    var key = parts[0] || '';
    var title = 'Miolo · Fornada de sábado';
    var nav = '';
    if (key === '') { main.innerHTML = viewHome(); }
    else if (key === 'fornada') {
      if (parts[1] === 'doces') catalogFilter = 'doce';
      else if (parts[1] === 'salgados') catalogFilter = 'salgado';
      else catalogFilter = 'todos';
      main.innerHTML = viewCatalog(); renderCatalogGrid(); title = 'A fornada · Miolo'; nav = 'fornada';
    }
    else if (key === 'produto' && BY_ID[parts[1]]) { main.innerHTML = viewProduct(BY_ID[parts[1]]); title = BY_ID[parts[1]].name + ' · Miolo'; nav = 'fornada'; }
    else if (key === 'encomenda') { main.innerHTML = viewOrder(); renderLines(); title = 'Sua encomenda · Miolo'; nav = 'encomenda'; }
    else if (key === 'creditos') { main.innerHTML = viewCredits(); title = 'Créditos das fotos · Miolo'; }
    else { main.innerHTML = viewNotFound(); title = 'Não encontrada · Miolo'; }
    document.title = title;
    document.querySelectorAll('[data-nav]').forEach(function (a) {
      if (a.getAttribute('data-nav') === nav) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    updateTotals();
    window.scrollTo(0, 0);
    if (route.started) { main.focus({ preventScroll: true }); live.textContent = title.split(' · ')[0]; }
    route.started = true;
  }

  /* ---------- events ---------- */
  document.addEventListener('click', function (e) {
    var t = e.target;
    var sc = t.closest('[data-scroll]');
    if (sc) {
      e.preventDefault();
      var target = document.getElementById(sc.getAttribute('data-scroll'));
      if (target) { target.scrollIntoView({ behavior: reduceMotion() ? 'auto' : 'smooth' }); target.focus({ preventScroll: true }); }
      return;
    }
    var f = t.closest('[data-filter]');
    if (f) {
      catalogFilter = f.getAttribute('data-filter');
      var slug = { todos: '', doce: '/doces', salgado: '/salgados' }[catalogFilter];
      history.replaceState(null, '', '#/fornada' + slug);
      renderCatalogGrid();
      return;
    }
    var st = t.closest('[data-step]');
    if (st) {
      var input = document.getElementById(st.getAttribute('data-for'));
      input.value = clamp(input.value) + parseInt(st.getAttribute('data-step'), 10);
      input.dispatchEvent(new Event('change', { bubbles: true }));
      return;
    }
    var th = t.closest('[data-photo]');
    if (th) {
      var p = BY_ID[(location.hash.split('/')[2] || '')];
      var ph = p && p.photos[+th.getAttribute('data-photo')];
      if (!ph) return;
      var img = document.getElementById('mainPhoto');
      img.src = A + ph.f; img.alt = ph.alt; img.style.objectPosition = ph.pos;
      document.querySelectorAll('[data-photo]').forEach(function (b) { b.setAttribute('aria-pressed', String(b === th)); });
      return;
    }
    if (t.closest('#addBtn')) {
      var id = location.hash.split('/')[2];
      var prod = BY_ID[id];
      if (!prod) return;
      var q = clamp(document.getElementById('qty-detail').value);
      var line = state.items.filter(function (it) { return it.id === id; })[0];
      var capped = false;
      if (line) { var nq = line.qty + q; capped = nq > MAX; line.qty = clamp(nq); }
      else state.items.push({ id: id, qty: q });
      persist(); updateTotals();
      var cur = line ? line.qty : q;
      var msg = document.getElementById('addedMsg');
      msg.hidden = false;
      msg.innerHTML = ICON.check + '<span>' + (capped ? 'Limite de 12 por item. ' : 'Adicionado. ') + 'Você tem ' + cur + ' × ' + esc(prod.name) + ' na encomenda.</span> <a class="textlink" href="#/encomenda">Ver encomenda</a>';
      return;
    }
    var rm = t.closest('[data-remove]');
    if (rm) {
      var rid = rm.getAttribute('data-remove');
      var name = BY_ID[rid].name;
      state.items = state.items.filter(function (it) { return it.id !== rid; });
      persist(); clearSummary(); renderLines();
      live.textContent = name + ' removido da encomenda.';
      var next = document.querySelector('[data-testid="order-remove"]') || document.querySelector('[data-testid="order-empty"] a');
      if (next) next.focus();
      return;
    }
    if (t.closest('#reviewBtn')) { review(); return; }
    if (t.closest('#editBtn')) {
      clearSummary();
      var firstQ = document.querySelector('[data-testid="order-quantity"]');
      if (firstQ) { firstQ.focus(); firstQ.scrollIntoView({ block: 'center', behavior: reduceMotion() ? 'auto' : 'smooth' }); }
      return;
    }
  });

  function onQty(e) {
    var input = e.target;
    if (!(input instanceof HTMLInputElement) || input.type !== 'number') return;
    if (e.type === 'input' && input.value === '') return; // deixa apagar e digitar
    var v = syncStepper(input);
    var lineEl = input.closest('[data-line]');
    if (lineEl) {
      var id = lineEl.getAttribute('data-line');
      state.items.forEach(function (it) { if (it.id === id) it.qty = v; });
      lineEl.querySelector('[data-line-total]').textContent = eur(BY_ID[id].price * v);
      persist(); clearSummary(); updateTotals();
    }
  }
  document.addEventListener('change', function (e) {
    if (e.target.name === 'slot') {
      state.slot = e.target.value; persist(); clearSummary();
      var err = document.getElementById('slotErr'); if (err) err.textContent = '';
      return;
    }
    onQty(e);
  });
  document.addEventListener('input', onQty);
  document.addEventListener('focusout', function (e) {
    var input = e.target;
    if (input instanceof HTMLInputElement && input.type === 'number' && input.value === '') { input.value = MIN; onQty({ target: input, type: 'change' }); }
  });

  window.addEventListener('hashchange', route);
  route();
})();
