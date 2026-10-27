# Intelligence · proposta arquitetônica

**Fonte atual para revisão:** [STATUS.md](STATUS.md), [architecture-v0.3.md](architecture-v0.3.md) e [acceptance-v0.3.md](acceptance-v0.3.md).

**Gate 0: NOT PASSED; owner acceptance pending.** Nenhuma proposta aqui autoriza integração canônica, fonte real, armazenamento, métricas derivadas, orçamento, publicação ou release. O laboratório offline consolidado está no [PR #23](https://github.com/bribeirobr25/ai-creative-skill/pull/23), baseado diretamente em `main`; os experimentos #19/#21/#22 são apenas registro histórico de evolução e testes anteriores.

## Responsabilidades

`Research Evidence Synthesis` mantém autoridade sobre `research_execution`, source outcomes, Evidence Records, Evidence Clusters e status. Os métodos Ad/Funnel e Product/Marketplace detêm as entidades de domínio. Execution Contracts mantém aprovação, custo, stop codes, HANDOFF_PACKET e onboarding de provedores. Project Profile e AUTONOMY_ENVELOPE detêm autorização de ação. A análise estatística proposta não é um Specialist Method formalmente aprovado.

## Histórico de concepção, NÃO corrente

Arquitetura [v0.1](history/architecture-preimplementation-v0.1.md) e [v0.2](history/architecture-preimplementation-v0.2.md); matrizes [v0.1](history/acceptance-and-validation-v0.1.md) e [v0.2](history/acceptance-and-validation-v0.2.md); [revisão Gate 0](history/gate0-contract-compatibility-review-v0.1.md); [auditoria forense](history/forensic-audit-2026-10-23.md); [plano de segurança](history/revised-roadmap-security-gate-2026-10-23.md); [plano de simulação](history/simulation-adversarial-plan-v0.1.md). Estes documentos preservam raciocínios históricos e podem conter estados, URLs e esquemas superados. Não são instruções de execução nem fontes atuais de contratos.

Os materiais documentais antigos estão arquivados em [history/](history/README.md) e não definem o estado atual. O roteiro pessoal de candidatura ao YouTube foi excluído do snapshot candidato; commits anteriores da branch pública ainda podem conter versões antigas, motivo adicional para considerar squash merge após revisão. Modelos pessoais de candidatura devem permanecer em armazenamento privado.

## Limites permanentes da proposta

Gate 0 e integração canônica exigem decisões explícitas do proprietário e reconciliação versionada dos contratos. O laboratório offline não transfere autoridade para `src/` e não autoriza APIs reais, gasto ou publicação. O PR #17 mantém sua própria governança e inventário, independente desta pesquisa.
