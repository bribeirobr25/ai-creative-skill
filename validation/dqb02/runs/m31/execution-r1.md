# Execução m31 · R1 (revisão própria)

- Início (UTC): 2026-10-21T00:16:02Z
- Fim (UTC): 2026-10-21T00:18Z (aprox.)
- Tempo ativo aproximado: ~4 minutos
- Entrega: `/tmp/dqb/runs/m31/r1/index.html`. Copiado de `r0`, e `r0` não foi alterado.
- Método: passo 7 do Work Profile Web Experience v0.2 (QA visual em 1440/390/768, corrigir só defeitos materiais na menor superfície, repetir as verificações afetadas, não inventar revisão sem defeito) e a rubrica `rubric.md`. Não li nenhum arquivo novo do método nesta rodada.

## Problemas encontrados (nas capturas de R0)

1. **Encomenda, desktop 1440. Composição e usabilidade (defeito material).** O resumo aparecia abaixo das duas colunas, em largura total, longe do botão "Revisar encomenda". A coluna esquerda ficava com um grande vazio quando havia 1 item. A ação de revisar e o seu resultado ficavam desconectados.
2. **Cabeçalho em tablet 768. Tipografia e responsividade (defeito menor).** A assinatura ao lado do wordmark quebrava em duas linhas ("…encomendada na / sexta."), uma quebra acidental.

Pontos considerados e mantidos (preferência estética, não defeito):
- Na dobra do desktop, o título tem mais peso que a foto. Esse é o tradeoff declarado na direção.
- Na mobile home a foto do hero aparece abaixo do CTA. A prioridade é proposta → ação.

## Correções (somente em r1)

- `app.js`: só mudou o lugar do `#summary-slot`, que passou para dentro de `.order-layout`. Nenhuma lógica foi alterada.
- `style.css` recebeu um bloco acrescentado ao final:
  - No desktop (≥981px), o painel de retirada fica na coluna 2, ocupando duas linhas, e o resumo vai para a coluna 1, abaixo dos itens e ao lado do painel.
  - O resumo perdeu a margem extra.
  - A assinatura do header é ocultada até 980px; ela continua no rodapé.

## Preservado

Ficaram iguais a R0: identidade, paleta, tipografia, wordmark, home, fornada, detalhe, créditos, rodapé, textos, dados, rotas, `data-testid`, lógica da encomenda e comportamento mobile da encomenda (que já era uma coluna).

## Regressões e verificações

- **Suíte Playwright refeita sobre `r1`: 58/58 PASS** (`evidence-r1/qa-results.json`). Cobre:
  - nenhuma rolagem horizontal em 1440, 390 e 768;
  - filtros, €5,60, horário obrigatório, limites de quantidade, resumo, voltar/avançar, remover, créditos;
  - teclado e foco, `alt`, reduced motion;
  - nenhuma requisição externa e nenhum erro de console.
- **Revisão visual de `evidence-r1/desktop-order-summary.png`:** o resumo está ao lado do painel, sem vão.
- **Revisão visual de `tablet-home.png`:** o header está em uma linha.
- **Revisão visual de `mobile-order-summary.png`:** inalterado, sem regressão.
- Nas capturas full-page, o cabeçalho fixo aparece no meio da imagem. É um artefato da captura (a página estava rolada até o resumo), não um defeito do site.
- `diff -rq r0 r1`: só `app.js` e `style.css` diferem.

## Limitações

- QA feito pelo agente, sem avaliação humana nem leitor de tela.
- Não gerei um novo `web-delivery` para r1; o registro validado continua sendo o de r0.
- As limitações de R0 continuam válidas: só `file://`, filtro via `replaceState`, contador por unidades, wordmark provisório.
