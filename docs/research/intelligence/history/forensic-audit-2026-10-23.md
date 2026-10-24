> **ARQUIVO HISTÓRICO, NÃO CANÔNICO.** Documento preservado para rastreabilidade da pesquisa; seus estados, procedimentos, links e permissões não constituem instruções atuais. Consulte [STATUS v0.3](../STATUS.md), [arquitetura atual proposta](../architecture-v0.3.md) e [matriz de aceitação](../acceptance-v0.3.md). Nenhum acesso a provedores ou merge é autorizado por este documento.

# Auditoria independente do PR #18 · Design, lacunas e efeitos colaterais · 2026-10-23

**Tipo:** revisão crítica adicional, não aceite.  
**Status:** `AUDIT_COMPLETED_WITH_FINDINGS / GATE_0_NOT_PASSED / IMPLEMENTATION_BLOCKED`.  
**Objeto congelado para auditoria:** PR #18 no commit `143c9ebce1d19ac93459e6371ddcfcef2626d258`, anterior a este relatório. Base `main` `fb7f794ca2c51c2752afde5f907bd2866c9d1f25`; PR #17 independente.  
**Método:** leitura cruzada dos oito arquivos documentais do PR, contratos normativos relevantes e histórico de validação, verificação automática de links/tabelas/números do PR, inspeção do diff e checks de GitHub; verificação externa limitada às políticas oficiais YouTube/TikTok/Meta citadas.  
**Limite:** revisão documental e estática; não foram executados protótipo, APIs com credenciais, validações de schema v0.2, Monte Carlo da nova capacidade, testes de segurança ou revisão jurídica. Não é possível garantir ausência de qualquer bug futuro somente pela inspeção de documentos.

## 1. Veredicto independente

**A arquitetura macro é compatível em princípio com a AI Creative Skill; a implementação proposta não está pronta.** Foram identificados **4 achados P0, 7 P1 e 5 P2** na especificação e na estratégia de integração. Esta auditoria não altera os documentos v0.1/v0.2 preexistentes; recomenda um novo candidato documental v0.3 somente após a análise das decisões P0.

A avaliação anterior focou coerência de owners e contratos, mas deixou passar um **bloqueio de direitos sobre métricas derivadas** que impacta diretamente o vertical slice YouTube/vidIQ, além de lacunas de lifecycle, validação, segurança, estatística e inconsistências concretas da documentação.

### P0: impedimentos materiais antes de implementar

| ID | Achado e evidência | Consequência / correção necessária |
|---|---|---|
| A18-P0-01 | **YouTube Data API não concede uso geral para agregação e métricas derivadas.** Política oficial YouTube API Services III.E.2 proíbe agregação fora de situações delimitadas; III.E.4.h proíbe usar API Data para criar métricas derivadas ou scores, e dá como exemplo scores baseados em views/likes. Fonte: https://developers.google.com/youtube/terms/developer-policies (consultada 2026-10-23). Nossa v0.2 §5 e Gate 1 planejam outlier ratio, velocity, engagement e benchmarks de vídeos de terceiros a partir da API oficial. | **Substituir a premissa “YouTube Data API → algoritmo próprio de outliers” por dois caminhos:** (A) consulta/exibição de dados e ordenações permitidas, sem cálculo/armazenamento/agrupamento não autorizado; (B) **analytics derivados somente sobre fonte/licença/dataset explicitamente permitido para esse uso**, ou autorização formal aplicável. Validação jurídica/contratual por operação obrigatória. Não concluir que todo cálculo matemático ou acesso comercial é permitido porque o endpoint responde. |
| A18-P0-02 | **Histórico para concorrentes e watchlists enfrenta regras específicas de retenção, audiovisual e derivação.** YouTube III.E.4 limita Non-Authorized Data (inclusive estatísticas públicas) a no máximo 30 dias e prevê delete/refresh; III.E.1 restringe download/armazenamento audiovisual sem autorização. §6.3 da v0.2 apenas diz “snapshots permitidos” sem especificar origem, transformação e eliminação de derivados. | Implementar uma matriz `operation × source × data_field × purpose × transform × store × retain × redistribute` com avaliações separadas; negar derivação/processamento quando desconhecidos; TTL, backup/log, propagação de revogação, eliminação e política de export antes do motor histórico. Não inferir que renovar cache automaticamente autoriza séries históricas de métricas transformadas. |
| A18-P0-03 | **Contrato de pesquisa proposto como implementável sem executor canônico comprovado.** `RESEARCH_EVIDENCE_SYNTHESIS` define `research_execution` como *contrato metodológico em Markdown*; há modelos executáveis para Web/media/shape, mas nenhum executor/schema de pesquisa implementado ou testado foi demonstrado no PR. A v0.2 §§4.1–4.5 trata `work_id`, `research_execution_id`, Evidence Record e envelope como operacionalmente disponíveis. | Verificar separadamente **documented / schema executable / runtime / host tested** por campo; definir o primeiro adapter/DTO serializável sem duplicar owners. Provar serialização, erros, versionamento, dependências, replay/recovery e compatibilidade com a skill antes de prometer integração “nativa”. |
| A18-P0-04 | **Permissões de fonte devem preceder até o experimento de derivação.** Gate 1 da v0.2 sugere YouTube para testar “métricas reproduzíveis e ranking”, mas política real pode permitir consulta sem permitir transformar a mesma saída no score planejado. Não existe autorização de acesso e uso validada. | Separar `G0-data-feasibility` (documentação + revisão de direitos + finalidade) de `G1-read-only canary`; realizar testes analíticos matemáticos **somente com fixtures sintéticas** até ter dataset autorizado. Trocar estratégia caso a finalidade comercial não tenha caminho licenciado. |

### P1: lacunas de alto risco que já exigem reparo de especificação

| ID | Achado e evidência | Risco / reparo |
|---|---|---|
| A18-P1-01 | **Inconsistência da v0.2 no próprio fluxograma:** §3.1 ainda mostra `Research Request (proposta v0.1)` e `Research Result: COMPLETO / PARCIAL / BLOQUEADO`, enquanto §4.5 mantém `COMPLETE / PARTIAL / INSUFFICIENT_EVIDENCE / BLOCKED`. | Ambiguidade de tradução/status e potencial segundo contrato na implementação. Atualizar fluxograma para `intelligence_query` acoplado ao `research_execution` com estado canônico único. |
| A18-P1-02 | **Demonstrativo de entrada contém `research_execution_id` antes da execução.** Não diferencia ID de correlação/solicitação de ID de execução efetivamente materializada; conflita com exceções e lifecycle. | Definir criação do ID, estado pré-execução, retries, tentativa de fonte e idempotência; não pressupor que um campo YAML prova consistência transacional. |
| A18-P1-03 | **Amostragem e validade estatística insuficientemente especificadas.** `outlier ratio` depende de coorte, idade, tamanho mínimo, plataforma, Shorts/long, distribuição com cauda pesada e dados faltantes; busca `search.list` é filtro/ranqueamento da própria plataforma, não amostra representativa. | Definir eligibility/cohort, semântica de população acessível, amostragem enviesada, ties, censura de dados, incerteza e confiabilidade do top-k. Testar Simpson's paradox, seleção de destaque e missing-not-at-random. Sem população definível, não emitir “top nacional”. |
| A18-P1-04 | **Superfície de segurança ausente do plano de testes:** acesso a URLs externas pode criar SSRF, redirect em rede interna, DNS rebinding, exfiltração, HTML/CSV injection, arquivo grande/bomba, path traversal e exploração de CLI; considerar segredos em traces/logs. | Threat model por fronteira trust `user input → adapter → remote content → store → model → export`; fuzz negativo e testes de política de rede, limite de payload, tokens/redaction e isolamento por projeto. Não confiar apenas no teste de prompt injection textual RES-15. |
| A18-P1-05 | **Versionamento e propagação de direitos:** o plano menciona invalidação de cache, mas não explicita como remover derivados, relatórios, índices de busca/embeddings, backups e históricos dependentes de conteúdo cuja licença expirou. | Grafo de linhagem / políticas por registro, operações delete/update, reprocessamento, storage no-op, redaction de outputs e prova de invalidação cascata. |
| A18-P1-06 | **Escopo real do MVP / UX host:** “skill + biblioteca Python + CLI local” exige host com execução e rede; não há teste demonstrando que o ChatGPT cotidiano carrega/roda tais scripts. | Separar engine library, host adapter, distribuição e direitos. Escolher primeiro host alvo e publicar matriz `CAN_INVOKE / CAN_NETWORK / CAN_PERSIST / CAN_AUTH`; em host incompatível indicar `BLOCKED`, sem simular execução. |
| A18-P1-07 | **Cobertura das APIs e quotas não dimensionadas.** YouTube `search.list` documenta hoje um bucket padrão de 100 chamadas/dia (1 unidade por chamada), com páginas adicionais consumindo chamadas; acesso a dados de audiência por país continua indisponível em pesquisa pública geral. Fonte: https://developers.google.com/youtube/data/reference/rest/v3/search/list e https://developers.google.com/youtube/data/determine_quota_cost. | Calcular orçamento de chamadas, paginação, tempo, utilidade e políticas antes do canary; diferenciar bucket de search dos demais. Testar cobertura por fonte; não assumir que “gratuito” significa volume adequado ou todo produto/mercado. |

### P2: defeitos documentais e refinamentos comprovados

| ID | Achado e evidência | Correção |
|---|---|---|
| A18-P2-01 | **Tabela Markdown quebrada** em `acceptance-and-validation-v0.2.md` entre INT-26 (linha 43) e INT-27 (linha 45): linha em branco divide o bloco de tabela, deixando INT-27..INT-35 fora da mesma tabela em alguns renderizadores. | Corrigir na próxima versão documental e adicionar smoke de renderização/linters a documentos relevantes. |
| A18-P2-02 | **Referências historicamente ultrapassadas**: `architecture-preimplementation-v0.2.md` linha 398 aponta para a matriz v0.1 (26 casos), embora a v0.2 (35 casos) seja atual; adendos v0.1 continuam dizendo INT-01..26, sem um aviso local de supersessão. | Atualizar links e seção “status atual”, sem modificar snapshots históricos sem necessidade; resolver via índice ou v0.3 consolidada. |
| A18-P2-03 | **Gates e IDs ainda não mapeiam todos os contratos normativos** de execução: `PAID_RESEARCH` permanece `LATER`; `SOURCE_OUTCOME` em Markdown não é parser/schema implementado; `RESEARCH_REPORT` não está no shape checker. | Registrar a diferença entre documentação, runtime e aceitação, com owner e custo por remediação. |
| A18-P2-04 | **Sem teste de comparabilidade do output do próprio agente**: INT/CR futuros não fixam ainda protocolo de avaliadores cegos, metadados de contexto, versões, causalidade ou armazenamento permitido de evidência de teste. | Definir protocolo reprodutível de teste humano/agent, ablações, diversidade sem novelty obrigatória e não atribuir causalidade a mudança simultânea de modelo/dados. |
| A18-P2-05 | **Diferença entre verificações de CI e validade do novo desenho**: os checks do PR atual (“Boundary hardening candidate” e “Immutable V2.5 integrity”) passaram, mas só cobrem código existente; o diff do PR #18 é exclusivamente documental, oito arquivos `docs/research/intelligence/`. | Registrar `NO_EXECUTABLE_REGRESSION_INTRODUCED_BY_PR` como inferência fundada no diff, **não** `NEW_CAPABILITY_TESTED`. Não promover prontidão por CI verde. |

## 2. Não regressões e efeitos colaterais: resultado limitado, mas verificável

**Comparação real do PR:** 8 arquivos adicionados e **nenhum** em `src/`, `tests/`, `validation/`, `SKILL.md`, `packaging/` ou `.github/workflows/`; `main` permanecia em `fb7f794ca2` e PR #17 não foi modificado na revisão. Portanto **o PR #18 não altera diretamente o comportamento executável da skill atual**. Seu risco de regressão é **indireto e futuro**: reimplementação que duplique estado, trate métrica ilícita como válida, altere autoridades, use cache proibido ou execute fluxo fora do host correto.

**Checks observados:** 2 checks de código concluídos com sucesso, referentes a V2.5 integrity e boundary hardening. **Nenhum** executou os 35 testes INT, 24 RES, 4 CR ou novos cenários de licenciamento, porque não existe implementação de inteligência. Não chamar isso de prova de Gate 0 aprovado.

## 3. Plano de reestruturação exigido (não implementado nesta auditoria)

**Primeiro, não começar pelo algoritmo YouTube de outlier.** Reavaliar três caminhos, sem preferência antes das evidências:
- **Caminho A:** MVP de **pesquisa read-only** que só usa/exibe dados e ordenações oficialmente permitidos, com direitos demonstrados e sem derivação proibida.
- **Caminho B:** Motor de performance/outlier sobre **dados próprios ou dataset de terceiros cujo contrato permita expressamente métricas derivadas, comparação, histórico e uso comercial**. Checar separadamente termos do próprio produtor de conteúdo/plataforma e sublicença.
- **Caminho C:** Começar com Meta/TikTok EU para **descoberta de anúncios e padrões qualitativos**, se API/autorizações permitirem. Isso não resolve automaticamente medição de viralidade nem US/BR.

**Antes de selecionar:** fonte × operação × região × finalidade × fields × retention × transformations × consent. Se a licença não permitir a transformação, resposta pode entregar dados brutos limitados ou `INSUFFICIENT_EVIDENCE`; não fazer cálculo “fora da API” para disfarçar.

**Depois da decisão sobre fonte:** corrigir fluxograma, contrato canônico e serialização, política de persistência/derivados, threat model, métricas/comparabilidade, teste negativo, orçamento de quota e host canary. A primeira versão implementada será um vertical slice e não sistema de monitoramento global.

## 4. Novos testes propostos para futura matriz de aceite

| ID | Caso | Aceite |
|---|---|---|
| AUD-01 | API de leitura disponível, mas política proíbe derived metric | Rejeitar `outlier_ratio`, `engagement_score` e ranking derivado; consulta permitida, se existir, permanece limitada |
| AUD-02 | Cache de estatísticas de terceiro a 29/30/31 dias | Respeitar delete/refresh e proibir uso derivado não autorizado |
| AUD-03 | Fonte permite consulta, mas veda embedding/derivação/republicação | Gate granular por ação e campo, com dados transitórios apenas quando uso permitido |
| AUD-04 | Usuário escolhe múltiplos canais; origem do dado não admite agregação | Não combinar dados indevidamente, mesmo se matematicamente calculável |
| AUD-05 | A fonte só permite video search e ranking do provider | Usar apenas operação autorizada, com descrição fiel da origem |
| AUD-06 | Mutação de parser inverte `UNKNOWN`→0 | Teste de mutação detecta violação e interrompe análise |
| AUD-07 | URL de post controla redirecionamento para IP interno/metadata | Bloquear SSRF, redirects indevidos e acesso fora do allowlist |
| AUD-08 | Token aparece em exception, trace, cache ou fixture | Redação e leak test em logs e reports |
| AUD-09 | Dados ligados a fonte revogada permanecem em índices/derivados | Propagação de delete/invalidations verificada |
| AUD-10 | Query obtém `search.list` e tenta mais de 100 buscas no dia (quota padrão) | Quota preflight, fallback legítimo sem alegar pesquisa exaustiva |
| AUD-11 | População incompleta/seleção enviesada com top-k estável por acaso | Recusar “top nacional” e preservar universo observado |
| AUD-12 | Execução de Research em host sem runtime nem rede | Não simular coleta, reportar limitação, preservar boundary |
| AUD-13 | Fluxograma usa estados em português e método usa enum em inglês | Adaptador normaliza só alias **formalmente declarado**, sem inventar equivalência |
| AUD-14 | Vários resultados do mesmo conteúdo mas uma única origem | Dedup com `independence_key`; não contar evidência múltipla |
| AUD-15 | Canal pequeno/Shorts/longform misturados, janela irregular | Coortes explícitas, não estimar outlier não suportado |
| AUD-16 | Ensaios de Monte Carlo retornam zero falhas, porém evento de segurança raro está ausente | Não concluir risco zero, acrescentar teste focado e limite estatístico |

Todos **NOT_RUN**, meros casos de projeto. Não usar a existência de ID como evidência de execução. Integração ao `validation/scenarios/register.json` só depois de implementar e aprovar o contrato.

## 5. Requisitos para uma nova aprovação de Gate 0

`GATE_0 = FAIL_FOR_IMPLEMENTATION` até demonstrar:

1. Política das fontes escolhidas autoriza **explicitamente** não só consulta, mas os *usos pretendidos* dos dados (métrica derivada, comparação entre criadores, histórico, análise comercial, relatório).
2. Conexão entre método normativo descrito e executor/DTO/schema que realmente existe, sem segundo motor de governança.
3. Política testável de `processing/storage/derived data` + eliminação + segregação + logs/backup.
4. Contratos de tempo/geo/identidade/metric+cohort com saída `UNKNOWN` e `INSUFFICIENT_EVIDENCE` válida.
5. Host alvo, quota/custo, testes adversariais e critérios de sucesso definidos antes do primeiro canary.

**Resultado final desta auditoria:** existem lacunas materiais; não alegar verificação completa de todas as futuras regressões ou inexistência de bugs. O próximo trabalho deve ser resolver as restrições da fonte e contratos de execução, e não dar start automaticamente no protótipo de outliers. O PR #18 permanece DRAFT.
