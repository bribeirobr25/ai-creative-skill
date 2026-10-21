# Execução m50 · R1 (rodada única de autorrevisão)

- Início: 2026-10-21T00:15:57Z
- Fim: 2026-10-21T00:18:30Z (aprox.)
- Tempo ativo aproximado: ~3 min
- Entrega: `/tmp/dqb/runs/m50/r1/index.html`. Foi copiada de `r0/`, que não foi alterada: os hashes de r0 são idênticos aos registrados em `execution.md`.
- Base da revisão: a rubrica (`rubric.md`) e o próprio Work Profile Web v0.2. O passo 7 dele pede QA no navegador, no mesmo build, em 1440/390 e 768 px. Não li nenhum arquivo novo do método nesta rodada.

## Problemas encontrados na revisão de r0

Fiz a revisão pelas capturas das telas que não tinha inspecionado no R0: catálogo desktop, home tablet e encomenda com resumo no desktop.

1. **Tipografia e componentes (catálogo).** No catálogo, os títulos dos cartões são `h2`. O CSS só estilizava `.card h3`, então na fornada os nomes saíam na fonte padrão do navegador: sans, negrito, sem a Fraunces e com margens grandes. Isso quebrava a família visual entre a home (onde os cartões usam `h3`) e o catálogo. Foi o defeito mais visível.
2. **Composição (catálogo, 1440 e 768).** Os 5 itens deixavam um buraco: na grade de 3 colunas, a 2ª linha tinha 2 cartões e um espaço vazio. No tablet (2 colunas), sobrava um cartão órfão.
3. **Responsividade (home em 768 px).** Os destaques (3 cartões) caíam numa grade de 2 colunas com um cartão órfão na segunda linha.
4. **Espaçamento (encomenda).** O espaço inferior ficava no bloco `.order`, antes do resumo. Por isso o resumo encostava no rodapé, sem respiro, e o vão grande ficava no lugar errado.

Também vi o cabeçalho aparecendo no meio da captura de página inteira da encomenda. Isso é artefato da captura full-page com cabeçalho `sticky`, não um defeito real. Medi depois no viewport: o topo do resumo fica 21 px abaixo do cabeçalho.

## Correções feitas (somente em r1)

- `styles.css`: `.card h2, .card h3` agora compartilham o mesmo estilo serifado. Os cartões ficaram idênticos na home e na fornada.
- Catálogo: no fim da grade entrou um bloco escuro "Como encomendar", na mesma cor noturna do "Como funciona". Ele resume os prazos (até sexta, 18h · sábado, 8h–12h · 1 a 12 por item), explica o fluxo em uma frase e leva a um link real, "Ver encomenda" (`#/encomenda`).
  - Em 3 colunas, ele fecha a 2ª linha. Em 2 colunas, ocupa o lugar do órfão. Com o filtro, completa as linhas (Doces: 4 + 1; Salgados: 1 + 1).
  - Todo o conteúdo dele vem do briefing; a informação "1 a 12" é a regra da encomenda.
- Home em 561–960 px: os destaques ficam numa grade própria de 3 colunas (`.grid--feat`), mais compacta, com preço sob o nome e sem a descrição (que continua na fornada e no detalhe). Abaixo de 560 px, volta a 1 coluna com descrição.
- Encomenda: o espaço inferior passou para `#summaryHost`, e o resumo ganhou `margin-top` de 32 px.

## O que foi preservado

Ficaram iguais a r0:
- Todo o conteúdo obrigatório, os textos e a direção (paleta, fontes, arco, faixa noturna).
- As rotas, a lógica da encomenda e todos os `data-testid`.
- `index.html` e `credits-data.js` (os hashes são idênticos aos de r0).
- O aviso do sorvete, o aviso de alérgenos e os créditos.

Nenhuma foto foi alterada.

## Verificações (BROWSER_OBSERVED, Chromium headless, `file://`)

- `evidence-r1/qa_r1.py` (o mesmo script do R0, apontado para r1): **35/35 PASS**. Resultados em `evidence-r1/qa-results.json`, capturas em `evidence-r1/`.
  - Filtros (Salgados = só o scone; a contagem ignora o bloco, que não tem `data-testid` de produto).
  - €5,60 para 2 nós de cardamomo; limites 1–12; sem NaN.
  - Horário obrigatório, resumo, remoção e estado vazio.
  - Histórico do navegador e créditos (14).
  - Sem overflow em 1440, 390 e 768 px.
  - Teclado inicial, `alt` e movimento reduzido.
  - Zero requisições externas e zero erros de console.
- Verificação extra: no mobile, depois de "Revisar encomenda", o topo do resumo fica em y=90, abaixo do cabeçalho (y=69). PASS. A captura está em `evidence-r1/mobile-summary-viewport.png`.
- Inspeção visual: catálogo desktop (fonte dos cartões corrigida, grade completa), home tablet (destaques em 3 colunas), encomenda desktop (resumo com respiro antes do rodapé) e fim do catálogo no mobile (bloco legível, botão alcançável).

## Regressões

Nenhuma encontrada nos testes acima. Riscos não verificados:
- Entre 561 e 760 px os cartões compactos dos destaques ficam estreitos. Verifiquei só a 768 px.
- O bloco "Como encomendar" usa o amarelo-gema sobre azul-noite para texto mono pequeno. O contraste é alto à vista, mas não foi medido numericamente.

Hashes de r1:
```
495c8cb49a86e1ea42572205f11bfd3ecd3b33ad81f7f9a0c92626f1effdc1f4  app.js
ff28f6b33fd011a1fa56c0a832068f0964fdfed2f807e6fcd48646396b73379e  credits-data.js
bfbd3af370a484c560d0cc7eab9ca1c16cc7667c975b989bc13c984db126a36b  index.html
81e668e1a2044d679156e4aa13e7db5f695094566a8a18b1417f1dc11ec2c94c  styles.css
```

## Limitações que continuam

As de r0 seguem valendo:
- Preview só por `file://`.
- Sem registro validado pelo schema web v0.2.
- Sem leitor de tela, dispositivo físico ou outros navegadores.
- O teclado foi testado só no início da página.
- A revisão foi autoavaliação, sem revisor independente.
