/* Tábua — protótipo local. Sem rede, sem envio, sem armazenamento de dados pessoais. */
(function () {
  'use strict';

  var SESSIONS = {
    'aberta': {
      id: 'aberta', name: 'Sessão aberta', short: 'Aberta', duration: '90 min',
      price: 18, unit: 'por pessoa', perPerson: true, min: 1, max: 8,
      capacity: 'até 8 pessoas', when: 'Ter–Sex 17:00 e 19:00 · Sáb 10:00, 14:00, 17:00 · Dom 10:00',
      img: 'assets/bench-2.jpg', imgPos: '50% 60%',
      alt: 'Banco de troncos sobre um deque de madeira, com a água da enseada e morros ao fundo sob céu nublado.',
      lede: 'O formato do dia a dia: você divide a sauna e o deque com outras pessoas, no seu próprio ritmo.',
      notes: [
        'Chegue cerca de 10 minutos antes para trocar de roupa com calma.',
        'O tempo dentro da sauna é por sua conta; a sugestão é de 10 a 15 minutos por rodada.',
        'Ambiente compartilhado: a sauna é um espaço de silêncio.'
      ]
    },
    'nascer-sol': {
      id: 'nascer-sol', name: 'Nascer do sol', short: 'Nascer do sol', duration: '90 min',
      price: 22, unit: 'por pessoa', perPerson: true, min: 1, max: 8,
      capacity: 'até 8 pessoas', when: 'Sáb e Dom 07:00',
      img: 'assets/abyfjorden-estuary-2.jpg', imgPos: '30% 55%',
      alt: 'Luz baixa de sol entre nuvens sobre a enseada, com uma pequena cabana de madeira na margem rochosa.',
      lede: 'A primeira sessão do fim de semana, às 07:00, com a luz ainda baixa sobre a enseada.',
      notes: [
        'Somente sábado e domingo, às 07:00.',
        'No começo da manhã o deque pode estar úmido e frio: traga chinelo e um agasalho para depois.',
        'Ambiente compartilhado: a sauna é um espaço de silêncio.'
      ]
    },
    'privativa': {
      id: 'privativa', name: 'Sauna privativa', short: 'Privativa', duration: '2 h',
      price: 120, unit: 'por grupo', perPerson: false, min: 1, max: 6,
      capacity: '1 a 6 pessoas', when: 'Dom 15:00 · Qua 20:00',
      img: 'assets/jetties-1.jpg', imgPos: '45% 60%',
      alt: 'Deque de madeira na beira da água sob nuvens de fim de tarde, com outros píeres ao fundo.',
      lede: 'A sauna e o deque só para o seu grupo, por duas horas. Valor fixo para o grupo, de 1 a 6 pessoas.',
      notes: [
        'Valor fixo de €120 para o grupo inteiro, de 1 a 6 pessoas.',
        'Todas as pessoas do grupo precisam ter mais de 18 anos.',
        'As regras da casa valem igualmente para grupos privativos.'
      ]
    }
  };
  var ORDER = ['aberta', 'nascer-sol', 'privativa'];

  var WEEK = [
    { key: 'seg', name: 'Segunda', abbr: 'Seg', closed: true, slots: [] },
    { key: 'ter', name: 'Terça', abbr: 'Ter', slots: [['17:00', 'aberta'], ['19:00', 'aberta']] },
    { key: 'qua', name: 'Quarta', abbr: 'Qua', slots: [['17:00', 'aberta'], ['19:00', 'aberta'], ['20:00', 'privativa']] },
    { key: 'qui', name: 'Quinta', abbr: 'Qui', slots: [['17:00', 'aberta'], ['19:00', 'aberta']] },
    { key: 'sex', name: 'Sexta', abbr: 'Sex', slots: [['17:00', 'aberta'], ['19:00', 'aberta']] },
    { key: 'sab', name: 'Sábado', abbr: 'Sáb', slots: [['07:00', 'nascer-sol'], ['10:00', 'aberta'], ['14:00', 'aberta'], ['17:00', 'aberta']] },
    { key: 'dom', name: 'Domingo', abbr: 'Dom', slots: [['07:00', 'nascer-sol'], ['10:00', 'aberta'], ['15:00', 'privativa']] }
  ];

  var RULES = [
    ['Maiores de 18 anos', 'A entrada é permitida somente para maiores de 18 anos, em qualquer sessão.'],
    ['Banho de mar por sua conta e risco', 'Não há salva-vidas no local. Entrar no mar é opcional e é responsabilidade de cada pessoa.'],
    ['Sem álcool', 'Não é permitido consumir bebidas alcoólicas no píer, no deque ou na sauna.'],
    ['Silêncio na sauna', 'Dentro da sauna, silêncio. Conversas ficam para o deque.']
  ];

  var NOTICE = 'Protótipo demonstrativo. Marca, local, horários e preços fictícios. Nada é reservado.';
  var ILLUSTRATIVE = 'Programação ilustrativa; disponibilidade não verificada neste protótipo.';
  var PHOTO_NOTE = 'Fotografias ilustrativas de outro local (domínio público, CC0); não retratam as instalações da marca fictícia.';

  var main = document.getElementById('conteudo');
  var state = { filter: 'todas', plan: { session: 'aberta', people: '2' } };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function euro(n) { return '€' + n.toLocaleString('pt-BR'); }

  /* ---------- views ---------- */

  function photo(src, alt, pos, cls) {
    return '<figure class="ph ' + (cls || '') + '"><img src="' + src + '" alt="' + esc(alt) + '" style="object-position:' + (pos || '50% 50%') + '" decoding="async"></figure>';
  }

  function stepsHTML() {
    var steps = [
      ['Aqueça na sauna', '10 a 15 min', 'Sente-se no banco de madeira e deixe o calor da lenha fazer o resto. Saia quando quiser.'],
      ['Desça a escada para o mar, se quiser', 'opcional', 'A escada desce direto do píer para a água. Sem salva-vidas no local: o banho é por sua conta e risco.'],
      ['Descanse no deque', 'sem pressa', 'Sente-se ao ar livre, respire o vento da enseada e espere o corpo assentar.'],
      ['Repita no seu ritmo', 'até o fim da sessão', 'Quantas rodadas couberem na sessão, do jeito que fizer sentido para você.']
    ];
    return '<ol class="steps">' + steps.map(function (s, i) {
      return '<li class="step" style="--i:' + i + '"><span class="step-n" aria-hidden="true">' + (i + 1) + '</span>' +
        '<div><h3>' + s[0] + '</h3><p class="step-meta">' + s[1] + '</p><p>' + s[2] + '</p></div></li>';
    }).join('') + '</ol>';
  }

  function bringHTML() {
    var items = [
      ['Toalha', '<path d="M5 4h14v16H5zM5 9h14M9 4v16"/>'],
      ['Roupa de banho', '<path d="M7 4v5c0 3 2 5 5 5s5-2 5-5V4M7 14l-1 6h12l-1-6"/>'],
      ['Chinelo', '<path d="M8 3c3 0 4 3 4 7s-1 11-4 11-4-6-4-11 1-7 4-7zM5 9c2 1 4 1 6 0M16 6c2 0 3 2 3 5s-1 9-3 9-3-5-3-9"/>'],
      ['Garrafa de água', '<path d="M10 2h4v3l2 3v13H8V8l2-3zM8 12h8"/>']
    ];
    return '<ul class="bring">' + items.map(function (it) {
      return '<li><svg viewBox="0 0 24 24" aria-hidden="true">' + it[1] + '</svg><span>' + it[0] + '</span></li>';
    }).join('') + '</ul>';
  }

  function rulesHTML(compact) {
    return '<ul class="rules' + (compact ? ' rules-compact' : '') + '">' + RULES.map(function (r) {
      return '<li><strong>' + r[0] + '</strong>' + (compact ? '' : '<span>' + r[1] + '</span>') + '</li>';
    }).join('') + '</ul>';
  }

  function sessionCards() {
    return '<div class="cards">' + ORDER.map(function (id) {
      var s = SESSIONS[id];
      return '<a class="card" href="#/sessao/' + id + '" data-testid="session-' + id + '">' +
        photo(s.img, s.alt, s.imgPos, 'card-ph') +
        '<span class="card-body"><span class="card-name">' + s.name + '</span>' +
        '<span class="card-facts"><span>' + s.duration + '</span><span>' + euro(s.price) + ' ' + s.unit + '</span><span>' + s.capacity + '</span></span>' +
        '<span class="card-when">' + s.when + '</span>' +
        '<span class="card-go">Ver detalhes <span aria-hidden="true">→</span></span></span></a>';
    }).join('') + '</div>';
  }

  function viewHome() {
    return '' +
      '<section class="hero" aria-labelledby="hero-title">' +
        '<div class="hero-ph"><img src="assets/bathing-ladder.jpg" alt="Píer de madeira com uma escada de banho que desce direto para a água da enseada, sob céu nublado." style="object-position:72% 55%"></div>' +
        '<div class="hero-copy">' +
          '<p class="eyebrow">Calor de lenha. Mar logo ali.</p>' +
          '<h1 id="hero-title" class="hero-title"><span>Aqueça.</span><span>Mergulhe.</span><span>Descanse.</span></h1>' +
          '<p class="hero-text">Uma sauna a lenha sobre o píer, com escada direto para o mar.</p>' +
          '<div class="hero-actions"><a class="btn btn-primary" href="#/horarios">Ver horários</a><a class="btn btn-quiet" href="#como-funciona" data-scroll="como-funciona">Como funciona</a></div>' +
        '</div>' +
        '<p class="hero-place">Sauna a lenha · Enseada do Norte · ter a dom</p>' +
      '</section>' +

      '<section class="sec how" id="como-funciona" aria-labelledby="how-title">' +
        '<div class="sec-head"><p class="kicker">O ritual</p><h2 id="how-title">Como funciona</h2>' +
        '<p class="sec-lede">Quatro passos, nesta ordem, quantas vezes quiser dentro da sessão.</p></div>' +
        stepsHTML() +
      '</section>' +

      '<section class="band" aria-label="O lugar">' +
        photo('assets/jetty-and-water-2.jpg', 'Tábuas gastas de um píer de madeira na beira da água, com a superfície do mar ondulada logo à frente.', '50% 70%', 'band-ph') +
        '<p class="band-text">A sauna fica no fim do píer. Do banco quente até a água são poucos passos de madeira.</p>' +
      '</section>' +

      '<section class="sec bring-sec" aria-labelledby="bring-title">' +
        '<div class="split">' +
          '<div><p class="kicker">Antes de sair de casa</p><h2 id="bring-title">O que levar</h2>' + bringHTML() + '</div>' +
          '<div class="rules-box"><p class="kicker">Regras da casa</p><h2 class="h-small">Quatro regras, sem exceção</h2>' + rulesHTML(true) +
          '<a class="link-arrow" href="#/regras">Regras e perguntas frequentes <span aria-hidden="true">→</span></a></div>' +
        '</div>' +
      '</section>' +

      '<section class="sec sess" aria-labelledby="sess-title">' +
        '<div class="sec-head"><p class="kicker">Três formatos</p><h2 id="sess-title">Sessões</h2>' +
        '<p class="sec-lede">Escolha um formato para ver duração, preço, capacidade e horários.</p></div>' +
        sessionCards() +
        '<div class="cta-row"><a class="btn btn-primary" href="#/horarios">Ver horários da semana</a><a class="btn btn-ghost" href="#/planejar">Estimar o valor da visita</a></div>' +
      '</section>';
  }

  function scheduleHTML(filter) {
    return WEEK.map(function (d) {
      var slots = d.slots.filter(function (s) { return filter === 'todas' || s[1] === 'nascer-sol'; });
      if (filter !== 'todas' && !slots.length && !d.closed) {
        return '<li class="day day-empty"><span class="day-name"><abbr title="' + d.name + '">' + d.abbr + '</abbr></span><span class="day-none">Sem sessão Nascer do sol</span></li>';
      }
      if (d.closed) {
        return '<li class="day day-closed"><span class="day-name"><abbr title="' + d.name + '">' + d.abbr + '</abbr></span><span class="day-none">Fechado</span></li>';
      }
      return '<li class="day"><span class="day-name"><abbr title="' + d.name + '">' + d.abbr + '</abbr></span><ul class="slots" aria-label="' + d.name + '">' +
        slots.map(function (s) {
          var ses = SESSIONS[s[1]];
          return '<li><a class="slot slot-' + s[1] + '" href="#/sessao/' + s[1] + '" data-testid="schedule-slot" data-session="' + s[1] + '">' +
            '<span class="slot-time">' + s[0] + '</span><span class="slot-name">' + ses.short + '</span>' +
            '<span class="sr-only">, ' + d.name + ', ' + ses.duration + ', ' + euro(ses.price) + ' ' + ses.unit + '</span></a></li>';
        }).join('') + '</ul></li>';
    }).join('');
  }

  function viewSchedule() {
    return '<section class="page sched-page" aria-labelledby="sched-title">' +
      '<div class="page-head"><p class="kicker">Programação semanal</p><h1 id="sched-title">Horários</h1>' +
      '<p class="sec-lede">Terça a domingo. Segunda-feira: fechado. Toque num horário para ver os detalhes da sessão.</p></div>' +
      '<div class="filter" role="group" aria-label="Filtrar sessões">' +
        '<button type="button" class="chip" data-filter="todas" data-testid="schedule-filter-all" aria-pressed="' + (state.filter === 'todas') + '">Todas</button>' +
        '<button type="button" class="chip" data-filter="nascer" data-testid="schedule-filter-sunrise" aria-pressed="' + (state.filter === 'nascer') + '">Nascer do sol</button>' +
      '</div>' +
      '<p class="sr-only" aria-live="polite" id="filter-status"></p>' +
      '<ul class="week" id="week">' + scheduleHTML(state.filter) + '</ul>' +
      '<div class="legend" aria-hidden="true"><span><i class="lg lg-aberta"></i>Sessão aberta</span><span><i class="lg lg-nascer-sol"></i>Nascer do sol</span><span><i class="lg lg-privativa"></i>Sauna privativa</span></div>' +
      '<p class="illustrative">' + ILLUSTRATIVE + '</p>' +
      '<div class="sec-head sec-head-tight"><h2>Tipos de sessão</h2></div>' +
      sessionCards() +
      '</section>';
  }

  function viewSession(id) {
    var s = SESSIONS[id];
    if (!s) return viewNotFound();
    var times = [];
    WEEK.forEach(function (d) { d.slots.forEach(function (x) { if (x[1] === id) times.push([d.name, x[0]]); }); });
    return '<article class="page detail" aria-labelledby="det-title">' +
      '<a class="back" href="#/horarios"><span aria-hidden="true">←</span> Voltar aos horários</a>' +
      '<div class="detail-grid">' +
        '<div class="detail-ph">' + photo(s.img, s.alt, s.imgPos, '') + '</div>' +
        '<div class="detail-body">' +
          '<p class="kicker">Tipo de sessão</p><h1 id="det-title">' + s.name + '</h1>' +
          '<p class="sec-lede">' + s.lede + '</p>' +
          '<dl class="facts">' +
            '<div><dt>Duração</dt><dd>' + s.duration + '</dd></div>' +
            '<div><dt>Preço</dt><dd>' + euro(s.price) + ' <small>' + s.unit + '</small></dd></div>' +
            '<div><dt>Capacidade</dt><dd>' + s.capacity + '</dd></div>' +
          '</dl>' +
          '<h2 class="h-small">Horários</h2>' +
          '<ul class="times">' + times.map(function (t) { return '<li><span>' + t[0] + '</span><span class="mono">' + t[1] + '</span></li>'; }).join('') + '</ul>' +
          '<p class="illustrative">' + ILLUSTRATIVE + '</p>' +
          '<h2 class="h-small">Bom saber</h2><ul class="notes">' + s.notes.map(function (n) { return '<li>' + n + '</li>'; }).join('') + '</ul>' +
          '<h2 class="h-small">Regras da casa</h2>' + rulesHTML(false) +
          '<div class="cta-row"><a class="btn btn-primary" href="#/planejar?sessao=' + id + '">Estimar valor desta sessão</a><a class="btn btn-ghost" href="#/horarios">Ver todos os horários</a></div>' +
          '<nav class="other" aria-label="Outras sessões">' + ORDER.filter(function (o) { return o !== id; }).map(function (o) {
            return '<a href="#/sessao/' + o + '" data-testid="session-' + o + '">' + SESSIONS[o].name + ' <span aria-hidden="true">→</span></a>';
          }).join('') + '</nav>' +
        '</div>' +
      '</div></article>';
  }

  function viewPlan(params) {
    if (params && SESSIONS[params.sessao]) state.plan.session = params.sessao;
    return '<section class="page plan-page" aria-labelledby="plan-title">' +
      '<div class="page-head"><p class="kicker">Cálculo local</p><h1 id="plan-title">Planejar visita</h1>' +
      '<p class="sec-lede">Escolha a sessão e o número de pessoas para ver o valor estimado. Nada é enviado nem reservado.</p></div>' +
      '<div class="plan-grid">' +
        '<form class="plan" id="plan-form" novalidate>' +
          '<fieldset><legend>Tipo de sessão</legend><div class="radios">' +
            ORDER.map(function (id) {
              var s = SESSIONS[id];
              return '<label class="radio"><input type="radio" name="plan-session" value="' + id + '" data-testid="plan-session"' + (state.plan.session === id ? ' checked' : '') + '>' +
                '<span class="radio-box"><span class="radio-name">' + s.name + '</span><span class="radio-meta">' + euro(s.price) + ' ' + s.unit + ' · ' + s.capacity + '</span></span></label>';
            }).join('') +
          '</div></fieldset>' +
          '<div class="field"><label for="plan-people">Número de pessoas</label>' +
            '<div class="stepper"><button type="button" class="step-btn" data-step="-1" aria-label="Diminuir uma pessoa">−</button>' +
            '<input id="plan-people" name="plan-people" type="number" inputmode="numeric" min="1" max="8" step="1" value="' + esc(state.plan.people) + '" data-testid="plan-people" aria-describedby="people-hint">' +
            '<button type="button" class="step-btn" data-step="1" aria-label="Aumentar uma pessoa">+</button></div>' +
            '<p class="hint" id="people-hint"></p>' +
          '</div>' +
          '<div id="plan-error-slot" aria-live="assertive"></div>' +
        '</form>' +
        '<aside class="receipt" aria-labelledby="receipt-title">' +
          '<p class="kicker" id="receipt-title">Valor estimado</p>' +
          '<p class="total" aria-live="polite"><output data-testid="plan-total" id="plan-total" for="plan-people">—</output></p>' +
          '<p class="calc" id="plan-calc"></p>' +
          '<p class="receipt-note">' + NOTICE + '</p>' +
          '<p class="receipt-small">Sem envio, pagamento, conta ou dados pessoais. Para ver quando há sessão, consulte os <a href="#/horarios">horários</a>.</p>' +
        '</aside>' +
      '</div></section>';
  }

  function viewRules() {
    var faq = [
      ['Preciso ter experiência com sauna?', 'Não. O ritual é simples: aqueça, desça ao mar se quiser, descanse e repita. Você decide quanto tempo fica em cada etapa; a sugestão é de 10 a 15 minutos na sauna por rodada.'],
      ['Sou obrigado a entrar no mar?', 'Não. O banho de mar é opcional. Não há salva-vidas no local, então entrar na água é por conta e risco de cada pessoa.'],
      ['O que preciso levar?', 'Toalha, roupa de banho, chinelo e garrafa de água.'],
      ['Qual a diferença entre as sessões?', 'A Sessão aberta e a Nascer do sol são compartilhadas, com até 8 pessoas e preço por pessoa. A Sauna privativa é só do seu grupo, de 1 a 6 pessoas, com valor fixo de €120 por 2 horas.'],
      ['Posso reservar por este site?', 'Não. Este é um protótipo demonstrativo: marca, local, horários e preços são fictícios e nada é reservado. O planejador apenas calcula um valor estimado no seu aparelho.'],
      ['Há sessão às segundas-feiras?', 'Não. Segunda-feira: fechado.'],
      ['Menores de idade podem participar?', 'Não. A entrada é somente para maiores de 18 anos, também na sauna privativa.']
    ];
    return '<section class="page rules-page" aria-labelledby="rules-title">' +
      '<div class="page-head"><p class="kicker">Antes de vir</p><h1 id="rules-title">Regras e perguntas frequentes</h1>' +
      '<p class="sec-lede">Regras curtas, para que todo mundo aproveite o mesmo calor e o mesmo silêncio.</p></div>' +
      '<div class="split split-rules"><div><h2 class="h-small">Regras obrigatórias</h2>' + rulesHTML(false) +
      '<h2 class="h-small">O que levar</h2>' + bringHTML() + '</div>' +
      '<div><h2 class="h-small">Perguntas frequentes</h2><div class="faq">' + faq.map(function (q) {
        return '<details><summary>' + q[0] + '</summary><p>' + q[1] + '</p></details>';
      }).join('') + '</div></div></div>' +
      '<div class="cta-row"><a class="btn btn-primary" href="#/horarios">Ver horários</a><a class="btn btn-ghost" href="#/planejar">Planejar visita</a></div>' +
      '</section>';
  }

  var CREDITS = window.TABUA_CREDITS || null;
  function viewCredits() {
    var body = '<p>A lista de créditos está em <a href="assets/credits.json">assets/credits.json</a>.</p>';
    if (CREDITS) {
      body = '<ul class="credits">' + CREDITS.map(function (c) {
        return '<li><span class="mono">' + esc(c.file) + '</span><span>' + esc(c.title) + ' — ' + esc(c.author) + ' · ' + esc(c.license) + '</span>' +
          '<span class="src">Fonte: ' + esc(c.source) + '</span></li>';
      }).join('') + '</ul>';
    }
    return '<section class="page credits-page" aria-labelledby="cred-title">' +
      '<div class="page-head"><p class="kicker">Fotografias</p><h1 id="cred-title">Créditos</h1>' +
      '<p class="sec-lede">' + PHOTO_NOTE + '</p></div>' + body +
      '<p class="receipt-small">Arquivo completo: <a href="assets/credits.json">assets/credits.json</a>. Fontes tipográficas Fraunces, Instrument Sans e IBM Plex Mono sob SIL Open Font License, em <span class="mono">fonts/licenses/</span>.</p>' +
      '</section>';
  }

  function viewNotFound() {
    return '<section class="page" aria-labelledby="nf-title"><div class="page-head"><h1 id="nf-title">Página não encontrada</h1>' +
      '<p class="sec-lede">Este endereço não existe neste protótipo.</p></div>' +
      '<div class="cta-row"><a class="btn btn-primary" href="#/">Voltar ao início</a><a class="btn btn-ghost" href="#/horarios">Ver horários</a></div></section>';
  }

  /* ---------- behaviour ---------- */

  function bindSchedule() {
    var btns = main.querySelectorAll('[data-filter]');
    Array.prototype.forEach.call(btns, function (b) {
      b.addEventListener('click', function () {
        state.filter = b.getAttribute('data-filter') === 'nascer' ? 'nascer' : 'todas';
        Array.prototype.forEach.call(btns, function (o) { o.setAttribute('aria-pressed', String(o === b)); });
        var week = document.getElementById('week');
        week.innerHTML = scheduleHTML(state.filter);
        week.classList.remove('swap'); void week.offsetWidth; week.classList.add('swap');
        var n = week.querySelectorAll('[data-testid="schedule-slot"]').length;
        document.getElementById('filter-status').textContent = (state.filter === 'todas' ? 'Mostrando todas as sessões: ' : 'Mostrando somente Nascer do sol: ') + n + ' horários.';
      });
    });
  }

  function bindPlan() {
    var form = document.getElementById('plan-form');
    var input = document.getElementById('plan-people');
    var total = document.getElementById('plan-total');
    var calc = document.getElementById('plan-calc');
    var hint = document.getElementById('people-hint');
    var slot = document.getElementById('plan-error-slot');

    function current() {
      var r = form.querySelector('input[name="plan-session"]:checked');
      return SESSIONS[r ? r.value : 'aberta'];
    }
    function update() {
      var s = current();
      state.plan.session = s.id; state.plan.people = input.value;
      input.max = String(s.max);
      hint.textContent = s.perPerson ? 'De 1 a ' + s.max + ' pessoas. ' + euro(s.price) + ' por pessoa.' : 'De 1 a ' + s.max + ' pessoas. Valor fixo de ' + euro(s.price) + ' para o grupo.';
      var raw = String(input.value).trim();
      var err = null;
      var n = Number(raw);
      if (raw === '') err = 'Informe o número de pessoas, de 1 a ' + s.max + '.';
      else if (!/^\d+$/.test(raw) || !isFinite(n)) err = 'Use um número inteiro de pessoas, de 1 a ' + s.max + '.';
      else if (n < 1) err = 'O mínimo é 1 pessoa.';
      else if (n > s.max) err = s.perPerson
        ? s.name + ' comporta até ' + s.max + ' pessoas. Ajuste para um número entre 1 e ' + s.max + '.'
        : 'A Sauna privativa é para grupos de 1 a 6 pessoas. Ajuste para um número entre 1 e 6.';
      if (err) {
        slot.innerHTML = '<p class="plan-error" id="plan-error" data-testid="plan-error" role="alert"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 21h20zM12 10v5M12 17.5v.5"/></svg><span>' + esc(err) + '</span></p>';
        input.setAttribute('aria-invalid', 'true');
        input.setAttribute('aria-describedby', 'people-hint plan-error');
        total.textContent = '—';
        total.parentNode.classList.add('is-empty');
        calc.textContent = 'Sem valor estimado enquanto o número de pessoas for inválido.';
        return;
      }
      slot.innerHTML = '';
      input.removeAttribute('aria-invalid');
      input.setAttribute('aria-describedby', 'people-hint');
      var value = s.perPerson ? s.price * n : s.price;
      total.textContent = euro(value);
      total.parentNode.classList.remove('is-empty');
      total.parentNode.classList.remove('tick'); void total.offsetWidth; total.parentNode.classList.add('tick');
      calc.textContent = s.perPerson
        ? s.name + ': ' + euro(s.price) + ' × ' + n + (n === 1 ? ' pessoa' : ' pessoas') + ' · ' + s.duration
        : s.name + ': ' + euro(s.price) + ' fixos para ' + n + (n === 1 ? ' pessoa' : ' pessoas') + ' · ' + s.duration;
    }
    form.addEventListener('submit', function (e) { e.preventDefault(); update(); });
    form.addEventListener('change', update);
    input.addEventListener('input', update);
    Array.prototype.forEach.call(form.querySelectorAll('[data-step]'), function (b) {
      b.addEventListener('click', function () {
        var n = parseInt(input.value, 10);
        if (!isFinite(n)) n = 0;
        n = Math.max(1, Math.min(current().max, n + parseInt(b.getAttribute('data-step'), 10)));
        input.value = String(n); update();
      });
    });
    update();
  }

  function currentRoute() {
    var h = location.hash.replace(/^#/, '');
    if (h === '' || h === '/') return { name: 'home' };
    if (h.charAt(0) !== '/') return { name: 'home', anchor: h };
    var q = {}, path = h, qi = h.indexOf('?');
    if (qi > -1) {
      path = h.slice(0, qi);
      h.slice(qi + 1).split('&').forEach(function (p) { var kv = p.split('='); q[decodeURIComponent(kv[0])] = decodeURIComponent(kv[1] || ''); });
    }
    var parts = path.split('/').filter(Boolean);
    if (parts[0] === 'horarios') return { name: 'horarios' };
    if (parts[0] === 'planejar') return { name: 'planejar', params: q };
    if (parts[0] === 'regras') return { name: 'regras' };
    if (parts[0] === 'creditos') return { name: 'creditos' };
    if (parts[0] === 'sessao' && parts[1]) return { name: 'sessao', id: parts[1] };
    return { name: '404' };
  }

  var TITLES = { home: 'Tábua · Sauna a lenha no píer', horarios: 'Horários · Tábua', planejar: 'Planejar visita · Tábua', regras: 'Regras e perguntas · Tábua', creditos: 'Créditos · Tábua', '404': 'Página não encontrada · Tábua' };
  var lastRoute = null;

  function render() {
    var r = currentRoute();
    var html;
    switch (r.name) {
      case 'home': html = viewHome(); break;
      case 'horarios': html = viewSchedule(); break;
      case 'planejar': html = viewPlan(r.params); break;
      case 'regras': html = viewRules(); break;
      case 'creditos': html = viewCredits(); break;
      case 'sessao': html = viewSession(r.id); break;
      default: html = viewNotFound();
    }
    main.innerHTML = html;
    main.className = 'route-' + r.name;
    document.title = r.name === 'sessao' && SESSIONS[r.id] ? SESSIONS[r.id].name + ' · Tábua' : (TITLES[r.name] || TITLES.home);
    var navKey = r.name === 'sessao' ? 'horarios' : r.name;
    Array.prototype.forEach.call(document.querySelectorAll('[data-nav]'), function (a) {
      if (a.getAttribute('data-nav') === navKey) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    if (r.name === 'horarios') bindSchedule();
    if (r.name === 'planejar') bindPlan();
    Array.prototype.forEach.call(main.querySelectorAll('[data-scroll]'), function (a) {
      a.addEventListener('click', function (e) {
        var t = document.getElementById(a.getAttribute('data-scroll'));
        if (t) { e.preventDefault(); t.scrollIntoView({ behavior: reduced() ? 'auto' : 'smooth' }); t.setAttribute('tabindex', '-1'); t.focus({ preventScroll: true }); }
      });
    });
    main.classList.remove('enter'); void main.offsetWidth; main.classList.add('enter');
    if (r.anchor) {
      var t = document.getElementById(r.anchor);
      if (t) { t.scrollIntoView(); return; }
    }
    if (lastRoute !== null) {
      window.scrollTo(0, 0);
      main.focus({ preventScroll: true });
    }
    lastRoute = r.name;
  }

  function reduced() { return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches; }

  window.addEventListener('hashchange', render);
  render();
})();
