# DQB-03 — Emendas e desvios

- **E1 (coletor, 21/10 ~13:10 UTC):** `check_site.py` abria a navegação só por elementos visíveis; uma entrega (f91) usa
  menu recolhido no mobile e falhou em "no visible nav-how" a 390 px. O coletor passou a abrir o menu (`aria-expanded`
  com `aria-controls`, ou botão "menu") antes de clicar em `nav-*`. Na mesma emenda, imagens de logo/wordmark deixaram
  de contar no teste de "imagem minúscula/colapsada", que visa fotos colapsadas. As duas mudanças valem para todas as
  entregas; o coletor é rodado de novo em todas no fim, com a mesma versão.
- **E2 (coletor):** o teste "thumbnails in one row" exigia o mesmo `y` exato; d11 teve miniaturas na mesma linha com
  2 px de diferença (alinhamento por baseline). Tolerância de 8 px, aplicada a todas as entregas na rodada final.
- **E3 (capturas):** depois de navegar, a página mantinha a rolagem anterior e algumas capturas de estado (produto,
  como funciona, confirmações) saíam no meio ou no rodapé. As capturas passaram a rolar para o topo (páginas) ou para o
  elemento do estado (erro/confirmação) antes de fotografar. Não muda nenhuma verificação funcional; aplicado a todas as
  entregas na mesma rodada final.
- **Erro da coordenação (registrado depois):** em `assets/credits.json` da Della, `limao-open-flower.jpg` foi descrito
  como "open with applied flower clip". O objeto verde é um prendedor de cabelo (adereço), não a flor aplicada do Limão.
  A descrição chegou às 4 execuções da Della; d79 legendou o prendedor como "flor aplicada" no R0 e corrigiu no R1.
  O erro vale igualmente para A e B e não muda a comparação, mas é um defeito de material de entrada.

## E4 · Normalização de texto no coletor (22/10/2026, depois do estudo)

No teste dos 18 estilos (mesmo coletor, outra rodada), um site falhou em "hero copy preserved" porque um SVG decorativo
dentro do `h1` quebrava o `innerText` ("details\n."). O título aparecia correto na tela. A comparação de cópia passa a
colapsar espaços e quebras e a remover espaço antes de pontuação (`norm()`). Não muda nenhum resultado do DQB-03:
as 16 entregas já passavam.
