# Intelligence · Pesquisa arquitetônica (PR #18)

**Estado:** GATE 0 DESK REVIEW REALIZADA · COMPATIBILIDADE CONDICIONAL · ACEITE DO PROPRIETÁRIO PENDENTE · NÃO CANÔNICA/NÃO EXECUTADA  
**Base:** `main` 2.6.0-dev no commit `fb7f794ca2c51c2752afde5f907bd2866c9d1f25`; V2.5.0 no commit `39a0bfa39270ea4b685b0f862e7dbf647cf81d77` preservada.  
**Branch:** `proposal/intelligence-architecture-pre-v0-1-20261023` (nome histórico da branch, apesar da revisão documental v0.2).  
**PR #17:** paralelo e não alterado.

## CORREÇÃO POSTERIOR: USO PESSOAL + AUTORIZAÇÃO ANALÍTICA DO YOUTUBE (2026-10-23)

O proprietário esclareceu que a ferramenta é **de uso próprio e não será comercializada**. A auditoria anterior também deixou de considerar a [política adicional do YouTube introduzida em 2026](personal-use-youtube-2026-policy-clarification.md), que prevê scores, comparações e retenção ampliada para determinados casos de Analytics & Reporting **formalmente aprovados**. Portanto, o bloqueio do YouTube é de **escopo e autorização ainda não resolvidos**, não de inviabilidade absoluta de rankings/outliers. O uso pessoal não concede automaticamente permissões especiais, e eventuais pesquisas para campanhas de marca merecem classificação por finalidade. A revisão mantém `GATE_0_NOT_PASSED` até essa verificação, preservando as conclusões históricas anteriores com a correção visível.

## ALERTA DE AUDITORIA INDEPENDENTE (2026-10-23)

**Status atualizado: `GATE_0_NOT_PASSED / IMPLEMENTATION_BLOCKED`.** A [auditoria forense independente](forensic-audit-2026-10-23.md) identificou 4 achados P0, 7 P1 e 5 P2. **Principal bloqueio:** a política oficial da YouTube Data API restringe agregações, métricas derivadas e armazenamento de dados de terceiros; não podemos assumir que ela permite o algoritmo de outliers/viralidade planejado. O vertical slice “YouTube primeiro” requer revisão de fonte/licença e finalidade **antes** de qualquer implementação.

Os documentos v0.1/v0.2 abaixo continuam como **propostas históricas sob crítica** e não conferem licença, aprovação de arquitetura, readiness nem permissão de consulta paga. Esta auditoria é estática e não executa dados/API; não altera os contratos canônicos ou a `main`.

## Aprendizado promovido a proposta de governança transversal

O [PR #20](https://github.com/bribeirobr25/ai-creative-skill/pull/20) contém a **ADR-0003-PROPOSED** e um guard experimental de publicação, com scanner de diff, testes e workflow de PR. A intenção é aplicar a segurança de publicação e o ciclo PLAN → IMPLEMENT → VERIFY → REVIEW → LEARN a **todas** as capacidades, não apenas Intelligence.

**Importante:** o guard ainda não foi integrado à main nem é invocado automaticamente por escritas via GitHub connector. A varredura de histórico completo continua pendente. O [PR #19](https://github.com/bribeirobr25/ai-creative-skill/pull/19) registra separadamente correções de revisão cruzada e suas limitações; a sessão de website continua dona do PR #17.

## Nova prioridade: revisão cruzada e proteção do Git público

A [sequência revisada e o Security/Privacy Gate](revised-roadmap-security-gate-2026-10-23.md) passam a orientar o **planejamento** antes da implementação real: primeiro triagem de possível exposição em repositório/histórico, revisão cruzada dos PRs #18/#19 e estabelecimento de controles pré-publicação; depois fonte e autorização, testes avançados e integração. **O procedimento está documentado, mas scanner/hook ainda não foram instalados e a auditoria específica de exposição ainda não foi executada.** PR #17 permanece sob seu responsável até a retomada.

## Viabilidade de fontes e laboratório sintético

- [YouTube: roteiro de solicitação Analytics & Reporting (23/10/2026)](youtube-analytics-approval-checklist-2026-10-23.md): formulário oficial, inscrição como pessoa física, evidências e texto-base. Ainda não submetido; não inserir informações privadas no GitHub.
- [YouTube: policy preflight por operação (23/10/2026)](youtube-source-permission-preflight-2026-10-23.md): política geral, aprovação adicional para Analytics & Reporting, retenção por classe de dados e quota. Verificação documental, **sem chaves, chamadas ou aprovação recebida**.
- [PR #19 · Canário sintético independente](https://github.com/bribeirobr25/ai-creative-skill/pull/19): experimento Python offline, não integrado à skill; resultados dos testes devem ser consultados no CI do PR. Os algoritmos desse PR **não podem receber dados reais da YouTube API sem verificação de permissão**.

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
