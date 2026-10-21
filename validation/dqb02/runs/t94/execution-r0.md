# Execução t94 · R0

- Início (UTC): 2026-10-21T00:12:48Z
- Fim (UTC): 2026-10-21T00:23Z (aprox.; último registro de relógio em 00:22:18Z, antes de escrever este arquivo)
- Tempo ativo aproximado: cerca de 11 minutos de relógio de parede, dentro do limite de 30 min.
- Entrega: `/tmp/dqb/runs/t94/r0/index.html`, com rotas por hash: `#/`, `#/horarios` (`?f=nascer-sol`), `#/sessao/{aberta|nascer-sol|privativa}`, `#/planejar` (`?s=`), `#/regras`, `#/creditos`.

## Arquivos do método lidos

| Arquivo | Leitura |
|---|---|
| `ai-creative-skill/SKILL.md` | integral |
| `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` | integral |
| `web/docs/DELTA_AND_GATES.md` | integral |
| `web/README_PTBR.md` | integral |
| `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md` | parcial: linhas 1–40 (§1 sequência de execução; contratos CHARACTER_BIBLE, CONTENT_IDEA, STORYBOARD_PLAN, VIDEO_CREATIVE_DIRECTION). Um grep por "web/site/page/landing" nas linhas 40–77 não encontrou contrato específico de website. |
| `references/AI_Creative_Skill_Method_Typography_Layout_Pre-v0.8.md` | parcial: §1–§4 (linhas 1–135) e §5–§7 (linhas 193–242): autoridade do texto, hierarquia, legibilidade em celular e "UI truth". |
| `scripts/creative_web.py` | só `--help`. Não executei `route`, `validate`, `preview` nem `audit`. |

Não li: os manifestos de versão, Architecture Spec, Runtime Activation, Execution Contracts, Specialist Method System, o JSON Schema web v0.2 nem os demais métodos. Por isso não produzi o registro `web-delivery-r0.json`, que seria opcional.

## WEB_BRIEF (resumo)

- Rota: `WEB_PREVIEW`, FAST. Ação principal: "Ver horários". Formulário: `LOCAL_CALCULATION`, sem captura de dados, envio ou pagamento.
- Fatos: todo o conteúdo vem de `briefing.md`. Não inventei preço, depoimento, vaga, benefício de saúde nem instalação. A marca, o local e os preços são fictícios e isso fica sinalizado.
- Fotos: CC0 de outro local, sem alteração de pixels. O enquadramento é feito só com `object-fit` e `object-position`, e os créditos estão em `#/creditos`, gerados a partir de `credits.json` (cópia embutida em `credits.js`).

## WEB_DIRECTION (provisória)

- Ideia: a palavra "tábua" vira a unidade do layout. Há faixas horizontais com juntas finas, como as tábuas do deck, nos fundos escuros, nos passos do ritual, na lista da semana e no recibo do planejador. O wordmark tem um ícone de tábuas em SVG próprio.
- Paleta: papel de madeira lavada (#f1ede5), mar e ardósia (#253035), brasa da lenha (#b4471b) só para a ação e os destaques, e uma cor de amanhecer (#c98a3d) só para a sessão Nascer do sol.
- Tipografia (pacote local): Fraunces para títulos e o wordmark, Instrument Sans para o texto e IBM Plex Mono para horários, rótulos e números.
- Fotos: o hero usa a escada de banho, ligação direta com "escada direto para o mar". Os passos do ritual usam o deck junto à água. Cada sessão tem a sua foto: o banco para a aberta, a luz baixa para o nascer do sol e o deck com píer para a privativa. A faixa final do planejador usa o píer ao entardecer.
- Movimento: discreto (setas, leve aproximação na foto dos cartões, transição do filtro, "tick" no total). Tudo é desligado com `prefers-reduced-motion`.

## Verificações (BROWSER_OBSERVED, Playwright/Chromium via file://)

Script em `evidence-r0/qa.py`, resultados em `evidence-r0/qa-results.json` e capturas `evidence-r0/{d,m,t}-*.png` em 1440×900, 390×844 e 768×1024. Rodada final: **51/51 PASS** no build abaixo.

- Nenhuma rolagem horizontal em 6 rotas × 3 viewports.
- `nav-home`, `nav-schedule` e `nav-plan` navegam corretamente. O voltar do navegador funciona.
- Programação: 16 `schedule-slot` com "Todas" (12 aberta, 2 nascer-sol, 2 privativa). "Nascer do sol" deixa exatamente 2, ambos 07:00 e `data-session="nascer-sol"` (Sáb e Dom). "Todas" restaura os 16.
- `session-aberta`, `session-nascer-sol` e `session-privativa` abrem o detalhe correto.
- Planejador: aberta×3=€54, nascer-sol×2=€44, privativa×4=€120, privativa×1=€120, aberta×8=€144. Os casos aberta×9, privativa×7, 0, vazio, −2 e 2.5 mostram `plan-error`, total "—", sem NaN e sem negativo.
- Teclado: o primeiro Tab leva ao link "Pular para o conteúdo". O Tab chega a `nav-schedule` com foco visível (`d-focus.png`) e Enter navega.
- Todas as imagens têm `alt`, sem imagem quebrada. O aviso de protótipo aparece no planejador e no rodapé.
- Com `reduced_motion=reduce`: animação `none` e transição `0s`.
- Zero requisições fora de file:// e zero erros de JS no console.
- Revisão visual das capturas desktop, mobile e tablet: corrigi um estouro horizontal dos cartões de sessão no mobile (grid `1fr` → `minmax(0,1fr)`) e o corpo dos cartões, que sumia abaixo da imagem em ≤620px. Troquei o ícone de três barras do wordmark, que parecia um menu hambúrguer sem função, por um bloco de tábuas.

Hashes do build final:
- `styles.css` 6e5ff864…
- `app.js` a3a279f9…
- `index.html` b33984ca…
- `credits.js` df7b3052…

As capturas foram feitas antes da última pequena correção de CSS e JS, mas o QA funcional de 51 itens rodou de novo depois dela. As capturas `m-home.png` e `t-home-fold.png` foram regeneradas nessa rodada.

## Limitações conhecidas

- O preview do método (`creative_web.py preview start`, servidor HTTP) não foi usado. A navegação local é por `file://` abrindo `r0/index.html`.
- Sem teste com leitor de tela real nem dispositivo físico. O contraste foi verificado visualmente, não medido.
- O `history.replaceState` do filtro pode falhar em alguns navegadores em `file://`; está protegido por try/catch e o filtro continua funcionando.
- Os links de origem nos créditos apontam para o Wikimedia Commons (são só âncoras; nada é carregado).
- Sem registro `web-delivery-r0.json` validado pelo schema e sem semântica de status canônico do método, porque o schema não foi lido.
- A nota estética é por autoavaliação, sem revisor humano.
