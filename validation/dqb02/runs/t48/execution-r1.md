# Execução t48 · R1 (revisão própria, sem feedback externo)

- Início: 2026-10-21T00:29:03Z
- Fim: 2026-10-21T00:32:30Z (aprox.)
- Tempo ativo: ~4 min
- Entrega: `/tmp/dqb/runs/t48/r1/index.html` (cópia de r0 com correções); r0 não foi alterado (hashes e mtimes conferidos)
- Método aplicado: Web Experience v0.2, passo 7 (QA a partir do mesmo build, 1440/390 e 768 px, recorte de imagem, sem overflow) e rubrica `rubric.md`. Nenhum arquivo novo do método foi lido nesta rodada.

## Problemas encontrados (revisão das capturas de r0)

1. **Cards de sessão sem imagem** (Imagens/Componentes). As 3 imagens dos cards da home tinham `loading="lazy"` e apareciam brancas nas capturas de página inteira em 390 e 768. Em navegação real elas carregam ao rolar, mas o estado inicial ficava frágil e a evidência mostrava blocos vazios.
2. **Card "Sauna privativa" desproporcional em 768 px** (Responsividade/Composição). Ocupando a linha inteira em coluna, a imagem 3:2 deixava o card com cerca de 900 px de altura, um bloco vazio dominante.
3. **Rótulo do hero pouco legível no mobile** (Tipografia/Imagens). O eyebrow "Sauna a lenha · Enseada do Norte" ficava sobre a área clara e movimentada da foto, com contraste baixo.

## Correções feitas (somente em r1)

- `app.js`: removi o `loading="lazy"` das imagens dos cards de sessão (são só 3). As demais imagens lazy foram mantidas.
- `styles.css`:
  - Entre 721 e 1000 px, o card "Sauna privativa" virou horizontal (imagem 50% / texto 50%, altura mínima de 240 px). Abaixo de 720 px ele volta a ser vertical.
  - Abaixo de 720 px, o gradiente do hero fica mais escuro a partir de cerca de 48% da altura.

## Preservado

- **Conteúdo:** todo o conteúdo, a direção visual (paleta, tipografia, wordmark, ritmo de tábuas) e o desktop 1440, a não ser pelo carregamento das imagens dos cards.
- **Estrutura e comportamento:** as rotas, o filtro, o planejador e toda a instrumentação `data-testid`.
- **Textos obrigatórios:** os avisos e os créditos.
- **Arquivos inalterados:** `index.html` e `credits-data.js`.

## Regressões e verificações

- **Testes funcionais:** o mesmo script de QA de r0, apontado para r1, deu **65/65 PASS** (`evidence-r1/qa-results.json`). Cobre: valores e erros do planejador, filtro (16 / 2 horários), detalhe de sessão + voltar, ausência de overflow nas 6 rotas × 3 viewports, teclado/foco, alt, reduced motion, nenhuma requisição externa e nenhum erro de console.
- **Imagens após rolagem:** depois de rolar a home no mobile, todas as imagens carregaram, exceto uma da faixa de fotos que fica oculta no mobile (`display:none`). Isso é esperado.
- **Inspeção visual:**
  - `evidence-r1/tablet-sessions.png`: card horizontal correto.
  - `evidence-r1/mobile-sessions.png`: 3 imagens visíveis. A barra de topo sticky aparece no meio da captura do elemento; é um artefato da captura, não do layout.
  - `evidence-r1/mobile-home-fold.png`: rótulo do hero mais legível.
  - `evidence-r1/mobile-plan-error.png`: opções do select já sem corte, estado de erro correto.
- Nenhuma regressão observada.

## Limitações

- Mantêm-se as de r0: sem leitor de tela, dispositivo físico ou outros navegadores; a revisão é autoavaliação.
- Desta vez não rodei de novo o `creative_web.py audit` do método. As mudanças são só de CSS e de um atributo de imagem, e o falso positivo das âncoras `#/` seria o mesmo.
