/* Tábua — protótipo local. Sem rede, sem envio, sem armazenamento de dados pessoais. */
(function () {
  'use strict';

  var SESSIONS = {
    'aberta': {
      id: 'aberta', name: 'Sessão aberta', short: 'Aberta',
      duration: '90 min', price: 18, priceLabel: '€18 por pessoa', mode: 'person',
      min: 1, max: 8, capacity: 'até 8 pessoas',
      when: 'Ter–Sex 17:00 e 19:00 · Sáb 10:00, 14:00, 17:00 · Dom 10:00',
      img: 'assets/bench-1.jpg', pos: '50% 62%',
      alt: 'Banco de troncos de madeira sobre um deck, com o mar e rochas ao fundo sob céu nublado.',
      lede: 'Disponível de terça a domingo. Você divide a sauna e o deck com outras pessoas e segue o ritual no seu ritmo.',
      rules: ['Sauna compartilhada: silêncio dentro da sauna.', 'Maiores de 18 anos.', 'Banho de mar opcional, por conta e risco de cada pessoa; não há salva-vidas no local.', 'Sem álcool.']
    },
    'nascer-sol': {
      id: 'nascer-sol', name: 'Nascer do sol', short: 'Nascer do sol',
      duration: '90 min', price: 22, priceLabel: '€22 por pessoa', mode: 'person',
      min: 1, max: 8, capacity: 'até 8 pessoas',
      when: 'Sáb e Dom 07:00',
      img: 'assets/abyfjorden-estuary-2.jpg', pos: '30% 55%',
      alt: 'Luz baixa de sol entre nuvens sobre uma enseada calma, com uma casinha de madeira junto às rochas.',
      lede: 'A primeira sessão do sábado e do domingo, às 07:00. Mesmo formato da Sessão aberta, em outro horário e com outro preço.',
      rules: ['Silêncio dentro da sauna.', 'Maiores de 18 anos.', 'Banho de mar opcional, por conta e risco de cada pessoa; não há salva-vidas no local.', 'Sem álcool.']
    },
    'privativa': {
      id: 'privativa', name: 'Sauna privativa', short: 'Privativa',
      duration: '2 h', price: 120, priceLabel: '€120 por grupo', mode: 'group',
      min: 1, max: 6, capacity: '1 a 6 pessoas',
      when: 'Dom 15:00 · Qua 20:00',
      img: 'assets/jetties-1.jpg', pos: '50% 60%',
      alt: 'Deck de madeira em primeiro plano diante de um píer e da água refletindo o céu do fim de tarde.',
      lede: 'A sauna e o deck só para o seu grupo, por duas horas. O valor é o mesmo para 1 a 6 pessoas.',
      rules: ['Valor fixo por grupo, de 1 a 6 pessoas.', 'Todas as pessoas do grupo devem ter mais de 18 anos.', 'Banho de mar opcional, por conta e risco de cada pessoa; não há salva-vidas no local.', 'Sem álcool, também em grupo privado.']
    }
  };
  var ORDER = ['aberta', 'nascer-sol', 'privativa'];

  var WEEK = [
    { key: 'seg', name: 'Segunda', abbr: 'Seg', slots: [] },
    { key: 'ter', name: 'Terça', abbr: 'Ter', slots: [['17:00', 'aberta'], ['19:00', 'aberta']] },
    { key: 'qua', name: 'Quarta', abbr: 'Qua', slots: [['17:00', 'aberta'], ['19:00', 'aberta'], ['20:00', 'privativa']] },
    { key: 'qui', name: 'Quinta', abbr: 'Qui', slots: [['17:00', 'aberta'], ['19:00', 'aberta']] },
    { key: 'sex', name: 'Sexta', abbr: 'Sex', slots: [['17:00', 'aberta'], ['19:00', 'aberta']] },
    { key: 'sab', name: 'Sábado', abbr: 'Sáb', slots: [['07:00', 'nascer-sol'], ['10:00', 'aberta'], ['14:00', 'aberta'], ['17:00', 'aberta']] },
    { key: 'dom', name: 'Domingo', abbr: 'Dom', slots: [['07:00', 'nascer-sol'], ['10:00', 'aberta'], ['15:00', 'privativa']] }
  ];

  var STEPS = [
    ['Aqueça na sauna', '10 a 15 min', 'Entre, sente-se no banco de madeira e fique enquanto estiver confortável. O tempo é uma referência, não uma meta.'],
    ['Desça a escada para o mar', 'se quiser', 'A escada sai do píer direto para a água. Entrar é opcional e por sua conta e risco: não há salva-vidas no local.'],
    ['Descanse no deck', 'sem pressa', 'Sente-se ao ar livre, enrole-se na toalha e olhe a enseada.'],
    ['Repita no seu ritmo', 'quantas vezes quiser', 'Volte ao calor quando tiver vontade, dentro do tempo da sessão.']
  ];

  var BRING = [
    ['Toalha', 'towel'], ['Roupa de banho', 'swim'], ['Chinelo', 'sandal'], ['Garrafa de água', 'bottle']
  ];

  var RULES = [
    ['Maiores de 18 anos', 'Todas as sessões são só para adultos.'],
    ['Banho de mar por conta e risco de cada pessoa', 'Não há salva-vidas no local. Entrar no mar é sempre opcional.'],
    ['Sem álcool', 'Não é permitido trazer nem consumir bebidas alcoólicas.'],
    ['Silêncio na sauna', 'Dentro da sauna, silêncio. Para conversar, use o deck.']
  ];

  var DISCLAIMER = 'Protótipo demonstrativo. Marca, local, horários e preços fictícios. Nada é reservado.';
  var SCHEDULE_NOTE = 'Programação ilustrativa; disponibilidade não verificada neste protótipo.';

  /* ---------- helpers ---------- */
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function euro(n) { return '€' + n; }

  var ICONS = {
    towel: '<path d="M7 5h14v22H7z"/><path d="M7 10h14M7 22h14"/><path d="M21 5h4v16h-4"/>',
    swim: '<path d="M4 22c3 0 3-2 6-2s3 2 6 2 3-2 6-2 3 2 6 2"/><path d="M4 27c3 0 3-2 6-2s3 2 6 2 3-2 6-2 3 2 6 2"/><path d="M12 17l4-9 6 3"/><circle cx="22" cy="6" r="2"/>',
    sandal: '<path d="M10 4c-3 0-5 3-5 9s2 15 5 15 4-3 4-12-1-12-4-12z"/><path d="M5.5 12c3 1 5.5 1 8.3 0"/><path d="M22 4c-3 0-4 3-4 12s1 12 4 12 5-9 5-15-2-9-5-9z"/><path d="M18.2 12c2.8 1 5.3 1 8.3 0"/>',
    bottle: '<path d="M13 3h6v4h-6z"/><path d="M12 7h8l2 4v17a1 1 0 0 1-1 1H11a1 1 0 0 1-1-1V11z"/><path d="M10 15h12M10 22h12"/>'
  };
  function icon(name) {
    return '<svg class="ico" viewBox="0 0 32 32" aria-hidden="true" focusable="false">' + ICONS[name] + '</svg>';
  }
  var ARROW = '<svg class="arr" viewBox="0 0 20 12" aria-hidden="true" focusable="false"><path d="M0 6h18M13 1l5 5-5 5"/></svg>';

  function sessionCard(s, headingTag) {
    var h = headingTag || 'h3';
    return '<article class="scard">' +
      '<a class="scard__link" href="#/sessao/' + s.id + '" data-testid="session-' + s.id + '">' +
      '<div class="scard__img"><img src="' + s.img + '" alt="' + esc(s.alt) + '" loading="lazy" style="object-position:' + s.pos + '"></div>' +
      '<div class="scard__body">' +
      '<' + h + ' class="scard__title">' + esc(s.name) + '</' + h + '>' +
      '<dl class="facts"><div><dt>Duração</dt><dd>' + s.duration + '</dd></div><div><dt>Preço</dt><dd>' + s.priceLabel + '</dd></div><div><dt>Capacidade</dt><dd>' + s.capacity + '</dd></div></dl>' +
      '<p class="scard__when">' + esc(s.when) + '</p>' +
      '<span class="scard__more">Ver detalhes ' + ARROW + '</span>' +
      '</div></a></article>';
  }

  /* ---------- views ---------- */
  function viewHome() {
    var steps = STEPS.map(function (st, i) {
      return '<li class="plank"><span class="plank__n">0' + (i + 1) + '</span>' +
        '<div class="plank__t"><h3>' + esc(st[0]) + '</h3><span class="plank__tag">' + esc(st[1]) + '</span></div>' +
        '<p>' + esc(st[2]) + '</p></li>';
    }).join('');
    var bring = BRING.map(function (b) { return '<li>' + icon(b[1]) + '<span>' + esc(b[0]) + '</span></li>'; }).join('');
    var rules = RULES.map(function (r) { return '<li><strong>' + esc(r[0]) + '</strong><span>' + esc(r[1]) + '</span></li>'; }).join('');
    var weekMini = WEEK.map(function (d) {
      var times = d.slots.length ? d.slots.map(function (s) { return s[0]; }).join(' · ') : 'Fechado';
      return '<li class="' + (d.slots.length ? '' : 'is-closed') + '"><span class="wk__d">' + d.abbr + '</span><span class="wk__t">' + times + '</span></li>';
    }).join('');

    return '' +
      '<section class="hero" aria-labelledby="h-hero">' +
        '<div class="hero__media"><img src="assets/bathing-ladder.jpg" alt="Escada de banho de madeira descendo de um píer para a água calma, com outros píeres e rochas ao fundo." style="object-position:62% 58%"></div>' +
        '<div class="hero__panel">' +
          '<p class="eyebrow">Tábua · sauna a lenha no píer</p>' +
          '<h1 id="h-hero" class="hero__title" tabindex="-1"><span>Aqueça.</span> <span>Mergulhe.</span> <span>Descanse.</span></h1>' +
          '<p class="hero__text">Uma sauna a lenha sobre o píer, com escada direto para o mar.</p>' +
          '<div class="hero__actions"><a class="btn btn--ember" href="#/horarios">Ver horários ' + ARROW + '</a>' +
          '<a class="btn btn--line" href="#/planejar">Calcular uma visita</a></div>' +
        '</div>' +
      '</section>' +

      '<section class="sig wrap" aria-label="Assinatura">' +
        '<p class="sig__line"><span>Calor de lenha.</span> <em>Mar logo ali.</em></p>' +
        '<ul class="sig__facts">' +
          '<li><span class="k">Funciona</span><span class="v">Ter a Dom</span></li>' +
          '<li><span class="k">Segunda</span><span class="v">Fechado</span></li>' +
          '<li><span class="k">Sessões</span><span class="v">90 min ou 2 h</span></li>' +
          '<li><span class="k">A partir de</span><span class="v">€18</span></li>' +
        '</ul>' +
      '</section>' +

      '<section class="how" id="como-funciona" aria-labelledby="h-how">' +
        '<div class="wrap how__grid">' +
          '<div class="how__head">' +
            '<p class="eyebrow">Como funciona</p>' +
            '<h2 id="h-how" class="h2">Quatro passos, no seu ritmo.</h2>' +
            '<figure class="how__fig"><img src="assets/jetty-and-water-2.jpg" alt="Tábuas de um deck de madeira na borda do píer, com a água ondulada logo à frente." loading="lazy" style="object-position:50% 70%"></figure>' +
          '</div>' +
          '<ol class="planks">' + steps + '</ol>' +
        '</div>' +
      '</section>' +

      '<section class="sessions wrap" aria-labelledby="h-sess">' +
        '<div class="sec-head"><p class="eyebrow">Sessões</p><h2 id="h-sess" class="h2">Três formas de visitar.</h2></div>' +
        '<div class="scards">' + ORDER.map(function (id) { return sessionCard(SESSIONS[id]); }).join('') + '</div>' +
      '</section>' +

      '<section class="week" aria-labelledby="h-week">' +
        '<div class="wrap week__in">' +
          '<div><p class="eyebrow eyebrow--light">Programação semanal</p><h2 id="h-week" class="h2">A semana no píer.</h2>' +
          '<p class="muted-light">' + SCHEDULE_NOTE + '</p>' +
          '<a class="btn btn--ember" href="#/horarios">Ver horários ' + ARROW + '</a></div>' +
          '<ul class="wk">' + weekMini + '</ul>' +
        '</div>' +
      '</section>' +

      '<section class="prep wrap" aria-labelledby="h-bring">' +
        '<div class="prep__col">' +
          '<p class="eyebrow">O que levar</p><h2 id="h-bring" class="h2">Pouca coisa.</h2>' +
          '<ul class="bring">' + bring + '</ul>' +
        '</div>' +
        '<div class="prep__col">' +
          '<p class="eyebrow">Regras</p><h2 class="h2">Quatro combinados.</h2>' +
          '<ul class="rules">' + rules + '</ul>' +
          '<a class="link" href="#/regras">Regras e perguntas frequentes ' + ARROW + '</a>' +
        '</div>' +
      '</section>' +

      '<section class="band" aria-labelledby="h-band">' +
        '<div class="band__img"><img src="assets/pier-and-jetty-3.jpg" alt="Píer comprido avançando sobre a enseada ao entardecer, com nuvens iluminadas." style="object-position:50% 62%"></div>' +
        '<div class="band__txt wrap"><h2 id="h-band" class="h2">Quanto custa a sua visita?</h2>' +
        '<p>Escolha a sessão e o número de pessoas para ver um valor estimado. Nada é reservado.</p>' +
        '<a class="btn btn--paper" href="#/planejar">Planejar visita ' + ARROW + '</a></div>' +
      '</section>';
  }

  function scheduleRows(filter) {
    var rows = WEEK.map(function (d) {
      var slots = d.slots.filter(function (s) { return filter === 'nascer-sol' ? s[1] === 'nascer-sol' : true; });
      if (filter === 'nascer-sol' && !slots.length) return '';
      var cells = slots.length ? slots.map(function (s) {
        var ses = SESSIONS[s[1]];
        return '<li><a class="slot slot--' + ses.id + '" href="#/sessao/' + ses.id + '" data-testid="schedule-slot" data-session="' + ses.id + '">' +
          '<span class="slot__t">' + s[0] + '</span><span class="slot__n">' + esc(ses.name) + '</span><span class="slot__p">' + ses.duration + ' · ' + ses.priceLabel + '</span>' +
          '<span class="sr">, ' + d.name + '</span></a></li>';
      }).join('') : '<li class="slot-closed">Fechado</li>';
      return '<div class="day' + (slots.length ? '' : ' day--closed') + '"><h3 class="day__name"><span class="day__abbr" aria-hidden="true">' + d.abbr + '</span><span class="day__full">' + d.name + '</span></h3><ul class="day__slots">' + cells + '</ul></div>';
    }).join('');
    return rows;
  }

  function viewSchedule(q) {
    var filter = q.f === 'nascer-sol' ? 'nascer-sol' : 'todas';
    return '' +
      '<section class="page-head wrap">' +
        '<p class="eyebrow">Horários</p>' +
        '<h1 class="h1" tabindex="-1">Programação semanal</h1>' +
        '<p class="lede">Terça a domingo. Segunda-feira: fechado. Toque num horário para ver a sessão.</p>' +
      '</section>' +
      '<section class="wrap sched" aria-label="Programação">' +
        '<div class="sched__bar">' +
          '<div class="seg" role="group" aria-label="Filtrar programação">' +
            '<button type="button" class="seg__b" data-filter="todas" data-testid="schedule-filter-all" aria-pressed="' + (filter === 'todas') + '">Todas</button>' +
            '<button type="button" class="seg__b" data-filter="nascer-sol" data-testid="schedule-filter-sunrise" aria-pressed="' + (filter === 'nascer-sol') + '">Nascer do sol</button>' +
          '</div>' +
          '<p class="sched__note" role="note">' + SCHEDULE_NOTE + '</p>' +
        '</div>' +
        '<p class="sr" aria-live="polite" id="sched-status">' + (filter === 'nascer-sol' ? 'Mostrando somente sessões Nascer do sol.' : 'Mostrando todas as sessões.') + '</p>' +
        '<div class="days" id="days">' + scheduleRows(filter) + '</div>' +
        '<ul class="legend" aria-label="Tipos de sessão">' + ORDER.map(function (id) {
          var s = SESSIONS[id];
          return '<li><a href="#/sessao/' + id + '" data-testid="session-' + id + '" class="legend__a"><span class="dot dot--' + id + '" aria-hidden="true"></span><span class="legend__n">' + esc(s.name) + '</span><span class="legend__m">' + s.duration + ' · ' + s.priceLabel + ' · ' + s.capacity + '</span>' + ARROW + '</a></li>';
        }).join('') + '</ul>' +
        '<div class="sched__cta"><a class="btn btn--ember" href="#/planejar">Calcular valor estimado ' + ARROW + '</a></div>' +
      '</section>';
  }

  function viewSession(id) {
    var s = SESSIONS[id];
    if (!s) return viewNotFound();
    var times = WEEK.filter(function (d) { return d.slots.some(function (x) { return x[1] === id; }); }).map(function (d) {
      return '<li><span class="t-day">' + d.name + '</span><span class="t-times">' + d.slots.filter(function (x) { return x[1] === id; }).map(function (x) { return x[0]; }).join(' · ') + '</span></li>';
    }).join('');
    var others = ORDER.filter(function (o) { return o !== id; }).map(function (o) {
      return '<a class="other" href="#/sessao/' + o + '" data-testid="session-' + o + '"><span>' + esc(SESSIONS[o].name) + '</span>' + ARROW + '</a>';
    }).join('');
    return '' +
      '<article class="detail">' +
        '<div class="detail__media"><img src="' + s.img + '" alt="' + esc(s.alt) + '" style="object-position:' + s.pos + '"></div>' +
        '<div class="detail__body">' +
          '<nav class="crumb" aria-label="Você está em"><a href="#/horarios">Horários</a> <span aria-hidden="true">/</span> <span aria-current="page">' + esc(s.name) + '</span></nav>' +
          '<h1 class="h1" tabindex="-1">' + esc(s.name) + '</h1>' +
          '<p class="lede">' + esc(s.lede) + '</p>' +
          '<dl class="facts facts--lg"><div><dt>Duração</dt><dd>' + s.duration + '</dd></div><div><dt>Preço</dt><dd>' + s.priceLabel + '</dd></div><div><dt>Capacidade</dt><dd>' + s.capacity + '</dd></div></dl>' +
          '<h2 class="h3">Horários</h2>' +
          '<ul class="times">' + times + '</ul>' +
          '<p class="small muted">' + SCHEDULE_NOTE + '</p>' +
          '<h2 class="h3">Regras desta sessão</h2>' +
          '<ul class="ticks">' + s.rules.map(function (r) { return '<li>' + esc(r) + '</li>'; }).join('') + '</ul>' +
          '<div class="detail__actions">' +
            '<a class="btn btn--ember" href="#/planejar?s=' + id + '">Calcular esta visita ' + ARROW + '</a>' +
            '<a class="btn btn--line" href="#/horarios">Ver horários</a>' +
          '</div>' +
          '<div class="others"><p class="eyebrow">Outras sessões</p>' + others + '</div>' +
        '</div>' +
      '</article>';
  }

  function viewPlan(q) {
    var sel = SESSIONS[q.s] ? q.s : 'aberta';
    return '' +
      '<section class="page-head wrap">' +
        '<p class="eyebrow">Planejar visita</p>' +
        '<h1 class="h1" tabindex="-1">Quanto fica a sua visita</h1>' +
        '<p class="lede">Um cálculo feito aqui no seu aparelho. Sem envio, sem pagamento, sem cadastro.</p>' +
      '</section>' +
      '<section class="wrap planner" aria-label="Planejador">' +
        '<form class="pl" id="plan-form" novalidate>' +
          '<div class="field">' +
            '<label for="plan-session">Tipo de sessão</label>' +
            '<div class="select"><select id="plan-session" name="session" data-testid="plan-session">' +
              ORDER.map(function (id) { var s = SESSIONS[id]; return '<option value="' + id + '"' + (id === sel ? ' selected' : '') + '>' + esc(s.name) + ' · ' + s.priceLabel + '</option>'; }).join('') +
            '</select></div>' +
          '</div>' +
          '<div class="field">' +
            '<label for="plan-people">Número de pessoas</label>' +
            '<div class="stepper">' +
              '<button type="button" class="stepper__b" data-step="-1" aria-label="Diminuir uma pessoa" aria-controls="plan-people">−</button>' +
              '<input id="plan-people" name="people" type="number" inputmode="numeric" min="1" max="8" step="1" value="2" data-testid="plan-people" aria-describedby="plan-hint plan-error-slot">' +
              '<button type="button" class="stepper__b" data-step="1" aria-label="Aumentar uma pessoa" aria-controls="plan-people">+</button>' +
            '</div>' +
            '<p class="hint" id="plan-hint"></p>' +
            '<div id="plan-error-slot" aria-live="assertive"></div>' +
          '</div>' +
        '</form>' +
        '<aside class="receipt" aria-labelledby="h-rec">' +
          '<h2 id="h-rec" class="receipt__h">Valor estimado</h2>' +
          '<output class="receipt__total" id="plan-total" data-testid="plan-total" for="plan-session plan-people" aria-live="polite">—</output>' +
          '<p class="receipt__calc" id="plan-calc"></p>' +
          '<dl class="receipt__dl" id="plan-dl"></dl>' +
          '<p class="receipt__note"><strong>' + DISCLAIMER + '</strong></p>' +
          '<p class="receipt__note">' + SCHEDULE_NOTE + '</p>' +
          '<a class="link" id="plan-detail" href="#/sessao/' + sel + '">Ver detalhes da sessão ' + ARROW + '</a>' +
        '</aside>' +
      '</section>';
  }

  function viewRules() {
    var faq = [
      ['Preciso entrar no mar?', 'Não. Descer a escada é opcional. Se entrar, é por sua conta e risco: não há salva-vidas no local.'],
      ['Qual a idade mínima?', 'Todas as sessões são para maiores de 18 anos.'],
      ['Qual a diferença entre as sessões?', 'A Sessão aberta (90 min, €18 por pessoa, até 8 pessoas) e a Nascer do sol (90 min, €22 por pessoa, até 8 pessoas, sábado e domingo às 07:00) são compartilhadas. A Sauna privativa (2 h, €120 por grupo de 1 a 6 pessoas) é só para o seu grupo.'],
      ['Quanto tempo devo ficar na sauna?', 'A referência do ritual é de 10 a 15 minutos por vez. Saia quando quiser e repita no seu ritmo.'],
      ['O que preciso levar?', 'Toalha, roupa de banho, chinelo e garrafa de água.'],
      ['Posso conversar?', 'No deck, sim. Dentro da sauna, silêncio.'],
      ['Posso levar bebida alcoólica?', 'Não. A Tábua não permite álcool.'],
      ['Abre na segunda-feira?', 'Não. Segunda-feira: fechado. As sessões acontecem de terça a domingo.'],
      ['Consigo reservar por este site?', 'Não. Este é um protótipo demonstrativo: marca, local, horários e preços são fictícios e nada é reservado. O planejador só calcula um valor estimado no seu aparelho.'],
      ['Os horários mostram vagas disponíveis?', 'Não. ' + SCHEDULE_NOTE]
    ];
    return '' +
      '<section class="page-head wrap">' +
        '<p class="eyebrow">Regras e perguntas</p>' +
        '<h1 class="h1" tabindex="-1">Antes de subir no píer</h1>' +
        '<p class="lede">Combinados simples para todo mundo aproveitar o calor e o mar com tranquilidade.</p>' +
      '</section>' +
      '<section class="wrap rules-page">' +
        '<div><h2 class="h3">Regras obrigatórias</h2>' +
        '<ol class="rules rules--big">' + RULES.map(function (r) { return '<li><strong>' + esc(r[0]) + '</strong><span>' + esc(r[1]) + '</span></li>'; }).join('') + '</ol>' +
        '<h2 class="h3">O que levar</h2>' +
        '<ul class="bring bring--row">' + BRING.map(function (b) { return '<li>' + icon(b[1]) + '<span>' + esc(b[0]) + '</span></li>'; }).join('') + '</ul></div>' +
        '<div><h2 class="h3">Perguntas frequentes</h2>' +
        '<div class="faq">' + faq.map(function (f) { return '<details><summary>' + esc(f[0]) + '</summary><p>' + esc(f[1]) + '</p></details>'; }).join('') + '</div></div>' +
      '</section>';
  }

  function viewCredits() {
    var c = window.TABUA_CREDITS || { images: [] };
    var items = c.images.map(function (im) {
      return '<li class="cr"><img src="assets/' + esc(im.file) + '" alt="" loading="lazy">' +
        '<div><p class="cr__t">' + esc(im.title) + '</p>' +
        '<p class="cr__m">Autor: ' + esc(im.author) + ' · Licença: <a href="' + esc(im.license_url) + '" rel="noopener">' + esc(im.license) + '</a> · <a href="' + esc(im.source) + '" rel="noopener">Fonte (Wikimedia Commons)</a></p>' +
        '<p class="cr__m">' + esc(im.description) + ' Arquivo: ' + esc(im.file) + '. ' + esc(im.modification) + '.</p></div></li>';
    }).join('');
    return '' +
      '<section class="page-head wrap">' +
        '<p class="eyebrow">Créditos</p>' +
        '<h1 class="h1" tabindex="-1">Créditos das fotografias</h1>' +
        '<p class="lede">Fotografias ilustrativas de outro local (domínio público, CC0); não retratam as instalações da marca fictícia.</p>' +
      '</section>' +
      '<section class="wrap"><ul class="credits">' + items + '</ul></section>';
  }

  function viewNotFound() {
    return '<section class="page-head wrap"><p class="eyebrow">Página não encontrada</p><h1 class="h1" tabindex="-1">Este caminho não leva ao píer.</h1>' +
      '<p class="lede">Volte para o início ou veja os horários.</p><div class="hero__actions"><a class="btn btn--ember" href="#/">Início</a> <a class="btn btn--line" href="#/horarios">Ver horários</a></div></section>';
  }

  /* ---------- planner logic ---------- */
  function computePlan(sessionId, raw, badInput) {
    var s = SESSIONS[sessionId];
    if (!s) return { error: 'Escolha um tipo de sessão.' };
    var str = String(raw == null ? '' : raw).trim();
    var range = s.mode === 'group' ? 'de 1 a 6 pessoas' : 'de 1 a 8 pessoas';
    if (badInput) return { error: 'Use apenas números inteiros: ' + range + '.' };
    if (str === '') return { error: 'Informe o número de pessoas (' + range + ').' };
    if (!/^\d+$/.test(str)) return { error: 'Use um número inteiro de pessoas, ' + range + '.' };
    var n = parseInt(str, 10);
    if (!isFinite(n) || n < s.min) return { error: 'O mínimo é 1 pessoa.' };
    if (n > s.max) {
      return { error: s.mode === 'group'
        ? 'A Sauna privativa recebe ' + range + '. Com ' + n + ' pessoas, não há valor estimado.'
        : 'A ' + s.name + ' recebe ' + range + ' por visita. Com ' + n + ' pessoas, não há valor estimado.' };
    }
    var total = s.mode === 'group' ? s.price : s.price * n;
    if (!isFinite(total) || total < 0) return { error: 'Não foi possível calcular. Revise os valores.' };
    return { total: total, n: n, s: s };
  }

  function bindPlanner() {
    var sel = document.getElementById('plan-session');
    var inp = document.getElementById('plan-people');
    var out = document.getElementById('plan-total');
    var calc = document.getElementById('plan-calc');
    var dl = document.getElementById('plan-dl');
    var hint = document.getElementById('plan-hint');
    var slot = document.getElementById('plan-error-slot');
    var det = document.getElementById('plan-detail');
    var rec = document.querySelector('.receipt');

    function update() {
      var s = SESSIONS[sel.value];
      inp.max = String(s.max);
      hint.textContent = s.mode === 'group' ? 'Sauna privativa: valor fixo de €120 para 1 a 6 pessoas.' : s.name + ': ' + euro(s.price) + ' por pessoa, de 1 a 8 pessoas.';
      det.setAttribute('href', '#/sessao/' + s.id);
      var r = computePlan(sel.value, inp.value, inp.validity && inp.validity.badInput);
      if (r.error) {
        slot.innerHTML = '<p class="err" id="plan-error" data-testid="plan-error" role="alert">' + esc(r.error) + '</p>';
        inp.setAttribute('aria-invalid', 'true');
        out.textContent = '—';
        calc.textContent = 'Sem valor estimado enquanto o número de pessoas estiver fora do limite.';
        dl.innerHTML = '';
        rec.classList.add('is-error');
      } else {
        slot.innerHTML = '';
        inp.removeAttribute('aria-invalid');
        out.textContent = euro(r.total);
        calc.textContent = s.mode === 'group'
          ? euro(s.price) + ' por grupo · ' + r.n + (r.n === 1 ? ' pessoa' : ' pessoas')
          : euro(s.price) + ' × ' + r.n + (r.n === 1 ? ' pessoa' : ' pessoas');
        dl.innerHTML = '<div><dt>Sessão</dt><dd>' + esc(s.name) + '</dd></div><div><dt>Duração</dt><dd>' + s.duration + '</dd></div><div><dt>Quando</dt><dd>' + esc(s.when) + '</dd></div>';
        rec.classList.remove('is-error');
        out.classList.remove('tick'); void out.offsetWidth; out.classList.add('tick');
      }
      var n = parseInt(inp.value, 10);
      document.querySelector('[data-step="-1"]').disabled = !(n > 1);
      document.querySelector('[data-step="1"]').disabled = (n >= s.max);
    }
    sel.addEventListener('change', update);
    inp.addEventListener('input', update);
    document.getElementById('plan-form').addEventListener('submit', function (e) { e.preventDefault(); update(); });
    Array.prototype.forEach.call(document.querySelectorAll('.stepper__b'), function (b) {
      b.addEventListener('click', function () {
        var s = SESSIONS[sel.value];
        var n = parseInt(inp.value, 10);
        if (!isFinite(n)) n = 0;
        n = Math.min(s.max, Math.max(1, n + Number(b.getAttribute('data-step'))));
        inp.value = String(n);
        update();
      });
    });
    update();
  }

  function bindSchedule() {
    var btns = document.querySelectorAll('.seg__b');
    Array.prototype.forEach.call(btns, function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-filter');
        Array.prototype.forEach.call(btns, function (x) { x.setAttribute('aria-pressed', String(x === b)); });
        var days = document.getElementById('days');
        days.innerHTML = scheduleRows(f);
        days.classList.remove('fade'); void days.offsetWidth; days.classList.add('fade');
        document.getElementById('sched-status').textContent = f === 'nascer-sol' ? 'Mostrando somente sessões Nascer do sol.' : 'Mostrando todas as sessões.';
        try { history.replaceState(null, '', f === 'nascer-sol' ? '#/horarios?f=nascer-sol' : '#/horarios'); } catch (e) { /* file:// sem history */ }
      });
    });
  }

  /* ---------- router ---------- */
  function parse() {
    var h = (location.hash || '#/').replace(/^#/, '');
    if (h === '' || h.charAt(0) !== '/') h = '/' + h;
    var parts = h.split('?');
    var q = {};
    (parts[1] || '').split('&').forEach(function (kv) { if (!kv) return; var p = kv.split('='); q[decodeURIComponent(p[0])] = decodeURIComponent(p[1] || ''); });
    return { path: parts[0].replace(/\/+$/, '') || '/', q: q };
  }

  var main = document.getElementById('conteudo');
  var first = true;

  function render() {
    var r = parse();
    var html, route = 'home', title = 'Tábua · Sauna no píer';
    var m;
    if (r.path === '/' ) { html = viewHome(); }
    else if (r.path === '/horarios') { html = viewSchedule(r.q); route = 'horarios'; title = 'Horários · Tábua'; }
    else if (r.path === '/planejar') { html = viewPlan(r.q); route = 'planejar'; title = 'Planejar visita · Tábua'; }
    else if (r.path === '/regras') { html = viewRules(); route = 'regras'; title = 'Regras e perguntas · Tábua'; }
    else if (r.path === '/creditos') { html = viewCredits(); route = 'creditos'; title = 'Créditos das fotos · Tábua'; }
    else if ((m = r.path.match(/^\/sessao\/([a-z-]+)$/)) && SESSIONS[m[1]]) { html = viewSession(m[1]); route = 'sessao'; title = SESSIONS[m[1]].name + ' · Tábua'; }
    else if (r.path === '/como-funciona') { html = viewHome(); }
    else { html = viewNotFound(); route = 'none'; title = 'Página não encontrada · Tábua'; }

    main.innerHTML = '<div class="view view--' + route + '">' + html + '</div>';
    document.title = title;
    document.body.setAttribute('data-route', route);
    Array.prototype.forEach.call(document.querySelectorAll('.nav a'), function (a) {
      var on = a.getAttribute('data-route') === route || (route === 'sessao' && a.getAttribute('data-route') === 'horarios');
      if (on) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    if (route === 'planejar') bindPlanner();
    if (route === 'horarios') bindSchedule();

    if (r.path === '/como-funciona') {
      var el = document.getElementById('como-funciona');
      if (el) el.scrollIntoView();
    } else {
      window.scrollTo(0, 0);
    }
    if (!first) {
      var h1 = main.querySelector('h1');
      if (h1) h1.focus({ preventScroll: true });
    }
    first = false;
  }

  window.addEventListener('hashchange', render);
  render();

  window.TABUA = { computePlan: computePlan };
})();
