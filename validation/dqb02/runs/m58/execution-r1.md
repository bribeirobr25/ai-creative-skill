# Execução m58 · R1 (autorrevisão, sem feedback externo)

- Início (UTC): 2026-10-21T00:16:04Z
- Fim (UTC): 2026-10-21T00:18:48Z
- Tempo ativo aproximado: ~7 min (limite: 15 min)
- Base: cópia integral de `r0/` para `r1/`. `r0/` não foi modificado: `diff` mostra só `app.js` e `styles.css` diferentes, e os timestamps de r0 são de antes do início do R1.
- Método: perfil WEB_EXPERIENCE v0.2, passos 7–8 (QA da mesma versão no navegador em 1440/390/768, com foco em crop, overflow, teclado/foco e CTA), e a rubrica `rubric.md`. Nenhum arquivo novo do método foi lido no R1.

## Problemas encontrados (pelas capturas do R0)
1. **Encomenda, desktop:** o resumo aparecia sob o bilhete, na coluna esquerda, deixando um vazio grande sob o painel de horários. O bloco "Total" ficava encostado no menu fixo ao rolar. (Composição / UI)
2. **Títulos com anel de foco azul:** ao trocar de rota, o `h1` recebe foco por código e mostrava o anel de foco (visível na captura mobile da fornada). Parecia um estado de erro. (Componentes / acabamento)
3. **Fornada, 768px:** com 5 produtos em 2 colunas, o scone ficava sozinho na última linha, com meia linha vazia. Na home, os 3 destaques ocupavam 2+1. (Responsividade)
4. **Detalhe, 390px:** as 4 miniaturas quebravam em duas linhas (3+1). O aviso flutuante "Adicionado" aparecia no rodapé, por cima do botão "Adicionar à encomenda". (Responsividade / UI)
5. **Botão no mobile:** "Adicionar à encomenda" quebrava em duas linhas ao lado do seletor de quantidade. (Componentes)
6. **Encomenda sem atalho de volta:** a única forma de voltar à fornada era pela navegação. (Clareza / usabilidade, leve)

## Correções em r1
- **Encomenda:**
  - o resumo (`#summaryHost`) passou a ser um item próprio da grade, abaixo do bilhete, com o painel de horários ocupando as duas linhas à direita; no mobile, a ordem continua linear;
  - o rodapé do bilhete ganhou o link "+ Adicionar mais itens da fornada" (destino real `#/fornada`).
- **Títulos focados por código:** `h1/h2[tabindex=-1]:focus` sem anel. Controles interativos mantêm `:focus-visible` (re-testado).
- **Tablet (641–1024px):** destaques da home em 3 colunas; na fornada, o último cartão ímpar ocupa a linha inteira, com foto à esquerda e texto ao lado.
- **Mobile (≤640px):**
  - miniaturas em uma linha de 4;
  - aviso flutuante no topo, sob o menu, sem cobrir o botão principal;
  - seletor de quantidade e botão em linhas próprias, com o botão em largura total.

## Preservado
- Direção "bilhete da fornada", paleta, tipografia, wordmark, hero em arco e linha do tempo dos três passos.
- Todo o conteúdo obrigatório, todos os `data-testid`, rotas, regras de quantidade (1–12) e horário obrigatório.
- Avisos de protótipo, alérgenos, sorvete e créditos.
- Fotos sem alteração de pixels.

## Regressões e verificações
- `evidence-r1/qa.py` (mesmo script do R0, apontado para r1): **42/42 PASS**, executado depois de cada rodada de mudança (duas vezes). Cobre:
  - textos exatos, filtros (Salgados = só o scone), 5 detalhes;
  - 2 × Nó de cardamomo = €5,60, 12 = €33,60, revisão bloqueada sem horário, resumo;
  - remover / vazio, voltar/avançar, sem NaN;
  - foco visível em controle, alt em todas as imagens;
  - sem overflow em 1440/390/768;
  - reduced motion, nenhuma requisição externa, nenhum erro de JS.
- Depois de revisar, o foco vai para o resumo (`order-summary`) nos 3 viewports, sem overflow horizontal.
- Capturas revisadas em `evidence-r1/`:
  - desktop: encomenda com resumo;
  - tablet: fornada e home;
  - mobile: detalhe com o aviso flutuante no topo.
- Nenhuma regressão observada.
- Não reemiti o registro `web-delivery` para r1. O de R0 continua válido apenas para o hash de r0.

## Limitações remanescentes
- No desktop, o resumo ainda fica parcialmente sob o menu fixo quando a janela rola até ele com pouco conteúdo. O `scroll-margin` de 84px ajuda, mas a captura full-page mostra o menu sobreposto, porque é um artefato da captura de página inteira com o topo fixo.
- No tablet, "Nó de cardamomo" quebra em duas linhas no cartão de destaque de 3 colunas (aceitável, mas desalinha levemente as alturas).
- Revisão estética continua sendo autorrevisão; não houve revisão humana nem leitor de tela.
