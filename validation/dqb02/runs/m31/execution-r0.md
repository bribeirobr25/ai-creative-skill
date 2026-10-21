# Execução m31 · R0

- Início (UTC): 2026-10-20T23:54:42Z
- Fim (UTC): 2026-10-21T00:05:33Z
- Tempo ativo aproximado: ~11 minutos (dentro do limite de 30)
- Entrega: `/tmp/dqb/runs/m31/r0/index.html` (abrir via `file://`, sem servidor). Arquivos: `index.html`, `style.css`, `app.js`, `data.js`, `assets/` (14 fotos + credits.json), `fonts/` (pacote OFL comum).

## Arquivos do método lidos

- `ai-creative-skill/SKILL.md`: inteiro.
- `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`: inteiro. É o perfil indicado pelo SKILL.md para `WEB_PREVIEW`.
- `references/AI_Creative_Skill_V2.5_Integration_Manifest.md`: inteiro.
- `web/README_PTBR.md` e `web/docs/DELTA_AND_GATES.md`: inteiros. São os documentos de apoio citados pelo perfil.
- `references/AI_Creative_Skill_Deliverable_Completeness_Catalog_Pre-v0.1-V2.4-CANDIDATE.md`: leitura parcial, só os primeiros ~2.500 caracteres (§1, sequência de execução, e o início do §2 com CHARACTER_BIBLE). Não encontrei contrato específico de website no trecho lido e não li o restante.
- `web/schemas/web_delivery_v0.2.schema.json`: lido via script, nas partes necessárias para preencher o registro.
- `web/runtime/validate.py`: leitura parcial (linhas 1–60 e as funções `build_hash` e de checks), para entender as regras de validação.
- `scripts/creative_web.py`: só o cabeçalho e o `--help`.
- Não li: o manifesto V2.4, Architecture, Runtime Activation, Execution Contracts, Specialist Method System e os demais métodos. O SKILL.md manda carregá-los apenas quando forem relevantes, e para este pedido não eram (sem execução paga, sem estado persistente, sem handoff).

## Roteamento e brief (método)

- Rota `WEB_PREVIEW`, modo FAST e `MANUAL_SPEC_GUIDED`. O site foi construído à mão com as ferramentas do host, sem módulo automático.
- WEB_BRIEF: fatos vêm do briefing e do credits.json. Desconhecidos: ingredientes, alérgenos, endereço exato, peso e tamanho. Ação principal: "Ver a fornada" → adicionar → revisar encomenda.
- Sem pesquisa externa: o isolamento proíbe e o briefing é suficiente. As capturas em `references/` não foram usadas como modelo, e nenhuma trade dress foi herdada.

## Decisões de direção (WEB_DIRECTION)

- **Ideia:** "ficha da fornada", ou seja, o tempo entre sexta e sábado como fio condutor.
- **Decisão de composição:** uma régua temporal em três tempos (Até sexta, 18h · Madrugada de sábado · Sábado, 8h–12h). Os pontos vão de massa crua (creme) a brasa (terracota). A mesma lógica volta no seletor de retirada, desenhado como régua de quatro faixas com escala 8h–12h.
- **Consequência observável:** no desktop, a régua é horizontal sob o hero. No mobile, vira uma linha do tempo vertical e os horários passam a uma grade 2×2.
- **Tradeoff:** na dobra do desktop o título tipográfico grande tem mais peso que a fotografia (a foto ocupa cerca de 5/12).
- **Paleta:** farinha `#F5EEE1`, papel, miolo `#F0D9A8`, crosta `#7E4420`, brasa `#A9441D` (CTA) e forno `#2A1C13` (texto e rodapé).
- **Tipografia:** Fraunces para títulos (itálico em "começa na sexta." e na assinatura), Instrument Sans para texto e IBM Plex Mono para horários, preços e rótulos. A mono funciona como "etiqueta de padaria".
- **Wordmark:** "miolo" em Fraunces minúscula, cor crosta, com a assinatura em itálico ao lado no desktop.
- **Imagens:** sem edição de pixels, com `object-fit: cover` e `object-position` definido por foto. No hero vão os nós sob o pano (massa "descansando"). O nó de cardamomo é o destaque da home. No catálogo, os dois primeiros cartões são maiores para criar ritmo.
- **Fidelidade:** o aviso do sorvete aparece no cartão ("Sorvete da foto não acompanha.") e no detalhe, em nota junto à foto ("Na foto, a fatia aparece com uma bola de sorvete. O sorvete não acompanha o produto."). O aviso de alérgenos está em todo detalhe. O aviso de protótipo aparece no rodapé, na encomenda (cheia e vazia) e no resumo. Créditos completos (autor, licença com link e fonte) ficam em `#/creditos`. O site não tem escassez, depoimentos nem alegações sobre ingredientes.

## Funcionamento

- **Rotas por hash:** `#/`, `#/fornada`, `#/fornada/doces`, `#/fornada/salgados`, `#/produto/<id>`, `#/encomenda`, `#/creditos`. Há também uma página para rota inexistente.
- **Encomenda:** guardada em `sessionStorage` (local) e protegida por try/catch. Quantidade inteira de 1 a 12, com clamp em blur/change. Botões ± ficam desabilitados nos limites. O horário é obrigatório: sem ele, "Revisar encomenda" mostra um erro e leva o foco aos horários. O resumo é invalidado quando algo muda.
- Todos os `data-testid` pedidos estão presentes.

## Verificações (método passo 7)

- **Playwright/Chromium headless via `file://`, 58/58 PASS** (`evidence-r0/qa-results.json`):
  - sem overflow horizontal em home, fornada e encomenda, nos tamanhos 1440×900, 390×844 e 768×1024;
  - textos obrigatórios, testids, CTA levando a `#/fornada`, filtros (Salgados retorna só o scone, Doces 4, Todos 5);
  - detalhe dos 5 produtos com aviso de alérgenos e controles, aviso do sorvete, estado vazio;
  - 2 nós = €5,60;
  - revisão bloqueada sem horário, 4 horários;
  - quantidades 0, −5, 99, "e" e 3.7 viram 1, 1, 12, 1 e 3, sem NaN nem valor negativo;
  - resumo com total e horário, voltar/avançar do navegador, remover levando ao estado vazio, 14 créditos;
  - skip link no primeiro Tab, outline de foco, `alt` em todas as imagens;
  - reduced motion desativa a animação;
  - zero requisições não-`file://`, zero erros de console.
- **Uma falha na primeira rodada:** era um artefato do teste (valor injetado sem foco, então o blur não disparava). Confirmei com digitação real que o campo volta para 1, e o teste corrigido passa.
- **Revisão visual das capturas pelo agente e correções:**
  1. A foto do hero estava altíssima no desktop, porque o atributo `height` vencia o `aspect-ratio`. Corrigido com `height:auto` e `max-height`.
  2. Havia um vão vazio sob o cartão do muffin na primeira linha do catálogo. Corrigido fazendo a imagem esticar.
  3. O título do resumo ficava sob o cabeçalho fixo no mobile. Corrigido com `scroll-margin-top`.
  - Depois disso, o QA completo foi reexecutado (58/58).
- **Registro do método:** `web-delivery-r0.json` validado com `creative_web.py validate --site-dir /tmp/dqb/runs/m31`, resultado `ok: true`. O build hash é o da função do validador. Estado `PREVIEW_REVIEWED`, não `PREVIEW_ACCEPTED` (essa aprovação é humana).
- Capturas em `evidence-r0/`: `{desktop,mobile,tablet}-{home,catalog,detail-bolo,order-summary}.png` e `mobile-summary-viewport.png`. As capturas do estado final são da última rodada de QA. A captura avulsa `mobile-summary-viewport.png` também veio depois da última correção de CSS.

## Limitações conhecidas

- O QA é crítica do próprio agente com navegador headless. Não houve avaliação humana, leitor de tela real, dispositivo físico nem Safari/Firefox.
- O preview HTTP do método (`preview start`) não foi usado: o site abre direto por `file://`.
- Os rótulos do filtro na URL (`#/fornada/doces`) usam `history.replaceState`, então a troca de filtro não cria entrada nova no histórico.
- O badge da encomenda conta unidades, não linhas.
- O wordmark é só tipográfico e provisório; o nome não foi verificado para registro (conforme o briefing).
- O Deliverable Completeness Catalog foi lido apenas parcialmente.
