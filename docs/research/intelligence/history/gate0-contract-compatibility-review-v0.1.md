> **ARQUIVO HISTÓRICO, NÃO CANÔNICO.** Documento preservado para rastreabilidade da pesquisa; seus estados, procedimentos, links e permissões não constituem instruções atuais. Consulte [STATUS v0.3](../STATUS.md), [arquitetura atual proposta](../architecture-v0.3.md) e [matriz de aceitação](../acceptance-v0.3.md). Nenhum acesso a provedores ou merge é autorizado por este documento.

# Gate 0 · Revisão de compatibilidade de contratos · v0.1

**Data:** 2026-10-23  
**Tipo:** revisão técnica estática da proposta de inteligência, sem implementação.  
**Estado:** REVIEW COMPLETED / COMPATIBILITY CONDITIONAL / OWNER ACCEPTANCE PENDING / NOT EXECUTED.  
**Base exata:** `main` = `fb7f794ca2c51c2752afde5f907bd2866c9d1f25` (2.6.0-dev); baseline V2.5.0 = `39a0bfa39270ea4b685b0f862e7dbf647cf81d77`.  
**Branch de proposta:** `proposal/intelligence-architecture-pre-v0-1-20261023`. PR #17 de Web Runtime separado.  
**Material revisado:** os cinco documentos do PR #18, `SKILL.md`, ADR-0001/ADR-0002, Architecture Spec (§§2–7/24.1), Execution Contracts (§§2–5, 26, V2.3 handoff), Specialist Method System (§§3, 6.2–6.4, 15–17), Research Evidence Synthesis (§§3–16), Product Marketplace Intelligence, Ad/Funnel Intelligence, Calibration and Experience Memory, Deliverable Completeness contracts e metodologia de validação/Monte Carlo.

> A avaliação é de compatibilidade **documental**. Não executa código, APIs nem testes da nova capacidade; não constitui aprovação de produção, revisão jurídica, licença ou aceite formal do proprietário. Os reparos a seguir são condições da especificação de implementação, não modificações da governança canônica.

## 1. Resultado executivo

**Compatibilidade estrutural: POSSÍVEL, COM CONDIÇÕES.** O projeto já contém as camadas A–E, `RESEARCH_ONLY`, uma taxonomia de Source Outcomes, Evidence Record, HANDOFF_PACKET e controles de orçamento, liberdade criativa e validação. Nova infraestrutura cabe em Architecture §24.1 `ANALYTICS / DATA-SOURCE CONNECTORS`.

**Gate 0 documental:** análise realizada; conflitos identificados e respectivas correções propostas. **Decisão final de implementação: BLOQUEADA** até endereçar os itens G0-01..G0-05 na próxima revisão de contrato, de forma versionada. Não marcar Gate 0 como aprovado automaticamente.

### 1.1 Achados por severidade

| ID | Severidade | Achado / risco | Resolução requerida antes de código |
|---|---|---|---|
| G0-01 | BLOCKER-CONTRACT | `ResearchRequest`/`ResearchResult` v0.1 poderiam virar um novo executor de pesquisa paralelo ao `research_execution` e aos estados `COMPLETE/PARTIAL/INSUFFICIENT_EVIDENCE/BLOCKED` | Introduzir uma extensão **namespaced** de filtro/inteligência, mantendo o envelope original e suas classes de resultados; mapear IDs/estado canônicos |
| G0-02 | BLOCKER-CONTRACT | `ObservationRecord` + `source_outcomes` podem duplicar o Evidence Record, `source_outcome_ref`, provenance, freshness e os owners existentes | `MetricObservation` apenas como componente numérico de evidência, com referência ao `evidence_id` e a `research_execution_id`; nunca segunda verdade sobre fonte |
| G0-03 | BLOCKER-AUTHORITY | Contrato de paid research §4.1 é `LATER`, não há executor aprovado que vincule qualquer fonte paga à aprovação/reserva/fingerprint | MVP read-only com **zero chamadas pagas**; se houver paid connector, primeiro implementar e validar binding de execução, approval, reservation, reconciliations e retry |
| G0-04 | BLOCKER-RIGHTS | Direitos de consulta não asseguram permissão de cache, histórico, redistribuição, embeddings, vídeo ou reuso em treino | Matriz de direitos **por operação e campo**, storage default DENY/EPHEMERAL até licença confirmada; revogação/TTL/invalidação comprováveis |
| G0-05 | BLOCKER-SEMANTICS | API oferece totais atuais que podem ser indevidamente apresentados como VPH histórico, audiência local ou “top 10 nacional” | Definir métricas tipadas e base geográfica/temporal; `UNKNOWN` e impossibilidade de ranking representam saídas válidas |
| G0-06 | REFINEMENT | Termos candidatos `EXACT/BOUNDED_DISCOVERY/OPEN_EXPLORATION` poderiam virar novo enum concorrente da creative-latitude | Usar a `dimension_policy` existente como autoridade; qualquer *intent* de pesquisa é hint de seleção, não nova permissão |
| G0-07 | REFINEMENT | `CONTENT_WORK`, `CONTENT_PUBLICATION` e `ADVERTISEMENT` precisam não colidir com `concept_id`, `variant_id`, `publication_id` de performance | IDs explícitos por plataforma/ocorrência, relações evidenciadas, segmentação de domínio e namespace |
| G0-08 | REFINEMENT | Fonte com fallback semântico diferente pode satisfazer superficialmente um filtro trocando país/tempo/unidade | Capabilities por operação; incompatibilidade retorna `PARTIAL/BLOCKED`, jamais substituição silenciosa |
| G0-09 | REFINEMENT | Simular aleatoriedade não comprova resiliência a eventos raros ou segurança do host | P0 invariantes, P1 metamorfismo/mutação/falha, P2 concorrência, P3 Monte Carlo offline; depois canaries empíricos e QA humana |
| G0-10 | REFINEMENT | Criatividade pode colapsar em buscas repetitivas ou virar expansão injustificada | Divergência condicional e orçamento de evidência; avaliação humana relevante sem exigir novelty universal |
| G0-11 | REFINEMENT | `SourceCapabilityRecord` pode se confundir com `Execution Route` do gerador | Registro separado `DATA_SOURCE_CAPABILITY`; transformar uma consulta paga em ação associada aos contratos de execução, sem renomear media routes |
| G0-12 | REFINEMENT | Validador de `deliverable_contracts_v0.1.json` não possui tipo de `RESEARCH_REPORT` | MVP usa a rubrica existente de Research Evidence Synthesis; estudar contrato de completude novo **somente se necessário** após canary, sem fingir QA determinística já instalada |

## 2. Mapa de compatibilidade campo a campo

**Fonte de verdade existente:** `RESEARCH_EVIDENCE_SYNTHESIS` entrega o `research_execution` com `research_execution_id, research_intent, primary_entity, market, language, range_from, range_to, generated_at, query_plan, source_outcomes, coverage, evidence_clusters, counterevidence, freshness_verdicts, status, unknowns, reuse_notes`. Mantê-lo como owner.

| Campo da proposta v0.1 | Owner atual | Destino seguro proposto | Observação |
|---|---|---|---|
| `ResearchRequest.request_id` | Core Task / research execution | `work_id` + `research_execution_id` quando resolvido; correlation ID opcional distinto | Não criar ID alternativo como autoridade |
| `research_mode: AD_DISCOVERY` | `RESEARCH_ONLY` / Specialist Stack | Filtro de suboperação dentro de `research_intent` | Não novo Work Profile |
| `entity_query` | Research plan | Query intent associado a `primary_entity`, stable refs quando resolvidos | Strings não definem identidade sozinhas |
| `platforms` / `period` / `market` | Research Evidence Synthesis | Extensão de filtros versionada e *namespaced* | Preservar `market_scope`, jurisdição e idioma separadamente quando aplicável |
| `market.basis` e `period.basis` | Fonte + contrato de consulta | Extensão **tipada de semântica** de geografia/tempo, sem inventar valores | `AUDIENCE_GEO` ≠ `CREATOR_REGISTERED_GEO` |
| `ranking.measure` | Runtime analítico + método consumidor | Especificação de métrica com versão, denominador, janela, coorte e fonte | Não score universal |
| `execution.allow_paid_sources` | Approval + Budget Ledger | Gate prévio, NÃO autorização isolada | `true` não é aprovação; exija fingerprint/reservation autorizados |
| `execution.allow_generation` | Creative owner + Action Authority | Bloqueio por default, seguido de autorização própria | Pedido de pesquisa nunca autoriza media |
| `SourceCapabilityRecord` | Nova infraestrutura de fontes | Registry descritivo por operação/país/métrica/licença/limite | Separado do Media Provider Registry |
| `ObservationRecord` | Evidence Record + camada analítica | `MetricObservation` referenciando `evidence_id` e fonte, sem duplicar origem | Campos `UNKNOWN` não viram 0/null silenciosamente |
| `ResearchResult.source_outcomes` | Research Evidence Synthesis | **Reuso literal** do enum canônico | Inclui `PAYMENT_REQUIRED, SCHEMA_DRIFT, SKIPPED_UNCONFIGURED` |
| `ResearchResult.completion_boundary` | Task Path + Research `status` | `COMPLETE/PARTIAL/INSUFFICIENT_EVIDENCE/BLOCKED` | `PARTIAL` de fonte não equivale automaticamente ao status da pesquisa |
| `ResearchResult.ranked_results` | Método de performance / Ad Funnel / Product Market | Extensão de achados dentro de `evidence_clusters` com método e cobertura | Ranking não altera conclusão canônica |
| `ResearchResult.evidence_refs` | Evidence Record | IDs canônicos, `independence_key` e provenance | Dedup não prova independência |
| `HANDOFF_PACKET` downstream | Execution Contracts V2.3 | Padrão exato do projeto; `permissions_carried: NONE` | Não passar aprovação para execução posterior |
| Histórico/metric series | Storage policy sob contrato da fonte | Derivados com `derived_from`, timestamps, version, rights | Dados não armazenáveis não entram no cache |
| Exploratory `dimension_policy_ref` | Specialist Method System | Apenas referência ao escopo de latitude resolvido | Não recriar prioridades/enums canônicos |

### 2.1 Correção central: **não criar um segundo Research Execution**

Em termos concretos, a eventual API interna deve ter esta forma lógica:

~~~text
Existing Core/RESEARCH_ONLY owns lifecycle
  -> research_execution (canonical envelope)
    -> intelligence_query_filter (optional, namespaced)
    -> source_outcomes / evidence records (canonical)
    -> metric_observations (extension linked by evidence_id)
    -> derived_metrics (versioned, deterministic)
    -> domain_interpretation (Ads/Product/Creator as eligible)
    -> result/coverage/unknowns/stop (canonical)
~~~

A camada de inteligência **não** pode possuir um ciclo independente de aceitação, estado de trabalho, gastos ou canon. `Content Performance` só vira novo Specialist Method quando o Growth Rule demonstrar decisão própria não coberta por métodos existentes.

### 2.2 Segmentação e cardinalidade de entidades

Modelo mínimo por escopo de fonte:

- `BRAND` (já existente no Product Marketplace) pode ter **várias** `SOCIAL_ACCOUNT` (nova entidade candidata).
- `SOCIAL_ACCOUNT` pode ter **muitas** `CONTENT_PUBLICATION`. Cada publicação tem ID nativo na plataforma e conjunto próprio de observações.
- `ADVERTISEMENT` é uma ocorrência de entrega/publicação publicitária, não uma métrica de venda; pode referenciar um `CONTENT_WORK`/asset e múltiplas variantes com **evidência de relação**.
- `PRODUCT_FAMILY/VARIANT/LISTING/SELLER` mantêm o contrato existente e não são derivados de correspondência puramente visual.
- `concept_id/variant_id/asset_id/publication_id` da Calibration são ligações de linhagem criativa/performance, não identidades públicas automaticamente equivalentes a ID de anúncio ou vídeo.

**Regra:** uma mesma ideia audiovisual em duas plataformas não autoriza somar seus views como se fossem mesma audiência; contabilização por ocorrência e direitos da fonte.

## 3. Contrato de elegibilidade e comportamento negativo

Antes de buscar:
1. Resolver `subject`, `source scope`, `time basis`, `geo basis`, `metric eligibility`, `purpose/rights`, `source available`, `cost/approval`, `stop condition`.
2. Comparar cada fonte elegível com a operação e não só com o nome da plataforma.
3. Se o usuário pedir geografia de audiência e a API só tiver país do canal, registrar **incompatível** e propor comparação explicitamente marcada. Não gerar substituição automática.
4. Se uma consulta falhar com `AUTH_FAILED`, `RATE_LIMITED`, `PAYMENT_REQUIRED`, `SCHEMA_DRIFT` ou `PARTIAL`, preservar resultado real e nunca declarar `NO_RESULTS`.
5. Se o resultado não sustentar “top N”, emitir `PARTIAL` ou `INSUFFICIENT_EVIDENCE` com universo pesquisado e hipótese explicada.
6. Identificadores, dados pessoais e observações sem licença de retenção operam somente transitoriamente, se o próprio uso for permitido; proibir cache/derivado persistente na incerteza de direitos.
7. Persistir metadados de decisão apenas quando sua retenção específica também for permitida. Aprovação de leitura não equivale a autorização de redistribuir texto, mídia ou embeddings.
8. Não permitir consulta paga ou exploração automática que altere limites, classes de ações, geografia ou finalidade.

## 4. Criatividade dentro de uma pesquisa auditável

O envelope canônico `dimension_policy` estabelece prioridade e latitude por dimensão. A nova etapa de consulta pode:
- **PRESERVE**: identidade, janela, país/fundamento, métricas, claims, licenças, aprovação, canon.
- **BOUNDED_VARIATION**: variar termos de busca e estrutura de hipóteses quando a pesquisa é aberta e isso ajuda o objetivo.
- **OPEN_EXPLORATION**: explorar explicações, casos de uso e analogias culturais com contraprovas, quando a intenção legitima.

Não criar enum de risk/creativity concorrente. `creative_risk_level` não é “data-risk” ou “tool permission”. A diversidade de abordagens deve ser comparada por utilidade e diferença substantiva, não por contagem de saídas.

Para pedido exato, `PRESERVE` pode cobrir todo o escopo. Para investigação aberta, divergência condicional e limites de busca controlam custo, sem exigir três trilhas sempre. Se a fonte não comprova hipótese, saída permanece inferida ou UNKNOWN.

## 5. Simulações: contratos e claims de validação

**Status atual:** `NOT_RUN` para INT-01..INT-26, RES-01..RES-24, CR-01..CR-04. O arquivo `validation/simulations/economics.py` é precedente real de simulação de **outro problema** e não valida esta iniciativa.

Ordem de testes proposta:

1. **Propriedades determinísticas:** invariantes de fonte, provenance, identidade, denominador, tempo, região, orçamento e permissões.
2. **Metamorfismo + mutação + fault injection + concorrência:** teste de perdas, duplicações, divergência de estado, replay, prompt injection e missing values.
3. **Monte Carlo offline:** simular operação em cenários de incerteza, falhas correlacionadas, caudas longas, estabilidade de ranking e custo. Seeds fixas, oracles, sensitivity, distribuição explicitada e confronto com testes-limite forçados.
4. **Canary real autorizado:** observação real YouTube/Meta, licenças documentadas, custo real e cobertura observada, sem afirmar causalidade.
5. **QA criativa humana:** relevância, distinção e utilidade; não só temperatura/variedade lexical.

**Monte Carlo não deve decidir automaticamente o provider, ranking de mercado ou produção**. Modela hipóteses, não substitui dados de campo. Testes de API real não devem ser simulados com credenciais e relatados como execução concluída.

## 6. Sequência concreta de resolução / exit do Gate 0

| Prioridade | Ação documental/contratual na futura candidata | Critério auditável |
|---|---|---|
| P0-A | Determinar campos de extensão sem duplicar `research_execution`, `evidence_id` e `HANDOFF_PACKET` | Um único owner por dado/estado; mapa compatível |
| P0-B | Especificar métrica + janela + geo + population + missing + version + rights | As seis consultas exemplo têm respostas elegíveis e saídas honestas de não cobertura |
| P0-C | Definir `source capability`/policy para YouTube e Meta por operação | Capabilities demonstradas/UNKNOWN, sem alegação de licença não verificada |
| P0-D | Ficar em read-only/grátis até que Paid Research Binding seja implementado e testado | Sem tentativa paga com `approval_ref` solto; controle real de ledger |
| P0-E | Declarar default-deny de persistência, política de expiração e propagação de invalidação | Simular violação sem gravação durável |
| P1-A | Determinar se novo `CONTENT_PERFORMANCE_INTELLIGENCE` é necessário | Teste de ablação + Growth Rule |
| P1-B | Verificar comportamento de expressão aberta e pesquisa exata | Testes CR-01..CR-04 com rubrica |
| P1-C | Adicionar fixtures ao harness e Monte Carlo somente após algoritmo/contrato | Testes reportam NOT_RUN até execução e evidência |
| P1-D | Rever interface CLI host sem impor MCP, servidor ou banco | Skill continua utilizável sem runtime adicional onde apropriado |
| P1-E | Definir gates de release separados de CI e benchmarking sintético | PASS técnico ≠ aprovação humana/produção |

**Gate 0 pode ser aceito para preparar uma implementação candidata** somente quando P0-A..P0-E tiverem proposta concreta aprovada e os limites de execução estiverem claros. Esta revisão **não concede** tal aceite. O próximo pacote deve incorporar estes ajustes numa especificação versionada, sem reescrever v0.1 historicamente e sem alterar `main`.

## 7. Decisão recomendada

`REVIEW VERDICT = CONDITIONAL_COMPATIBILITY`, não `PASS_FOR_PRODUCTION`.

- **Reutilizar:** `RESEARCH_ONLY`, Research Evidence Synthesis, Product Marketplace, Ad Funnel, Buyer, Video Evidence, Existing Core/Contracts, Specialist Creative Latitude, ADR-0002 e validation harness.
- **Adicionar em candidato:** analytics runtime nativo, registry de fontes, observações numéricas vinculadas a evidência, métricas versionadas e CLI opcional.
- **Adiar até prova:** nova família specialist; histórico persistente; score universal; MCP; dashboard; agendador; paid APIs; monitoramento automatizado; treinamento próprio.
- **Bloquear desde já:** novo Work Profile arbitrário, segundo ledger, claims de ranking nacional/global sem população, dados privados em GitHub e propagação de autoridade via handoff.

### Rastro de arquivos

- [Proposta original v0.1](architecture-preimplementation-v0.1.md).
- [Revisão da liberdade criativa e resiliência v0.1](design-review-creative-latitude-resilience-v0.1.md).
- [Acceptance INT-01..INT-26](acceptance-and-validation-v0.1.md).
- [RES/CR/Monte Carlo planejados](simulation-adversarial-plan-v0.1.md).
- Canônicos: `src/ai-creative-skill/references/`, `docs/decisions/ADR-0002-capability-bounded-invocation.md`, `validation/methodology/`.

**Nenhum arquivo em `src/`, `validation/` ou `main` é modificado por esta revisão.**
