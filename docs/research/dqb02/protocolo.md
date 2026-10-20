# DQB-02 — Visual Direction Method Validation · protocolo congelado

**Congelado antes de qualquer execução**, no commit que introduz este arquivo. Mudanças
posteriores são registradas como emendas, sem reescrever esta versão.
Data: 21/10/2026. Estado: piloto controlado, exploratório; não é prova estatística.

## Pergunta

A candidata do PR #12 faz o mesmo agente produzir websites visualmente melhores na
**primeira entrega** do que o método Web Experience da V2.5?

## Versões fixadas

| Condição | Fonte da metodologia | Commit |
|---|---|---|
| A | `src/ai-creative-skill/` da baseline V2.5 (`main`) | `39a0bfa39270ea4b685b0f862e7dbf647cf81d77` |
| B | `src/ai-creative-skill/` da candidata `experiment/web-design-direction-v0-1` | `2cdc46bac6f2d9239930f0abf915853816338234` |

Única diferença entre as árvores entregues: `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`
(cabeçalho experimental + FAST 3 + FAST 7). O README da candidata, que contém a hipótese e
o vocabulário comentado das seis famílias, **não** é entregue a nenhum executor.

## Desenho

- Dois briefings fictícios de categorias diferentes, ambos congelados:
  **B1 Miolo** (micro-padaria; catálogo, detalhe, encomenda simulada, horário de retirada) e
  **B2 Tábua** (sauna no píer; programação com filtro, detalhe de sessão, planejador local).
- Duas condições × duas repetições independentes por briefing = **8 execuções**.
  Cada execução: R0 obrigatório e uma única rodada R1.
- Executores: subagentes do mesmo host, com a mesma configuração de modelo herdada e sem
  override. Contextos limpos, sem histórico da conversa coordenadora. Isolamento por
  instrução e diretório (filesystem compartilhado, não sandbox físico).
- Identificadores neutros por execução; o mapeamento para condições fica com a coordenação.

## Materiais comuns (idênticos em todas as execuções)

- Briefing do respectivo caso, `executor-common.md` e `rubric.md`.
- Fotos: B1 com 14 imagens de panificação caseira (CC0, CC BY 4.0, CC BY-SA 4.0) e B2 com
  19 imagens de porto e litoral (CC0), todas do mesmo autor no Wikimedia Commons, com
  autor, licença, fonte e SHA-256 em `credits.json`. Escolhidas por coerência de sessão
  e por não exibirem marcas. Usadas sem alteração de pixels.
- Fontes: seis famílias SIL OFL hospedadas localmente (Fraunces, Newsreader, Inter,
  Instrument Sans, Bricolage Grotesque e IBM Plex Mono); uso opcional.
- Referências: capturas das seis aberturas citadas na candidata (1440 e 390 px) com
  descrições **neutras**, sem orientações de transferência. Material de terceiros, mantido
  fora do Git público.
- Ferramentas: shell e arquivos no diretório da execução, Python + Playwright/Chromium,
  jsonschema e bs4. Sem internet, sem skills de design do host e sem geração de imagens.

## Rodadas

- **R0 (resultado principal):** primeira entrega autônoma completa, incluindo as
  verificações internas que o método da condição pedir. Teto: 30 minutos ativos,
  medidos pelo executor (UTC início e fim) e pelas notificações da coordenação. Uma vez
  entregue, R0 é congelado com hashes.
- **R1 (secundário):** a mesma instrução genérica, idêntica para todas as execuções, sem
  achados da coordenação: copiar R0 para R1, revisar a própria entrega pelo método
  atribuído e pela rubrica, corrigir o que julgar necessário em até 15 minutos ou
  registrar `NO_CHANGE` justificado. R1 mede o benefício de uma autorrevisão extra, não a
  qualidade da primeira entrega.

## Evidência comum da coordenação

Mesmo script para todas as execuções e rodadas: carregamento local, erros de script,
requisições externas, imagens decodificadas e visíveis, overflow horizontal em 1440, 768,
390 e 320 px, tarefas do briefing via `data-testid` (filtros, detalhe, adicionar, totais
esperados, erros) e reduced motion. Capturas padronizadas por estado em 1440×900 e
390×844. Testes não pontuam estética. A coordenação não envia esses resultados aos
executores antes do R1.

## Avaliação humana e regra de decisão (congelada)

- Pacote obrigatório: **quatro pares R0** (B1-rep1, B1-rep2, B2-rep1, B2-rep2), A×B com
  rótulos neutros X/Y e lado e ordem contrabalançados. Pacote R1 separado e opcional.
- Pelo menos dois revisores humanos independentes, um com experiência em UI/design.
  Avaliam antes de ler qualquer relatório; exposição prévia é registrada. Nenhum revisor é
  simulado por IA.
- Dimensões decisivas, definidas antes da execução: **Direção de arte/identidade,
  Composição/espaçamento e Tipografia/hierarquia**. As demais dimensões são registradas e
  usadas como verificação de regressão.
- Por par e dimensão: preferência X, Y ou empate, com justificativa.
- Uma dimensão conta como **vantagem de B num briefing** quando, somando os dois pares
  do briefing, nenhum revisor prefere A na maioria dos pares e pelo menos um revisor
  prefere B na maioria. Divergência entre revisores = empate naquela dimensão.
- **Regressão crítica:** Fidelidade < 3, Clareza/usabilidade < 3 ou tarefa central
  bloqueada, segundo qualquer revisor ou pela evidência comum.

| Rótulo de pesquisa | Condição |
|---|---|
| `ACCEPT FOR NEXT INTEGRATION REVIEW` | Vantagem de B em ≥ 2 das 3 dimensões decisivas nos **dois** briefings, sem regressão crítica de B |
| `REVISE CANDIDATE` | Vantagem em apenas um briefing, ou vantagem acompanhada de regressão crítica |
| `REJECT CANDIDATE` | A preferido em ≥ 2 dimensões decisivas nos dois briefings, ou B mais caro sem nenhuma vantagem |
| `INCONCLUSIVE — MORE EVIDENCE REQUIRED` | Revisão humana ausente ou incompleta, apenas um briefing executado, ou empate geral |

Sem revisões humanas, a decisão formal é `INCONCLUSIVE` e o estado é
`AWAITING_HUMAN_REVIEW`. A análise da coordenação é exploratória, não cega e não independente.

## Limites e integridade

- Sem créditos pagos, publicação, merge, release, alteração da baseline ou de hashes
  históricos. O CI de atestação V2.5 falha na branch candidata por design; isso não é mascarado.
- Inputs, R0, R1, registros dos executores e evidências preservados com hashes.
  Falhas de infraestrutura e retries registrados separadamente.
- Não comparamos com a Higgsfield; o DQB-02 mede a candidata contra a nossa baseline.
