# Execução m50 · R0 · Miolo / Fornada de sábado

- Início: 2026-10-20T23:54:43Z
- Fim: 2026-10-21T00:04Z (aprox.; último hash de build 00:03:02Z)
- Tempo ativo aproximado: ~10 min
- Entrega: `/tmp/dqb/runs/m50/r0/index.html` (abre via `file://`, sem servidor; rotas por hash)

## Arquivos do método lidos

| Arquivo | Leitura |
|---|---|
| `ai-creative-skill/SKILL.md` | integral |
| `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` | integral |
| `web/README_PTBR.md` | integral |
| `web/docs/DELTA_AND_GATES.md` | integral |
| `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md` | integral (nenhum contrato do catálogo se aplica a website; registrado como não aplicável) |
| `references/AI_Creative_Skill_Method_Typography_Layout_Pre-v0.8.md` | parcial: lista de títulos, §3 Hierarchy, §4 Composition and Spacing (início), §5 Phone-Size Readability, §6 Controlled Finishing, §7 UI Truth, §10 Acceptance Rubric |
| `scripts/creative_web.py` (CLI) | só o `--help` e a execução de `route` e `audit`; o código-fonte não foi lido |

Não lidos: Integration Manifest, Design Manifest, Architecture, Runtime Activation, Execution Contracts, Specialist Method System e o schema `web_delivery_v0.2.schema.json`. O SKILL.md diz para carregar só o que a tarefa limitada exige. Não houve execução externa, gasto ou publicação, então os contratos de execução não eram relevantes. Por isso **não** foi produzido registro `web-delivery-r0.json` validado pelo schema.

## Rota e WEB_BRIEF (resumo)

- Rota: `WEB_PREVIEW`, modo FAST. A confirmação veio de `creative_web.py route --intent WEB_PREVIEW` (com frases em linguagem natural, o roteador recusou por ambiguidade).
- Fatos (briefing): nome, assinatura, textos do hero, três passos, 5 produtos com preço e unidade, avisos, horários e instrumentação. Nada foi inventado além disso: sem ingredientes extras, origem, "artesanal", depoimentos, escassez ou contagem regressiva.
- Ação principal: "Ver a fornada". Formulário: `LOCAL_CALCULATION` (resumo local, sem envio).
- Direitos: 14 fotos de W.carter (CC0 / CC BY 4.0 / CC BY-SA 4.0), usadas sem edição de pixels, só com `object-fit`/`object-position` via CSS. Todas recebem crédito em `#/creditos` com autor, licença (link) e fonte.

## WEB_DIRECTION (provisória)

- Ideia: "da sexta à noite ao sábado de manhã". Base em farinha/creme quente, com uma faixa noturna azul-marinho no "Como funciona". Nela, uma linha do tempo vai do azul ao amarelo-gema: lua → forno → sol.
- Tipografia: Fraunces (voz da casa, títulos, wordmark minúsculo "miolo" com um ponto cor de brasa), Instrument Sans (leitura/UI), IBM Plex Mono (horários, preços e prazos, como numa comanda/etiqueta de padaria). Tudo local, de `fonts/`.
- Forma recorrente: arco de forno (`border-radius` em arco) na foto do hero e na galeria do detalhe. Um "ticket" pontilhado mostra os prazos.
- Componentes: cartões de produto com tag Doce/Salgado, preço em mono e "por unidade/fatia/inteira, 8 fatias"; stepper de quantidade 1–12; horários em blocos tipo etiqueta; resumo com borda forte.
- Referências de `references/`: só observei `warm-organic-desktop.jpg` para calibrar o tom. Nada foi copiado.
- Fidelidade do bolo de maçã: o aviso "o sorvete não acompanha o bolo" aparece no cartão, na legenda da foto e num callout do detalhe. O texto alternativo das fotos também menciona isso.

## Implementação

- `r0/index.html`, `r0/styles.css`, `r0/app.js`, `r0/credits-data.js` (gerado de `assets/credits.json`), `r0/assets/` (cópia integral), `r0/fonts/` (cópia com licenças).
- Rotas: `#/`, `#/fornada`, `#/fornada/doces`, `#/fornada/salgados`, `#/produto/<id>`, `#/encomenda`, `#/creditos`.
- A encomenda fica guardada em `localStorage` (com try/catch); nada sai do navegador.
- A quantidade é sempre forçada a um inteiro entre 1 e 12. Campo vazio vira 1 ao sair do campo. O total é calculado em centavos e nunca fica negativo ou NaN. Mudar qualquer item ou o horário fecha o resumo, que precisa ser revisado de novo.
- Todos os `data-testid` exigidos estão presentes.

## Verificações (BROWSER_OBSERVED, Chromium headless via Playwright, `file://`)

Script: `evidence-r0/qa_r0.py`. Resultado final: `evidence-r0/qa-results.json`, **35/35 PASS**, no build com os hashes abaixo.

- Sem overflow horizontal: home e fornada em 1440×900, 390×844 e 768×1024; detalhe e encomenda em 390×844.
- A fornada mostra 5 itens. Doces mostra 4. Salgados mostra só `product-scone-queijo`. Todos volta para 5.
- Os 5 detalhes têm aviso de alérgenos e `add-order`. O bolo de maçã tem o aviso do sorvete.
- Encomenda vazia mostra `order-empty`. 2 × Nó de cardamomo dá `order-subtotal` = **€5,60**.
- Revisar sem horário bloqueia e mostra erro. Quantidade 99 vira 12 (€33,60). −3 vira 1 (€2,80). Campo vazio não gera NaN.
- Com horário 09:00–10:00, `order-summary` aparece com o horário e €5,60. Remover leva ao estado vazio e a €0,00.
- Voltar/avançar do navegador funciona. A página de créditos lista 14 fotos. O aviso aparece no rodapé e na encomenda.
- Teclado: o primeiro Tab vai para "Pular para o conteúdo", o segundo para `nav-home`. Todas as `img` têm `alt`.
- Com `prefers-reduced-motion: reduce`, a animação dura ~0.
- Zero requisições não-`file:` e zero erros de console.
- Inspeção visual das capturas: home desktop/mobile, detalhe desktop, detalhe do bolo em mobile, encomenda com resumo em mobile.
- Correções após a 1ª QA visual: a seção "Como funciona" estava sem margem lateral (uma regra de padding anulava a do `.wrap`). E o resumo rolava para baixo do cabeçalho fixo (corrigido com `scroll-margin-top`). A QA foi rodada de novo depois: 35/35.
- Auditoria do método (`creative_web.py audit`, numa cópia descartável de r0, porque o helper exige saída dentro do site), em `evidence-r0/method-static-audit/`:
  - `assets_available` PASS e `js_syntax` PASS (STATIC_INSPECTED).
  - `anchors_static` FAIL: falso positivo, porque o helper não entende rotas por hash `#/...`. A navegação foi confirmada no navegador.
  - `browser_render` e `content_truth` NOT_TESTED por esse helper.

Hashes do build verificado:
```
6d71c2089e6ab236dfe827e9d7c0fbc1b1eb4f3c48d449afbee7452bcb116df5  app.js
ff28f6b33fd011a1fa56c0a832068f0964fdfed2f807e6fcd48646396b73379e  credits-data.js
bfbd3af370a484c560d0cc7eab9ca1c16cc7667c975b989bc13c984db126a36b  index.html
fe74a26c86e68403a65ba64ef9780d9e1151dc14249233fb88f75997468f2083  styles.css
```

## Limitações conhecidas

- O preview foi aberto via `file://`, não pelo `preview start` do método. Não há URL persistente.
- Não houve teste com leitor de tela real, dispositivo físico ou Safari/Firefox. Também não houve avaliação humana nem revisão independente: a QA visual foi autoavaliação.
- A interação de teclado foi testada só no início da página (skip link → nav). A navegação completa por teclado no fluxo de encomenda e o foco após remover/revisar foram implementados, mas não testados ponto a ponto.
- Não há registro `web-delivery` validado pelo schema v0.2.
- Os links de crédito apontam para o Wikimedia Commons, que é externo e só abre por clique do usuário. Nenhuma requisição é feita automaticamente.
- Os textos de apoio ("Micro-padaria no Vale", descrições dos passos, "A padaria") são redação provisória baseada no briefing.
- O sábado não tem data; o protótipo não calcula datas reais nem o prazo de sexta, 18h.
