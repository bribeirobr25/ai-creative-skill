/* Miolo — protótipo local. Sem rede, sem envio, sem dados pessoais. */
(function () {
  'use strict';

  var A = 'assets/';

  var PRODUCTS = [
    {
      id: 'no-cardamomo', name: 'Nó de cardamomo', cat: 'doce', price: 280, unit: 'unidade',
      desc: 'Massa enriquecida, enrolada em nó, com açúcar e cardamomo.',
      photos: [
        { f: 'cardamom-buns.jpg', alt: 'Tigela de madeira cheia de nós de cardamomo dourados, sobre toalha xadrez vermelha e branca.', pos: '50% 45%' },
        { f: 'two-layers-of-cardamom-buns-on-grate.jpg', alt: 'Grade de metal com duas camadas de nós de cardamomo recém-assados.', pos: '50% 50%' },
        { f: 'one-layer-of-cardamom-buns-on-grate.jpg', alt: 'Uma camada de nós de cardamomo enfileirados sobre uma grade, vistos de cima.', pos: '50% 50%' },
        { f: 'cardamom-buns-on-grate-under-towel.jpg', alt: 'Nós de cardamomo sobre uma grade, parcialmente cobertos por um pano de linho claro.', pos: '50% 60%' }
      ]
    },
    {
      id: 'muffin-baunilha', name: 'Muffin de baunilha', cat: 'doce', price: 250, unit: 'unidade',
      desc: 'Massa simples de baunilha, assada em forminha de papel.',
      photos: [
        { f: 'plain-vanilla-muffins-1.jpg', alt: 'Três muffins de baunilha em forminhas de papel sobre papel manteiga amassado.', pos: '50% 50%' },
        { f: 'plain-vanilla-muffin.jpg', alt: 'Um muffin de baunilha em forminha de papel, de perto.', pos: '50% 55%' },
        { f: 'plain-vanilla-muffins-2.jpg', alt: 'Três muffins de baunilha com o topo rachado, em forminhas de papel.', pos: '50% 55%' },
        { f: 'plain-vanilla-muffins-3.jpg', alt: 'Três muffins de baunilha dispostos em diagonal sobre papel manteiga.', pos: '50% 50%' }
      ]
    },
    {
      id: 'torta-morango', name: 'Torta de morango', cat: 'doce', price: 2400, unit: 'inteira, 8 fatias',
      desc: 'Base amanteigada coberta de morangos.',
      photos: [
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-3.jpg', alt: 'Torta de morango inteira, sem o aro da forma, coberta de morangos fatiados e brilhantes.', pos: '50% 50%' },
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-1.jpg', alt: 'Torta de morango dentro de uma forma de aro removível, vista de cima e de lado.', pos: '50% 45%' },
        { f: 'strawberry-pie-in-springform-pan-with-drip-tray-2.jpg', alt: 'Torta de morango na forma de aro, sobre um prato metálico e pano de cozinha.', pos: '50% 45%' }
      ]
    },
    {
      id: 'bolo-maca', name: 'Bolo de maçã', cat: 'doce', price: 420, unit: 'fatia',
      desc: 'Bolo de maçã com canela.',
      note: 'Na foto há uma bola de sorvete: o sorvete não acompanha o produto.',
      photos: [
        { f: 'apple-cake-with-vanilla-ice-cream-2.jpg', alt: 'Fatia de bolo de maçã com canela num prato branco, com uma bola de sorvete por cima (o sorvete não acompanha o produto).', pos: '45% 50%' },
        { f: 'apple-cake-with-vanilla-ice-cream-1.jpg', alt: 'Fatia de bolo de maçã servida com uma bola de sorvete, sobre toalha xadrez azul (o sorvete não acompanha o produto).', pos: '45% 50%' }
      ]
    },
    {
      id: 'scone-queijo', name: 'Scone de queijo', cat: 'salgado', price: 300, unit: 'unidade',
      desc: 'Scone salgado com queijo.',
      photos: [
        { f: 'swedish-cheese-scones.jpg', alt: 'Scones de queijo dourados e rústicos sobre papel de forno.', pos: '35% 60%' }
      ]
    }
  ];

  var CREDITS = [
    ['apple-cake-with-vanilla-ice-cream-1.jpg', 'Apple cake with vanilla ice cream 1.jpg', 'W.carter', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Apple_cake_with_vanilla_ice_cream_1.jpg'],
    ['apple-cake-with-vanilla-ice-cream-2.jpg', 'Apple cake with vanilla ice cream 2.jpg', 'W.carter', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Apple_cake_with_vanilla_ice_cream_2.jpg'],
    ['cardamom-buns-on-grate-under-towel.jpg', 'Cardamom buns on grate under towel.jpg', 'W.carter', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Cardamom_buns_on_grate_under_towel.jpg'],
    ['cardamom-buns.jpg', 'Cardamom buns.jpg', 'W.carter', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Cardamom_buns.jpg'],
    ['one-layer-of-cardamom-buns-on-grate.jpg', 'One layer of cardamom buns on grate.jpg', 'W.carter', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:One_layer_of_cardamom_buns_on_grate.jpg'],
    ['plain-vanilla-muffin.jpg', 'Plain vanilla muffin in Tuntorp.jpg', 'W.carter', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Plain_vanilla_muffin_in_Tuntorp.jpg'],
    ['plain-vanilla-muffins-1.jpg', 'Plain vanilla muffins in Tuntorp 1.jpg', 'W.carter', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Plain_vanilla_muffins_in_Tuntorp_1.jpg'],
    ['plain-vanilla-muffins-2.jpg', 'Plain vanilla muffins in Tuntorp 2.jpg', 'W.carter', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Plain_vanilla_muffins_in_Tuntorp_2.jpg'],
    ['plain-vanilla-muffins-3.jpg', 'Plain vanilla muffins in Tuntorp 3.jpg', 'W.carter', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Plain_vanilla_muffins_in_Tuntorp_3.jpg'],
    ['strawberry-pie-in-springform-pan-with-drip-tray-1.jpg', 'Strawberry pie in springform pan with drip tray in Tuntorp, Brastad 1.jpg', 'W.carter', 'CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0', 'https://commons.wikimedia.org/wiki/File:Strawberry_pie_in_springform_pan_with_drip_tray_in_Tuntorp,_Brastad_1.jpg'],
    ['strawberry-pie-in-springform-pan-with-drip-tray-2.jpg', 'Strawberry pie in springform pan with drip tray in Tuntorp, Brastad 2.jpg', 'W.carter', 'CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0', 'https://commons.wikimedia.org/wiki/File:Strawberry_pie_in_springform_pan_with_drip_tray_in_Tuntorp,_Brastad_2.jpg'],
    ['strawberry-pie-in-springform-pan-with-drip-tray-3.jpg', 'Strawberry pie in springform pan with drip tray in Tuntorp, Brastad 3.jpg', 'W.carter', 'CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0', 'https://commons.wikimedia.org/wiki/File:Strawberry_pie_in_springform_pan_with_drip_tray_in_Tuntorp,_Brastad_3.jpg'],
    ['swedish-cheese-scones.jpg', 'Swedish cheese scones.jpg', 'W.carter', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Swedish_cheese_scones.jpg'],
    ['two-layers-of-cardamom-buns-on-grate.jpg', 'Two layers of cardamom buns on grate.jpg', 'W.carter', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Two_layers_of_cardamom_buns_on_grate.jpg']
  ];

  var SLOTS = ['08:00–09:00', '09:00–10:00', '10:00–11:00', '11:00–12:00'];
  var MAXQ = 12;
  var NOTICE = 'Protótipo demonstrativo. Marca, produtos e preços fictícios. Nenhuma encomenda é enviada.';

  /* ---------- Estado ---------- */
  var state = { items: {}, slot: '', reviewed: false };
  var KEY = 'miolo-demo-v1';
  try {
    var saved = JSON.parse(window.localStorage.getItem(KEY) || 'null');
    if (saved && typeof saved === 'object') {
      Object.keys(saved.items || {}).forEach(function (id) {
        var q = clampQ(saved.items[id]);
        if (byId(id) && q > 0) state.items[id] = q;
      });
      if (SLOTS.indexOf(saved.slot) > -1) state.slot = saved.slot;
    }
  } catch (e) { /* armazenamento indisponível: segue em memória */ }

  function persist() {
    try { window.localStorage.setItem(KEY, JSON.stringify({ items: state.items, slot: state.slot })); } catch (e) {}
  }

  function byId(id) { for (var i = 0; i < PRODUCTS.length; i++) if (PRODUCTS[i].id === id) return PRODUCTS[i]; return null; }
  function clampQ(v) {
    var n = parseInt(v, 10);
    if (!isFinite(n) || isNaN(n)) return 0;
    return Math.max(0, Math.min(MAXQ, n));
  }
  function eur(cents) {
    var c = Math.max(0, Math.round(Number(cents) || 0));
    var s = (c / 100).toFixed(2).split('.');
    s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return '€' + s[0] + ',' + s[1];
  }
  function count() { return Object.keys(state.items).reduce(function (a, id) { return a + state.items[id]; }, 0); }
  function total() { return Object.keys(state.items).reduce(function (a, id) { var p = byId(id); return a + (p ? p.price * state.items[id] : 0); }, 0); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function catLabel(c) { return c === 'salgado' ? 'Salgado' : 'Doce'; }

  /* ---------- Componentes ---------- */
  function card(p, opts) {
    opts = opts || {};
    var ph = p.photos[0];
    return '<a class="card' + (opts.wide ? ' card--wide' : '') + '" href="#/produto/' + p.id + '" data-testid="product-' + p.id + '">' +
      '<div class="card__img"><img src="' + A + ph.f + '" alt="' + esc(ph.alt) + '" loading="lazy" style="object-position:' + ph.pos + '"></div>' +
      '<div class="card__body">' +
        '<div class="card__row"><span class="card__cat">' + catLabel(p.cat) + '</span><span class="card__price">' + eur(p.price) + '</span></div>' +
        '<h3 class="card__name">' + esc(p.name) + '</h3>' +
        '<span class="card__unit">por ' + esc(p.unit) + '</span>' +
        (p.note ? '<span class="card__note">Sorvete da foto não incluso.</span>' : '') +
        '<span class="card__more">Ver detalhes <span aria-hidden="true">→</span></span>' +
      '</div></a>';
  }

  var ICON_BAG = '<svg width="56" height="56" viewBox="0 0 56 56" fill="none" aria-hidden="true"><path d="M12 20h32l-3 26a4 4 0 0 1-4 3.5H19A4 4 0 0 1 15 46L12 20Z" stroke="currentColor" stroke-width="2"/><path d="M21 20v-3a7 7 0 0 1 14 0v3" stroke="currentColor" stroke-width="2"/><path d="M22 33c3 2.5 9 2.5 12 0" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';

  /* ---------- Páginas ---------- */
  function viewHome() {
    var feat = ['no-cardamomo', 'torta-morango', 'scone-queijo'].map(byId);
    return '<div class="view">' +
      '<section class="hero" aria-labelledby="h-hero"><div class="wrap hero__grid">' +
        '<div>' +
          '<p class="eyebrow">Miolo · micro-padaria do Vale</p>' +
          '<h1 class="display" id="h-hero" tabindex="-1">O pão de sábado começa na <em>sexta.</em></h1>' +
          '<p class="hero__text">Encomende até sexta, 18h. Retire no sábado entre 8h e 12h, ainda morno.</p>' +
          '<div class="hero__actions"><a class="btn" href="#/fornada">Ver a fornada <span class="arrow" aria-hidden="true">→</span></a>' +
          '<a class="btn btn--ghost" href="#como-funciona" data-scroll="como-funciona">Como funciona</a></div>' +
        '</div>' +
        '<div class="hero__media">' +
          '<div class="hero__photo"><img src="' + A + 'cardamom-buns.jpg" alt="Tigela de madeira com nós de cardamomo sobre toalha xadrez vermelha e branca." style="object-position:58% 50%"></div>' +
          '<p class="hero__ticket"><b>Uma fornada por semana</b>Massa na sexta à noite.<br>Forno na madrugada de sábado.</p>' +
        '</div>' +
      '</div></section>' +

      '<section class="week" id="como-funciona" aria-labelledby="h-week"><div class="wrap">' +
        '<div class="week__head"><div><p class="eyebrow">Como funciona</p><h2 class="h2" id="h-week">Uma semana, um forno, três passos.</h2></div>' +
        '<p>Miolo assa somente uma vez por semana. Você escolhe com antecedência, nós assamos o que foi encomendado e você busca de manhã no Vale.</p></div>' +
        '<ol class="steps">' +
          '<li class="step"><span class="step__dot">1</span><p class="step__when">Sexta, até 18h</p><h3 class="step__title">Escolha até sexta, 18h</h3><p>Monte sua encomenda com o que estará na fornada e o horário de retirada.</p></li>' +
          '<li class="step"><span class="step__dot">2</span><p class="step__when">Sábado, madrugada</p><h3 class="step__title">Assamos na madrugada de sábado</h3><p>A massa descansa desde sexta à noite e vai ao forno antes do amanhecer.</p></li>' +
          '<li class="step"><span class="step__dot">3</span><p class="step__when">Sábado, 8h–12h</p><h3 class="step__title">Retire entre 8h e 12h</h3><p>Escolha uma faixa de uma hora e busque sua encomenda ainda morna.</p></li>' +
        '</ol>' +
      '</div></section>' +

      '<section class="feature" aria-labelledby="h-feat"><div class="wrap">' +
        '<div class="feature__head"><div><p class="eyebrow">Nesta fornada</p><h2 class="h2" id="h-feat">Doces e um salgado.</h2></div>' +
        '<p>Cinco itens nesta semana. Abaixo, três deles; a fornada completa tem filtro por doces e salgados.</p></div>' +
        '<div class="grid">' + feat.map(function (p) { return card(p); }).join('') + '</div>' +
        '<p style="margin-top:28px"><a class="btn btn--ghost" href="#/fornada">Ver a fornada completa <span class="arrow" aria-hidden="true">→</span></a></p>' +
      '</div></section>' +
    '</div>';
  }

  function viewCatalog(filter) {
    var f = filter === 'doces' ? 'doce' : filter === 'salgados' ? 'salgado' : 'all';
    var list = PRODUCTS.filter(function (p) { return f === 'all' || p.cat === f; });
    var nD = PRODUCTS.filter(function (p) { return p.cat === 'doce'; }).length;
    var nS = PRODUCTS.length - nD;
    function chip(key, label, tid, n) {
      var on = (key === 'all' && f === 'all') || (key === 'doces' && f === 'doce') || (key === 'salgados' && f === 'salgado');
      return '<button type="button" class="chip" data-filter="' + key + '" data-testid="' + tid + '" aria-pressed="' + on + '">' + label + ' <span class="chip__n">' + n + '</span></button>';
    }
    return '<div class="view wrap">' +
      '<header class="page-head"><p class="eyebrow">Fornada de sábado</p><h1 class="display" tabindex="-1">A fornada</h1>' +
      '<p>Tudo o que vai ao forno neste sábado. Abra um item para ver fotos, preço e escolher a quantidade.</p>' +
      '<div class="filters" role="group" aria-label="Filtrar a fornada">' +
        chip('all', 'Todos', 'filter-all', PRODUCTS.length) + chip('doces', 'Doces', 'filter-sweet', nD) + chip('salgados', 'Salgados', 'filter-savory', nS) +
      '</div>' +
      '<p class="result-count" aria-live="polite">' + list.length + (list.length === 1 ? ' item' : ' itens') + (f === 'all' ? ' na fornada' : f === 'doce' ? ' doces' : ' salgado' + (list.length === 1 ? '' : 's')) + '</p></header>' +
      '<section class="catalog" aria-label="Produtos"><div class="grid">' +
        list.map(function (p, i) { return card(p, { wide: f === 'all' && i < 2 }); }).join('') +
      '</div></section>' +
    '</div>';
  }

  function viewDetail(id) {
    var p = byId(id);
    if (!p) return viewNotFound();
    var main = p.photos[0];
    var thumbs = p.photos.length > 1 ? '<div class="gallery__thumbs" role="group" aria-label="Outras fotos">' + p.photos.map(function (ph, i) {
      return '<button type="button" class="thumb" data-photo="' + i + '" aria-label="Mostrar foto ' + (i + 1) + ' de ' + p.photos.length + '"' + (i === 0 ? ' aria-current="true"' : '') + '><img src="' + A + ph.f + '" alt="" style="object-position:' + ph.pos + '"></button>';
    }).join('') + '</div>' : '';
    var others = PRODUCTS.filter(function (o) { return o.id !== p.id; });
    var inOrder = state.items[p.id] || 0;
    return '<div class="view wrap detail">' +
      '<a class="back" href="#/fornada"><span aria-hidden="true">←</span> Voltar à fornada</a>' +
      '<div class="detail__grid">' +
        '<div class="gallery">' +
          '<div class="gallery__main"><img id="mainPhoto" src="' + A + main.f + '" alt="' + esc(main.alt) + '" style="object-position:' + main.pos + '"></div>' +
          thumbs +
          (p.note ? '<p class="caveat"><strong>Atenção:</strong> ' + esc(p.note) + ' Você recebe somente a fatia de bolo.</p>' : '') +
          '<p class="photo-note">Fotografia ilustrativa de terceiros (<a href="#/creditos">créditos</a>).</p>' +
        '</div>' +
        '<div class="detail__info">' +
          '<p class="eyebrow">' + catLabel(p.cat) + '</p>' +
          '<h1 class="display" tabindex="-1">' + esc(p.name) + '</h1>' +
          '<p class="detail__price"><span class="mono">' + eur(p.price) + '</span><span>por ' + esc(p.unit) + '</span></p>' +
          '<p class="detail__desc">' + esc(p.desc) + '</p>' +
          '<p class="allergen">Informações sobre alérgenos não disponíveis neste protótipo.</p>' +
          '<div class="buy">' +
            '<div class="field"><label for="qty">Quantidade</label>' +
              '<div class="stepper"><button type="button" data-step="-1" aria-label="Diminuir quantidade">−</button>' +
              '<input id="qty" type="number" inputmode="numeric" min="1" max="' + MAXQ + '" step="1" value="1">' +
              '<button type="button" data-step="1" aria-label="Aumentar quantidade">+</button></div></div>' +
            '<button type="button" class="btn" id="addBtn" data-testid="add-order" data-id="' + p.id + '">Adicionar à encomenda</button>' +
          '</div>' +
          '<p class="added" id="added" role="status" aria-live="polite">' + (inOrder ? 'Já na encomenda: ' + inOrder + '. <a href="#/encomenda">Ver encomenda</a>' : '') + '</p>' +
        '</div>' +
      '</div>' +
      '<section class="more" aria-labelledby="h-more"><h2 id="h-more">Também na fornada</h2><div class="grid">' +
        others.map(function (o) { return card(o); }).join('') + '</div></section>' +
    '</div>';
  }

  function viewOrder() {
    var ids = Object.keys(state.items);
    var body;
    if (!ids.length) {
      body = '<div class="ticket"><div class="empty" data-testid="order-empty">' + ICON_BAG +
        '<h2>Sua encomenda está vazia</h2><p>Escolha itens na fornada desta semana. A encomenda fica só neste navegador.</p>' +
        '<a class="btn" href="#/fornada">Ver a fornada <span class="arrow" aria-hidden="true">→</span></a></div></div>';
    } else {
      body = '<div class="ticket"><p class="ticket__title">Bilhete de encomenda</p><ul class="lines">' +
        ids.map(function (id) {
          var p = byId(id), q = state.items[id];
          var opts = '';
          for (var n = 1; n <= MAXQ; n++) opts += '<option value="' + n + '"' + (n === q ? ' selected' : '') + '>' + n + '</option>';
          return '<li class="line">' +
            '<div class="line__img"><img src="' + A + p.photos[0].f + '" alt="" style="object-position:' + p.photos[0].pos + '"></div>' +
            '<div><p class="line__name"><a href="#/produto/' + p.id + '">' + esc(p.name) + '</a></p>' +
              '<div class="line__meta"><span class="line__unit">' + eur(p.price) + ' / ' + esc(p.unit) + '</span>' +
              '<button type="button" class="remove" data-remove="' + p.id + '" data-testid="order-remove" aria-label="Remover ' + esc(p.name) + '">Remover</button></div></div>' +
            '<div class="line__qty"><label class="visually-hidden" for="q-' + p.id + '">Quantidade de ' + esc(p.name) + '</label>' +
              '<select id="q-' + p.id + '" data-qty="' + p.id + '" data-testid="order-quantity">' + opts + '</select></div>' +
            '<span class="line__sum" data-line-sum="' + p.id + '">' + eur(p.price * q) + '</span>' +
          '</li>';
        }).join('') +
        '</ul><div class="total"><span>Total</span><span class="mono" data-testid="order-subtotal" id="subtotal">' + eur(total()) + '</span></div>' +
        '<p class="line__unit" style="margin:0">Até ' + MAXQ + ' unidades de cada item.</p></div>';
    }

    var slots = SLOTS.map(function (s, i) {
      return '<label class="slot"><input type="radio" name="pickup" value="' + s + '" data-testid="pickup-slot"' + (state.slot === s ? ' checked' : '') + ' aria-describedby="slotErr"><span>' + s + '</span></label>';
    }).join('');

    var side = '<aside class="side" aria-label="Retirada e revisão">' +
      '<div class="ticket"><fieldset class="slots"><legend>Horário de retirada</legend>' +
        '<p class="slots__hint">Sábado, no Vale. Escolha uma faixa (obrigatório).</p>' +
        '<div class="slots__grid">' + slots + '</div></fieldset>' +
        '<p class="error" id="slotErr" aria-live="polite"></p>' +
        '<button type="button" class="btn btn--block" id="reviewBtn" data-testid="order-review"' + (ids.length ? '' : ' disabled aria-disabled="true"') + '>Revisar encomenda</button>' +
      '</div>' +
      '<p class="notice-box"><strong>' + NOTICE.split('. ')[0] + '.</strong> ' + NOTICE.split('. ').slice(1).join('. ') + ' Sem pagamento, conta ou dados pessoais.</p>' +
    '</aside>';

    return '<div class="view wrap order">' +
      '<header class="page-head"><p class="eyebrow">Fornada de sábado, encomendada na sexta.</p><h1 class="display" tabindex="-1">Sua encomenda</h1>' +
      '<p>Ajuste quantidades, escolha o horário de retirada e revise o resumo.</p></header>' +
      '<div class="order__grid"><div>' + body + '<div id="summaryHost"></div></div>' + side + '</div>' +
    '</div>';
  }

  function summaryHTML() {
    var ids = Object.keys(state.items);
    return '<section class="summary" data-testid="order-summary" tabindex="-1" aria-labelledby="h-sum">' +
      '<p class="ticket__title">Resumo local</p><h2 id="h-sum">Encomenda revisada</h2>' +
      '<dl><dt>Retirada</dt><dd>Sábado, ' + state.slot + '</dd><dt>Itens</dt><dd>' + count() + '</dd></dl>' +
      '<ul>' + ids.map(function (id) { var p = byId(id); return '<li><span>' + state.items[id] + ' × ' + esc(p.name) + '</span><span>' + eur(p.price * state.items[id]) + '</span></li>'; }).join('') + '</ul>' +
      '<div class="sumtotal"><span>Total</span><span>' + eur(total()) + '</span></div>' +
      '<p class="small">' + NOTICE + ' Este resumo existe só nesta tela.</p>' +
      '<button type="button" class="btn btn--ghost" id="editBtn">Editar encomenda</button>' +
    '</section>';
  }

  function viewCredits() {
    var used = {};
    PRODUCTS.forEach(function (p) { p.photos.forEach(function (ph) { used[ph.f] = true; }); });
    return '<div class="view wrap credits">' +
      '<header class="page-head"><p class="eyebrow">Créditos</p><h1 class="display" tabindex="-1">Fotografias</h1>' +
      '<p>Fotografias ilustrativas de terceiros, sob licenças CC0, CC BY 4.0 e CC BY-SA 4.0. Não mostram produtos nem o local da Miolo, que é uma marca fictícia. Arquivos usados sem alteração de pixels; o enquadramento é feito apenas na exibição.</p></header>' +
      '<ul class="credit-list">' + CREDITS.filter(function (c) { return used[c[0]]; }).map(function (c) {
        return '<li class="credit"><img src="' + A + c[0] + '" alt="" loading="lazy"><div>' +
          '<p class="t">' + esc(c[1]) + '</p><p>Autor: ' + esc(c[2]) + '</p>' +
          '<p>Licença: <a href="' + c[4] + '" rel="noopener noreferrer">' + esc(c[3]) + '</a></p>' +
          '<p><a href="' + c[5] + '" rel="noopener noreferrer">Fonte (Wikimedia Commons)</a></p></div></li>';
      }).join('') + '</ul>' +
      '<p style="margin-top:28px"><a class="btn btn--ghost" href="#/">Voltar ao início</a></p>' +
    '</div>';
  }

  function viewNotFound() {
    return '<div class="view wrap page-head"><h1 class="display" tabindex="-1">Página não encontrada</h1><p>Este endereço não existe no protótipo.</p><p style="margin-top:20px"><a class="btn" href="#/fornada">Ver a fornada</a></p></div>';
  }

  /* ---------- Roteador ---------- */
  var main = document.getElementById('main');
  var lastRoute = '';

  function parse() {
    var h = (location.hash || '#/').replace(/^#/, '');
    if (h.charAt(0) !== '/') return null; // âncora interna
    var parts = h.split('/').filter(Boolean);
    return parts;
  }

  function render(focus) {
    var parts = parse();
    if (parts === null) {
      if (main.innerHTML.trim()) return; // âncora dentro da página atual
      parts = [];
    }
    var route = parts[0] || '';
    var html, nav = 'home', title = 'Miolo · Fornada de sábado';
    if (route === '') html = viewHome();
    else if (route === 'fornada') { html = viewCatalog(parts[1]); nav = 'catalog'; title = 'Fornada · Miolo'; }
    else if (route === 'produto') { html = viewDetail(parts[1]); nav = 'catalog'; var p = byId(parts[1]); title = (p ? p.name : 'Produto') + ' · Miolo'; }
    else if (route === 'encomenda') { html = viewOrder(); nav = 'order'; title = 'Encomenda · Miolo'; }
    else if (route === 'creditos') { html = viewCredits(); nav = ''; title = 'Créditos das fotos · Miolo'; }
    else { html = viewNotFound(); nav = ''; }
    state.reviewed = false;
    document.getElementById('toast').classList.remove('is-on');
    main.innerHTML = html;
    document.title = title;
    document.querySelectorAll('.nav__link').forEach(function (a) {
      if (a.getAttribute('data-route') === nav) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    var sameSection = lastRoute && lastRoute === route && route === 'fornada';
    lastRoute = route;
    if (!sameSection) window.scrollTo(0, 0);
    if (focus !== false && !sameSection) {
      var h1 = main.querySelector('h1');
      if (h1) h1.focus({ preventScroll: true });
    }
    updateCount();
  }

  function updateCount() {
    var el = document.getElementById('navCount');
    var n = count();
    el.textContent = n;
    el.setAttribute('data-empty', n === 0 ? 'true' : 'false');
    el.setAttribute('aria-label', n === 1 ? '1 item na encomenda' : n + ' itens na encomenda');
  }

  var toastT;
  function toast(msg) {
    var t = document.getElementById('toast');
    t.textContent = msg; t.classList.add('is-on');
    clearTimeout(toastT); toastT = setTimeout(function () { t.classList.remove('is-on'); }, 2600);
  }

  /* ---------- Atualização da encomenda sem re-render completo ---------- */
  function refreshOrderTotals() {
    Object.keys(state.items).forEach(function (id) {
      var el = main.querySelector('[data-line-sum="' + id + '"]');
      if (el) el.textContent = eur(byId(id).price * state.items[id]);
    });
    var st = document.getElementById('subtotal');
    if (st) st.textContent = eur(total());
    clearSummary();
    updateCount();
  }
  function clearSummary() {
    var host = document.getElementById('summaryHost');
    if (host && host.innerHTML) host.innerHTML = '';
  }

  /* ---------- Eventos ---------- */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('button, a');
    if (!t) return;

    if (t.hasAttribute('data-scroll')) {
      e.preventDefault();
      var target = document.getElementById(t.getAttribute('data-scroll'));
      if (target) {
        var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        target.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
        var hh = target.querySelector('h2'); if (hh) { hh.setAttribute('tabindex', '-1'); hh.focus({ preventScroll: true }); }
      }
      return;
    }
    if (t.hasAttribute('data-filter')) {
      var k = t.getAttribute('data-filter');
      var next = k === 'all' ? '#/fornada' : '#/fornada/' + k;
      if (location.hash !== next) location.hash = next;
      setTimeout(function () { var b = main.querySelector('[data-filter="' + k + '"]'); if (b) b.focus(); }, 0);
      return;
    }
    if (t.hasAttribute('data-photo')) {
      var p = byId(document.getElementById('addBtn').getAttribute('data-id'));
      var ph = p.photos[+t.getAttribute('data-photo')];
      var img = document.getElementById('mainPhoto');
      img.src = A + ph.f; img.alt = ph.alt; img.style.objectPosition = ph.pos;
      main.querySelectorAll('.thumb').forEach(function (b) { b.removeAttribute('aria-current'); });
      t.setAttribute('aria-current', 'true');
      return;
    }
    if (t.hasAttribute('data-step')) {
      var inp = document.getElementById('qty');
      var v = clampQ(inp.value) || 1;
      inp.value = Math.max(1, Math.min(MAXQ, v + parseInt(t.getAttribute('data-step'), 10)));
      syncStepper();
      return;
    }
    if (t.id === 'addBtn') {
      var id = t.getAttribute('data-id');
      var q = Math.max(1, clampQ(document.getElementById('qty').value) || 1);
      var cur = state.items[id] || 0;
      var nq = Math.min(MAXQ, cur + q);
      state.items[id] = nq;
      persist(); updateCount();
      var prod = byId(id);
      var msg = nq - cur < q
        ? 'Limite de ' + MAXQ + ' por item. Na encomenda: ' + nq + '.'
        : 'Adicionado: ' + q + ' × ' + prod.name + '. Na encomenda: ' + nq + '.';
      document.getElementById('added').innerHTML = esc(msg) + ' <a href="#/encomenda">Ver encomenda</a>';
      toast(msg);
      return;
    }
    if (t.hasAttribute('data-remove')) {
      var rid = t.getAttribute('data-remove');
      var name = byId(rid).name;
      delete state.items[rid];
      persist();
      render(false);
      var nextBtn = main.querySelector('[data-remove]') || main.querySelector('.empty .btn');
      if (nextBtn) nextBtn.focus();
      toast(name + ' removido da encomenda.');
      return;
    }
    if (t.id === 'reviewBtn') {
      var err = document.getElementById('slotErr');
      if (!Object.keys(state.items).length) return;
      if (!state.slot) {
        err.textContent = 'Escolha um horário de retirada para revisar.';
        var first = main.querySelector('input[name="pickup"]'); if (first) first.focus();
        return;
      }
      err.textContent = '';
      var host = document.getElementById('summaryHost');
      host.innerHTML = summaryHTML();
      var s = host.firstChild;
      var reduce2 = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      s.scrollIntoView({ behavior: reduce2 ? 'auto' : 'smooth', block: 'start' });
      s.focus({ preventScroll: true });
      return;
    }
    if (t.id === 'editBtn') {
      clearSummary();
      var sel = main.querySelector('[data-qty]'); if (sel) sel.focus();
      return;
    }
  });

  function syncStepper() {
    var inp = document.getElementById('qty'); if (!inp) return;
    var v = clampQ(inp.value);
    main.querySelector('[data-step="-1"]').disabled = v <= 1;
    main.querySelector('[data-step="1"]').disabled = v >= MAXQ;
  }

  document.addEventListener('change', function (e) {
    var t = e.target;
    if (t.matches('[data-qty]')) {
      var id = t.getAttribute('data-qty');
      var q = clampQ(t.value);
      if (q < 1) q = 1;
      t.value = q;
      state.items[id] = q;
      persist(); refreshOrderTotals();
    } else if (t.name === 'pickup') {
      state.slot = SLOTS.indexOf(t.value) > -1 ? t.value : '';
      persist();
      var err = document.getElementById('slotErr'); if (err) err.textContent = '';
      clearSummary();
    } else if (t.id === 'qty') {
      var v = clampQ(t.value);
      t.value = v < 1 ? 1 : v;
      syncStepper();
    }
  });
  document.addEventListener('input', function (e) {
    if (e.target.id === 'qty') syncStepper();
  });

  window.addEventListener('hashchange', function () { render(); });
  render(false);
  syncStepper();
  window.addEventListener('hashchange', syncStepper);
})();
