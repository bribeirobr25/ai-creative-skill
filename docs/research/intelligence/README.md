# Intelligence · Pesquisa arquitetônica (PR #18)

**Status:** PROPOSTA PARA REVISÃO · NÃO CANÔNICA · NÃO EXECUTADA · NÃO APROVADA PARA RELEASE  
**Base:** main 2.6.0-dev no commit `fb7f794ca2c51c2752afde5f907bd2866c9d1f25`; V2.5.0 preservada.  
**Branch:** `proposal/intelligence-architecture-pre-v0-1-20261023`.

## Ordem de leitura

1. [Arquitetura pré-implementação v0.1](architecture-preimplementation-v0.1.md) — fundamentos, interfaces propostas, dados, fontes e gates.
2. [Revisão de liberdade criativa e resiliência v0.1](design-review-creative-latitude-resilience-v0.1.md) — aplicação dos princípios criativos existentes, ownership e revisão crítica; **adendo complementar à proposta base, não autoridade canônica**.
3. [Plano de aceitação v0.1](acceptance-and-validation-v0.1.md) — INT-01..INT-26 para casos básicos e negativos.
4. [Plano de simulação e testes adversariais v0.1](simulation-adversarial-plan-v0.1.md) — INV-01..INV-10, RES-01..RES-24, CR-01..CR-04, Monte Carlo e ablações de criatividade, todos **NOT_RUN**.

## Recomendações convergentes desta revisão

- **Manter a criatividade controlada da skill:** preservar fatos/autoridade/claims/medidas, abrir dimensões legítimas de pesquisa e conceito de modo proporcional à tarefa, com comparação e convergência sem mode collapse.
- **Não duplicar governança:** Research Evidence, Ad/Funnel, Product/Marketplace, Video Evidence, Ads e Organic são owners existentes; um novo método de performance depende de prova de Growth Rule.
- **Primeira execução nativa:** bibliotecas Python + CLI do host, MCP opcional e sem servidor/banco obrigatório no início.
- **Reusar o validation harness:** começar por fixtures/propriedades/falhas; Monte Carlo **offline** após contrato e oracles estabilizarem; somente depois canaries autorizados e QA humana.
- **Sem leitura como aprovação:** drafts/PR não fornecem acesso a API, licença para persistir, dados reais, autorização de despesas, endosso jurídico nem certificação de produção.

## Estado / gates

| Gate | Estado atual |
|---|---|
| Proposta documentada | CONCLUÍDO no PR, ainda não aprovada |
| Revisão de ownership, contratos e latitude criativa | PROPOSTA REGISTRADA, aceite pendente |
| Testes INT/RES/CR e Monte Carlo da nova capacidade | NOT_RUN |
| Canaries YouTube/Meta e política efetiva de fontes | NOT_RUN |
| `src/`, `SKILL.md`, pacote e runtime modificados | NÃO |
| Integração na main, release, execução paga | NÃO |

**Não confundir:** `validation/simulations/economics.py` já contém um benchmark Monte Carlo histórico para uma questão econômica diferente; este PR **não** executa novas simulações e **não** altera os resultados anteriores.

A revisão de código / decisão de integração deve seguir os contratos normativos, as ADRs e a preservação de PR #17. Este conjunto não modifica a skill instalada.
