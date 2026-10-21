(function () {
  "use strict";

  /* ---------- Dados (fictícios, do briefing) ---------- */
  var SESSIONS = {
    "aberta": {
      id: "aberta", name: "Sessão aberta", short: "Aberta",
      duration: "90 min", price: 18, unit: "por pessoa", priceLabel: "€18",
      capacity: "até 8 pessoas", min: 1, max: 8, mode: "per",
      when: "Ter–Sex 17:00 e 19:00 · Sáb 10:00, 14:00, 17:00 · Dom 10:00",
      img: "assets/bench-1.jpg", imgPos: "50% 60%",
      alt: "Banco de madeira rústico sobre um píer, com a água e as rochas da enseada ao fundo sob céu nublado.",
      lead: "O formato de todo dia: você chega no horário, divide a sauna com até oito pessoas e segue o ritual no seu ritmo.",
      notes: [
        "Sauna compartilhada: o silêncio vale para todos lá dentro.",
        "A descida ao mar é opcional e por sua conta e risco; não há salva-vidas no local."
      ]
    },
    "nascer-sol": {
      id: "nascer-sol", name: "Nascer do sol", short: "Nascer do sol",
      duration: "90 min", price: 22, unit: "por pessoa", priceLabel: "€22",
      capacity: "até 8 pessoas", min: 1, max: 8, mode: "per",
      when: "Sáb e Dom 07:00",
      img: "assets/abyfjorden-estuary-2.jpg", imgPos: "30% 55%",
      alt: "Enseada ao amanhecer, com luz baixa e dourada entre as nuvens sobre morros de pedra e água calma.",
      lead: "A primeira sessão do fim de semana, às 07:00. Mesmo ritual da sessão aberta, com o dia começando sobre a água.",
      notes: [
        "Às 07:00 a água costuma estar mais fria; entre devagar, se for entrar.",
        "A descida ao mar é opcional e por sua conta e risco; não há salva-vidas no local."
      ]
    },
    "privativa": {
      id: "privativa", name: "Sauna privativa", short: "Privativa",
      duration: "2 h", price: 120, unit: "por grupo", priceLabel: "€120",
      capacity: "1 a 6 pessoas", min: 1, max: 6, mode: "flat",
      when: "Dom 15:00 · Qua 20:00",
      img: "assets/bathing-ladder.jpg", imgPos: "60% 50%",
      alt: "Escada de madeira que desce de um píer direto para a água da enseada.",
      lead: "A sauna e o deck só para o seu grupo, por duas horas. Valor fixo para 1 a 6 pessoas.",
      notes: [
        "O valor é o mesmo para 1 ou 6 pessoas; grupos maiores que 6 não são possíveis.",
        "Todas as pessoas do grupo precisam ter 18 anos ou mais.",
        "A descida ao mar é opcional e por sua conta e risco; não há salva-vidas no local."
      ]
    }
  };
  var ORDER = ["aberta", "nascer-sol", "privativa"];

  var WEEK = [
    { key: "seg", name: "Segunda", abbr: "Seg", slots: [] },
    { key: "ter", name: "Terça", abbr: "Ter", slots: [["17:00", "aberta"], ["19:00", "aberta"]] },
    { key: "qua", name: "Quarta", abbr: "Qua", slots: [["17:00", "aberta"], ["19:00", "aberta"], ["20:00", "privativa"]] },
    { key: "qui", name: "Quinta", abbr: "Qui", slots: [["17:00", "aberta"], ["19:00", "aberta"]] },
    { key: "sex", name: "Sexta", abbr: "Sex", slots: [["17:00", "aberta"], ["19:00", "aberta"]] },
    { key: "sab", name: "Sábado", abbr: "Sáb", slots: [["07:00", "nascer-sol"], ["10:00", "aberta"], ["14:00", "aberta"], ["17:00", "aberta"]] },
    { key: "dom", name: "Domingo", abbr: "Dom", slots: [["07:00", "nascer-sol"], ["10:00", "aberta"], ["15:00", "privativa"]] }
  ];

  var RULES = [
    ["18+", "Somente maiores de 18 anos", "A Tábua recebe apenas adultos, inclusive na sauna privativa."],
    ["Mar", "Banho de mar por conta e risco", "Descer a escada é opcional. Não há salva-vidas no local: cada pessoa decide e responde por si."],
    ["0%", "Sem álcool", "Nada de bebida alcoólica no píer, no deck ou na sauna, antes ou durante a sessão."],
    ["Shh", "Silêncio na sauna", "Dentro da sauna, silêncio. Conversa, se for o caso, fica para o deck."]
  ];

  var FAQ = [
    ["Nunca fui a uma sauna. Como funciona?",
      "<p>Você entra na sauna aquecida a lenha e fica de 10 a 15 minutos. Depois, se quiser, desce a escada do píer para o mar. Em seguida descansa no deck. E repete, no seu ritmo, até o fim da sessão.</p><p>Ninguém precisa entrar no mar, e não existe número certo de rodadas.</p>"],
    ["O que eu preciso levar?",
      "<p>Toalha, roupa de banho, chinelo e garrafa de água.</p>"],
    ["Preciso entrar no mar?",
      "<p>Não. A descida é opcional. Se decidir entrar, é por sua conta e risco: não há salva-vidas no local.</p>"],
    ["Quanto custa uma visita?",
      "<p>Sessão aberta: €18 por pessoa. Nascer do sol: €22 por pessoa. Sauna privativa: €120 por grupo de 1 a 6 pessoas. Use o <a class=\"textlink\" href=\"#/planejar\">planejador</a> para ver o valor estimado da sua visita.</p>"],
    ["Posso reservar por aqui?",
      "<p>Não. Este site é um protótipo demonstrativo: marca, local, horários e preços são fictícios e nada é reservado. O planejador só faz a conta no seu próprio aparelho, sem enviar nada.</p>"],
    ["Os horários estão disponíveis?",
      "<p>A programação é ilustrativa; a disponibilidade não é verificada neste protótipo.</p>"],
    ["Abre todos os dias?",
      "<p>De terça a domingo. Segunda-feira: fechado.</p>"],
    ["Posso levar menores de idade?",
      "<p>Não. A entrada é somente para maiores de 18 anos.</p>"]
  ];

  /* ---------- Utilidades ---------- */
  var ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M1 8h12M9 3.5 13.5 8 9 12.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>';
  var BACK = '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M15 8H3M7 3.5 2.5 8 7 12.5" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>';
  var INFO = '<svg viewBox="0 0 18 18" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="8" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M9 8v5M9 5.2v.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';
  var WARN = '<svg viewBox="0 0 18 18" aria-hidden="true" focusable="false"><path d="M9 1.5 17 16H1z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M9 7v4.2M9 13.4v.1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';
  var DISCLAIMER = "Protótipo demonstrativo. Marca, local, horários e preços fictícios. Nada é reservado.";
  var SCHED_NOTE = "Programação ilustrativa; disponibilidade não verificada neste protótipo.";

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function eur(n) { return "€" + n; }
  function slotsFor(id) {
    var out = [];
    WEEK.forEach(function (d) { d.slots.forEach(function (s) { if (s[1] === id) out.push([d.abbr, s[0]]); }); });
    return out;
  }

  var main = document.getElementById("conteudo");

  /* ---------- Views ---------- */
  function viewHome() {
    var cards = ORDER.map(function (id) {
      var s = SESSIONS[id];
      return '<a class="scard" href="#/sessao/' + id + '" data-testid="session-' + id + '">' +
        '<div class="scard__img"><img src="' + s.img + '" alt="' + esc(s.alt) + '" style="object-position:' + s.imgPos + '" loading="lazy"></div>' +
        '<div class="scard__body"><span class="tag tag--' + id + '">' + esc(s.short) + '</span>' +
        '<h3>' + esc(s.name) + '</h3>' +
        '<p class="scard__facts"><span>' + s.duration + '</span><span>' + esc(s.capacity) + '</span></p>' +
        '<p class="mono" style="font-size:13.5px;color:var(--muted)">' + esc(s.when) + '</p>' +
        '<p class="scard__price">' + s.priceLabel + '<small>' + s.unit + '</small></p>' +
        '<span class="scard__go">Ver sessão ' + ARROW + '</span></div></a>';
    }).join("");

    return '' +
      '<section class="hero on-dark" aria-labelledby="hero-t">' +
        '<div class="hero__warm">' +
          '<p class="eyebrow hero__place">Píer de Enseada do Norte · Sauna a lenha</p>' +
          '<div>' +
            '<h1 id="hero-t"><span class="w1">Aqueça.</span><span class="w2">Mergulhe.</span><span class="w3">Descanse.</span></h1>' +
            '<p class="hero__lead">Uma sauna a lenha sobre o píer, com escada direto para o mar.</p>' +
            '<div class="hero__acts"><a class="btn btn--ember" href="#/horarios">Ver horários ' + ARROW + '</a>' +
            '<a class="btn btn--ghost" href="#como-funciona" data-scroll="como-funciona">Como funciona</a></div>' +
          '</div>' +
          '<p class="hero__sig">Calor de lenha. Mar logo ali.</p>' +
        '</div>' +
        '<div class="hero__cold"><img src="assets/bathing-ladder.jpg" alt="Escada de madeira presa a um píer, descendo direto para a água escura da enseada, com rochas e céu nublado ao fundo." fetchpriority="high">' +
          '<div class="temp" aria-hidden="true"><span>Lenha</span><span>Mar</span></div></div>' +
      '</section>' +

      '<section class="sec" id="como-funciona" aria-labelledby="cf-t" tabindex="-1">' +
        '<div class="wrap">' +
          '<div class="sec__head"><div><p class="eyebrow">O ritual</p><h2 id="cf-t">Como funciona</h2></div>' +
          '<p>Quatro passos, sempre nesta ordem. Não há número certo de rodadas, e entrar no mar é escolha sua.</p></div>' +
          '<ol class="ritual">' +
            '<li><div class="ritual__bar"></div><span class="ritual__n">01</span><h3>Aqueça na sauna</h3><p>Sente-se no banco de madeira e fique no calor da lenha.</p><span class="ritual__meta">10 a 15 min</span></li>' +
            '<li><div class="ritual__bar"></div><span class="ritual__n">02</span><h3>Desça a escada para o mar</h3><p>Se quiser. A escada sai do píer direto para a água. Sem salva-vidas no local.</p><span class="ritual__meta">opcional</span></li>' +
            '<li><div class="ritual__bar"></div><span class="ritual__n">03</span><h3>Descanse no deck</h3><p>Ao ar livre, sobre as tábuas, com a enseada na frente.</p><span class="ritual__meta">sem pressa</span></li>' +
            '<li><div class="ritual__bar"></div><span class="ritual__n">04</span><h3>Repita no seu ritmo</h3><p>Volte para o calor quando sentir vontade, até o fim da sessão.</p><span class="ritual__meta">quantas vezes quiser</span></li>' +
          '</ol>' +
        '</div>' +
      '</section>' +

      '<section class="place on-dark" aria-labelledby="pl-t">' +
        '<div class="place__img"><img src="assets/jetty-and-water-2.jpg" alt="Tábuas de um píer de madeira na beira da água, com pequenas ondulações na superfície." loading="lazy"></div>' +
        '<div class="place__txt">' +
          '<p class="eyebrow" style="color:rgba(243,237,228,.6)">O lugar</p>' +
          '<h2 id="pl-t">Madeira, fogo e água a poucos passos.</h2>' +
          '<p>A sauna fica sobre o píer de Enseada do Norte. Da porta ao deck são algumas tábuas; do deck ao mar, uma escada.</p>' +
          '<div class="place__strip">' +
            '<img src="assets/bench-2.jpg" alt="Banco de madeira sobre um deck à beira da água, com pedras em primeiro plano." loading="lazy">' +
            '<img src="assets/pier-and-jetty-4.jpg" alt="Píer de pedra e trapiches flutuantes numa enseada calma sob céu nublado." loading="lazy">' +
          '</div>' +
          '<p style="font-size:13.5px;color:rgba(243,237,228,.62)">Fotografias ilustrativas de outro local (domínio público, CC0); não retratam as instalações da marca fictícia. <a href="#/creditos">Créditos</a></p>' +
        '</div>' +
      '</section>' +

      '<section class="sec" aria-labelledby="lv-t">' +
        '<div class="wrap two">' +
          '<div class="listcard"><p class="eyebrow">Antes de sair de casa</p><h2 id="lv-t">O que levar</h2>' +
            '<ul class="ticks">' +
              '<li><span class="k">01</span><strong>Toalha</strong></li>' +
              '<li><span class="k">02</span><strong>Roupa de banho</strong></li>' +
              '<li><span class="k">03</span><strong>Chinelo</strong></li>' +
              '<li><span class="k">04</span><strong>Garrafa de água</strong></li>' +
            '</ul></div>' +
          '<div class="listcard"><p class="eyebrow">Para todo mundo</p><h2>Regras da casa</h2>' +
            '<ul class="ticks">' +
              RULES.map(function (r, i) { return '<li><span class="k">0' + (i + 1) + '</span><span><strong>' + r[1] + '</strong><small>' + r[2] + '</small></span></li>'; }).join("") +
            '</ul>' +
            '<p class="listcard__foot"><a class="textlink" href="#/regras">Regras e perguntas frequentes</a></p></div>' +
        '</div>' +
      '</section>' +

      '<div class="rule" aria-hidden="true"></div>' +

      '<section class="sec" aria-labelledby="ss-t">' +
        '<div class="wrap">' +
          '<div class="sec__head"><div><p class="eyebrow">Três formatos</p><h2 id="ss-t">Sessões</h2></div>' +
          '<p>Terça a domingo. Segunda-feira: fechado. Abra cada sessão para ver horários, capacidade e regras.</p></div>' +
          '<div class="sessions">' + cards + '</div>' +
        '</div>' +
      '</section>' +

      '<section class="band on-dark" aria-labelledby="bd-t"><div class="wrap band__in">' +
        '<h2 id="bd-t">Escolha um horário e veja quanto custa a visita.</h2>' +
        '<div class="band__acts"><a class="btn btn--ember" href="#/horarios">Ver horários ' + ARROW + '</a>' +
        '<a class="btn btn--ghost" href="#/planejar">Planejar visita</a></div>' +
      '</div></section>';
  }

  function viewSchedule(filter) {
    var legend = ORDER.map(function (id) {
      return '<a class="tag tag--' + id + '" href="#/sessao/' + id + '" data-testid="session-' + id + '">' + esc(SESSIONS[id].short) + '</a>';
    }).join("");
    return '' +
      '<header class="phead"><div class="wrap phead__in">' +
        '<p class="eyebrow">Programação semanal</p><h1>Horários</h1>' +
        '<p class="lead">Terça a domingo. Toque em um horário para abrir a sessão.</p>' +
      '</div></header>' +
      '<section class="sec--tight"><div class="wrap">' +
        '<div class="sched-bar">' +
          '<div class="seg" role="group" aria-label="Filtrar programação">' +
            '<button type="button" data-testid="schedule-filter-all" data-filter="todas" aria-pressed="' + (filter !== "nascer-sol") + '">Todas</button>' +
            '<button type="button" data-testid="schedule-filter-sunrise" data-filter="nascer-sol" aria-pressed="' + (filter === "nascer-sol") + '">Nascer do sol</button>' +
          '</div>' +
          '<div class="legend" aria-label="Tipos de sessão">' + legend + '</div>' +
        '</div>' +
        '<p class="sched-count" id="sched-count" role="status" aria-live="polite"></p>' +
        '<div class="board" id="board" data-filter="' + (filter || "todas") + '"></div>' +
        '<p class="sched-note">' + INFO + '<span>' + SCHED_NOTE + '</span></p>' +
      '</div></section>';
  }

  function renderBoard(filter) {
    var board = document.getElementById("board");
    if (!board) return;
    board.setAttribute("data-filter", filter);
    var count = 0;
    var html = WEEK.map(function (d) {
      var slots = d.slots.filter(function (s) { return filter === "nascer-sol" ? s[1] === "nascer-sol" : true; });
      if (filter === "nascer-sol" && !slots.length) return "";
      if (!d.slots.length) {
        return '<div class="day day--closed"><p class="day__name">' + d.name + '<small>' + d.abbr + '</small></p><p class="day__slots">Fechado</p></div>';
      }
      count += slots.length;
      return '<div class="day"><p class="day__name">' + d.name + '<small>' + d.abbr + '</small></p><ul class="day__slots" role="list" style="list-style:none;margin:0;padding:0">' +
        slots.map(function (s) {
          var ss = SESSIONS[s[1]];
          return '<li style="display:contents"><a class="slot" href="#/sessao/' + s[1] + '" data-testid="schedule-slot" data-session="' + s[1] + '" aria-label="' + d.name + ', ' + s[0] + ': ' + esc(ss.name) + ', ' + ss.duration + '">' +
            '<span class="slot__t">' + s[0] + '</span><span class="slot__n">' + esc(ss.name) + '</span><span class="slot__d">' + ss.duration + ' · ' + ss.priceLabel + '</span></a></li>';
        }).join("") + '</ul></div>';
    }).join("");
    board.innerHTML = html;
    var c = document.getElementById("sched-count");
    if (c) c.textContent = filter === "nascer-sol" ? count + " horários de nascer do sol: sábado e domingo, 07:00" : count + " horários na semana";
  }

  function viewSession(id) {
    var s = SESSIONS[id];
    if (!s) return null;
    var times = slotsFor(id).map(function (t) { return '<li><b>' + t[0] + '</b>' + t[1] + '</li>'; }).join("");
    var others = ORDER.filter(function (o) { return o !== id; }).map(function (o) {
      return '<a class="textlink" href="#/sessao/' + o + '" data-testid="session-' + o + '">' + esc(SESSIONS[o].name) + '</a>';
    }).join("");
    return '' +
      '<header class="phead"><div class="wrap phead__in">' +
        '<a class="crumb" href="#/horarios">' + BACK + ' Horários</a>' +
        '<p style="margin-top:22px"><span class="tag tag--' + id + '">' + esc(s.short) + '</span></p>' +
        '<h1>' + esc(s.name) + '</h1>' +
        '<p class="lead">' + esc(s.lead) + '</p>' +
      '</div></header>' +
      '<section class="sec--tight"><div class="wrap detail">' +
        '<div>' +
          '<dl class="facts">' +
            '<div><dt>Duração</dt><dd>' + s.duration + '</dd></div>' +
            '<div><dt>Preço</dt><dd>' + s.priceLabel + '<small>' + s.unit + '</small></dd></div>' +
            '<div><dt>Capacidade</dt><dd>' + esc(s.capacity.replace("até ", "até ")) + '</dd></div>' +
          '</dl>' +
          '<h2>Horários</h2>' +
          '<ul class="times" aria-label="Horários semanais">' + times + '</ul>' +
          '<p class="sched-note">' + INFO + '<span>' + SCHED_NOTE + ' Segunda-feira: fechado.</span></p>' +
          '<h2>Regras desta sessão</h2>' +
          '<ul class="ticks">' +
            '<li><span class="k">18+</span><span><strong>Somente maiores de 18 anos</strong></span></li>' +
            '<li><span class="k">0%</span><span><strong>Sem álcool</strong></span></li>' +
            '<li><span class="k">Shh</span><span><strong>Silêncio na sauna</strong></span></li>' +
            s.notes.map(function (n) { return '<li><span class="k">Nota</span><span>' + esc(n) + '</span></li>'; }).join("") +
          '</ul>' +
          '<h2>O que levar</h2>' +
          '<p>Toalha, roupa de banho, chinelo e garrafa de água.</p>' +
          '<div class="other"><span class="eyebrow" style="align-self:center">Outras sessões</span>' + others + '</div>' +
        '</div>' +
        '<aside class="detail__aside" aria-label="Planejar esta sessão">' +
          '<img src="' + s.img + '" alt="' + esc(s.alt) + '" style="object-position:' + s.imgPos + '">' +
          '<div class="calc-cta on-dark"><p class="eyebrow" style="color:rgba(243,237,228,.6)">Valor estimado</p>' +
          '<p>' + (s.mode === "flat" ? "€120 fixos para o grupo, de 1 a 6 pessoas." : s.priceLabel + " × número de pessoas, de 1 a 8.") + '</p>' +
          '<a class="btn btn--ember" href="#/planejar?sessao=' + id + '">Calcular esta visita ' + ARROW + '</a></div>' +
        '</aside>' +
      '</div></section>';
  }

  function viewPlan(pre) {
    var sel = SESSIONS[pre] ? pre : "aberta";
    var opts = ORDER.map(function (id) {
      var s = SESSIONS[id];
      return '<option value="' + id + '"' + (id === sel ? " selected" : "") + '>' + esc(s.name) + ' · ' + s.priceLabel + ' ' + s.unit + '</option>';
    }).join("");
    return '' +
      '<header class="phead"><div class="wrap phead__in">' +
        '<p class="eyebrow">Planejador de visita</p><h1>Quanto custa?</h1>' +
        '<p class="lead">Escolha a sessão e o número de pessoas. A conta é feita aqui no seu aparelho: nada é enviado, pago ou reservado.</p>' +
      '</div></header>' +
      '<section class="sec--tight"><div class="wrap planner">' +
        '<form class="pform" id="plan-form" novalidate onsubmit="return false">' +
          '<div class="field"><label for="plan-session">Sessão</label>' +
            '<div class="selectwrap"><select id="plan-session" name="sessao" data-testid="plan-session">' + opts + '</select></div>' +
            '<p class="hint" id="plan-session-hint"></p></div>' +
          '<div class="field"><label for="plan-people">Número de pessoas</label>' +
            '<div class="stepper"><button type="button" id="dec" aria-label="Diminuir uma pessoa">−</button>' +
            '<input id="plan-people" name="pessoas" type="number" inputmode="numeric" min="1" max="8" step="1" value="2" data-testid="plan-people" aria-describedby="plan-people-hint">' +
            '<button type="button" id="inc" aria-label="Aumentar uma pessoa">+</button></div>' +
            '<p class="hint" id="plan-people-hint"></p>' +
            '<div id="plan-error-slot"></div></div>' +
          '<p class="hint">Sem cadastro, sem dados pessoais, sem pagamento.</p>' +
        '</form>' +
        '<div class="result on-dark" aria-labelledby="res-t">' +
          '<p class="eyebrow" id="res-t">Valor estimado</p>' +
          '<p class="total" data-testid="plan-total" id="plan-total" aria-live="polite" aria-atomic="true">€36</p>' +
          '<p class="formula" id="plan-formula"></p>' +
          '<hr>' +
          '<ul id="plan-summary"></ul>' +
          '<p class="notice" role="note">' + DISCLAIMER + '</p>' +
          '<a class="btn btn--ghost" href="#/horarios">Ver horários ' + ARROW + '</a>' +
        '</div>' +
      '</div></section>' +
      '<div class="mtotal" id="mtotal" aria-hidden="true"><div><p class="mtotal__l">Valor estimado</p><p class="mtotal__v" id="mtotal-v">€36</p></div><a href="#res-t" tabindex="-1" id="mtotal-go">Ver resumo</a></div>';
  }

  function bindPlan() {
    var selEl = document.getElementById("plan-session");
    var pEl = document.getElementById("plan-people");
    var tot = document.getElementById("plan-total");
    var form = document.getElementById("plan-formula");
    var sum = document.getElementById("plan-summary");
    var slot = document.getElementById("plan-error-slot");
    var sHint = document.getElementById("plan-session-hint");
    var pHint = document.getElementById("plan-people-hint");
    var dec = document.getElementById("dec"), inc = document.getElementById("inc");
    var mv = document.getElementById("mtotal-v"), mbar = document.getElementById("mtotal");
    var resBox = document.querySelector(".result");
    if (mbar && resBox && "IntersectionObserver" in window) {
      new IntersectionObserver(function (en) { mbar.setAttribute("data-hidden", String(en[0].isIntersecting)); }, { threshold: 0.15 }).observe(resBox);
    }
    document.getElementById("mtotal-go").addEventListener("click", function (e) {
      e.preventDefault();
      var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      resBox.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
    });
    function mirror(v, isErr) { if (mv) { mv.textContent = v; mv.classList.toggle("is-err", !!isErr); } }

    function setError(msg) {
      var ex = document.getElementById("plan-error");
      if (!msg) { if (ex) ex.remove(); pEl.removeAttribute("aria-invalid"); pEl.setAttribute("aria-describedby", "plan-people-hint"); return; }
      if (!ex) {
        ex = document.createElement("p");
        ex.id = "plan-error"; ex.className = "perr"; ex.setAttribute("data-testid", "plan-error"); ex.setAttribute("role", "alert");
        slot.appendChild(ex);
      }
      ex.innerHTML = WARN + "<span>" + esc(msg) + "</span>";
      pEl.setAttribute("aria-invalid", "true");
      pEl.setAttribute("aria-describedby", "plan-people-hint plan-error");
    }

    function calc() {
      var s = SESSIONS[selEl.value] || SESSIONS.aberta;
      pEl.max = String(s.max);
      sHint.textContent = s.duration + " · " + s.capacity + " · " + s.when;
      pHint.textContent = s.mode === "flat" ? "De 1 a 6 pessoas. O valor é fixo para o grupo." : "De 1 a 8 pessoas.";
      var raw = String(pEl.value).trim();
      var n = Number(raw);
      var err = "";
      if (raw === "" || pEl.validity.badInput) err = "Informe o número de pessoas, de " + s.min + " a " + s.max + ".";
      else if (!isFinite(n) || Math.floor(n) !== n) err = "Use um número inteiro de pessoas, de " + s.min + " a " + s.max + ".";
      else if (n < s.min) err = "O mínimo é 1 pessoa.";
      else if (n > s.max) err = s.mode === "flat" ? "A sauna privativa recebe no máximo 6 pessoas. Reduza o grupo para ver o valor." : s.name + " recebe no máximo 8 pessoas. Reduza o número para ver o valor.";

      dec.disabled = !err && n <= s.min;
      inc.disabled = !err && n >= s.max;

      if (err) {
        setError(err);
        tot.textContent = "—";
        tot.classList.add("is-empty");
        tot.setAttribute("aria-label", "Sem valor estimado: corrija o número de pessoas");
        form.textContent = "Sem valor até corrigir o número de pessoas.";
        mirror("Corrija o número de pessoas", true);
        sum.innerHTML = '<li>' + esc(s.name) + '</li>';
        return;
      }
      setError("");
      var total = s.mode === "flat" ? s.price : s.price * n;
      if (!(total >= 0) || !isFinite(total)) { setError("Não foi possível calcular. Revise os valores."); tot.textContent = "—"; return; }
      tot.textContent = eur(total);
      mirror(eur(total), false);
      tot.classList.remove("is-empty");
      tot.removeAttribute("aria-label");
      form.textContent = s.mode === "flat" ? "€120 fixos · " + n + (n === 1 ? " pessoa" : " pessoas") : s.priceLabel + " × " + n + (n === 1 ? " pessoa" : " pessoas");
      sum.innerHTML = '<li>' + esc(s.name) + ', ' + s.duration + '</li><li>' + esc(s.when) + '</li><li>Leve toalha, roupa de banho, chinelo e garrafa de água.</li>';
    }
    function step(d) {
      var s = SESSIONS[selEl.value];
      var n = parseInt(pEl.value, 10);
      if (!isFinite(n)) n = 0;
      n = Math.min(s.max, Math.max(s.min, n + d));
      pEl.value = n; calc();
    }
    selEl.addEventListener("change", calc);
    pEl.addEventListener("input", calc);
    pEl.addEventListener("change", calc);
    dec.addEventListener("click", function () { step(-1); });
    inc.addEventListener("click", function () { step(1); });
    calc();
  }

  function viewRules() {
    return '' +
      '<header class="phead"><div class="wrap phead__in">' +
        '<p class="eyebrow">Antes da primeira visita</p><h1>Regras e perguntas</h1>' +
        '<p class="lead">Poucas regras, iguais para todas as sessões.</p>' +
      '</div></header>' +
      '<section class="sec--tight"><div class="wrap">' +
        '<ul class="rules">' + RULES.map(function (r) {
          return '<li><span class="ritual__meta" style="margin-top:0">' + r[0] + '</span><h3>' + r[1] + '</h3><p>' + r[2] + '</p></li>';
        }).join("") + '</ul>' +
      '</div></section>' +
      '<section class="sec--tight" aria-labelledby="faq-t" style="padding-top:0"><div class="wrap">' +
        '<div class="faq-head"><p class="eyebrow">Perguntas frequentes</p><h2 id="faq-t">Dúvidas comuns</h2></div>' +
        '<div class="faq">' + FAQ.map(function (f, i) {
          return '<details' + (i === 0 ? " open" : "") + '><summary>' + esc(f[0]) + '</summary><div class="a">' + f[1] + '</div></details>';
        }).join("") + '</div>' +
      '</div></section>';
  }

  function viewCredits() {
    var list = (window.TABUA_CREDITS || []).map(function (c) {
      return '<figure class="credit" style="margin:0"><img src="assets/' + esc(c.file) + '" alt="' + esc(c.description) + '" loading="lazy">' +
        '<figcaption><div><b>' + esc(c.title) + '</b><span>Autor: ' + esc(c.author) + ' · Licença: ' + esc(c.license) + '</span>' +
        '<span>' + esc(c.description) + '</span>' +
        '<span>Fonte: <span class="mono" style="word-break:break-all;font-size:12px">' + esc(c.source) + '</span></span></div></figcaption></figure>';
    }).join("");
    return '' +
      '<header class="phead"><div class="wrap phead__in">' +
        '<p class="eyebrow">Fotografias</p><h1>Créditos</h1>' +
        '<p class="lead">Fotografias ilustrativas de outro local (domínio público, CC0); não retratam as instalações da marca fictícia. Todas as imagens são de W.carter, via Wikimedia Commons, sem alteração de pixels. A lista completa também está em <a class="textlink" href="assets/credits.json">credits.json</a>.</p>' +
      '</div></header>' +
      '<section class="sec--tight"><div class="wrap"><div class="credits">' + list + '</div></div></section>';
  }

  function viewNotFound() {
    return '<header class="phead"><div class="wrap phead__in"><p class="eyebrow">Página não encontrada</p><h1>Nada aqui.</h1>' +
      '<p class="lead"><a class="textlink" href="#/">Voltar ao início</a> ou <a class="textlink" href="#/horarios">ver horários</a>.</p></div></header>';
  }

  /* ---------- Router ---------- */
  var TITLES = { home: "Tábua · Sauna a lenha no píer", horarios: "Horários · Tábua", planejar: "Planejar visita · Tábua", regras: "Regras e perguntas · Tábua", creditos: "Créditos · Tábua" };
  var currentFilter = "todas";
  var first = true;

  function parse() {
    var h = location.hash.replace(/^#\/?/, "");
    var q = {};
    var qi = h.indexOf("?");
    if (qi > -1) { h.slice(qi + 1).split("&").forEach(function (p) { var kv = p.split("="); q[decodeURIComponent(kv[0])] = decodeURIComponent(kv[1] || ""); }); h = h.slice(0, qi); }
    var parts = h.split("/").filter(Boolean);
    return { parts: parts, q: q };
  }

  function route() {
    var h = location.hash;
    // âncoras internas da home (ex.: #como-funciona) não são rotas
    if (h && h.charAt(1) !== "/" && h.length > 1) {
      var t = document.getElementById(h.slice(1));
      if (t) { t.scrollIntoView(); return; }
    }
    var r = parse();
    var key = r.parts[0] || "home";
    var html, navKey = key, title;
    if (key === "home") html = viewHome();
    else if (key === "horarios") { currentFilter = r.q.filtro === "nascer-sol" ? "nascer-sol" : "todas"; html = viewSchedule(currentFilter); }
    else if (key === "sessao") { html = viewSession(r.parts[1]); navKey = "horarios"; if (html) title = SESSIONS[r.parts[1]].name + " · Tábua"; }
    else if (key === "planejar") html = viewPlan(r.q.sessao);
    else if (key === "regras") html = viewRules();
    else if (key === "creditos") html = viewCredits();
    if (!html) { html = viewNotFound(); navKey = ""; title = "Página não encontrada · Tábua"; }

    main.innerHTML = '<div class="view">' + html + '</div>';
    document.body.classList.toggle("planner-page", key === "planejar");
    document.title = title || TITLES[key] || "Tábua";

    document.querySelectorAll(".nav a").forEach(function (a) {
      if (a.getAttribute("data-route") === navKey) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });

    if (key === "horarios") { renderBoard(currentFilter); bindFilter(); }
    if (key === "planejar") bindPlan();
    bindScrollLinks();

    if (!first) { window.scrollTo(0, 0); main.focus({ preventScroll: true }); }
    first = false;
  }

  function bindFilter() {
    document.querySelectorAll(".seg button").forEach(function (b) {
      b.addEventListener("click", function () {
        currentFilter = b.getAttribute("data-filter");
        document.querySelectorAll(".seg button").forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
        renderBoard(currentFilter);
        var target = currentFilter === "nascer-sol" ? "#/horarios?filtro=nascer-sol" : "#/horarios";
        if (location.hash !== target) history.replaceState(null, "", target);
      });
    });
  }

  function bindScrollLinks() {
    document.querySelectorAll("[data-scroll]").forEach(function (a) {
      a.addEventListener("click", function (e) {
        var t = document.getElementById(a.getAttribute("data-scroll"));
        if (!t) return;
        e.preventDefault();
        var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        t.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
        t.focus({ preventScroll: true });
      });
    });
  }

  window.addEventListener("hashchange", route);
  route();
})();
