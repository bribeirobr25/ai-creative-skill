# Execução t92 · R1 (autorrevisão)

- Início: 2026-10-21T00:29:07Z
- Fim: 2026-10-21T00:32:30Z (aprox.)
- Tempo ativo: ~4 min
- Base: cópia integral de `r0/` para `r1/`. O `r0/` não foi alterado: hashes iguais a `evidence-r0/build-sha256.txt`.
- Método: `Work_Profile_Web_Experience_v0.2`, passo 7. O profile manda corrigir defeitos materiais na menor superfície possível (`WEB_EDIT`), repetir as verificações afetadas e não inventar revisão extra. Classifiquei cada achado como defeito objetivo, falha da direção escolhida ou preferência estética, e só corrigi os dois primeiros tipos. Não li nenhum arquivo novo do método nesta rodada.

## Problemas encontrados (revisão das capturas R0 com a rubrica)

1. **Usabilidade e responsividade (defeito objetivo).** No 390px, o link "Regras" sumia do menu do topo (`display:none`). Como regras e FAQ são exigências do briefing, achá-las ficava mais difícil no mobile. A medição mostrou que os quatro itens cabem na largura.
2. **Clareza na tarefa crítica do mobile (defeito objetivo leve).** No planejador em 390px, o valor estimado ficava abaixo do formulário, fora da dobra (top ≈ 1.050px). Quem muda o número de pessoas não via o resultado sem rolar a tela.
3. **Componentes (detalhe).** No detalhe da sessão, as notas específicas usavam um "·" quase invisível como marcador, inconsistente com os marcadores "18+", "0%" e "Shh".
4. **Composição (detalhe).** No cabeçalho do FAQ havia o texto "Toque em uma pergunta…" alinhado à base, à direita, criando uma coluna vazia e desequilibrada no desktop. O texto também era redundante.

Avaliei e mantive como preferência estética, sem mudança: o recorte da foto do hero; a página longa da programação no mobile (o filtro e a contagem já ficam no topo); o hero com altura máxima no desktop.

## Correções feitas em `r1/`

- `styles.css`, menu mobile: os quatro itens ficam visíveis (padding 7px, fonte 14px). O sublinhado do item ativo foi ajustado.
- `app.js` e `styles.css`, barra fixa de total (somente ≤900px e somente na rota `#/planejar`):
  - Espelha o valor estimado, ou "Corrija o número de pessoas" quando há erro.
  - Some quando o painel de resultado está visível (IntersectionObserver).
  - Tem um link "Ver resumo" que rola até o painel e respeita reduced motion.
  - É `aria-hidden`: a região viva `plan-total` continua sendo a fonte acessível única, e o `data-testid="plan-total"` continua único.
  - O rodapé ganha um respiro inferior nessa rota.
- `app.js`, detalhe da sessão: o marcador das notas passou de "·" para "Nota".
- `app.js` e `styles.css`, FAQ: o cabeçalho virou um bloco simples (eyebrow + h2), sem a frase redundante.

## Preservado

Direção visual, paleta, tipografia, hero, home, programação, filtro, rotas, toda a instrumentação `data-testid`, cálculos e mensagens de erro, textos obrigatórios, avisos e créditos. `index.html`, `credits-data.js`, `assets/` e `fonts/` estão idênticos ao R0 (hash conferido). As mudanças ficaram em `app.js` e `styles.css`.

## Verificações (Playwright/Chromium, build R1)

- `evidence-r1/qa_r1.py` repete a bateria completa do R0: **50/50 PASS**, sem regressões. Ela cobre overflow em 3 viewports × 6 rotas, filtro, detalhes, navegação, os 11 casos do planejador, teclado e foco, alt, rede externa, console e reduced motion.
- Verificações novas do R1: **9/9 PASS**.
  - Menu mobile com 4 itens visíveis, dentro de 390px, e "Regras" navega.
  - A barra mostra €54 com 3 pessoas e um texto sem "€" com 9 pessoas.
  - A barra some quando o resultado está visível.
  - `plan-total` continua único.
  - A barra fica oculta no desktop e não existe fora do planejador.
- Revisão visual das capturas R1: `m-plan-bar.png`, `m-plan-bar-error.png`, `m-home-fold.png`, `d-rules-fold.png`.
- Hashes: `evidence-r1/build-sha256.txt`.

## Regressões

Nenhuma detectada nos testes acima.

Risco residual: em larguras abaixo de cerca de 360px o menu de 4 itens pode ficar justo. Isso não foi testado; testei apenas 390, 768 e 1440.

## Limitações

Continuam valendo as do R0: QA automatizada feita pelo próprio agente, sem revisão humana nem leitor de tela, e sem registro no schema `web_delivery_v0.2`.
