# Execução m13 · R0 · Miolo / Fornada de sábado

- **Início:** 2026-10-20T23:54:40Z
- **Fim:** 2026-10-21T00:12Z (aprox.)
- **Tempo ativo aproximado:** ~18 min (leitura do método ~4 min; build ~7 min; QA e correções ~7 min)
- **Entrega:** `/tmp/dqb/runs/m13/r0/index.html` (abre direto via `file://`, sem servidor)
- **Registro do método:** `/tmp/dqb/runs/m13/web-delivery-r0.json` (schema v0.2; `creative_web.py validate` → `ok: true`)
- **Evidências:** `/tmp/dqb/runs/m13/evidence-r0/`

## Arquivos do método lidos

| Arquivo | Leitura |
|---|---|
| `ai-creative-skill/SKILL.md` | integral |
| `references/AI_Creative_Skill_V2.5_Integration_Manifest.md` | integral |
| `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` | integral (fluxo FAST de 8 passos seguido) |
| `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md` | integral (nenhum contrato de domínio se aplica a websites; usado só o princípio de PASS/PARTIAL honesto) |
| `web/README_PTBR.md` | integral |
| `web/docs/DELTA_AND_GATES.md` | integral |
| `web/schemas/web_delivery_v0.2.schema.json` | integral, via impressão do JSON |
| `web/runtime/validate.py` | linhas 1–22 parcial, 23–117 integral (para entender os checks FAST obrigatórios e o build hash) |
| `web/runtime/cli.py`, `scripts/creative_web.py` | só as assinaturas dos subcomandos (grep) |

Não li: o Current Design Manifest V2.4, o Architecture Spec, o Runtime Activation, os Execution Contracts, o Specialist Method System e o Typography/Layout. O SKILL.md manda carregar só o que a tarefa exige, e para WEB_PREVIEW ele aponta diretamente para o Work Profile Web. O método de Typography/Layout não é referenciado pelo perfil Web.

Ferramentas do método executadas:
- `creative_web.py route` sem `--intent` → `ValueError: Ambiguous request`. Com `--intent WEB_PREVIEW` → `WEB_PREVIEW / FAST / build_required`.
- `creative_web.py audit` → só aceita a pasta de saída dentro da raiz do site. Para não sujar `r0/`, rodei sobre uma cópia; resultado em `evidence-r0/static-audit-on-copy/`.
- `creative_web.py validate web-delivery-r0.json --site-dir .` → `ok: true`.
- Não usei `preview start`: o site funciona via `file://`, e a instrução comum pede verificação com `file://`.

## WEB_BRIEF (resumo)

- **Verdade do produto:** só a tabela do briefing (nomes, categorias, preços, unidades e descrições literais).
- **Desconhecido e não alegado:** ingredientes além da descrição, alérgenos e endereço.
- **Público:** vizinhos de 25 a 55 anos no Vale.
- **Ação principal:** "Ver a fornada" → encomenda demonstrativa.
- **Marca:** PROVISIONAL (nome e assinatura são fixos).

## Direção (WEB_DIRECTION)

- **Ideia:** "ficha de fornada", ou seja, o tempo de sexta a sábado como estrutura.
  - Paleta: papel creme `#F6EFE3`, tinta marrom-casca `#2A1C13`, caramelo `#9C5224` e um acento vermelho tirado das toalhas xadrez das próprias fotos.
  - Tipografia: Fraunces (títulos; o itálico em caramelo marca "começa na sexta."), Instrument Sans (texto) e IBM Plex Mono (horários, preços e rótulos, como numa etiqueta de forno).
  - Wordmark: "miolo" em Fraunces semibold, minúsculo, com um ponto vermelho (uma "migalha").
- **Decisão de composição:** o recorte em arco (boca de forno) é o enquadramento recorrente de todas as fotos de produto (hero, cards, detalhe, miniaturas na encomenda). O título grande divide o hero com uma única foto em arco, e o CTA fica logo abaixo do texto.
  - **Consequência observável:** no desktop, título e arco ficam lado a lado na dobra. No mobile, o arco vem primeiro, mais baixo (5:4), e o título com o CTA entram na primeira tela.
  - **Tradeoff:** o arco corta as bordas superiores das fotos. Aceitei porque os produtos ficam centrados e só se perde o fundo.
- **"Como funciona":** régua temporal com três marcadores (aberto → cheio → vermelho = sexta → madrugada → retirada). Fica horizontal no desktop e vira linha vertical no mobile.
- **Encomenda:** "ticket" com linhas tracejadas. O resumo aparece como um bloco escuro, para contrastar com o rascunho.
- **Referências:** observei só warm-organic e editorial-brand-led, por dimensão (calor do fundo creme; serifa grande como voz). Não herdei layout, ilustrações, botões-pílula azuis nem logo.
- **Movimento:** subida curta de 8px na troca de rota e hover discreto nos cards. Com `prefers-reduced-motion`, as durações vão a ≈0.

## Fidelidade

- Títulos, textos, CTA e as palavras-chave dos três passos são os do briefing. A assinatura aparece no rodapé.
- **Bolo de maçã:**
  - Selo "Sorvete não incluso" no card.
  - Caixa "O sorvete da foto não acompanha o bolo. A fatia é vendida sem acompanhamento." ao lado da foto no detalhe.
  - "sem sorvete" na linha da encomenda e no resumo.
  - O alt das duas fotos também diz que o sorvete não acompanha.
- O aviso de alérgenos está em todos os detalhes.
- O aviso de protótipo aparece no rodapé (todas as páginas), na encomenda (cheia e vazia) e no resumo.
- A linha de fotos com o link "créditos" leva a `#/creditos`, com as 14 fotos: título, autor, licença com link e fonte com link.
- Não há escassez, contagem regressiva, depoimentos, prêmios nem alegações de ingrediente ou origem.

## Verificações realizadas (Playwright Chromium headless, `file://`)

O script está em `work/qa.py`; os resultados, em `evidence-r0/functional-results.json`. **84 asserções, 0 falhas**, sobre o build final.

- **Viewports:** 1440×900, 390×844 e 768×1024.
- **Rotas:** home, fornada, detalhe (bolo e nó), encomenda vazia e créditos. Nenhuma tem overflow horizontal.
- **Filtros:** Salgados = só `product-scone-queijo`; Doces = 4; Todos = 5.
- **Detalhe:** rota por hash e aviso de alérgenos presentes.
- **Encomenda:**
  - 2 × Nó de cardamomo dá `order-subtotal` = **€5,60**.
  - A quantidade −3 vira 1 (€2,80); 99 vira 12 (€33,60); campo vazio não gera NaN nem valor negativo.
  - "Revisar encomenda" sem horário mostra um erro e não exibe o resumo. Com 09:00–10:00, `order-summary` mostra o horário e €5,60.
  - Duas linhas → remover as duas → aparece `order-empty`.
- **Navegação:** voltar e avançar do navegador funcionam (home ↔ fornada).
- **Créditos:** 14 entradas.
- **Acessibilidade:** todas as imagens têm atributo alt.
- **Rede e erros:** 0 erros de console ou página; 0 requisições fora de `file://`/`data:`.
- **Teclado:** a sequência de Tab (skip link → wordmark → Início → Fornada → Encomenda → CTA) mostra outline de 3px. Enter em `add-order` adiciona o item.
- **Reduced motion:** `animationDuration` computada ≈0.

**Revisão visual** pelas capturas (autocrítica do agente; não é aprovação humana). Correções feitas a partir dela:
1. As fotos dos cards da home saíam vazias por causa de `loading="lazy"` → removi o lazy desses cards.
2. Números "1/2/3" soltos e redundantes na régua → removi.
3. Contorno de foco no h1 quando ele recebe foco programático na troca de rota → removi só em `h1/h2[tabindex=-1]:focus`.
4. No mobile e no tablet, o resumo aparecia longe do botão, abaixo do ticket, e a coluna lateral vinha depois → passei a usar grid-areas (ticket → horário/revisar → resumo).
5. Em 768px, o destaque da home ficava em 2+1 cards → agora são 3 colunas entre 561 e 1024px.

O QA foi repetido depois de cada correção. O registro aponta para o build hash final (`7779e678…`).

**Helper estático do método:** `anchors_static` = FAIL. Ele trata os `href="#/..."` como âncoras quebradas, um falso positivo para rotas por hash; a navegação foi observada funcionando no browser. O check está registrado como FAIL/ADVISORY. Por isso o veredito é `PARTIAL`.

## Limitações conhecidas

- QA somente em Chromium headless. Não testei Safari/Firefox, leitor de tela real nem dispositivo físico. O contraste foi avaliado visualmente, sem medição automática.
- A autocrítica visual é do próprio agente; não houve revisão humana nem cega.
- O estado da encomenda persiste em `localStorage` só por conveniência (tolerante a falhas). Em outro navegador, a encomenda começa vazia.
- Os links de licença e fonte na página de créditos apontam para creativecommons.org e commons.wikimedia.org. São links de navegação, não chamadas de rede automáticas.
- Wordmark, paleta e tipografia são provisórios (marca fictícia).
- A rota `#/produto/<id>` com id inexistente mostra uma página "não encontrada" própria.
