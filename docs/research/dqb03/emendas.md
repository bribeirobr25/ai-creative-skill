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
