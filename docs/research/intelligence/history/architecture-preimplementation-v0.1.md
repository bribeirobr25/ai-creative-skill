> **ARQUIVO HISTÓRICO, NÃO CANÔNICO.** Documento preservado para rastreabilidade da pesquisa; seus estados, procedimentos, links e permissões não constituem instruções atuais. Consulte [STATUS v0.3](../STATUS.md), [arquitetura atual proposta](../architecture-v0.3.md) e [matriz de aceitação](../acceptance-v0.3.md). Nenhum acesso a provedores ou merge é autorizado por este documento.

# AI Creative Skill · Intelligence Architecture · Pré-implementação v0.1

**Data:** 2026-10-23  
**Estado:** PROPOSTA PARA REVISÃO · NÃO CANÔNICA · NÃO IMPLEMENTADA · NÃO INSTALADA  
**Base examinada:** `main` 2.6.0-dev, commit `fb7f794ca2c51c2752afde5f907bd2866c9d1f25`  
**Referência de release preservada:** V2.5.0, `39a0bfa39270ea4b685b0f862e7dbf647cf81d77`  
**Paralelo em andamento:** PR #17, `feature/web-runtime-2.6`, fora desta proposta.  
**Classe:** desenho técnico / research candidate. Nenhuma autoridade de release, geração, publicação, compra, consulta paga ou alteração de cânone.

## 0. Síntese executiva

Criar uma infraestrutura **nativa, independente, provider-neutral e MCP-opcional** de inteligência para pesquisas de vídeos, anúncios, criadores, marcas, produtos, marketplaces e tendências. A infraestrutura **não** é um novo Work Profile, uma segunda governança ou um sistema de geração. Conecta-se à AI Creative Skill por meio de operações limitadas e dos métodos existentes. Implementação inicial sem MCP, com adaptador MCP apenas caso a necessidade de interoperabilidade seja demonstrada.

Esta proposta **não** recomenda copiar código, algoritmos, bases privadas ou interfaces proprietárias de vidIQ ou Orthogonal. Suas funcionalidades observáveis inspiram critérios de produto; métodos analíticos e código serão próprios, e o acesso a dados se dará por canais autorizados.

### Autoridades normativas existentes (não reescritas aqui)

1. `src/ai-creative-skill/SKILL.md` (roteamento host e limites de autoridade).
2. `src/ai-creative-skill/references/AI_Creative_Skill_V2.5_Integration_Manifest.md` e o Current Design Manifest V2.4 herdado (resolução de versões).
3. `AI_Creative_Skill_Architecture_Spec_Pre-v0.17-V2.4-CANDIDATE.md` (núcleo, §24.1 DATA-SOURCE CONNECTORS).
4. `AI_Creative_Skill_Execution_Contracts_Pre-v0.21-V2.4-CANDIDATE.md` (aprovação, orçamento, estado, ingestão, handoff).
5. `AI_Creative_Skill_Specialist_Method_System_Pre-v0.14-V2.4-CANDIDATE.md` (owners e Growth Rule).
6. `RESEARCH_EVIDENCE_SYNTHESIS`, `PRODUCT_MARKETPLACE_INTELLIGENCE`, `BUYER_RESEARCH`, `AD_FUNNEL_INTELLIGENCE`, `VIDEO_EVIDENCE_INSPECTION`, `ADS_STRATEGY` e `ORGANIC_CONTENT_CRAFT`.
7. `docs/decisions/ADR-0001-source-of-truth.md` e `ADR-0002-capability-bounded-invocation.md`.

Em conflito com qualquer norma atual, esta proposta cede precedência. Nomes dos exemplos abaixo são **rascunhos de contratos**, não campos canônicos aceitos.

## 1. Intenções, escopo e limites

### 1.1 Solicitações representativas

- **R1:** “Encontre anúncios promissores/virais para nécessaires e bolsas de maquiagem na Alemanha no último mês.”
- **R2:** “Quais os 10 anúncios mais virais na Alemanha no último mês?”
- **R3:** “Mostre os conteúdos de maior destaque de uma marca (ex.: Nubank), por plataforma e período.”
- **R4:** “Encontre vídeos sobre um nicho que superam a performance habitual do canal.”
- **R5:** “Compare evidências de publicidade, demanda e concorrência para uma categoria nos EUA, Brasil e Alemanha.”
- **R6:** “Pesquise referências e depois proponha um briefing original.” A pesquisa termina e faz handoff; produção não é autorizada automaticamente.

Dimensões parametrizáveis: termo/produto/entidade/conta, modalidade `PAID_AD|ORGANIC_CONTENT|PRODUCT|MIXED`, plataforma, localização e fundamento geográfico, janela temporal e fundamento do tempo, métrica desejada, limite de resultados, licença/cobertura da fonte, idioma e custo máximo autorizado.

### 1.2 Não objetivos desta fase

Não construir um novo hub de APIs, crawler indiscriminado, um clone integral de vidIQ/Orthogonal, mecanismo de publicação, aquisição automática de produtos, medidor de ROAS de terceiros, painel web obrigatório, agente autônomo de gastos ou pipeline de produção obrigatória após pesquisa. Não prometer “top global/nacional” fora do universo efetivamente observado; não presumir visões, vendas ou público geolocalizado quando a fonte não revela essas métricas.

## 2. Princípios e fronteiras

- **Uma autoridade:** execução integrada ao Stage 0, Project Profile, Work Profile e Specialist Method Stack da skill.
- **Menor caminho suficiente:** entrada, verificação e saída independentes segundo ADR-0002.
- **Intelligence Runtime não é Creative Core:** o runtime busca, normaliza, calcula e devolve dados com proveniência; métodos especializados interpretam.
- **Conector não escolhe metodologia:** disponibilidade de API não decide propriedade da tarefa.
- **AI interpretação; analytics cálculo:** métricas e agregações devem ser determinísticas, versionadas e auditáveis. Análise criativa por modelo é uma camada separada e explicitamente inferencial.
- **Ausência não é zero:** métrica não fornecida = `UNKNOWN`, jamais `0`.
- **Observação ≠ verdade comercial:** longevity ≠ conversão, views ≠ vendas, origem do canal ≠ origem da audiência.
- **Sem dependência de MCP:** interface opcional e fina sobre as mesmas operações internas.
- **Políticas por fonte:** acesso, escopo, quotas, armazenagem e finalidade exigem revisão por provedor, inclusive fornecedores de dados terceirizados.

## 3. Responsabilidades e ponto de integração

| Componente | Dono existente ou proposta | Responsabilidade | Não pode assumir |
|---|---|---|---|
| Roteamento, autoridade, task boundary | Architecture / `SKILL.md` | Propriedade do pedido, limites, canon | Autoampliar pesquisa para geração |
| Pesquisa genérica e fontes | `RESEARCH_EVIDENCE_SYNTHESIS` | Plano, freshness, source outcome, cobertura | Interpretar “vencedor” por contagem de ads |
| Anúncios e funis | `AD_FUNNEL_INTELLIGENCE` | Criativos, mecanismos, variantes, sinais de publicidade | Declarar ROAS/CPA sem dados |
| Produto e marketplace | `PRODUCT_MARKETPLACE_INTELLIGENCE` | Famílias, variantes, listing, seller, equivalência, sinais de demanda | Confundir similaridade com mesma origem |
| Buyer/reviews | `BUYER_RESEARCH` | Voz do consumidor e intenção | Converter comentários em vendas |
| Inspeção de vídeo | `VIDEO_EVIDENCE_INSPECTION` | Evidência temporal/visual/áudio com cobertura | Reinterpretar métricas de canal |
| Performance de conteúdo | **Candidato** `CONTENT_PERFORMANCE_INTELLIGENCE` | Estatística de outliers, velocidade e benchmarks contextualizados | Duplicar fonte, vídeo-inspection, estratégia |
| Produção e direção | ADS / ORGANIC e métodos atuais | Conceito original, script, produção e QA | Considerar pesquisa autorização de gastar |
| Coleta e métricas | **Novo** Intelligence Runtime | Adapters, observações, métricas, persistence sob licença | Nova governança ou decidir cânone |
| Interface de cliente | CLI/host adapter primeiro; MCP opcional | Invocar operações autorizadas e entregar resultados estruturados | Nova lógica de inteligência |

**Growth Rule:** só promover `CONTENT_PERFORMANCE_INTELLIGENCE` a método formal depois de demonstrar, por ablação com exemplos representativos, que os métodos existentes não expressam a disciplina estatística. Não criar um Work Profile por tecnologia/plataforma.

### 3.1 Caminho de execução lógico

~~~text
USER
  -> Stage 0: autoridade, finalidade, limites, perfil responsável
  -> Research Request (proposta v0.1)
  -> Fonte/capacidade elegível e policy preflight
  -> Aprovação e orçamento (quando aplicáveis, contratos existentes)
  -> Conectores oficiais/autorizados ou import de dataset permitido
  -> Proveniência, deduplicação e entidades
  -> Observações e séries permitidas
  -> Algoritmos de performance (sem LLM)
  -> Interpretação pelo(s) especialista(s) carregado(s) JIT
  -> QA: evidência, cobertura, política, conclusões, custo
  -> Research Result: COMPLETO / PARCIAL / BLOQUEADO conforme contratos vigentes
  -> Entrega e STOP
  -> HANDOFF_PACKET opcional somente se o próximo trabalho foi solicitado
~~~

## 4. Contratos propostos e semântica

Os schemas abaixo são **intenção de desenho**, sem substituir enums canônicos. Antes de implementar, mapear/compatibilizar campos com Execution Contracts e Manifest.

### 4.1 ResearchRequest v0.1 (ilustrativo)

~~~yaml
request_id: request-001
deliverable: RESEARCH_REPORT
research_mode: AD_DISCOVERY
entity_query: "makeup pouch bags"
platforms: [META_AD_LIBRARY]
market:
  code: DE
  geo_level: COUNTRY
  basis: AD_DELIVERY_GEO
period:
  start: "2026-09-23"
  end_exclusive: "2026-10-23"
  basis: ACTIVE_DURING_WINDOW
ranking:
  measure: AD_PERSISTENCE
  limit: 10
  require_observed_metrics: true
execution:
  allow_paid_sources: false
  allow_background_collection: false
  allow_generation: false
  approval_ref: null
~~~

**Fundamentos geográficos distintos:** `AD_DELIVERY_GEO`, `CREATOR_REGISTERED_GEO`, `AUDIENCE_GEO`, `SEARCH_RESULT_LOCALE`, `SELLER_GEO`, `SHIPPING_DESTINATION`. Cidade/estado só quando a fonte o oferecer com significado correspondente. Não rebaixar automaticamente `AUDIENCE_GEO` para país do criador.

**Fundamentos temporais distintos:** `PUBLISHED_DURING_WINDOW`, `ACTIVE_DURING_WINDOW`, `ENGAGEMENT_GAINED_DURING_WINDOW`, `OBSERVED_AS_OF`. Um total acumulado atual não demonstra visualizações ganhas dentro da janela. Horários UTC para armazenamento; fuso original e interpretação local preservados.

### 4.2 SourceCapabilityRecord v0.1

~~~yaml
source_id: YOUTUBE_DATA_API
adapter_version: pre-v0.1
access_kind: OFFICIAL_API
operations: [PUBLIC_VIDEO_SEARCH, VIDEO_CURRENT_STATS, CHANNEL_LOOKUP]
geographic_semantics: [SEARCH_RESULT_LOCALE, CREATOR_REGISTERED_GEO]
metric_support: [VIEW_COUNT_CURRENT, LIKE_COUNT_CURRENT, COMMENT_COUNT_CURRENT]
history_mode: CURRENT_ONLY
authorization: TO_VERIFY
license_review_status: TO_VERIFY
data_retention_rule_ref: TO_VERIFY
purposes_allowed: TO_VERIFY
cost_model: FREE_QUOTA_WITH_LIMITS
rate_limit_profile: TO_VERIFY
verified_at: null
~~~

A tabela de suporte real deve ser obtida por preflight/documentação atual e ensaio com resposta real. Este exemplo **não** representa uma certificação de cobertura do YouTube. Marcas como Meta, TikTok, X, Reddit, Etsy, Amazon e Google Shopping terão registros próprios, por operação, escopo geográfico e modalidade de acesso. Não assumir paridade entre site público, Creative Center e API.

### 4.3 Modelo de entidades e identidade

**Reusar** `PRODUCT_FAMILY`, `PRODUCT_VARIANT`, `LISTING`, `SELLER`, `BRAND`, `SOURCE_PRODUCT_REF` do Product/Marketplace Method; não criar versões concorrentes.

**Adicionar somente onde necessário:**

- `SOCIAL_ACCOUNT`: identidade da conta com IDs e aliases por plataforma.
- `CONTENT_WORK`: ideia/obra audiovisual abstrata, quando há evidência de identidade entre publicações.
- `CONTENT_PUBLICATION`: postagem/publicação específica em plataforma, com ID estável e URL.
- `ADVERTISEMENT`: execução/publicação publicitária identificável, ligada a criativo e anunciante quando verificável.
- `CREATIVE_VARIANT_RELATION`: repost, recorte, tradução, nova legenda, hook, anúncio derivado; vínculo com confiança e evidência.
- `OBSERVATION`: dado medido ou fornecido, associado ao objeto e à fonte.
- `METRIC_SERIES`: derivação temporal **somente quando histórico autorizado e existente**.
- `RESEARCH_REPORT`: saída com escopo, proveniência e conclusão.

ID interno estável, ID da fonte, URL original e time stamp de descoberta são coisas distintas. Match exato, provável, similar e insuficiente permanecem separados. Uma mesma peça publicada em duas plataformas possui **observações separadas**.

### 4.4 ObservationRecord v0.1

~~~yaml
observation_id: obs-001
subject_type: CONTENT_PUBLICATION
subject_id: yt:video:example
source_id: YOUTUBE_DATA_API
source_native_id: example
collected_at: "2026-10-23T08:00:00Z"
metric: PUBLIC_VIEW_COUNT
value: 125000
unit: views
measurement_kind: PLATFORM_REPORTED_CUMULATIVE
window: null
geography_basis: UNKNOWN
sampling_scope: SINGLE_PUBLICATION
dataset_coverage: PARTIAL
provenance_ref: source-record-001
method_version: adapter-0.1
usage_rights_ref: license-policy-001
retain_until: null # obrigatório calcular pela política antes de persistir
~~~

**Regras:** uma métrica derivada ganha novo registro com `derived_from_observations[]`, fórmula e versão. Não falsificar número, janela temporal, localização, denominador nem status de direitos. Conteúdo e métricas que não podem ser armazenados devem permanecer transitórios e não entrar no banco.

### 4.5 ResearchResult v0.1

Registrar `source_outcomes[]` com vocabulário canônico (`OK`, `NO_RESULTS`, `PARTIAL`, `RATE_LIMITED`, `AUTH_FAILED`, `PAYMENT_REQUIRED`, `UNREACHABLE`, `TIMEOUT`, `SCHEMA_DRIFT`, `SKIPPED_UNCONFIGURED`, `ERROR`), `population_definition`, `sample_coverage`, `metric_eligibility`, `ranked_results[]`, `excluded_results[]`, `assumptions[]`, `counterevidence[]`, `unverified_claims[]`, `data_access_cost`, `evidence_refs[]`, `verified_at`, `completion_boundary`.

Sinalizar explicitamente “top 10 **na amostra acessível**” quando cobertura populacional não for demonstrada; falta de resultados com falha de API não é `NO_RESULTS`. Mapeamento final do estado de entrega deve reutilizar os status efetivos da skill, sem um novo enum proprietário.

## 5. Métricas e rankings

Modelos separados e explicáveis:

1. **Outlier ratio:** visualizações observadas do vídeo com idade \(t\) / mediana dos vídeos comparáveis do mesmo canal na idade \(t\). Exigir grupo comparável, mínimo de amostras definido em teste, tratar zeros e intervalos ausentes. Fórmula **nossa**, não alegação sobre vidIQ.
2. **Velocity:** delta de contador entre duas observações permitidas / horas efetivamente decorridas. Total atual ÷ idade não é velocity medida; no máximo proxy rotulada.
3. **Engagement rate:** definir numerador, denominador, plataforma, tipo de conteúdo e janela; nunca comparar métricas com denominadores incompatíveis.
4. **Trend momentum:** evolução de indicadores observáveis dentro de uma definição de universo, janela e amostragem consistente; ausência de histórico = `UNKNOWN`.
5. **Advertising persistence:** datas e recapturas verificadas; captura isolada não confirma atividade contínua nem vendas.
6. **Demand/opportunity:** síntese multidimensional, com sinais de busca, preços, comentários, competição e viabilidade. Distinguir demanda observada, interesse inferido, intenção de compra e evidência econômica.
7. **Creative analysis:** interpretação pelo método existente de Video Evidence Inspection + Ads/Organic, nunca mecanismo de substituição de métricas reais.

Todo ranking preserva `eligible_population`, `sort_definition`, `metric_version`, `normalization_group`, `missing_rate`, `source_coverage` e `confidence_notes`. Pontuações entre plataformas ficam separadas por padrão; agregação só após um protocolo de comparabilidade testado. Não criar score universal 0–100 sem calibração externa.

## 6. Infraestrutura e modos de execução

### 6.1 Primeiro modo: `ON_DEMAND_LOCAL`

Biblioteca Python provider-neutral invocada por um adaptador local/CLI do host autorizado. Sem servidor sempre ativo, sem MCP, sem agendamento. A skill permanece distribuível sem login GitHub/Drive e sem credenciais no pacote. Em host sem execução de código ou sem rede, retornar capacidade ausente/limitação honesta.

### 6.2 Modos opcionais, não no MVP

- `ON_DEMAND_HOSTED`: mesmo motor acessível por API autenticada, sem duplicar regras.
- `SCHEDULED_COLLECTION`: agendador e store, somente para fontes, métricas, finalidades e retenções permitidas; não surge automaticamente.
- `DATASET_IMPORT`: ingestão de export autorizado, com escopo e direitos explícitos.
- `MCP_ADAPTER`: interface adicional, quando exigida por interoperabilidade, reaproveitando operações existentes.

### 6.3 Persistência por permissões

Três classes operacionais: **transitório em memória** (dados cujo uso não autoriza retenção); **cache normalizado com prazo por fonte**; **estado durável da skill** (metadados de execução, decisões e proveniência quando permitido). Remoção/atualização por TTL, autorizações, revogações e termos. Histórico só com snapshots licenciados. Não guardar vídeo, thumbnail, comentário, postagem ou dado pessoal por padrão. Identificadores de origem e hashes não concedem direito de retenção.

Protótipo: SQLite local **se armazenamento permitido**; Postgres/objeto/cloud apenas quando acesso multi-host/histórico justificar. Instalação sem banco também deve funcionar para pesquisa sob demanda.

### 6.4 Idempotência, custo e erros

Consultas com paginação, timeout, retry condicionado à classe do erro, deduplicação e quotas. `RATE_LIMITED` não pode virar “sem anúncios”. Para fonte paga, reutilizar aprovação, orçamento/reserva e registro de gasto de Execution Contracts §4.1; esse binding é declarado `LATER` e precisará de implementação/validação antes de chamadas pagas autônomas. Limite zero de gastos por padrão. `use` pago, geração, publicação e ações externas permanecem bloqueadas sem autorização específica.

## 7. Segurança, direitos e evidência

- Repositório **público**: proibido inserir chaves, tokens, cookies, mídia de clientes, dados de usuários, resultados privados, prompts confidenciais ou modelos/pesos de terceiros.
- Segredos só via ambiente/secret store e escopo mínimo, nunca embutidos em prompts ou distribuídos no ZIP.
- Nenhuma coleta automatizada que viole termos, login/cookie harvesting ou bypass de limites; terceiros exigem contrato/licença, inclusive quanto a armazenamento, uso comercial e redistribuição.
- Conteúdo externo é dado não confiável: separar texto recuperado de comandos de execução, URLs e instruções, aplicar allowlist e impedir exfiltração e prompt injection.
- Sem inferir localização real de audiência por idioma, país do canal ou plataforma de busca.
- Identificar finalidade, minimização, base jurídica e transferência internacional quando houver dados pessoais, inclusive RGPD/GDPR quando aplicável. Revisão jurídica/compliance é gate, não decisão automática da LLM.
- Nunca transferir autoridade de produto, canon, aprovação, publicação ou gasto em `HANDOFF_PACKET`.
- Falha de permissão, termos desatualizados ou política desconhecida bloqueia uso persistente ou de fonte paga até revisão.

## 8. Fontes: matriz inicial de hipótese, não certificação

| Fonte | Inicial | Finalidade prioritária | Dependência ainda a validar |
|---|---|---|---|
| YouTube Data API | P0 | vídeos, canais e métricas públicas atuais | quota, permissões, histórico/retention e semântica regional |
| Meta Ad Library API | P0/P1 | anúncios comerciais em jurisdições cobertas | elegibilidade, escopo, campos reais e geografia |
| TikTok Commercial Content API | P1 | anúncios nas regiões permitidas | aprovação, cobertura e métricas |
| TikTok Creative Center | Pesquisa manual | filtros e formatos criativos | não presumir API automatizada |
| Instagram Graph API | P1 | descobertas autorizadas de contas profissionais | escopos e limitações de terceiros |
| X API / repositório de anúncios | P2 | posts e publicidade, conforme rota | modalidade, termos e custos |
| Etsy Open API | P2 | listagens, sellers, preços | aprovação, limites e finalidade comercial |
| Amazon / Google Shopping | P2 | catálogo e mercado | API de merchant/affiliate ≠ análise livre de concorrentes |
| Reddit | P2 condicional | demandas, perguntas e dores do público | permissão explícita para uso comercial |
| Provedores terceiros licenciados | Só após lacuna comprovada | ampliar mercado/plataforma autorizados | procedência, cobertura, direito de uso e custo |

**Gate de fontes:** antes de codificar cada conector, registrar endpoint/documentação oficiais atuais, amostra real, resposta, rate limits, direitos, políticas de retenção, cobertura geográfica, preço e taxa de resultados úteis. A conexão direta é preferida; provider pago é fallback justificado, não requisito estrutural.

## 9. Compatibilidade com a arquitetura existente

### 9.1 Futuro layout proposto (nenhum arquivo criado em `src/` nesta fase)

~~~text
src/ai-creative-skill/
  intelligence/
    core/            # contratos e normalização
    adapters/        # fontes autorizadas
    entities/        # resolução/deduplicação
    analytics/       # métricas determinísticas
    storage/         # persistência opcional, direitos e TTL
    policy/          # permissões, custos, capabilities
  scripts/
    creative_intelligence.py  # possível CLI thin
tests/
  test_intelligence_*.py
validation/
  fixtures/intelligence/      # dados sintéticos, não scraping real
  scenarios/...               # regressões do contrato
~~~

Esses diretórios são **propostos** e precisam passar pela disciplina de versionamento. Não mover nem duplicar métodos normativos em `references/`. A extensão somente poderá mudar `SKILL.md` após demonstração end-to-end e aprovação para candidate integration.

### 9.2 Handoff

Pesquisa independente é `RESEARCH_ONLY`. Se a solicitação inclui produção final, o resultado da pesquisa é um subtrabalho e os owners finais continuam Ads/Organic/outro. Handoff preserva IDs, evidência, direitos, o que é inferência, limitações, escopo e canon. Nunca converte `RESEARCH COMPLETE` em `GENERATION AUTHORIZED`.

### 9.3 Versionamento / branches

Preservar `main` 2.6.0-dev e a release V2.5.0. PR #17 é paralelo e não deve ser alterado. Esta proposta entra **somente em `docs/research/` numa branch própria**, sem alterar `src/`, testes, contracts, scripts, manifest ou históricos. A implementação futura pede outro candidate, integrações revisadas e gates de regressão oficiais; o PR de pesquisa não é aprovação de release.

## 10. Sequência e gates de desenvolvimento

**Gate 0 · Projeto da capacidade:** aprovar ownership, contratos, modelo de entidades, fontes permitidas, restrições e critérios de aceitação. Nenhuma execução externa.

**Gate 1 · Vertical slice YouTube, grátis/limitado:** um conector autorizado, amostra pequena, resultado observável, sem armazenamento indevido, métricas reproduzíveis e QA. Regra: dados atuais sozinhos não geram velocity medida.

**Gate 2 · Vertical slice anúncios:** Meta EU onde autorização existir, observações/variantes por produto e brand. Comparar a semântica da biblioteca com o output e impedir inferências de venda/ROAS.

**Gate 3 · Handoff integrado:** pesquisa para Ads/Organic via mecanismos existentes. Sem geração/publicação automática.

**Gate 4 · Expansão:** TikTok, Instagram, marketplaces, outros países/terceiros somente após custo-benefício e licenciamento; monitoramento contínuo somente sob demanda explícita.

**Gate 5 · Empacotamento/host:** candidato separado, validar `release_integrity`, `candidate_integrity`, testes novos, host canaries, direitos e usuário. Teste verde de código não é aprovação de qualidade editorial, legal ou comercial.

**Custos:** meta de experimento inicial `US$0–50` em serviços externos **excluindo desenvolvimento**; não é estimativa garantida nem teto implícito de autorização. Sem cobrança até aprovação. Escala/fonte define o custo real. Registrar custo por consulta, por resultado válido e por relatório útil para decisões posteriores.

## 11. Pendências de decisão antes de implementar

| ID | Proposta padrão | Validação necessária |
|---|---|---|
| D-01 | Bibliotecas Python + CLI local, MCP opcional | Host real onde se deseja executar |
| D-02 | Sem banco obrigatório na primeira pesquisa | Política de fonte e requisito de histórico |
| D-03 | Read-only e zero gasto por padrão | Contrato de paid research §4.1 quando aplicável |
| D-04 | YouTube primeiro, Meta depois | Acesso e licença de cada API |
| D-05 | Métricas independentes, sem score universal | Ensaios e calibração por tarefa |
| D-06 | Um candidato de método de performance, sem novo perfil | Ablation e Growth Rule |
| D-07 | Dados de marca/conta separados de países de audiência | Testes de semântica territorial |
| D-08 | Histórico permitido apenas por fonte e finalidade | Revisão legal/termos, TTL, revogação |
| D-09 | Publicar resultados somente após evidência e QA | Direitos, cobertura e proveniência |
| D-10 | Reutilizar contratos e testes da skill | Conformidade ADR-0002 e release gates |

## 12. Critério de aceitação desta especificação

Revisão aprovada somente quando: owners não conflitam; schemas não contradizem cânones; permissões/limites da fonte são claros; os três pedidos originais e exemplos de outlier estão cobertos; cada cenário de falha tem saída honesta; quotas e custos não implicam gasto sem autorização; MCP está realmente opcional; execução offline/fake dados cobre testes; a estratégia respeita PR #17 e a V2.5.

Ver [Plano de validação e critérios de aceitação v0.1](acceptance-and-validation-v0.1.md). **Este documento não executa nem certifica nenhuma dessas condições.**
