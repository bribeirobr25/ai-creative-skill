# Execução t48 · R0

- Início: 2026-10-21T00:12:48Z
- Fim: 2026-10-21T00:25:30Z (aprox.)
- Tempo ativo: ~13 min
- Entrega: `/tmp/dqb/runs/t48/r0/index.html` (SPA com rotas por hash, HTML/CSS/JS sem framework; `assets/` e `fonts/` copiados para `r0/`)

## Arquivos do método lidos

- `ai-creative-skill/SKILL.md`: completo. Encaminha para `WEB_PREVIEW`.
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`: completo. Segui o fluxo FAST: brief, direção provisória, assets reaproveitados, construção, QA no navegador e entrega.
- `references/AI_Creative_Skill_V2.5_Integration_Manifest.md`: completo.
- `web/README_PTBR.md` e `web/docs/DELTA_AND_GATES.md`: completos.
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`: completo. Nenhum dos contratos de domínio se aplica a websites.
- `references/AI_Creative_Skill_Specialist_Method_System_Pre-v0.14-V2.4-CANDIDATE.md`: só busquei os termos "web/landing/typograph" (2 ocorrências). Não li o arquivo.
- Não li: o método de Typography/Layout, Architecture, Execution Contracts nem o schema `web_delivery_v0.2` (por isso não há registro JSON de entrega).
- Script do método executado: `scripts/creative_web.py audit`.

## Brief (WEB_BRIEF, resumido)

- Fatos: marca fictícia Tábua, a assinatura fixa, o conteúdo do hero, os 4 passos, o que levar, as 4 regras, a tabela de sessões, segunda fechada e os avisos obrigatórios.
- Desconhecido: tudo o que não está no briefing. Não inventei nada sobre o local, instalações, equipe, temperatura nem saúde.
- Ação principal: "Ver horários".
- Formulário: `LOCAL_CALCULATION` (sem envio).

## Direção (DIRECTION_PROVISIONAL)

- **Ideia: "tábuas de píer".** Réguas horizontais e listas com divisórias finas, como as tábuas do deck, dão o ritmo. O wordmark tipográfico "Tábua" vem com um pequeno ornamento SVG de tábuas desencontradas.
- **Paleta:** pinho escuro #1f2930, linho #f2ede5, areia #e0b98a e brasa #9c4420. A brasa vai só na ação principal e na faixa do rodapé.
- **Contrastes medidos:** brasa sobre linho 5.5:1; secundário #5d6870 sobre linho 4.9:1; areia sobre pinho 8.1:1.
- **Tipografia:** Fraunces (display, com título do hero escalonado em três linhas e "Mergulhe." em itálico), Instrument Sans (texto) e IBM Plex Mono (horários, preços, rótulos).
- **Fotos:** hero `bathing-ladder.jpg` (escada para o mar). Também usei bench-1, jetty-and-water-2, pier-and-jetty-3, jetties-1/2 e abyfjorden-estuary-1/2. Todas são enquadradas com `object-fit`/`object-position`, sem editar pixels.
- **Microinterações:** transição de rota fade/translate de 8px, sublinhado da navegação e leve elevação dos cards. Tudo é anulado em `prefers-reduced-motion`.

## Estrutura e rotas

- `#/`: hero, como funciona, faixa de fotos, o que levar + regras, 3 sessões, resumo da semana e CTA.
- `#/horarios`: filtro Todas/Nascer do sol (aria-pressed, status aria-live, `?filtro=nascer-sol` na URL), semana com 16 horários, segunda "Fechado" e aviso de programação ilustrativa.
- `#/sessao/{aberta|nascer-sol|privativa}`: detalhe com preço, duração, capacidade, horários, regras, CTA para o planejador pré-selecionado e "Voltar aos horários".
- `#/planejar`:
  - select + stepper −/+ + input numérico;
  - total e conta (ex.: "€18 × 3 pessoas = €54");
  - erro `role=alert` com `data-testid=plan-error`, criado só quando há erro; nesse caso o total vira "Sem estimativa";
  - aviso de protótipo.
- `#/regras`: regras, o que levar e 10 FAQs em `<details>`.
- `#/creditos`: créditos completos de `credits.json`, embutidos em `credits-data.js` (sem fetch).
- Rodapé: assinatura, avisos obrigatórios e link para os créditos.
- Toda a instrumentação `data-testid` pedida está presente.

## Verificações (Playwright/Chromium, file://, mesmo build)

`evidence-r0/qa-results.json`: **65/65 PASS** na última execução (BROWSER_OBSERVED).

- **Sem overflow horizontal:** 6 rotas × 3 viewports (1440×900, 390×844, 768×1024).
- **Filtro:** 16 slots em "Todas"; "Nascer do sol" mostra só 2 (sáb/dom 07:00, `data-session=nascer-sol`); voltar para "Todas" mostra 16 de novo.
- **Detalhes:** os links `session-*` abrem o detalhe certo e o botão Voltar do navegador retorna a `#/horarios`.
- **Planejador, valores:** aberta×3=€54, nascer-sol×2=€44, privativa×4=€120, aberta×8=€144, privativa×1=€120.
- **Planejador, erros:** aparece erro e nenhum "€" no total para aberta×9, privativa×7, 0, −2, vazio e 2.5. Nunca aparece NaN.
- **Teclado:** Tab vai para o skip link e depois para o wordmark; o contorno de foco é visível.
- **Imagens:** todas com alt.
- **Textos obrigatórios:** presentes.
- **Reduced motion:** animação de rota = none.
- **Rede:** zero requisições não-file.
- **Erros:** zero erros de console/página.

Inspeção visual das capturas em `evidence-r0/*.png`, que levou a três correções:
- removi o contorno no foco programático do h1;
- alinhei os horários no mobile;
- encurtei as opções do select, que eram cortadas no mobile.

Também corrigi dois textos:
- "todos os dias da semana" era falso → "de terça a domingo";
- "na ordem que o corpo pedir" contradizia a ordem fixa → "nesta ordem".

Os testes foram rodados de novo depois dessas mudanças (65/65), e essa execução também regenerou as capturas `evidence-r0/*.png`. Os horários de modificação confirmam que elas são posteriores à última edição de `app.js` e `styles.css`. Revisei visualmente só algumas delas; `*-plan-error.png` é anterior ao encurtamento das opções do select.

**Audit do método** (`creative_web.py audit`), em cópia idêntica de r0, porque o script exige a pasta de saída dentro do site:
- PASS: assets e sintaxe JS.
- `anchors_static` FAIL (ADVISORY): falso positivo, porque o auditor estático não entende rotas `#/...`. Elas foram confirmadas no navegador.
- browser/content_truth: NOT_TESTED pelo script.
- Resultado: `evidence-r0/static-audit/`.

Não executei o `preview start` do método (servidor loopback); o preview foi aberto via `file://`, como pedem as instruções do estudo.

## Limitações conhecidas

- Não testei com leitor de tela real, dispositivo físico nem Safari/Firefox.
- O seletor `:has()` só dá destaque visual (não é essencial).
- Os links da página de créditos apontam para Wikimedia/CC. São externos, mas só abrem se o usuário clicar; nada é carregado automaticamente.
- As fotos são de um único local sueco nublado. Não há imagem de sauna nem de fogo; o calor é transmitido pela paleta e pelo texto.
- Não gerei o registro `web_delivery_v0.2` (schema não lido).
- A revisão é autoavaliação, não independente.
