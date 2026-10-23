# Intelligence · Pesquisa arquitetônica (PR #18)

**Estado:** GATE 0 DESK REVIEW REALIZADA · COMPATIBILIDADE CONDICIONAL · ACEITE DO PROPRIETÁRIO PENDENTE · NÃO CANÔNICA/NÃO EXECUTADA  
**Base:** `main` 2.6.0-dev no commit `fb7f794ca2c51c2752afde5f907bd2866c9d1f25`; V2.5.0 no commit `39a0bfa39270ea4b685b0f862e7dbf647cf81d77` preservada.  
**Branch:** `proposal/intelligence-architecture-pre-v0-1-20261023` (nome histórico da branch, apesar da revisão documental v0.2).  
**PR #17:** paralelo e não alterado.

## Documento de trabalho atual (proposta, não norma)

1. **[Arquitetura pré-implementação v0.2](architecture-preimplementation-v0.2.md)**: contrato de pesquisa alinhado ao `research_execution` existente, `MetricObservation` vinculada à evidência canônica, fontes e permissões, MCP opcional, métricas, rollout.
2. **[Gate 0: revisão de compatibilidade v0.1](gate0-contract-compatibility-review-v0.1.md)**: matriz G0-01..G0-12, cinco bloqueios de contrato/autoridade/direitos/semântica com propostas concretas de resolução, owners e aceite pendente.
3. **[Revisão de liberdade criativa e resiliência v0.1](design-review-creative-latitude-resilience-v0.1.md)**: Task-Relative Creative Latitude, diversidade significativa sem perda de fatos e riscos de overcontrol.
4. **[Matriz de aceitação v0.2](acceptance-and-validation-v0.2.md)**: INT-01..INT-35, todos NOT_RUN; nove casos novos para semântica/autoridade/evidência.
5. **[Simulações e testes adversariais v0.1](simulation-adversarial-plan-v0.1.md)**: INV-01..INV-10, RES-01..RES-24, CR-01..CR-04 e Monte Carlo offline, todos NOT_RUN.

**Histórico preservado, não atual:** [arquitetura v0.1](architecture-preimplementation-v0.1.md) e [matriz INT-01..INT-26 v0.1](acceptance-and-validation-v0.1.md). A v0.2 não apaga nem reescreve o desenho inicial, e ainda não substitui fontes normativas.

## Achados do Gate 0

- A arquitetura existente já cobre Research, Product Marketplace, Ad Funnel, Buyer, Video Evidence, Specialist Creative Latitude e cross-profile HANDOFF. **Não** criar um segundo mecanismo de governança ou estado.
- A proposta v0.1 tinha risco de duplicar `ResearchResult` e Evidence Record. **Na v0.2**, a inteligência aparece como extensão tipada do `research_execution` com observações numéricas referenciadas ao `evidence_id` original.
- Paid research binding está especificado como `LATER`: credencial, chave ou flag não autorizam cobrar; MVP fica read-only/grátis, sem chamadas pagas até aprovação/reserva verificadas.
- Período, geografia, universo e denominador de métricas são semanticamente tipados, sem transformar contagem cumulativa em VPH histórico ou busca localizada em audiência local.
- Dados/derivados de terceiros não podem ser processados ou armazenados quando os direitos necessários não forem demonstrados; cache/histórico não são default.
- Criatividade é condicional: busca exata preserva filtros; pesquisa exploratória pode divergir dentro do escopo e sem inventar sinais comerciais.
- Monte Carlo é planejado como investigação offline **após** estabilizar contratos/oracles e testes determinísticos, não como substituto de falha induzida nem dados reais.

## Gate 0 e execução

| Checagem | Estado |
|---|---|
| Inventário de owners/contratos e desk-review | REALIZADO |
| Remediações propostas dos cinco bloqueios G0-01..05 | DOCUMENTADAS NA V0.2, sem testes |
| Aprovação dos contratos tipados / decisão owner | PENDENTE |
| Licença, acesso e campos de dados de cada plataforma | NÃO VERIFICADOS AO VIVO NESTE PR |
| Testes INT-01..INT-35, RES-01..RES-24, CR-01..CR-04 | NOT_RUN |
| Monte Carlo da nova inteligência | NOT_RUN |
| YouTube/Meta canary, implementação, integração ou release | NÃO INICIADOS |
| Mudanças em `src/`, `SKILL.md`, `main`, testes/CI ou PR #17 | NÃO |

A compatibilidade foi **avaliada documentalmente, não aprovada operacionalmente**. O próximo gate é uma decisão explícita de aceitação dos contratos propostos da v0.2 e uma investigação de acesso/licença/cobertura das fontes antes da implementação. Não criar modelos, licenças, chaves, claims ou autorizações a partir destes documentos.

**Este PR permanece Draft, para review somente, sem promover `main` ou instalar skill.**
