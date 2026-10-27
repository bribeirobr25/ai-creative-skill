# DQB-03 — Relatório de decisão

Data: 21/10/2026. Estado: **8 execuções concluídas (16 entregas navegáveis); `AWAITING_HUMAN_REVIEW`.**
Decisão formal pelo protocolo congelado: **`INCONCLUSIVE — MORE EVIDENCE REQUIRED`** (sem revisores cegos independentes).
Leitura exploratória da coordenação: o passo "divergir e depois escolher" **foi seguido, não custou mais e quase não
mudou o resultado**. O agente produz as mesmas alternativas e escolhe a mesma direção que escolheria sem o passo.

> Análise da coordenação, que conhecia as condições: exploratória, não cega e não independente.

## 1. O que foi executado

| | D1 Della Berlin | D2 diBoaS Practice |
|---|---|---|
| A (método atual, `0f7089a`) | d79, d59 | f58, f61 |
| B (divergir e escolher, `4561218`) | d84, d11 | f50, f91 |

Marcas reais, materiais do proprietário, mesmas ferramentas, contextos isolados, R0 congelado com SHA-256 e uma R1 de
autorrevisão genérica. Novidade em relação ao DQB-02: 14 famílias de fontes, com a ordem embaralhada por execução.

## 2. A intervenção foi aplicada? Sim.

As quatro execuções B registraram três direções, por que duas perderam e um elemento emprestado. Exemplos:

| Execução | Escolhida | Perdedoras |
|---|---|---|
| d84 (Della) | "Café window & postcards", hero dividido, foto em arco | Editorial em tela cheia; álbum de adesivos |
| d11 (Della) | "Café-morning journal", hero dividido, foto em arco | Etiqueta e costura; álbum de adesivos |
| f50 (diBoaS) | "The ledger on paper", tipográfico em Fraunces | Costa em tela cheia; calendário denso escuro |
| f91 (diBoaS) | "Ledger on paper", tipográfico em Fraunces | Costa em tela cheia; "human split" |

## 3. O resultado mudou? Muito pouco.

- **As alternativas se repetem.** "Álbum de adesivos" aparece nas duas Della B; "costa em tela cheia" nas duas diBoaS B.
  As justificativas citam o briefing (legibilidade para leitor idoso, aviso da dona sobre luz dourada), e o próprio
  briefing empurra para a mesma resposta.
- **A escolhida é a mesma de A.** As execuções A, sem o passo, chegaram a "calm ledger on paper" e "rehearsal ledger"
  (diBoaS) e a "look closer" / "café paper and fabric label" (Della): mesma estrutura, mesma paleta, mesmo tom.
- **Descritores objetivos** (`results/convergence-r0.json`):

| Descritor | Resultado nas 8 R0 |
|---|---|
| Fonte do título (h1) | **Fraunces em 8/8**. Na ordem embaralhada, Fraunces nunca apareceu em primeiro (no máximo em 4º); na Della não havia recomendação de fonte. A ordem do pacote não explica a escolha |
| Fonte de apoio | Della variou (Manrope, Instrument Sans, IBM Plex Mono); diBoaS usou as fontes da marca (Inter, Space Grotesk) |
| Imagem do hero | Della: a mesma foto editorial da Croissant no café em 4/4; diBoaS: a mesma ilustração da costa em 4/4 |
| Fundo | creme/papel em 8/8 |
| Distância da abertura 1440 (dHash) | mesma marca, dentro de A: 0,332 e 0,238; dentro de B: 0,383 e 0,305; A×B: 0,333; marcas diferentes: 0,38 |

  B ficou um pouco mais variado que A nas duas marcas, mas é um par por marca e a diferença é menor que a variação
  entre marcas. No DQB-02 a distância entre briefings era 0,50; aqui as duas marcas reais ficaram mais parecidas entre
  si (creme, título serifado à esquerda, imagem à direita).
- **Arcos de novo.** Recorte em arco na abertura em 3 das 4 Della e em 1 diBoaS. No DQB-02 o proprietário pediu
  retângulo com cantos arredondados (perfil de preferências P01). O perfil não foi entregue aos executores, por
  desenho; o resultado mostra que, sem ele, o padrão volta.

## 4. Funcionamento e fidelidade

Evidência comum final (coletor com as emendas E1–E3, aplicado a todas): **16/16 entregas passam em todas as
verificações** (Della 88/88; diBoaS 42/42), incluindo preço "to be announced", nota de props, adesivos só na
Croissant, nenhum "Made in Berlin", números e avisos verbatim da diBoaS, palavras proibidas e overflow a 320 px.

Autorrevisão R1: todas mudaram algo; a maioria em responsividade e enquadramento. Um caso de fidelidade: **d79 (A)
encontrou no R1 que tinha chamado o prendedor de flor (adereço) de "flor aplicada" do Limão** e corrigiu. Nenhum
executor B encontrou erro de fidelidade.

## 5. Custo

| Média por execução | A | B |
|---|---:|---:|
| R0, tempo de relógio | 10,5 min | 9,6 min |
| R0, tokens de contexto | 182 mil | 175 mil |
| R1, tempo de relógio | 3,2 min | 3,6 min |

Diferente do DQB-02 (+33%), B não custou mais. Medidas das notificações do host, com latência e disputa de CPU.

## 6. Teste de campo do runtime 2.6 (PR #17)

Rodado nas 16 entregas reais:
- O QA da V2.5 marcaria **6 a 23 âncoras "quebradas" por site**, todas falsas (links `#/rota`). O QA 2.6 marca 0.
- O router da V2.5 recusa o pedido real usado pelos executores ("Create the website described in `brief.md`…") como
  ambíguo; o 2.6 roteia para `WEB_PREVIEW`.
- `narrow_render` (320 px) e `images_rendered` rodaram em todos; nenhum caminho absoluto apareceu nas evidências.
Nenhuma regressão encontrada. Isso sustenta o merge do #17 junto com o que o estudo pedir.

## 7. Diagnóstico

Pedir ao mesmo agente que considere alternativas e escolha **não cria diversidade**: ele gera alternativas previsíveis
e escolhe o próprio padrão, com justificativas tiradas do briefing. A escolha precisa sair do agente:

1. **Escolha pelo proprietário:** mostrar 2–3 direções curtas (texto + uma captura de abertura cada) e deixar o
   proprietário escolher antes de construir. Combina com o gate "parar e perguntar" já pedido por ele.
2. **Variantes construídas:** construir duas aberturas contrastantes de verdade e deixar o proprietário combinar
   componentes, que foi o que ele fez no DQB-02.
3. **Perfil de preferências como entrada:** testar o perfil v0.1 (sem arcos, imagens iguais na grade, etc.) como
   condição própria. Ainda não testado.

## 8. Recomendação

- **Formal:** `INCONCLUSIVE — MORE EVIDENCE REQUIRED` (sem revisores cegos).
- **Exploratória:** **não adotar B como está** (`REVISE CANDIDATE`). O ganho de diversidade foi pequeno e não mudou a
  direção escolhida. Próximo teste sugerido: gate de escolha de direção pelo proprietário (opção 1) contra A.
- **Runtime:** o #17 se comportou bem no campo; recomendamos o merge após o feedback do proprietário sobre os sites,
  como combinado.

## 9. Limites

- Duas repetições por condição e marca; não é prova estatística. Análise estética da coordenação, não cega.
- Isolamento por instrução e diretório, não sandbox.
- O ângulo da diBoaS e o texto do hero foram propostos pela coordenação a pedido do proprietário; aguardam aprovação.
- Material da Della (sites, fotos, capturas, folhas comparativas, briefing) fica fora do repositório público.
- Emendas do coletor em `emendas.md` (E1 menu móvel e logos; E2 tolerância de miniaturas; E3 rolagem das capturas).
