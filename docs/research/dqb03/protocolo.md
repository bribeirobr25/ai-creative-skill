# DQB-03 — Divergent Directions Method Validation · protocolo congelado

**Congelado antes de qualquer execução**, no commit que introduz este arquivo. Mudanças posteriores são registradas como
emendas, sem reescrever esta versão. Data: 21/10/2026. Piloto controlado, exploratório; não é prova estatística.

## Pergunta

Pedir ao agente **duas ou três direções visuais contrastantes antes de escolher uma** (condição B) produz websites
visualmente melhores e mais diversos na primeira entrega do que o método atual (condição A), com marcas reais?

## Versões fixadas

| Condição | Metodologia (`src/ai-creative-skill/`) | Commit |
|---|---|---|
| A | candidata `web-runtime-2.6-v1` (PR #17), método atual | `0f7089a5b473c0d878ba1cac1efbea27a960ecf1` |
| B | A + FAST 3 "Diverge, then choose" (`experiment/web-divergent-directions-v0-1`) | `45612189bf3ce933a49a9628ee2f767cd38a67c6` |

Única diferença entre as árvores entregues: `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`
(cabeçalho experimental + FAST 3). As correções de runtime do #17 valem para as duas condições.

## Desenho

- Duas marcas reais, briefings congelados: **D1 Della Berlin** (necessaires; coleção com filtro, página por modelo com
  galeria, lista de interesse local) e **D2 diBoaS Practice** (app de prática com dinheiro de brincadeira; como funciona,
  prévia local "Your system", lista de espera local, FAQ). Ângulo da diBoaS proposto pela coordenação a pedido do
  proprietário, a partir do webapp Practice.
- 2 condições × 2 repetições por marca = **8 execuções**, cada uma com R0 e uma única R1.
- Executores: subagentes do mesmo host e modelo herdado, contextos limpos, isolamento por instrução e diretório.
  Identificadores neutros; o mapa de condições fica com a coordenação.
- **Controle de confundidor tipográfico (novo):** o pacote de fontes tem 14 famílias OFL e a ordem de listagem em
  `fonts.css`/`FONTS.md` é embaralhada por execução, com semente = id da execução. Fontes da marca diBoaS (Fraunces,
  Space Grotesk, Inter) estão no pacote e são recomendadas, não obrigatórias.

## Materiais comuns

- Briefing da marca, `executor-common.md`, `rubric.md` (mesma rubrica do DQB-01/02, traduzida).
- D1: 42 imagens fornecidas pela proprietária (fotos reais, fotos de produção, ilustração de adesivos, renders e
  editoriais gerados por IA), com EXIF removido, redimensionadas a 1800 px; uso livre aprovado pela proprietária.
- D2: 22 arquivos da biblioteca de marca do repositório público diboas-platform (logos, ilustrações do Practice, fotos).
- Sem referências visuais externas (diferença do DQB-02).
- Ferramentas: shell e arquivos no diretório da execução, Python + Playwright/Chromium, jsonschema e bs4. Sem internet,
  sem skills de design do host, sem geração de imagens.

## Rodadas

- **R0 (principal):** primeira entrega autônoma completa. Teto de 30 minutos ativos. Congelado com hashes ao terminar.
- **R1 (secundário):** instrução genérica idêntica, sem achados da coordenação; até 15 minutos ou `NO_CHANGE`.

## Evidência comum da coordenação

`tools/check_site.py` (mesmo script para todas as execuções e rodadas): carregamento local, erros de script,
requisições externas, imagens decodificadas, overflow em 1440, 768, 390 e 320 px, tarefas do briefing via `data-testid`,
regras de fidelidade verificáveis (preço não numérico, nota de props, adesivos só na Croissant, sem "Made in Berlin";
números e avisos da diBoaS, palavras proibidas), teclado e reduced motion. Capturas por estado em 1440×900, 390×844,
768 e 320. Também roda o `qa.audit` do runtime 2.6 em cada entrega, como teste de campo do #17. Testes não pontuam
estética e não são enviados aos executores antes do R1.

Descritores de convergência (exploratórios): famílias de fontes efetivamente renderizadas, imagem do hero, cor de fundo,
distância perceptual (dHash) das aberturas A×B, dentro da condição e entre marcas. Hipótese específica de B: maior
distância dentro da condição B do que dentro de A.

## Avaliação e regra de decisão (congelada)

- **Revisão do proprietário** (não cega, como no DQB-02) por folhas comparativas por tela, com rótulos A1/A2/B1/B2.
- Pacotes cegos X/Y contrabalançados ficam disponíveis para revisores independentes.
- Dimensões decisivas: Direção de arte/identidade, Composição/espaçamento, Tipografia/hierarquia.
- Regra formal igual à do DQB-02 (vantagem de B em ≥ 2 das 3 dimensões nas duas marcas, sem regressão crítica, por pelo
  menos dois revisores independentes e cegos). Sem eles, a decisão formal é `INCONCLUSIVE` e o estado é
  `AWAITING_HUMAN_REVIEW`; a leitura do proprietário e da coordenação é registrada como evidência exploratória.
- **Regressão crítica:** fidelidade (afirmação inventada, número ou aviso alterado), tarefa central bloqueada ou
  evidência comum com falha de função.

## Privacidade e limites

- Repositório público: entram protocolo, ferramentas, briefing D2, hashes, registros textuais dos executores e métricas
  agregadas. **Não entram** fotos ou sites da Della, nem capturas com material da Della; ficam no Drive. O briefing D1 é
  registrado só por hash no Git e guardado no Drive.
- Sem créditos pagos, publicação, merge ou release. PR #17 continua aberto até o fim do estudo.
