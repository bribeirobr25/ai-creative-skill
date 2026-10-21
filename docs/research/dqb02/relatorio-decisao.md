# DQB-02 — Relatório de decisão

Data: 21/10/2026. Estado: **8 execuções concluídas (16 entregas navegáveis); `AWAITING_HUMAN_REVIEW`.**
Decisão formal pelo protocolo congelado: **`INCONCLUSIVE — MORE EVIDENCE REQUIRED`** (sem revisão humana).
Leitura exploratória da coordenação: a candidata **foi aplicada, custou mais e não produziu diferença visual
observável** em relação à baseline. Se as revisões humanas confirmarem, o rótulo esperado é `REVISE CANDIDATE`.

> A análise abaixo é da coordenação, que conhecia as condições: exploratória, não cega e não independente.
> Revisores humanos devem avaliar os pacotes cegos **antes** de ler este relatório.

## 1. O que foi executado

| | B1 Miolo (micro-padaria) | B2 Tábua (sauna no píer) |
|---|---|---|
| Condição A (V2.5 `39a0bfa`) | m58, m50 | t48, t94 |
| Condição B (candidata `2cdc46b`) | m13, m31 | t19, t92 |

- Mesmo host e modelo herdado, contextos novos e isolados por instrução, prompt idêntico; a única diferença
  nas árvores entregues é o Web Experience profile (verificado por hash).
- Mesmos materiais: briefing, 14/19 fotos do Commons com licença por arquivo, seis fontes OFL locais e
  seis capturas de referência com descrições neutras. Nenhum executor alterou pixels (verificado por hash).
- R0: primeira entrega autônoma. R1: uma única autorrevisão com instrução genérica e idêntica, sem achados
  da coordenação. Todas as 16 entregas foram congeladas com SHA-256 por arquivo antes de qualquer revisão.

## 2. A intervenção foi aplicada? Sim.

As quatro execuções B registraram explicitamente o que a candidata pede no FAST 3: uma decisão de
composição, uma consequência observável em desktop/mobile e um tradeoff. Nenhuma execução A registrou
tradeoff. Exemplos (registros dos executores):

- m13 (B): fotos em arco de "boca de forno" em todo o site; tradeoff: o arco corta as bordas das fotos.
- m31 (B): régua temporal em três tempos, repetida no seletor de retirada; tradeoff: título pesa mais que a foto.
- t19 (B): título do hero em três faixas com recuo crescente, repetidas como régua; tradeoff: hero escuro reduz o "acolhedor".
- t92 (B): hero dividido, painel tipográfico de 46% e foto à direita; tradeoff: menos imersão fotográfica.

Todas as execuções, das duas condições, inspecionaram capturas próprias e corrigiram defeitos antes da
entrega. A baseline já pede QA no navegador no FAST 7; a candidata acrescenta o confronto com a intenção.

## 3. O resultado visual mudou? Não de forma observável.

**Convergência medida** (`results/convergence-r0.json`; descritores, não notas):

| Descritor | Resultado nas 8 R0 |
|---|---|
| Conjunto de fontes efetivamente renderizado | **1 único**: Fraunces (títulos) + Instrument Sans + IBM Plex Mono, nas 8 |
| Foto escolhida para o hero | B2: a mesma (escada de banho) em 4/4; B1: a mesma em 3/4 |
| Fundo da página | creme/linho quente em 8/8 (RGB 241–246 / 235–239 / 225–229) |
| Distância perceptual da abertura 1440 (dHash) | mesmo briefing, A×B: **0,357**; mesmo briefing, mesma condição: **0,381**; briefings diferentes: 0,50 |

B não se afasta de A mais do que duas execuções A se afastam entre si. Em R1 os valores praticamente não
mudam (0,358 / 0,383).

**Observações concretas por tela** (galerias `galeria-r0.html` e `galeria-r1.html`):

- **B1, home 1440:** quatro aberturas com texto à esquerda e foto de nós de cardamomo à direita; "na sexta"
  em itálico ferrugem nas quatro; recorte em arco em três (m58 e m50, de A, e m13, de B). A decisão
  composicional "declarada" por m13 é a mesma que A tomou sem a candidata.
- **B1, catálogo e encomenda:** cartões com foto, nome serifado e preço em mono; painel "Horário de retirada"
  à direita nas quatro execuções, com os horários em grade 2×2 em três delas e como régua de quatro faixas em m31 (B).
- **B2, home 1440:** a mesma foto em 4/4; duas aberturas com foto em tela cheia e texto sobreposto (t48 A,
  t19 B) e duas divididas foto/painel escuro (t94 A, t92 B). "Mergulhe." destacado em itálico nas quatro.
- **B2, planejador:** formulário à esquerda e cartão escuro com o total grande (€120) à direita nas quatro.
- **Diferenças isoladas que existem:** grade semanal de 7 colunas na programação (t94, A); barra de abas inferior
  no mobile (t19, B); régua temporal recorrente (m31, B); faixa de valor no mobile do planejador (t19 e t92, B, só em R1).
  Há elementos distintivos nas duas condições; não há padrão atribuível a B.

**Diversidade entre marcas:** Miolo e Tábua diferem em paleta, fotografia e tom de copy, mas compartilham
sistema tipográfico, estrutura de hero, navegação em pílula, rótulos "eyebrow" em mono e cartões de resumo
escuros. A identidade de cada marca vem sobretudo das fotos e da cor; a candidata não aumentou essa distância.

## 4. Defeitos e fidelidade (evidência comum, mesmas checagens para todos)

| Execução | R0 | R1 | Falha |
|---|---|---|---|
| m58 A | 48/48 | 48/48 | — |
| m50 A | 47/48 | 47/48 | overflow de 20 px a 320 px |
| m13 B | 47/48 | 47/48 | overflow de 21 px a 320 px |
| m31 B | 48/48 | 48/48 | — |
| t48 A | 42/42 | 42/42 | — |
| t94 A | 42/42 | 42/42 | — |
| t19 B | 42/42 | 42/42 | — |
| t92 B | 41/42 | 41/42 | overflow a 320 px; **piora no R1 (4 → 41 px)** |

Nenhum executor testou 320 px; essa largura estava só na evidência comum. Todas as tarefas do briefing
(filtros, totais esperados, erros, resumo, estado vazio, avisos, créditos, teclado, reduced motion, nenhuma
rede externa) passaram em 16/16 entregas.

Defeitos que só apareceram na autorrevisão R1 (relatados pelos executores e conferidos nas capturas):
- m50 (A): o catálogo do R0 saiu com os nomes dos cartões na fonte padrão do navegador (h2 sem estilo).
- t94 (A): o R0 tinha afirmações sem base no briefing ("com o mar ainda quieto", uma regra inventada),
  removidas no R1.
- Execuções B também corrigiram problemas no R1 (resumo deslocado, faixa de valor no mobile), mas nenhum
  de fidelidade.

São casos isolados numa amostra de oito; sugerem que A deixou passar mais defeitos visíveis no R0, mas não
sustentam conclusão.

## 5. Custo da candidata

| Média por execução, R0 | A | B | Diferença |
|---|---:|---:|---:|
| Tempo de relógio | 10,8 min | 14,4 min | **+33%** |
| Chamadas de ferramenta | 40 | 45,8 | +14% |
| Tokens de contexto | 180 mil | 195 mil | +8% |

Medidas a partir das notificações de cada agente; incluem latência do modelo e disputa de CPU (as duas condições
rodaram simultaneamente em cada lote). O R1 custou 3,1 min (A) e 3,6 min (B).

## 6. Diagnóstico do valor agregado

| Fonte possível de diferença | Evidência | Leitura |
|---|---|---|
| Linguagem visual escolhida | Mesma família visual nas duas condições | Determinada pelo modelo e pelo briefing, não pelo método |
| Decisão de composição | B a registrou em 4/4; o conteúdo da decisão coincide com o que A fez espontaneamente | A candidata torna a decisão explícita, mas não a muda |
| Uso das referências | Quase nenhum nas duas condições; dois executores citaram ter olhado uma captura | O passo "aceitar referências por dimensão" não teve efeito observável |
| Tipografia | Trio idêntico em 8/8 | Forte viés do modelo; a ordem do pacote de fontes é um confundidor possível |
| Coordenação de imagens | Mesma foto de hero na maioria | Escolha dominada pela foto mais "icônica" do conjunto |
| Crítica renderizada | Todos corrigiram defeitos antes de entregar; B um pouco mais, por autorrelato | Ganho possível em prevenção de defeitos, não demonstrado |
| Comportamento do agente | Variação dentro da condição ≈ variação entre condições | Ruído de amostragem domina o sinal |

## 7. Recomendação

**Formal: `INCONCLUSIVE — MORE EVIDENCE REQUIRED`**, porque não há revisão humana. Os pacotes cegos estão prontos.

**Exploratória: inclinação para `REVISE CANDIDATE`.** A candidata é barata, compatível com o contrato
existente e foi seguida, mas pede ao agente que **justifique** uma escolha, não que **considere
alternativas**. O agente escolhe o próprio padrão e o racionaliza. A distância medida não mudou.

Propostas para a próxima rodada (testes de isolamento, não mudanças já recomendadas):

1. **Divergência antes da escolha:** no FAST 3, esboçar duas ou três direções contrastantes por escrito
   (estrutura do hero, sistema tipográfico, papel da foto) e escolher uma contra o briefing. Testar contra B atual.
2. **Referências operantes:** em vez de "consultar se útil", pedir que a direção cite qual princípio de qual
   referência foi aceito e o que foi rejeitado. Hoje o passo é ignorado.
3. **Controle de confundidores:** embaralhar a ordem das famílias no pacote de fontes entre execuções e medir
   se o trio idêntico persiste.
4. **Manter do FAST 7 apenas o que é verificável:** larguras extremas (320 px) e tarefas críticas entram na
   autoverificação; a crítica estética por si só não mostrou efeito.

Não recomendamos merge, release nem novas instruções na candidata antes das revisões humanas.

## 8. Limites

- Amostra de 2 execuções por condição e briefing; não é prova estatística.
- Isolamento por instrução e diretório, não sandbox: um executor (t92) relatou que um arquivo temporário seu,
  fora do diretório da execução, foi sobrescrito por outro processo; ele recriou o script no próprio diretório
  e declarou não ter lido outras execuções.
- Tempos de trabalho "ativo" são autorrelatos; os tempos de relógio vêm das notificações e incluem latência.
- O executor de B vê o cabeçalho "EXPERIMENTAL CANDIDATE" no profile; isso faz parte do diff testado.
- Toda a análise estética desta página é da coordenação. Não há aprovação profissional nem comparação com a Higgsfield.
- Desvios e emendas do protocolo estão em `emendas.md`.
