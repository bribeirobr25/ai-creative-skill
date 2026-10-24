> **ARQUIVO HISTÓRICO, NÃO CANÔNICO.** Documento preservado para rastreabilidade da pesquisa; seus estados, procedimentos, links e permissões não constituem instruções atuais. Consulte [STATUS v0.3](../STATUS.md), [arquitetura atual proposta](../architecture-v0.3.md) e [matriz de aceitação](../acceptance-v0.3.md). Nenhum acesso a provedores ou merge é autorizado por este documento.

# Revisão arquitetônica · Liberdade criativa e resiliência · v0.1

**Data:** 2026-10-23  
**Estado:** ADENDO DE REVISÃO · PROPOSTA NÃO CANÔNICA · SEM APROVAÇÃO DE IMPLEMENTAÇÃO/RELEASE  
**Escopo:** PR #18, branch `proposal/intelligence-architecture-pre-v0-1-20261023`.  
**Base:** `main` 2.6.0-dev, commit `fb7f794ca2c51c2752afde5f907bd2866c9d1f25`; PR #17 paralelo não alterado.  
**Ler junto:** [Arquitetura pré-implementação v0.1](architecture-preimplementation-v0.1.md) e [Plano de aceitação v0.1](acceptance-and-validation-v0.1.md). Este adendo especifica revisões propostas e não substitui o Manifest nem as definições normativas.

## 1. Achado principal

Não tratar inteligência de mercado como *pipeline determinístico de perguntas pré-escritas*. A skill já distingue **prioridade/autoridade** de **liberdade criativa** e preserva a criatividade dentro das dimensões legitimamente abertas. A mesma distinção deve governar a etapa de exploração de pesquisa, sem aplicar aleatoriedade a fatos, identidade, métricas, direitos ou gasto.

**Autoridades existentes verificadas:**
- `Specialist_Method_System_Pre-v0.14-V2.4-CANDIDATE.md` §§6.2–6.4: `HARD INVARIANT|REQUIRED|PREFERRED|FLEXIBLE|FORBIDDEN` versus `PRESERVE|BOUNDED_VARIATION|OPEN_EXPLORATION`; `SAFE|BALANCED|BOLD|EXPERIMENTAL` somente quando útil e jamais para risco factual/autoridade.
- `Calibration_and_Experience_Memory_Pre-v0.15-V2.4-CANDIDATE.md` §8.2: diversidade, mode collapse, canon ancorado e decisão por contraste.
- `Research_Evidence_Synthesis_Pre-v0.3.md`: planejamento de buscas não redundantes, evidência, freshness e estados de fonte.
- `ADR-0002`: invocação independente e mínimo caminho suficiente.
- `validation/methodology/design.md` e `validation/methodology/economics.md`: pairwise, metamorfismo, fault injection, mutação e Monte Carlo ilustrativo pré-existentes.

**Decisão de revisão R-01:** não alterar esses owners, enumeradores ou semânticas; aplicá-los aos novos contratos e testes.

## 2. Quatro superfícies com graus diferentes de liberdade

| Superfície | Política padrão | Permitido | Não permitido |
|---|---|---|---|
| **A. Fatos, canon e permissão** | `PRESERVE` + prioridades existentes | Fonte, IDs, datas, geografia, direitos, aprovações, custo real e estatísticas com origem | Criar observações para preencher lacunas; alterar controle de gastos |
| **B. Busca/descoberta** | `BOUNDED_VARIATION`, quando pesquisa aberta; `PRESERVE` para match exato | Expandir sinônimos, culturas, idioma, nichos relacionados; selecionar fontes elegíveis; reordenar subquestões | Reescrever entidade, mercado, janela ou métrica de forma silenciosa; consulta paga sem autorização |
| **C. Hipótese/interpretação** | `OPEN_EXPLORATION` condicionada à relevância | Propor diferentes explicações, contraprovas, padrões criativos e oportunidades adjacentes | Converter hipótese em causalidade medida, ROI ou demanda comprovada |
| **D. Conceitos criativos derivados** | `OPEN_EXPLORATION` só no Work Profile adequado | Ideias distintas, formatos, hooks, narrativa, direção expressiva com QA | Herança de marcas/claims, canon, design de produto, execução/publicação sem nova autoridade |

A **exploração de pesquisa** não é a mesma coisa que **geração de campanha**. Se a pessoa pede pesquisa, pode haver ampliação estratégica dentro do escopo; mas o sistema entrega pesquisa e para. O `creative_risk_level` da skill não pode ser reinterpretado como limite de orçamento, permissão de coleta ou risco estatístico.

### 2.1 Procedimento proposto: explorar sem sobrecontrolar

~~~text
INTENÇÃO E AUTORIDADE
 → Resolve precisão requerida: EXACT / BOUNDED_DISCOVERY / OPEN_EXPLORATION (rótulos propostos, não enum canônico)
 → Âncoras imutáveis: entidade/produto/canon, localização, tempo, modalidade, métrica, fonte permitida, custo
 → Consulta central (representativa, sem reescrita)
 → Opcional: 2–3 eixos realmente distintos de exploração, se enriquecem a decisão
 → Coleta autorizada → normalização/dedup e elegibilidade
 → Contraprova e comparação → convergência
 → Entrega delimitada com hipóteses separadas dos achados
~~~

Eixos distintos podem ser: **linguagem do comprador**, **caso de uso/benefício**, **formato de anúncio**, **produto substituto**, **mercado comparável autorizado**. São *candidatos*, nunca checklist obrigatório. A IA não deve rodar três trilhas só para cumprir números nem abrir um mercado que o usuário excluiu.

**Gatilhos opcionais:** pedido exploratório, busca inicial pouco fértil, contradição entre sinais ou solicitação expressa de oportunidades adjacentes. **Não usar** divergência em consulta exata, correção localizada, trabalho determinístico, um único resultado exigido ou execução sem dados adicionais elegíveis.

A expressão do resultado pode variar; a estrutura auditável (fontes, métricas, limitações, entidades, permissões e conclusão) permanece estável.

### 2.2 Prevenção de mode collapse e exploração artificial

Dois riscos opostos:
1. **Overcontrol:** o assistente repete variações triviais da mesma busca/mesmo insight, ignorando oportunidades relevantes.
2. **Randomness sem propósito:** o assistente diversifica para categorias irrelevantes, perde a intenção do usuário e introduz custo/risco.

Critérios para revisão criativa: diversidade de hipótese **material**, aderência ao objetivo, novidade útil, rastreabilidade, respeito às exclusões e custo incremental. Pairwise/avaliação humana para inferência criativa, não score universal de criatividade. Registrar motivo para não explorar quando não houver espaço legítimo.

### 2.3 Contrato leve de pesquisa: campos opcionais propostos

Acrescentar ao futuro `ResearchRequest` (ainda não implementado) *somente se validado por ablação*:

~~~yaml
exploration:
  intent: BOUNDED_DISCOVERY       # candidato, não enum atual
  dimension_policy_ref: source_method_policy_or_task_bound_ref
  open_dimensions: [BUYER_LANGUAGE, USE_CASE]
  exclusions: [CROSS_MARKET_EXPANSION]
  candidate_limit: 3
  evidence_budget: 0             # se não há autorização paga
  stop_on_sufficient_evidence: true
~~~

A `dimension_policy` normativa da skill já resolve `priority`, `creative_latitude`, `authority_ref`, `envelope_ref`, `task_scope` e `rationale`. Não copiá-la integralmente para um schema rival; os campos acima são apenas interface de aplicação ou referências.

O relatório pode registrar `exploration_trace` (propostas, caminhos rejeitados e motivo), `novel_hypotheses` com evidências distintas e `creative_latitude_utilization` apenas quando apropriado. Não publicar raciocínio privado nem guardar prompts privados sem finalidade e direito.

## 3. Revisão de fronteiras e lacunas reais

| ID | Checagem | Conclusão |
|---|---|---|
| AR-01 | Um novo Work Profile de inteligência? | **NÃO**. `RESEARCH_ONLY` responde pesquisa; Ads/Organic possuem o deliverable final criativo. |
| AR-02 | Um novo Specialist Method de performance? | **CONDITIONAL**. Precisa prova de lacuna pelo Growth Rule, com ablação e exemplos reais/sintéticos. |
| AR-03 | Novo banco obrigatório? | **NÃO**. On-demand sem persistência deve funcionar; histórico somente autorizado. |
| AR-04 | MCP obrigatório? | **NÃO**. CLI/host adapter; MCP futuro não contém algoritmos próprios. |
| AR-05 | Motor independente de decisões? | **NÃO**. Runtime calcula e normaliza; governança do core não é duplicada. |
| AR-06 | Métrica única de viralidade universal? | **NÃO**. Velocidade, outlier, persistência, demanda e evidência econômica ficam separados. |
| AR-07 | Simulação estatística para provar retorno de mercado? | **NÃO**. Simulações testam comportamento sob hipóteses; mercado precisa dados empíricos. |
| AR-08 | Espaço para exploração e iniciativa da IA? | **SIM, quando tarefa permite**; sem trocar intenção, fontes, aprovações ou canon. |

## 4. Arquitetura de testes: extensão do harness, não outro sistema

O repositório já contém `validation/harness.py`, `validation/scenarios/register.json`, `validation/generators/pairwise.py`, `validation/simulations/economics.py` e testes de mutação/falha descritos na metodologia existente. A nova capacidade deve entrar nesse inventário pelo mesmo padrão de evidência/risco/correção. Não criar `intelligence-test-runner` com governança independente.

Prioridade em camadas, *não* dez mil chamadas reais:

- **L0 – propriedades e fixtures**: invariantes de identidade, dedup, janela, missing, budget, direitos e fonte.
- **L1 – adversarial/metamorphic/mutation/fault/state**: verificar que o sistema detecta ausência, alterações, ataques, resposta parcial, retrys, concorrência e shutdown.
- **L2 – Monte Carlo e stress estocástico OFFLINE**: variabilidade de quotas, latência, gaps, cobertura, custos e perfis de falha sob distribuições assumidas; reprodutibilidade por seed.
- **L3 – canary autorizado com API real**: observações reais pequenas, sem persistência indevida; comparar com expectativas.
- **L4 – QA de uso real**: dois julgamentos independentes quando a qualidade interpretativa/variedade criativa for material; decisões de rollout restritas ao escopo examinado.

Monte Carlo **não substitui** testes de invariantes determinísticos, injeção adversarial nem avaliação criativa humana. O relatório deve dizer exatamente quais camadas foram executadas.

## 5. Regras de execução e governança

- Revisão e simulação sem chamadas comerciais, sem generative media, sem criação de credenciais, sem coleta privada.
- Nenhuma expansão exploratória pode transformar `PAYMENT_REQUIRED` em autorização; estados `RATE_LIMITED`/`PARTIAL`/`AUTH_FAILED` não são `NO_RESULTS`.
- Nenhum fallback silencioso que altere mercado, janela ou base geográfica.
- Causalidade, demanda e “viralidade nacional” não podem ser alegadas a partir de amostra enviesada.
- Risco criativo `BOLD/EXPERIMENTAL` jamais enfraquece controles de privacidade, gasto, direitos, claims e project canon.
- PR #17, V2.5, `main`, `SKILL.md`, hashes históricos e testes executáveis não são alterados por este adendo.

## 6. Decisões de review / gates

**DR-01 · Ownership:** proposta conforme arquitetura, sujeita ao próximo diff de implementação e Gate 0.  
**DR-02 · Creative latitude:** aplicar a política existente aos espaços de pesquisa permitidos; não criar novo método de criatividade; aceitar como proposta a ser verificada por canaries.  
**DR-03 · Resiliência:** incluir no roadmap e no Gate 1 testes adversariais/propriedades; Monte Carlo entra após existir contrato executável minimamente estável, primeiro em modo offline.  
**DR-04 · Critérios de aprovação:** PR documental permanece `DRAFT`, nenhum dado/licença/score/host validado por estes documentos.  
**DR-05 · Validação futura:** [Plano de simulação e falhas v0.1](simulation-adversarial-plan-v0.1.md) mais testes `INT-01..INT-26` da matriz anterior.

### Riscos restantes, em ordem

1. **Acesso a dados licenciado**: pode inviabilizar uma operação/mercado independentemente da arquitetura.
2. **Semântica de métricas**: ranking pode ser computacionalmente correto, mas conceitualmente falso sem grupo/janela elegível.
3. **Liberdade criativa sem limite**: expansão indesejada do escopo, dependência de prompts e custos.
4. **Retenção e privacidade**: histórico pode contrariar termos; uma URL pública não é licença de armazenagem.
5. **Conformidade de implementação**: o contrato descrito não equivale a código testado; revisão humana e real-host canaries continuam pendentes.

**Resultado:** desenho consistente para revisão, **não aprovação de produção nem de implementação canônica**.
