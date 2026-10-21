/* Miolo · protótipo demonstrativo. Sem rede, sem envio. Rotas por hash. */
(function () {
  'use strict';

  var A = 'assets/';
  var PRODUCTS = [
    { id: 'no-cardamomo', name: 'Nó de cardamomo', cat: 'doce', cents: 280, unit: 'unidade',
      desc: 'Massa enriquecida, enrolada em nó, com açúcar e cardamomo.',
      photos: [
        { f: 'cardamom-buns.jpg', alt: 'Nós de cardamomo dourados, polvilhados com açúcar, numa travessa sobre toalha xadrez vermelha.', pos: '60% 45%' },
        { f: 'one-layer-of-cardamom-buns-on-grate.jpg', alt: 'Uma camada de nós de cardamomo enfileirados numa grelha de metal.', pos: '50% 50%' },
        { f: 'two-layers-of-cardamom-buns-on-grate.jpg', alt: 'Nós de cardamomo empilhados em duas camadas numa grelha.', pos: '50% 50%' },
        { f: 'cardamom-buns-on-grate-under-towel.jpg', alt: 'Nós de cardamomo numa grelha, parcialmente cobertos por um pano de algodão.', pos: '55% 60%' }
      ] },
    { id: 'muffin-baunilha', name: 'Muffin de baunilha', cat: 'doce', cents: 250, unit: 'unidade',
      desc: 'Massa simples de baunilha, assada em forminha de papel.',
      photos: [
        { f: 'plain-vanilla-muffin.jpg', alt: 'Um muffin de baunilha com a casquinha rachada, numa forminha de papel pardo.', pos: '50% 55%' },
        { f: 'plain-vanilla-muffins-1.jpg', alt: 'Três muffins de baunilha em forminhas de papel sobre papel amassado.', pos: '50% 55%' },
        { f: 'plain-vanilla-muffins-2.jpg', alt: 'Dois muffins de baunilha lado a lado em forminhas de papel.', pos: '50% 55%' },
        { f: 'plain-vanilla-muffins-3.jpg', alt: 'Três muffins de baunilha vistos de cima, em forminhas de papel.', pos: '50% 50%' }
      ] },
    { id: 'torta-morango', name: 'Torta de morango', cat: 'doce', cents: 2400, unit: 'inteira, 8 fatias',
      desc: 'Base amanteigada coberta de morangos.',
      photos: [
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-3.jpg', alt: 'Torta de morango inteira, já fora do aro, sobre a base da forma.', pos: '50% 50%' },
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-1.jpg', alt: 'Torta de morango dentro da forma de aro removível, vista de cima.', pos: '50% 55%' },
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-2.jpg', alt: 'Torta de morango na forma de aro removível, vista de lado.', pos: '50% 50%' }
      ] },
    { id: 'bolo-maca', name: 'Bolo de maçã', cat: 'doce', cents: 420, unit: 'fatia',
      desc: 'Bolo de maçã com canela.',
      note: 'O sorvete da foto não acompanha o bolo.',
      photos: [
        { f: 'apple-cake-with-vanilla-ice-cream-2.jpg', alt: 'Fatia de bolo de maçã com canela num prato branco, com uma bola de sorvete por cima, que não acompanha o produto.', pos: '45% 50%' },
        { f: 'apple-cake-with-vanilla-ice-cream-1.jpg', alt: 'Fatia de bolo de maçã vista de lado, com uma bola de sorvete por cima, que não acompanha o produto.', pos: '40% 50%' }
      ] },
    { id: 'scone-queijo', name: 'Scone de queijo', cat: 'salgado', cents: 300, unit: 'unidade',
      desc: 'Scone salgado com queijo.',
      photos: [
        { f: 'swedish-cheese-scones.jpg', alt: 'Scones de queijo dourados sobre papel manteiga.', pos: '40% 60%' }
      ] }
  ];
  var BY_ID = {};
  PRODUCTS.forEach(function (p) { BY_ID[p.id] = p; });

  var SLOTS = ['08:00–09:00', '09:00–10:00', '10:00–11:00', '11:00–12:00'];
  var NOTICE = 'Protótipo demonstrativo. Marca, produtos e preços fictícios. Nenhuma encomenda é enviada.';
  var MAXQ = 12;

  /* ---------- state (localStorage é só conveniência; falha silenciosa) ---------- */
  var KEY = 'miolo-demo-order-v1';
  var state = { items: [], slot: null, reviewed: false };
  try {
    var raw = window.localStorage.getItem(KEY);
    if (raw) {
      var s = JSON.parse(raw);
      if (s && Array.isArray(s.items)) {
        state.items = s.items.filter(function (it) { return it && BY_ID[it.id]; })
          .map(function (it) { return { id: it.id, qty: clampQty(it.qty) }; });
        state.slot = SLOTS.indexOf(s.slot) >= 0 ? s.slot : null;
      }
    }
  } catch (e) { /* sem armazenamento: segue em memória */ }
  function save() {
    try { window.localStorage.setItem(KEY, JSON.stringify({ items: state.items, slot: state.slot })); } catch (e) {}
  }

  function clampQty(v) {
    var n = Math.floor(Number(v));
    if (!isFinite(n) || n < 1) return 1;
    if (n > MAXQ) return MAXQ;
    return n;
  }
  function money(cents) {
    cents = Math.max(0, Math.round(Number(cents) || 0));
    var e = Math.floor(cents / 100), c = cents % 100;
    var es = String(e).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return '€' + es + ',' + (c < 10 ? '0' : '') + c;
  }
  function totalCents() {
    return state.items.reduce(function (s, it) { return s + BY_ID[it.id].cents * it.qty; }, 0);
  }
  function itemCount() {
    return state.items.reduce(function (s, it) { return s + it.qty; }, 0);
  }
  function catLabel(c) { return c === 'salgado' ? 'Salgado' : 'Doce'; }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (ch) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[ch];
    });
  }

  /* ---------- tiny svg ornaments ---------- */
  var ICON_INFO = '<svg width="18" height="18" viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="8.5" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M10 9v5M10 6.2v.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';
  var ICON_SCOOP = '<svg width="20" height="20" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10a6 6 0 0 1 12 0z" fill="none" stroke="#9C5224" stroke-width="1.5"/><path d="M3 10h14M6 16l1 -3M14 16l-1 -3" stroke="#9C5224" stroke-width="1.5" stroke-linecap="round"/><path d="M3 3l14 14" stroke="#B8392A" stroke-width="1.8" stroke-linecap="round"/></svg>';
  var ARROW = '<span class="arrow" aria-hidden="true">→</span>';

  /* ---------- views ---------- */
  function card(p, opts) {
    var ph = p.photos[0];
    return '<a class="card" href="#/produto/' + p.id + '" data-testid="product-' + p.id + '">' +
      '<div class="arch"><img src="' + A + ph.f + '" alt="' + esc(ph.alt) + '" style="object-position:' + ph.pos + '" decoding="async"></div>' +
      (p.note ? '<span class="card-note">Sorvete não incluso</span>' : '') +
      '<div class="card-body">' +
        '<h3>' + esc(p.name) + '</h3>' +
        '<span class="price">' + money(p.cents) + '</span>' +
        '<span class="meta"><span class="tag' + (p.cat === 'salgado' ? ' tag-salgado' : '') + '">' + catLabel(p.cat) + '</span>' + esc(p.unit) + '</span>' +
        '<span class="open">Ver detalhes ' + ARROW + '</span>' +
      '</div></a>';
  }

  function viewHome() {
    var feat = ['no-cardamomo', 'torta-morango', 'scone-queijo'].map(function (id) { return card(BY_ID[id]); }).join('');
    return '<div class="view">' +
      '<section class="hero" aria-labelledby="h-hero"><div class="wrap hero-grid">' +
        '<div class="hero-copy">' +
          '<p class="eyebrow">Micro-padaria no Vale · uma fornada por semana</p>' +
          '<h1 id="h-hero" tabindex="-1">O pão de sábado <em>começa na sexta.</em></h1>' +
          '<p class="hero-lede">Encomende até <strong>sexta, 18h</strong>. Retire no <strong>sábado entre 8h e 12h</strong>, ainda morno.</p>' +
          '<div class="hero-actions"><a class="btn" href="#/fornada">Ver a fornada ' + ARROW + '</a>' +
          '<a class="btn btn-ghost" href="#como-funciona" data-scroll="como-funciona">Como funciona</a></div>' +
        '</div>' +
        '<figure class="hero-figure"><div class="arch"><img src="' + A + 'cardamom-buns-on-grate-under-towel.jpg" alt="Nós de cardamomo recém-assados numa grelha, parcialmente cobertos por um pano de algodão." style="object-position:56% 62%" fetchpriority="high"></div>' +
          '<figcaption class="figcap"><span>Nós de cardamomo, descansando sob o pano</span><span>Foto ilustrativa</span></figcaption></figure>' +
      '</div></section>' +

      '<section class="ruler-section" id="como-funciona" aria-labelledby="h-como"><div class="wrap">' +
        '<div class="section-head"><div><p class="eyebrow">Como funciona</p><h2 id="h-como">Três momentos, uma fornada.</h2></div>' +
        '<p>A massa é preparada na sexta à noite. Assamos uma vez, no sábado de madrugada, só o que foi encomendado.</p></div>' +
        '<ol class="ruler">' +
          '<li><span class="when">Até sexta · 18h</span><h3>Escolha até sexta, 18h</h3><p>Veja a fornada, escolha os itens e a faixa de horário para retirar.</p></li>' +
          '<li><span class="when">Sábado · madrugada</span><h3>Assamos na madrugada de sábado</h3><p>A massa descansa desde sexta à noite e vai ao forno antes de o bairro acordar.</p></li>' +
          '<li><span class="when">Sábado · 8h–12h</span><h3>Retire entre 8h e 12h</h3><p>Passe na faixa que você escolheu e leve tudo ainda morno.</p></li>' +
        '</ol>' +
      '</div></section>' +

      '<section class="highlight" aria-labelledby="h-dest"><div class="wrap">' +
        '<div class="section-head"><div><p class="eyebrow">Destaque da fornada</p><h2 id="h-dest">O que sai do forno neste sábado.</h2></div>' +
        '<p>Cinco itens, quatro doces e um salgado. Preços por unidade, fatia ou torta inteira.</p></div>' +
        '<div class="grid grid-home">' + feat + '</div>' +
        '<div class="more"><p>Também na fornada: muffin de baunilha e bolo de maçã.</p><a class="btn btn-ghost btn-small" href="#/fornada">Ver os cinco itens ' + ARROW + '</a></div>' +
      '</div></section>' +

      '<section class="about" aria-labelledby="h-sobre"><div class="wrap about-grid">' +
        '<figure class="about-figure"><div class="frame"><img src="' + A + 'two-layers-of-cardamom-buns-on-grate.jpg" alt="Duas camadas de nós de cardamomo numa grelha sobre toalha xadrez." style="object-position:50% 50%"></div></figure>' +
        '<div><p class="eyebrow">A padaria</p><h2 id="h-sobre">Uma padaria pequena, que assa uma vez por semana.</h2>' +
          '<p class="body">Miolo funciona no ritmo do fim de semana: os vizinhos encomendam durante a semana, a massa é preparada na sexta à noite e a fornada sai no sábado de manhã. Assim dá para planejar o café ou o lanche sabendo exatamente o que vai ter.</p>' +
          '<dl class="facts"><div><dt>Encomenda</dt><dd>até sex, 18h</dd></div><div><dt>Retirada</dt><dd>sáb, 8h–12h</dd></div><div><dt>Bairro</dt><dd>Vale</dd></div></dl>' +
        '</div>' +
      '</div></section>' +
    '</div>';
  }

  function viewCatalog(filter) {
    var f = filter === 'doces' ? 'doce' : filter === 'salgados' ? 'salgado' : 'all';
    var list = PRODUCTS.filter(function (p) { return f === 'all' || p.cat === f; });
    var nDoce = PRODUCTS.filter(function (p) { return p.cat === 'doce'; }).length;
    var nSal = PRODUCTS.length - nDoce;
    function chip(key, label, tid, n) {
      var on = (key === 'all' && f === 'all') || (key === 'doces' && f === 'doce') || (key === 'salgados' && f === 'salgado');
      return '<button type="button" class="chip" data-filter="' + key + '" data-testid="' + tid + '" aria-pressed="' + on + '">' + label + ' <span class="n">' + n + '</span></button>';
    }
    return '<div class="view"><div class="wrap">' +
      '<header class="page-head"><p class="eyebrow">Fornada de sábado</p><h1 tabindex="-1">A fornada</h1>' +
      '<p class="lede">Tudo o que vai ao forno no sábado. Escolha um item para ver as fotos, o preço e adicionar à encomenda.</p></header>' +
      '<div class="toolbar"><div class="filters" role="group" aria-label="Filtrar a fornada">' +
        chip('all', 'Todos', 'filter-all', PRODUCTS.length) + chip('doces', 'Doces', 'filter-sweet', nDoce) + chip('salgados', 'Salgados', 'filter-savory', nSal) +
      '</div><p class="result-count" aria-live="polite">' + list.length + (list.length === 1 ? ' item' : ' itens') + '</p></div>' +
      '<section class="catalog-section" aria-label="Produtos"><div class="grid grid-catalog">' + list.map(function (p) { return card(p); }).join('') + '</div></section>' +
    '</div></div>';
  }

  function viewProduct(id) {
    var p = BY_ID[id];
    if (!p) return viewNotFound();
    var ph = p.photos[0];
    var thumbs = p.photos.length > 1 ? '<div class="thumbs" role="group" aria-label="Fotos do produto">' + p.photos.map(function (x, i) {
      return '<button type="button" class="thumb" data-photo="' + i + '" aria-pressed="' + (i === 0) + '" aria-label="Foto ' + (i + 1) + ' de ' + p.photos.length + '"><img src="' + A + x.f + '" alt="" style="object-position:' + x.pos + '" loading="lazy"></button>';
    }).join('') + '</div>' : '';
    var caveat = p.note ? '<p class="photo-caveat">' + ICON_SCOOP + '<span><strong>' + esc(p.note) + '</strong> A fatia é vendida sem acompanhamento.</span></p>' : '';
    return '<div class="view"><div class="wrap">' +
      '<p class="crumbs"><a href="#/fornada">Fornada</a> / ' + esc(p.name) + '</p>' +
      '<article class="detail">' +
        '<figure class="gallery"><div class="main"><img id="main-photo" src="' + A + ph.f + '" alt="' + esc(ph.alt) + '" style="object-position:' + ph.pos + '"></div>' + thumbs + caveat + '</figure>' +
        '<div class="detail-info">' +
          '<p class="eyebrow">' + catLabel(p.cat) + ' · Fornada de sábado</p>' +
          '<h1 tabindex="-1">' + esc(p.name) + '</h1>' +
          '<div class="price-row"><span class="price">' + money(p.cents) + '</span><span class="unit">por ' + esc(p.unit) + '</span></div>' +
          '<p class="desc">' + esc(p.desc) + '</p>' +
          '<p class="allergen">' + ICON_INFO + '<span>Informações sobre alérgenos não disponíveis neste protótipo.</span></p>' +
          '<div class="buy">' +
            '<div class="buy-row"><div><label class="field-label" for="qty">Quantidade</label>' +
              '<div class="stepper"><button type="button" data-step="-1" aria-label="Diminuir quantidade">−</button>' +
              '<input id="qty" type="number" inputmode="numeric" min="1" max="12" step="1" value="1">' +
              '<button type="button" data-step="1" aria-label="Aumentar quantidade">+</button></div></div>' +
              '<button type="button" class="btn" data-testid="add-order" data-add="' + p.id + '">Adicionar à encomenda</button></div>' +
            '<div class="buy-foot"><span>De 1 a 12 por item.</span><span id="buy-sum">1 × ' + money(p.cents) + ' = ' + money(p.cents) + '</span></div>' +
            '<p class="added" id="added" role="status" aria-live="polite"></p>' +
          '</div>' +
          '<p class="pickup-note">Encomendas até sexta, 18h · retirada no sábado, 8h–12h.</p>' +
        '</div>' +
      '</article>' +
    '</div></div>';
  }

  function slotsHTML() {
    return '<fieldset class="slots" id="slots"><legend>Horário de retirada</legend>' +
      '<p class="hint">Sábado, no Vale. Escolha uma faixa (obrigatório).</p><div class="slot-grid">' +
      SLOTS.map(function (s, i) {
        return '<div class="slot"><input type="radio" name="pickup" id="slot-' + i + '" value="' + s + '" data-testid="pickup-slot"' + (state.slot === s ? ' checked' : '') + ' required>' +
          '<label for="slot-' + i + '">' + s.replace('–', ' – ') + '</label></div>';
      }).join('') + '</div><p class="error" id="slot-error" aria-live="assertive"></p></fieldset>';
  }

  function viewOrder() {
    var head = '<header class="page-head"><p class="eyebrow">Encomenda demonstrativa</p><h1 tabindex="-1">Sua encomenda</h1>' +
      '<p class="lede">Monte a encomenda, escolha a faixa de retirada e revise o resumo. Nada é enviado: tudo fica neste navegador.</p></header>';
    var notice = '<p class="demo-notice">' + ICON_INFO + '<span>' + NOTICE + '</span></p>';
    if (!state.items.length) {
      return '<div class="view"><div class="wrap">' + head +
        '<div class="ticket empty" data-testid="order-empty">' +
          '<svg class="bowl" viewBox="0 0 96 56" aria-hidden="true"><path d="M6 20h84c0 18-18 32-42 32S6 38 6 20z" fill="none" stroke="#2A1C13" stroke-width="2"/><path d="M28 14c4-6 10-6 14 0M50 12c4-6 10-6 14 0" fill="none" stroke="#9C5224" stroke-width="2" stroke-linecap="round"/></svg>' +
          '<h2>Sua encomenda está vazia.</h2><p>Escolha itens na fornada de sábado. Encomendas até sexta, 18h.</p>' +
          '<a class="btn" href="#/fornada">Ver a fornada ' + ARROW + '</a></div>' +
        '<div style="margin:18px 0 clamp(56px,8vw,96px)">' + notice + '</div>' +
      '</div></div>';
    }
    var lines = state.items.map(function (it) {
      var p = BY_ID[it.id], ph = p.photos[0];
      return '<li class="line" data-line="' + p.id + '">' +
        '<div class="line-img"><img src="' + A + ph.f + '" alt="" style="object-position:' + ph.pos + '"></div>' +
        '<div class="line-info"><div class="line-name"><a href="#/produto/' + p.id + '">' + esc(p.name) + '</a></div>' +
          '<div class="line-unit">' + money(p.cents) + ' / ' + esc(p.unit) + (p.note ? ' · sem sorvete' : '') + '</div></div>' +
        '<div class="line-qty"><div class="stepper"><button type="button" data-lstep="-1" aria-label="Diminuir ' + esc(p.name) + '"' + (it.qty <= 1 ? ' disabled' : '') + '>−</button>' +
          '<input type="number" inputmode="numeric" min="1" max="12" step="1" value="' + it.qty + '" data-testid="order-quantity" aria-label="Quantidade de ' + esc(p.name) + '">' +
          '<button type="button" data-lstep="1" aria-label="Aumentar ' + esc(p.name) + '"' + (it.qty >= MAXQ ? ' disabled' : '') + '>+</button></div>' +
          '<button type="button" class="remove" data-testid="order-remove" aria-label="Remover ' + esc(p.name) + '">Remover</button></div>' +
        '<div class="line-total" data-line-total>' + money(p.cents * it.qty) + '</div>' +
      '</li>';
    }).join('');
    return '<div class="view"><div class="wrap">' + head +
      '<div class="order-layout">' +
        '<div class="ticket-col">' +
          '<section class="ticket" aria-labelledby="h-ticket">' +
            '<div class="ticket-head"><h2 id="h-ticket">Fornada de sábado</h2><span class="mono" id="ticket-count">' + countLabel() + '</span></div>' +
            '<ul class="lines">' + lines + '</ul>' +
            '<div class="totals"><span class="label">Subtotal</span><span class="value" data-testid="order-subtotal" id="subtotal">' + money(totalCents()) + '</span></div>' +
          '</section>' +
        '</div>' +
        '<div id="summary-slot" class="summary-slot"></div>' +
        '<aside class="side" aria-label="Retirada e revisão">' +
          '<div class="panel">' + slotsHTML() + '</div>' +
          '<button type="button" class="btn" data-testid="order-review" id="review">Revisar encomenda</button>' +
          notice +
          '<a class="link" href="#/fornada">← Continuar escolhendo</a>' +
        '</aside>' +
      '</div>' +
    '</div></div>';
  }
  function countLabel() { var n = itemCount(); return n + (n === 1 ? ' item' : ' itens'); }

  function summaryHTML() {
    var rows = state.items.map(function (it) {
      var p = BY_ID[it.id];
      return '<tr><td>' + esc(p.name) + (p.note ? ' <span style="opacity:.7">(sem sorvete)</span>' : '') + '</td><td class="num">' + it.qty + '</td><td class="num">' + money(p.cents) + '</td><td class="num">' + money(p.cents * it.qty) + '</td></tr>';
    }).join('');
    return '<section class="summary" data-testid="order-summary" tabindex="-1" id="summary" aria-labelledby="h-summary">' +
      '<p class="eyebrow">Resumo local · não enviado</p>' +
      '<h2 id="h-summary">Retirada no sábado</h2>' +
      '<p class="when-big">' + esc(state.slot.replace('–', ' – ')) + ' · Vale</p>' +
      '<table><thead><tr><th>Item</th><th class="num">Qtd.</th><th class="num">Unit.</th><th class="num">Total</th></tr></thead>' +
      '<tbody>' + rows + '</tbody><tfoot><tr><td colspan="3">Subtotal</td><td class="num">' + money(totalCents()) + '</td></tr></tfoot></table>' +
      '<p class="sum-notice">' + NOTICE + ' Nenhum pagamento, conta ou dado pessoal é solicitado.</p>' +
      '<div class="sum-actions"><button type="button" class="btn btn-ghost btn-small" data-edit>Editar encomenda</button></div>' +
    '</section>';
  }

  function viewCredits() {
    var used = {};
    PRODUCTS.forEach(function (p) { p.photos.forEach(function (x) { used[x.f] = (used[x.f] ? used[x.f] + ', ' : '') + p.name; }); });
    used['cardamom-buns-on-grate-under-towel.jpg'] += ' · abertura';
    used['two-layers-of-cardamom-buns-on-grate.jpg'] += ' · a padaria';
    var list = (window.MIOLO_CREDITS || []).filter(function (c) { return used[c.file]; }).map(function (c) {
      return '<li class="credit"><img src="' + A + c.file + '" alt="" loading="lazy">' +
        '<div><h3>' + esc(c.title) + '</h3>' +
        '<p>Autor: ' + esc(c.author) + ' · Licença: <a href="' + esc(c.license_url) + '" rel="noopener license">' + esc(c.license) + '</a></p>' +
        '<p><a href="' + esc(c.source) + '" rel="noopener">Fonte: Wikimedia Commons</a></p>' +
        '<p>Usada em: ' + esc(used[c.file]) + '</p></div></li>';
    }).join('');
    return '<div class="view"><div class="wrap">' +
      '<header class="page-head"><p class="eyebrow">Créditos</p><h1 tabindex="-1">Fotografias</h1>' +
      '<p class="lede">Fotografias ilustrativas de terceiros, sob licenças CC0, CC BY 4.0 e CC BY-SA 4.0. Elas não mostram produtos ou locais da Miolo, que é uma marca fictícia. As imagens são usadas sem alteração de pixels; os recortes são feitos apenas na exibição.</p></header>' +
      '<ul class="credits-list">' + list + '</ul>' +
    '</div></div>';
  }

  function viewNotFound() {
    return '<div class="view"><div class="wrap"><header class="page-head"><p class="eyebrow">Página não encontrada</p><h1 tabindex="-1">Esse endereço não está na fornada.</h1>' +
      '<p class="lede"><a class="link" href="#/fornada">Ver a fornada</a> ou <a class="link" href="#/">voltar ao início</a>.</p></header></div></div>';
  }

  /* ---------- router ---------- */
  var main = document.getElementById('conteudo');
  var first = true, keepScroll = false;
  function parse() {
    var h = (location.hash || '#/').replace(/^#/, '');
    if (h === '' || h.charAt(0) !== '/') return null; // âncora interna
    var q = '', i = h.indexOf('?');
    if (i >= 0) { q = h.slice(i + 1); h = h.slice(0, i); }
    var parts = h.split('/').filter(Boolean);
    var params = {};
    q.split('&').forEach(function (kv) { if (kv) { var a = kv.split('='); params[a[0]] = decodeURIComponent(a[1] || ''); } });
    return { parts: parts, params: params };
  }
  function render() {
    var r = parse();
    if (!r) { if (main.querySelector('.view')) return; r = { parts: [], params: {} }; }
    var route = r.parts[0] || 'home', html, title = 'Miolo · Fornada de sábado';
    if (route === 'home') html = viewHome();
    else if (route === 'fornada') { html = viewCatalog(r.params.f); title = 'A fornada · Miolo'; }
    else if (route === 'produto') { html = viewProduct(r.parts[1]); title = (BY_ID[r.parts[1]] ? BY_ID[r.parts[1]].name : 'Produto') + ' · Miolo'; }
    else if (route === 'encomenda') { html = viewOrder(); title = 'Encomenda · Miolo'; }
    else if (route === 'creditos') { html = viewCredits(); title = 'Créditos · Miolo'; }
    else html = viewNotFound();
    main.innerHTML = html;
    document.title = title;
    var navKey = route === 'produto' ? 'fornada' : route;
    document.querySelectorAll('.main-nav [data-route]').forEach(function (a) {
      if (a.getAttribute('data-route') === navKey) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    if (route === 'encomenda' && state.reviewed && state.items.length && state.slot) showSummary(false);
    updateCount();
    if (!first && keepScroll) { keepScroll = false; }
    else if (!first) {
      window.scrollTo(0, 0);
      var h1 = main.querySelector('h1');
      if (h1) h1.focus({ preventScroll: true });
    }
    first = false;
  }
  window.addEventListener('hashchange', render);

  function updateCount() {
    var n = itemCount(), el = document.getElementById('nav-count');
    el.textContent = n;
    el.setAttribute('data-zero', n === 0 ? 'true' : 'false');
    var sr = document.getElementById('nav-count-sr'); if (sr) sr.textContent = ', ' + n + (n === 1 ? ' item' : ' itens');
  }

  /* ---------- order mutations ---------- */
  function invalidateSummary() {
    state.reviewed = false;
    var s = document.getElementById('summary-slot');
    if (s) s.innerHTML = '';
  }
  function addItem(id, qty) {
    qty = clampQty(qty);
    var it = state.items.filter(function (x) { return x.id === id; })[0];
    var capped = false;
    if (it) { var nq = it.qty + qty; if (nq > MAXQ) { capped = true; nq = MAXQ; } it.qty = nq; }
    else state.items.push({ id: id, qty: qty });
    state.reviewed = false;
    save(); updateCount();
    return { capped: capped, qty: (it || state.items[state.items.length - 1]).qty };
  }
  function setQty(id, qty) {
    var it = state.items.filter(function (x) { return x.id === id; })[0];
    if (!it) return;
    it.qty = clampQty(qty);
    save(); invalidateSummary(); refreshOrderNumbers(id);
  }
  function removeItem(id) {
    state.items = state.items.filter(function (x) { return x.id !== id; });
    save(); state.reviewed = false;
    var focusTarget = null;
    main.innerHTML = viewOrder();
    updateCount();
    focusTarget = main.querySelector('[data-testid="order-remove"]') || main.querySelector('[data-testid="order-empty"] .btn');
    if (focusTarget) focusTarget.focus();
  }
  function refreshOrderNumbers(id) {
    var li = main.querySelector('[data-line="' + id + '"]');
    var it = state.items.filter(function (x) { return x.id === id; })[0];
    if (li && it) {
      li.querySelector('input').value = it.qty;
      li.querySelector('[data-line-total]').textContent = money(BY_ID[id].cents * it.qty);
      li.querySelector('[data-lstep="-1"]').disabled = it.qty <= 1;
      li.querySelector('[data-lstep="1"]').disabled = it.qty >= MAXQ;
    }
    var st = document.getElementById('subtotal'); if (st) st.textContent = money(totalCents());
    var tc = document.getElementById('ticket-count'); if (tc) tc.textContent = countLabel();
    updateCount();
  }
  function showSummary(focus) {
    var s = document.getElementById('summary-slot');
    if (!s) return;
    s.innerHTML = summaryHTML();
    if (focus) {
      var el = document.getElementById('summary');
      el.focus({ preventScroll: true });
      el.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    }
  }

  /* ---------- events (delegação) ---------- */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('button, a');
    if (!t) return;

    if (t.hasAttribute('data-scroll')) {
      var target = document.getElementById(t.getAttribute('data-scroll'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); var h = target.querySelector('h2'); if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); } }
      return;
    }
    if (t.hasAttribute('data-filter')) {
      var key = t.getAttribute('data-filter');
      keepScroll = true;
      location.hash = key === 'all' ? '#/fornada' : '#/fornada?f=' + key;
      setTimeout(function () { var b = main.querySelector('[data-filter="' + key + '"]'); if (b) b.focus(); }, 0);
      return;
    }
    if (t.hasAttribute('data-photo')) {
      var p = BY_ID[(parse().parts || [])[1]]; if (!p) return;
      var i = +t.getAttribute('data-photo'), ph = p.photos[i], img = document.getElementById('main-photo');
      img.src = A + ph.f; img.alt = ph.alt; img.style.objectPosition = ph.pos;
      main.querySelectorAll('[data-photo]').forEach(function (b) { b.setAttribute('aria-pressed', b === t ? 'true' : 'false'); });
      return;
    }
    if (t.hasAttribute('data-step')) {
      var q = document.getElementById('qty');
      q.value = clampQty((parseInt(q.value, 10) || 1) + (+t.getAttribute('data-step')));
      syncBuy();
      return;
    }
    if (t.hasAttribute('data-add')) {
      var id = t.getAttribute('data-add');
      var qv = clampQty(document.getElementById('qty').value);
      document.getElementById('qty').value = qv;
      var r = addItem(id, qv);
      var msg = document.getElementById('added');
      msg.innerHTML = (r.capped ? 'Limite de 12 por item. ' : '') + 'Na encomenda: ' + r.qty + ' × ' + esc(BY_ID[id].name) + '. <a class="link" href="#/encomenda">Ver encomenda →</a>';
      return;
    }
    if (t.hasAttribute('data-lstep')) {
      var li = t.closest('[data-line]'), lid = li.getAttribute('data-line');
      var cur = state.items.filter(function (x) { return x.id === lid; })[0];
      setQty(lid, cur.qty + (+t.getAttribute('data-lstep')));
      if (t.disabled) li.querySelector('input').focus();
      return;
    }
    if (t.getAttribute('data-testid') === 'order-remove') {
      removeItem(t.closest('[data-line]').getAttribute('data-line'));
      return;
    }
    if (t.id === 'review') {
      var err = document.getElementById('slot-error'), fs = document.getElementById('slots');
      if (!state.slot) {
        err.textContent = 'Escolha um horário de retirada para revisar a encomenda.';
        fs.setAttribute('aria-invalid', 'true');
        var r0 = document.getElementById('slot-0'); if (r0) r0.focus();
        return;
      }
      err.textContent = ''; fs.removeAttribute('aria-invalid');
      state.reviewed = true;
      showSummary(true);
      return;
    }
    if (t.hasAttribute('data-edit')) {
      invalidateSummary();
      var first = main.querySelector('[data-testid="order-quantity"]'); if (first) first.focus();
      return;
    }
  });

  function syncBuy() {
    var q = document.getElementById('qty'); if (!q) return;
    var p = BY_ID[(parse().parts || [])[1]]; if (!p) return;
    var n = clampQty(q.value);
    document.getElementById('buy-sum').textContent = n + ' × ' + money(p.cents) + ' = ' + money(p.cents * n);
    var btns = main.querySelectorAll('[data-step]');
    btns[0].disabled = n <= 1; btns[1].disabled = n >= MAXQ;
  }

  document.addEventListener('input', function (e) {
    if (e.target.id === 'qty') { var v = e.target.value; if (v !== '') syncBuy(); }
  });
  document.addEventListener('change', function (e) {
    var t = e.target;
    if (t.id === 'qty') { t.value = clampQty(t.value); syncBuy(); return; }
    if (t.getAttribute('data-testid') === 'order-quantity') {
      setQty(t.closest('[data-line]').getAttribute('data-line'), t.value);
      return;
    }
    if (t.name === 'pickup') {
      state.slot = t.value; save(); invalidateSummary();
      var err = document.getElementById('slot-error'); if (err) err.textContent = '';
      var fs = document.getElementById('slots'); if (fs) fs.removeAttribute('aria-invalid');
    }
  });
  // Enter num campo de quantidade da encomenda confirma o valor
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && e.target.getAttribute && e.target.getAttribute('data-testid') === 'order-quantity') {
      e.preventDefault(); e.target.blur(); e.target.focus();
    }
  });

  render();
})();
