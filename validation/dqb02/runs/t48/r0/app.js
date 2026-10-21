/* Tábua — protótipo navegável. Sem rede, sem envio, sem armazenamento de dados pessoais. */
(function () {
  "use strict";

  /* ---------------- dados (do briefing) ---------------- */
  var SESSIONS = {
    "aberta": {
      id: "aberta", name: "Sessão aberta", short: "Aberta",
      duration: "90 min", price: 18, unit: "por pessoa", capacity: "até 8 pessoas",
      min: 1, max: 8, mode: "per-person",
      when: "Ter–Sex 17:00 e 19:00 · Sáb 10:00, 14:00, 17:00 · Dom 10:00",
      img: "assets/jetties-1.jpg", pos: "50% 62%",
      alt: "Píer de madeira e pontões sobre água calma, sob nuvens ao entardecer (foto ilustrativa de outro local)",
      intro: "A sessão regular, de terça a domingo. Você divide a sauna e o deck com outras pessoas e segue o ritual no seu ritmo.",
      note: "Cada pessoa paga a sua entrada. Até 8 pessoas por sessão."
    },
    "nascer-sol": {
      id: "nascer-sol", name: "Nascer do sol", short: "Nascer do sol",
      duration: "90 min", price: 22, unit: "por pessoa", capacity: "até 8 pessoas",
      min: 1, max: 8, mode: "per-person",
      when: "Sáb e Dom 07:00",
      img: "assets/abyfjorden-estuary-1.jpg", pos: "50% 55%",
      alt: "Luz baixa da manhã atravessando nuvens sobre uma enseada de águas calmas (foto ilustrativa de outro local)",
      intro: "A primeira sessão do fim de semana, às 07:00, com a luz da manhã sobre a enseada.",
      note: "Somente sábado e domingo, às 07:00. Cada pessoa paga a sua entrada."
    },
    "privativa": {
      id: "privativa", name: "Sauna privativa", short: "Privativa",
      duration: "2 h", price: 120, unit: "por grupo", capacity: "1 a 6 pessoas",
      min: 1, max: 6, mode: "flat",
      when: "Dom 15:00 · Qua 20:00",
      img: "assets/abyfjorden-estuary-2.jpg", pos: "40% 60%",
      alt: "Pequena casa de madeira junto a rochedos, à beira de uma enseada (foto ilustrativa de outro local)",
      intro: "A sauna e o deck só para o seu grupo, por duas horas.",
      note: "Valor fixo de €120 para o grupo, de 1 a 6 pessoas."
    }
  };
  var ORDER = ["aberta", "nascer-sol", "privativa"];

  var WEEK = [
    { key: "seg", name: "Segunda", slots: [] },
    { key: "ter", name: "Terça", slots: [["17:00", "aberta"], ["19:00", "aberta"]] },
    { key: "qua", name: "Quarta", slots: [["17:00", "aberta"], ["19:00", "aberta"], ["20:00", "privativa"]] },
    { key: "qui", name: "Quinta", slots: [["17:00", "aberta"], ["19:00", "aberta"]] },
    { key: "sex", name: "Sexta", slots: [["17:00", "aberta"], ["19:00", "aberta"]] },
    { key: "sab", name: "Sábado", slots: [["07:00", "nascer-sol"], ["10:00", "aberta"], ["14:00", "aberta"], ["17:00", "aberta"]] },
    { key: "dom", name: "Domingo", slots: [["07:00", "nascer-sol"], ["10:00", "aberta"], ["15:00", "privativa"]] }
  ];

  var RULES = [
    ["Maiores de 18 anos.", "Todas as sessões são só para adultos."],
    ["Banho de mar por conta e risco de cada pessoa.", "Não há salva-vidas no local. Descer a escada é opcional."],
    ["Sem álcool.", "Nem antes, nem durante a sessão."],
    ["Silêncio na sauna.", "Conversas ficam para o deck."]
  ];

  var STEPS = [
    ["Aqueça na sauna", "Entre na sauna a lenha e fique o tempo que for confortável.", "10 a 15 min"],
    ["Desça a escada para o mar, se quiser", "A escada sai do píer direto para a água. É opcional, e cada pessoa decide por si.", "opcional"],
    ["Descanse no deck", "Sente-se nas tábuas, ao ar livre, olhando a enseada.", "sem pressa"],
    ["Repita no seu ritmo", "Volte ao calor quantas vezes quiser dentro da sessão.", "quantas vezes quiser"]
  ];

  var BRING = [
    ["Toalha", '<path d="M6 4h12v16H6z"/><path d="M6 9h12M9 4v5"/>'],
    ["Roupa de banho", '<path d="M7 4c0 3 2 5 5 5s5-2 5-5"/><path d="M5 12h14l-2 8H7z"/>'],
    ["Chinelo", '<path d="M8 3c3 0 4 3 4 7s-1 11-4 11-4-6-4-11 1-7 4-7z"/><path d="M5 9c2 1 4 1 6 0"/>'],
    ["Garrafa de água", '<path d="M10 2h4v3l2 3v13H8V8l2-3z"/><path d="M8 13h8"/>']
  ];

  var DISCLAIMER = "Protótipo demonstrativo. Marca, local, horários e preços fictícios. Nada é reservado.";
  var SCHEDULE_NOTE = "Programação ilustrativa; disponibilidade não verificada neste protótipo.";
  var PHOTO_NOTE = "Fotografias ilustrativas de outro local (domínio público, CC0); não retratam as instalações da marca fictícia.";

  /* ---------------- utilitários ---------------- */
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function euro(n) { return "€" + n; }
  var ARROW = '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M3 10h13M11 5l5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
  var INFO = '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="8"/><path d="M10 9v5M10 6v.5"/></svg>';
  var ALERT = '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M10 2 1.5 17h17z"/><path d="M10 8v4M10 14.5v.5"/></svg>';
  var PLANKS = '<div class="planks" aria-hidden="true"><i></i><i></i><i></i></div>';

  function parseHash() {
    var h = location.hash.replace(/^#/, "") || "/";
    var q = {};
    var qi = h.indexOf("?");
    if (qi > -1) {
      h.slice(qi + 1).split("&").forEach(function (kv) {
        var p = kv.split("=");
        if (p[0]) q[decodeURIComponent(p[0])] = decodeURIComponent(p[1] || "");
      });
      h = h.slice(0, qi);
    }
    var parts = h.split("/").filter(Boolean);
    return { parts: parts, q: q };
  }

  /* ---------------- views ---------------- */
  function viewHome() {
    var steps = STEPS.map(function (s, i) {
      return '<li class="step"><span class="step__n">0' + (i + 1) + '</span><h3>' + esc(s[0]) + '</h3><p>' + esc(s[1]) + '</p><span class="step__tag">' + esc(s[2]) + '</span></li>';
    }).join("");
    var bring = BRING.map(function (b) {
      return '<li><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + b[1] + '</svg>' + esc(b[0]) + '</li>';
    }).join("");
    var rules = RULES.map(function (r) {
      return '<li><strong>' + esc(r[0]) + '</strong><span>' + esc(r[1]) + '</span></li>';
    }).join("");
    var cards = ORDER.map(function (id) { return sessionCard(SESSIONS[id], true); }).join("");
    var mini = WEEK.map(function (d) {
      var txt = d.slots.length ? d.slots.map(function (s) { return s[0]; }).join(" · ") : "fechado";
      return '<li class="' + (d.slots.length ? "" : "off") + '"><b>' + esc(d.name.slice(0, 3)) + '</b><span>' + esc(txt) + '</span></li>';
    }).join("");

    return '' +
      '<section class="hero" aria-labelledby="hero-title">' +
        '<img class="hero__img" src="assets/bathing-ladder.jpg" alt="Escada de madeira descendo de um píer direto para o mar, sob céu nublado (foto ilustrativa de outro local)">' +
        '<div class="hero__in">' +
          '<p class="eyebrow">Sauna a lenha · Enseada do Norte</p>' +
          '<h1 id="hero-title" tabindex="-1" data-focus><span>Aqueça.</span><span>Mergulhe.</span><span>Descanse.</span></h1>' +
          '<div class="hero__foot">' +
            '<p class="hero__text">Uma sauna a lenha sobre o píer, com escada direto para o mar.</p>' +
            '<div class="hero__actions">' +
              '<a class="btn btn--primary" href="#/horarios">Ver horários ' + ARROW + '</a>' +
              '<a class="btn btn--ghost" href="#/planejar">Estimar valor</a>' +
            '</div>' +
          '</div>' +
        '</div>' +
      '</section>' +

      '<section class="section" aria-labelledby="como-title">' +
        '<div class="wrap ritual">' +
          '<div class="ritual__head">' +
            '<p class="eyebrow">Como funciona</p>' +
            '<h2 class="h-sec" id="como-title">Quatro passos, nesta ordem.</h2>' +
            '<p class="lede">Primeira vez? É simples: calor, mar se quiser, deck. E de novo.</p>' +
            '<figure class="ritual__fig"><img src="assets/bench-1.jpg" alt="Banco de tronco rachado sobre um deck de madeira, com a enseada ao fundo (foto ilustrativa de outro local)" loading="lazy"><figcaption>Foto ilustrativa · outro local</figcaption></figure>' +
          '</div>' +
          '<ol class="steps">' + steps + '</ol>' +
        '</div>' +
      '</section>' +

      '<div class="band" aria-hidden="false">' +
        '<figure><img src="assets/jetty-and-water-2.jpg" alt="Tábuas de um deck de madeira na beira da água ondulada (foto ilustrativa de outro local)" loading="lazy"><figcaption>Foto ilustrativa · outro local</figcaption></figure>' +
        '<figure><img src="assets/pier-and-jetty-3.jpg" alt="Píer baixo avançando sobre a enseada ao fim da tarde (foto ilustrativa de outro local)" loading="lazy"><figcaption>Foto ilustrativa · outro local</figcaption></figure>' +
      '</div>' +

      '<section class="section on-dark" aria-labelledby="levar-title">' +
        '<div class="wrap two">' +
          '<div><p class="eyebrow">O que levar</p><h2 class="h-sec" id="levar-title">Quatro coisas na bolsa.</h2><ul class="bring">' + bring + '</ul></div>' +
          '<div><p class="eyebrow">Regras</p><h2 class="h-sec" id="regras-title">Combinados do píer.</h2><ol class="rules">' + rules + '</ol>' +
            '<p style="margin-top:24px"><a class="textlink" href="#/regras">Regras e perguntas frequentes</a></p></div>' +
        '</div>' +
      '</section>' +

      '<section class="section" aria-labelledby="sessoes-title">' +
        '<div class="wrap">' +
          '<p class="eyebrow">Sessões</p>' +
          '<h2 class="h-sec" id="sessoes-title">Três jeitos de visitar.</h2>' +
          '<div class="sessions">' + cards + '</div>' +
        '</div>' +
      '</section>' +

      '<section class="section on-dark" aria-labelledby="semana-title">' +
        '<div class="wrap teaser">' +
          '<figure class="teaser__fig"><img src="assets/jetties-2.jpg" alt="Pontões de madeira sobre água espelhada sob nuvens claras (foto ilustrativa de outro local)"></figure>' +
          '<div>' +
            '<p class="eyebrow">Semana</p>' +
            '<h2 class="h-sec" id="semana-title">De terça a domingo.</h2>' +
            '<ul class="mini-week">' + mini + '</ul>' +
            '<div class="hero__actions" style="margin-top:28px">' +
              '<a class="btn btn--primary" href="#/horarios">Ver horários ' + ARROW + '</a>' +
              '<a class="btn btn--ghost" href="#/planejar">Planejar visita</a>' +
            '</div>' +
            '<p class="out__note" style="border:0;padding-top:16px">' + esc(SCHEDULE_NOTE) + '</p>' +
          '</div>' +
        '</div>' +
      '</section>';
  }

  function sessionCard(s, withTestId) {
    return '<a class="scard" href="#/sessao/' + s.id + '"' + (withTestId ? ' data-testid="session-' + s.id + '"' : '') + '>' +
      '<div class="scard__img"><img src="' + s.img + '" style="object-position:' + s.pos + '" alt="' + esc(s.alt) + '" loading="lazy"></div>' +
      '<div class="scard__body">' +
        '<h3>' + esc(s.name) + '</h3>' +
        '<p class="facts"><span><b>' + euro(s.price) + '</b> ' + esc(s.unit) + '</span><span>' + esc(s.duration) + '</span><span>' + esc(s.capacity) + '</span></p>' +
        '<p class="scard__when">' + esc(s.when) + '</p>' +
        '<span class="scard__more">Ver detalhes ' + ARROW + '</span>' +
      '</div></a>';
  }

  function pageHead(eyebrow, title, lede, crumb) {
    return '<section class="phead on-dark"><div class="wrap">' +
      (crumb ? '<p class="crumb">' + crumb + '</p>' : '') +
      '<p class="eyebrow" style="margin-top:' + (crumb ? '18px' : '0') + '">' + esc(eyebrow) + '</p>' +
      '<h1 tabindex="-1" data-focus>' + esc(title) + '</h1>' +
      (lede ? '<p class="lede">' + esc(lede) + '</p>' : '') +
      '</div></section>';
  }

  function viewSchedule(q) {
    var filter = q.filtro === "nascer-sol" ? "nascer-sol" : "todas";
    var legend = ORDER.map(function (id) {
      return '<li><span class="dot dot--' + id + '"></span>' + esc(SESSIONS[id].name) + '</li>';
    }).join("");
    var links = ORDER.map(function (id) {
      var s = SESSIONS[id];
      return '<a href="#/sessao/' + id + '" data-testid="session-' + id + '">' + esc(s.name) + '</a>';
    }).join("");
    return pageHead("Programação semanal", "Horários", "Escolha uma sessão para ver duração, preço, capacidade e regras.") +
      '<section class="section" style="padding-top:8px"><div class="wrap">' +
        '<div class="toolbar">' +
          '<div class="seg" role="group" aria-label="Filtrar programação">' +
            '<button type="button" data-testid="schedule-filter-all" data-filter="todas" aria-pressed="' + (filter === "todas") + '">Todas</button>' +
            '<button type="button" data-testid="schedule-filter-sunrise" data-filter="nascer-sol" aria-pressed="' + (filter === "nascer-sol") + '">Nascer do sol</button>' +
          '</div>' +
          '<ul class="legend" aria-label="Legenda">' + legend + '</ul>' +
        '</div>' +
        '<p class="filter-status" id="filter-status" role="status" aria-live="polite"></p>' +
        '<ol class="week" id="week" aria-label="Programação da semana"></ol>' +
        '<p class="disclaim">' + INFO + '<span>' + esc(SCHEDULE_NOTE) + '</span></p>' +
        '<div style="margin-top:56px">' + PLANKS + '</div>' +
        '<h2 style="font-size:1.6rem;margin-top:32px">Tipos de sessão</h2>' +
        '<nav class="others" aria-label="Tipos de sessão">' + links + '</nav>' +
        '<p style="margin-top:28px"><a class="btn btn--primary" href="#/planejar">Estimar o valor da visita ' + ARROW + '</a></p>' +
      '</div></section>';
  }

  function renderWeek(filter) {
    var list = document.getElementById("week");
    if (!list) return;
    var count = 0;
    var html = WEEK.map(function (d) {
      var slots = d.slots.filter(function (s) { return filter === "todas" || s[1] === filter; });
      if (filter !== "todas" && !slots.length) return "";
      count += slots.length;
      var body = slots.length ? '<ul class="slots">' + slots.map(function (s) {
        var ss = SESSIONS[s[1]];
        return '<li><a class="slot" href="#/sessao/' + ss.id + '" data-testid="schedule-slot" data-session="' + ss.id + '" aria-label="' + esc(d.name + ", " + s[0] + ": " + ss.name + ", " + ss.duration + ", " + euro(ss.price) + " " + ss.unit) + '">' +
          '<span class="slot__t">' + s[0] + '</span><span class="slot__n">' + esc(ss.name) + '</span><span class="slot__m">' + esc(ss.duration + " · " + euro(ss.price) + " " + ss.unit) + '</span></a></li>';
      }).join("") + '</ul>' : '<p class="closed">Fechado</p>';
      return '<li class="day"><h2 class="day__name">' + esc(d.name) + '<small>' + (slots.length ? slots.length + (slots.length > 1 ? " horários" : " horário") : "sem sessões") + '</small></h2>' + body + '</li>';
    }).join("");
    list.innerHTML = html;
    var st = document.getElementById("filter-status");
    if (st) st.textContent = filter === "todas"
      ? "Mostrando todas as sessões: " + count + " horários de terça a domingo. Segunda-feira: fechado."
      : "Mostrando somente Nascer do sol: " + count + " horários, sábado e domingo às 07:00.";
  }

  function viewSession(id) {
    var s = SESSIONS[id];
    if (!s) return viewNotFound();
    var times = [];
    WEEK.forEach(function (d) { d.slots.forEach(function (x) { if (x[1] === id) times.push(d.name + " " + x[0]); }); });
    var rules = RULES.map(function (r) { return '<li><strong>' + esc(r[0]) + '</strong><span>' + esc(r[1]) + '</span></li>'; }).join("");
    var others = ORDER.filter(function (o) { return o !== id; }).map(function (o) {
      return '<a href="#/sessao/' + o + '">' + esc(SESSIONS[o].name) + '</a>';
    }).join("");
    return pageHead("Sessão", s.name, s.intro, '<a href="#/horarios">Horários</a> / ' + esc(s.name)) +
      '<section class="section"><div class="wrap detail">' +
        '<div>' +
          '<figure class="detail__fig"><img src="' + s.img + '" style="object-position:' + s.pos + '" alt="' + esc(s.alt) + '"></figure>' +
          '<p class="caption">Foto ilustrativa de outro local; não retrata as instalações.</p>' +
          '<div class="detail__rules light"><h2>Regras desta sessão</h2><ol class="rules">' + rules + '</ol></div>' +
        '</div>' +
        '<div>' +
          '<dl class="spec">' +
            '<div><dt>Preço</dt><dd class="big">' + euro(s.price) + ' <span style="font-family:var(--f-text);font-size:1rem">' + esc(s.unit) + '</span></dd></div>' +
            '<div><dt>Duração</dt><dd>' + esc(s.duration) + '</dd></div>' +
            '<div><dt>Capacidade</dt><dd>' + esc(s.capacity) + '</dd></div>' +
            '<div><dt>Horários</dt><dd><ul class="times">' + times.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join("") + '</ul></dd></div>' +
          '</dl>' +
          '<p style="margin-top:18px;color:var(--sea)">' + esc(s.note) + '</p>' +
          '<p class="disclaim">' + INFO + '<span>' + esc(SCHEDULE_NOTE) + '</span></p>' +
          '<div class="detail__actions">' +
            '<a class="btn btn--primary" href="#/planejar?sessao=' + id + '">Estimar valor desta sessão ' + ARROW + '</a>' +
            '<a class="btn btn--ghost light" href="#/horarios">Voltar aos horários</a>' +
          '</div>' +
          '<h2 style="font-size:1.4rem;margin-top:44px">Outras sessões</h2>' +
          '<nav class="others" aria-label="Outras sessões">' + others + '</nav>' +
        '</div>' +
      '</div></section>';
  }

  function viewPlan(q) {
    var sel = SESSIONS[q.sessao] ? q.sessao : "aberta";
    var opts = ORDER.map(function (id) {
      var s = SESSIONS[id];
      return '<option value="' + id + '"' + (id === sel ? " selected" : "") + '>' + esc(s.name + " · " + euro(s.price) + (s.mode === "flat" ? " o grupo" : " p/ pessoa")) + '</option>';
    }).join("");
    return pageHead("Planejador local", "Planejar visita", "Escolha a sessão e o número de pessoas para ver o valor estimado. O cálculo acontece só neste navegador.") +
      '<section class="section"><div class="wrap">' +
        '<div class="planner">' +
          '<form class="planner__form" id="plan-form" novalidate onsubmit="return false">' +
            '<div class="field">' +
              '<label for="plan-session">Tipo de sessão</label>' +
              '<div class="selectwrap"><select id="plan-session" data-testid="plan-session" class="select" aria-describedby="plan-session-hint">' + opts + '</select></div>' +
              '<span class="hint" id="plan-session-hint"></span>' +
            '</div>' +
            '<div class="field">' +
              '<label for="plan-people">Número de pessoas</label>' +
              '<div class="stepper">' +
                '<button type="button" id="ppl-minus" aria-label="Diminuir número de pessoas">−</button>' +
                '<input id="plan-people" data-testid="plan-people" type="number" inputmode="numeric" min="1" max="8" step="1" value="2" aria-describedby="plan-people-hint">' +
                '<button type="button" id="ppl-plus" aria-label="Aumentar número de pessoas">+</button>' +
              '</div>' +
              '<span class="hint" id="plan-people-hint"></span>' +
              '<div id="plan-error-slot"></div>' +
            '</div>' +
          '</form>' +
          '<div class="planner__out" aria-labelledby="out-label">' +
            '<p class="out__label" id="out-label">Valor estimado</p>' +
            '<p class="out__total" data-testid="plan-total" id="plan-total" aria-live="polite" aria-atomic="true">—</p>' +
            '<p class="out__calc" id="plan-calc"></p>' +
            '<p class="out__note"><strong>' + esc(DISCLAIMER) + '</strong><br>Sem envio, pagamento, conta ou dados pessoais. <a class="out__link" href="#/horarios">Ver horários</a></p>' +
          '</div>' +
        '</div>' +
      '</div></section>';
  }

  function bindPlan() {
    var sel = document.getElementById("plan-session");
    var ppl = document.getElementById("plan-people");
    var total = document.getElementById("plan-total");
    var calc = document.getElementById("plan-calc");
    var slot = document.getElementById("plan-error-slot");
    var sHint = document.getElementById("plan-session-hint");
    var pHint = document.getElementById("plan-people-hint");
    if (!sel) return;

    function update() {
      var s = SESSIONS[sel.value];
      ppl.max = String(s.max);
      sHint.textContent = s.duration + " · " + s.capacity + " · " + s.when;
      pHint.textContent = s.mode === "flat" ? "De 1 a 6 pessoas. Valor fixo por grupo." : "De 1 a 8 pessoas.";
      var raw = String(ppl.value).trim();
      var err = "";
      var n = NaN;
      if (raw === "" || !/^\d+$/.test(raw)) {
        err = raw === "" ? "Informe o número de pessoas (de " + s.min + " a " + s.max + ")." : "Use um número inteiro de pessoas, de " + s.min + " a " + s.max + ".";
      } else {
        n = parseInt(raw, 10);
        if (n < s.min) err = "O mínimo é 1 pessoa.";
        else if (n > s.max) err = s.name + " aceita no máximo " + s.max + " pessoas. Ajuste para " + s.min + " a " + s.max + ".";
      }
      var existing = document.getElementById("plan-error");
      if (err) {
        if (!existing) {
          existing = document.createElement("p");
          existing.id = "plan-error";
          existing.className = "err";
          existing.setAttribute("data-testid", "plan-error");
          existing.setAttribute("role", "alert");
          slot.appendChild(existing);
        }
        existing.innerHTML = ALERT + "<span>" + esc(err) + "</span>";
        ppl.setAttribute("aria-invalid", "true");
        ppl.setAttribute("aria-describedby", "plan-people-hint plan-error");
        total.textContent = "Sem estimativa";
        total.classList.add("is-empty");
        calc.textContent = "Corrija o número de pessoas para ver o valor.";
        return;
      }
      if (existing) existing.parentNode.removeChild(existing);
      ppl.removeAttribute("aria-invalid");
      ppl.setAttribute("aria-describedby", "plan-people-hint");
      var value = s.mode === "flat" ? s.price : s.price * n;
      if (!isFinite(value) || value < 0) { total.textContent = "Sem estimativa"; total.classList.add("is-empty"); calc.textContent = ""; return; }
      total.textContent = euro(value);
      total.classList.remove("is-empty");
      calc.textContent = s.mode === "flat"
        ? euro(s.price) + " fixos por grupo · " + n + (n > 1 ? " pessoas" : " pessoa")
        : euro(s.price) + " × " + n + (n > 1 ? " pessoas" : " pessoa") + " = " + euro(value);
    }
    function bump(d) {
      var v = parseInt(ppl.value, 10);
      if (isNaN(v)) v = 0;
      var s = SESSIONS[sel.value];
      v = Math.min(Math.max(v + d, s.min), s.max);
      ppl.value = String(v);
      update();
    }
    sel.addEventListener("change", function () {
      try { history.replaceState(null, "", "#/planejar?sessao=" + sel.value); } catch (e) {}
      update();
    });
    ppl.addEventListener("input", update);
    ppl.addEventListener("change", update);
    document.getElementById("ppl-minus").addEventListener("click", function () { bump(-1); });
    document.getElementById("ppl-plus").addEventListener("click", function () { bump(1); });
    update();
  }

  function viewRules() {
    var rules = RULES.map(function (r) { return '<li><strong>' + esc(r[0]) + '</strong><span>' + esc(r[1]) + '</span></li>'; }).join("");
    var bring = BRING.map(function (b) { return '<li><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">' + b[1] + '</svg>' + esc(b[0]) + '</li>'; }).join("");
    var faq = [
      ["Nunca fui a uma sauna a lenha. Como começo?", "Siga os quatro passos: aqueça na sauna por 10 a 15 minutos, desça a escada para o mar se quiser, descanse no deck e repita no seu ritmo. Saia do calor sempre que quiser."],
      ["Sou obrigado a entrar no mar?", "Não. O banho de mar é opcional e por conta e risco de cada pessoa. Não há salva-vidas no local. Você pode ficar só na sauna e no deck."],
      ["O que preciso levar?", "Toalha, roupa de banho, chinelo e garrafa de água."],
      ["Quanto tempo dura cada sessão?", "Sessão aberta e Nascer do sol: 90 minutos. Sauna privativa: 2 horas."],
      ["Posso ir em grupo?", "Sim. Na Sessão aberta e no Nascer do sol, cada pessoa paga a sua entrada (até 8 pessoas por sessão). A Sauna privativa custa €120 por grupo, de 1 a 6 pessoas."],
      ["Menores de idade podem participar?", "Não. Todas as sessões são para maiores de 18 anos."],
      ["Posso levar bebidas?", "Leve sua garrafa de água. Álcool não é permitido."],
      ["Posso conversar dentro da sauna?", "Na sauna o combinado é silêncio. Para conversar, use o deck."],
      ["Em que dias funciona?", "De terça a domingo. Segunda-feira: fechado. Veja todos os horários na programação semanal."],
      ["Consigo reservar por este site?", "Não. " + DISCLAIMER + " O planejador só calcula um valor estimado no seu navegador."]
    ].map(function (f) { return '<details><summary>' + esc(f[0]) + '</summary><p>' + esc(f[1]) + '</p></details>'; }).join("");
    return pageHead("Antes de ir", "Regras e perguntas frequentes", "O que vale para todas as sessões, o que levar e as dúvidas mais comuns.") +
      '<section class="section"><div class="wrap two light">' +
        '<div><p class="eyebrow">Regras</p><h2 class="h-sec">Combinados do píer.</h2><ol class="rules">' + rules + '</ol>' +
          '<p class="eyebrow" style="margin-top:56px">O que levar</p><ul class="bring">' + bring + '</ul></div>' +
        '<div><p class="eyebrow">Perguntas frequentes</p><h2 class="h-sec">Dúvidas comuns.</h2><div class="faq" style="margin-top:36px">' + faq + '</div>' +
          '<p style="margin-top:32px"><a class="btn btn--primary" href="#/horarios">Ver horários ' + ARROW + '</a></p></div>' +
      '</div></section>';
  }

  function viewCredits() {
    var data = window.TABUA_CREDITS || { images: [] };
    var items = data.images.map(function (c) {
      return '<li><img src="assets/' + esc(c.file) + '" alt="' + esc(c.description || c.title) + '" loading="lazy"><div>' +
        '<span class="t">' + esc(c.title) + '</span>' +
        '<span class="m">' + esc(c.author) + ' · <a href="' + esc(c.license_url) + '" rel="noopener">' + esc(c.license) + '</a></span>' +
        '<span class="m">' + esc(c.description) + '</span>' +
        '<span class="m">Fonte: <a href="' + esc(c.source) + '" rel="noopener">' + esc(c.source) + '</a></span>' +
        '<span class="m">' + esc(c.modification) + '</span>' +
        '</div></li>';
    }).join("");
    return pageHead("Créditos", "Créditos das fotografias", PHOTO_NOTE) +
      '<section class="section"><div class="wrap">' +
        '<p class="notice notice--light">' + esc(PHOTO_NOTE) + ' Links externos abrem a fonte original apenas se você clicar.</p>' +
        '<ul class="credits">' + items + '</ul>' +
      '</div></section>';
  }

  function viewNotFound() {
    return pageHead("Página não encontrada", "Este caminho não existe.", "Volte para o início ou veja os horários.") +
      '<section class="section"><div class="wrap"><a class="btn btn--primary" href="#/">Ir para o início</a> <a class="btn btn--ghost light" href="#/horarios">Ver horários</a></div></section>';
  }

  /* ---------------- roteador ---------------- */
  var main = document.getElementById("conteudo");
  var first = true;

  function route() {
    var r = parseHash();
    var p = r.parts;
    var html, title = "Tábua · Sauna a lenha no píer", active = "", after = null;
    if (!p.length) { html = viewHome(); }
    else if (p[0] === "horarios") {
      html = viewSchedule(r.q); title = "Horários · Tábua"; active = "horarios";
      after = function () { bindSchedule(r.q.filtro === "nascer-sol" ? "nascer-sol" : "todas"); };
    }
    else if (p[0] === "sessao") { html = viewSession(p[1]); title = (SESSIONS[p[1]] ? SESSIONS[p[1]].name : "Sessão") + " · Tábua"; active = "horarios"; }
    else if (p[0] === "planejar") { html = viewPlan(r.q); title = "Planejar visita · Tábua"; active = "planejar"; after = bindPlan; }
    else if (p[0] === "regras") { html = viewRules(); title = "Regras e perguntas · Tábua"; active = "regras"; }
    else if (p[0] === "creditos") { html = viewCredits(); title = "Créditos das fotos · Tábua"; }
    else { html = viewNotFound(); title = "Não encontrado · Tábua"; }

    main.innerHTML = '<div class="view">' + html + '</div>';
    document.title = title;
    document.querySelectorAll(".mainnav a").forEach(function (a) {
      if (a.getAttribute("data-route") === active) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
    if (after) after();
    if (!first) {
      window.scrollTo(0, 0);
      var f = main.querySelector("[data-focus]");
      if (f) f.focus({ preventScroll: true });
    }
    first = false;
  }

  function bindSchedule(filter) {
    renderWeek(filter);
    document.querySelectorAll(".seg button").forEach(function (b) {
      b.addEventListener("click", function () {
        var f = b.getAttribute("data-filter");
        document.querySelectorAll(".seg button").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        renderWeek(f);
        try { history.replaceState(null, "", f === "nascer-sol" ? "#/horarios?filtro=nascer-sol" : "#/horarios"); } catch (e) {}
      });
    });
  }

  window.addEventListener("hashchange", route);
  route();
})();
