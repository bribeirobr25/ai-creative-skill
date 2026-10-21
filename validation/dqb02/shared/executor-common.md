# Instrução comum de execução — DQB-02

Você é o executor de **uma** execução isolada. Todo o seu material está no diretório
de trabalho que lhe foi atribuído (`$RUN`). Trabalhe somente nele.

## O que você recebe em `$RUN`

- `briefing.md`: briefing fixo da marca fictícia. Siga-o integralmente.
- `rubric.md`: critérios pelos quais o resultado será avaliado.
- `assets/`, `fonts/`, `references/`: materiais comuns.
- `ai-creative-skill/`: a metodologia AI Creative Skill que você deve aplicar. Comece
  por `ai-creative-skill/SKILL.md` e carregue as referências que o próprio método indicar
  para um pedido de website (`WEB_PREVIEW`). Aplique o método tal como está escrito;
  não acrescente regras de outras fontes.

## Pedido

"Crie o website descrito em `briefing.md`, com acabamento visual profissional, usando os
materiais fornecidos. Entregue uma versão navegável local."

## Regras de isolamento e paridade

- Não leia nada fora de `$RUN`: outras execuções, branches, relatórios, histórico Git,
  outros diretórios do repositório ou da máquina. Não use `git`.
- Não acesse a internet (nada de WebSearch, WebFetch, curl ou CDN). As referências
  visuais permitidas são somente as de `references/`.
- Não carregue skills do host nem guias de design externos. A única metodologia é
  `ai-creative-skill/`.
- Não gere imagens, não edite pixels das fotos, não introduza outras imagens que
  representem produto ou local. Ícones ou ornamentos simples feitos por você, em SVG,
  são permitidos.
- Nenhuma publicação, deploy, serviço pago ou envio externo.

## Ferramentas disponíveis (iguais para todas as execuções)

- Arquivos e shell no diretório `$RUN`.
- Python 3 com Playwright e Chromium já instalados, para abrir o site no navegador e
  tirar capturas, se o seu método pedir verificação no navegador. Exemplo mínimo:
  `python3 -c "from playwright.sync_api import sync_playwright as p; ..."` com
  `page.goto('file://' + caminho_absoluto)`. Você pode ver as capturas abrindo os
  arquivos de imagem.
- `jsonschema` e `beautifulsoup4` disponíveis para os scripts opcionais do método.

## Entrega R0

- Site em `$RUN/r0/` com `index.html` e todos os recursos locais (copie `assets/` e, se
  usar, `fonts/` para dentro de `r0/`). HTML/CSS/JS sem framework, sem dependências e
  sem build. Rotas por hash ou páginas estáticas.
- `$RUN/execution.md` (fora do site) com: início e fim em UTC; arquivos do método que você
  efetivamente leu (com trechos, se a leitura foi parcial); decisões de direção;
  verificações realizadas e seus resultados; limitações conhecidas.
- Opcional: registro de entrega do método (por exemplo `web-delivery-r0.json`) e
  evidências de QA em `$RUN/evidence-r0/`.
- Limite: **30 minutos** de trabalho ativo para o R0, incluindo leitura do método,
  implementação e verificações internas que o método pedir. Não há prêmio por rapidez.
- Ao terminar, **não modifique mais `r0/`**. Responda com o caminho, o tempo
  aproximado e as limitações. Aguarde: pode haver uma única rodada de revisão posterior.
