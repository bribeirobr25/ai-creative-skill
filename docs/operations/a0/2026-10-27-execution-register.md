# A0 · Registro de execução e gates da evolução

**Data:** 2026-10-27  
**Estado:** preparação documental para revisão, não autorização de implementação.  
**Autorização A0 (2026-10-27):** criar, em branch/PR próprias, ADR-0004 PROPOSED, checklist M0, checklist pré-M2/M2 e este registro. **Proibidos neste A0:** merge, release, alteração src/ ou main, alteração da PR #17, dados privados, gastos, APIs de anúncios, envio a terceiros, instalação operacional ou alteração canônica.

## Linha de base verificada antes da PR A0

| Referência | Estado |
|---|---|
| Repositório | bribeirobr25/ai-creative-skill, branch main |
| HEAD main | 23c6dd641d5554178da67698c0008c8934811be4 |
| Security Gate | PR #20 integrado |
| Intelligence Architecture | PR #18 integrada; Gate 0 GATE_0_NOT_PASSED / OWNER_ACCEPTANCE_PENDING |
| Intelligence Lab | PR #23 integrado como offline/synthetic only, S1–S3; S4 e S5 não autorizados |
| Web 2.6 | PR #17 aberta, head 0baac348d94aa8006bde7ae374de331d5cfeaff7; não tocar no A0 |
| Ruleset Push Protection | ACTIVE, main, squash-only, required: Immutable V2.5 integrity; Boundary hardening candidate; scan-publication-diff |
| Outros Issues | #1 ADR-0002 T1–T7; #4 ZIPs mistos; #24 evidências administrativas parcialmente desatualizadas |
| Fonte canônica | src/ai-creative-skill/ mantida sem alteração |
| Referência de proposta | PROPOSTA-EVOLUCAO-v1.1-2026-10-26.md (anexo fornecido pelo proprietário) |

Status acima é snapshot datado, não substitui nova leitura de GitHub a cada ação.

## A0 — pacote / arquivo / gate

| Entrega | Artefato | Critério de aceite |
|---|---|---|
| A0-01 | docs/decisions/ADR-0004-PROPOSED-agent-workspace-durable-memory.md | Quatro camadas; quatro responsabilidades transversais; separação autoridade; stateless/stateful; privacidade real; efeito externo idempotente; build 2.6 independente; estado PROPOSED |
| A0-02 | docs/operations/a0/2026-10-27-M0-acceptance-checklist.md | PR #17, 7 browser tests, three checks, ISSUE #24, STATUS.md, M0b e gate release M1 descritos sem executar |
| A0-03 | docs/operations/a0/2026-10-27-pre-M2-M2-pilot01-acceptance-checklist.md | Contratos, SQLite, isolamento, scanner, 8 cenários, concorrência e salvaguardas |
| A0-04 | docs/operations/a0/2026-10-27-execution-register.md | Escopo/autorização, decisões por marco, dependências, riscos, responsáveis e logs de aceitação |
| A0-05 | PR A0 para main, em Draft | Diff restrito aos quatro arquivos; nenhuma alteração canônica, código, workflows, pacotes ou arquivos reais |

**A0 aceite técnico documental:** links e caminhos válidos; sem URLs confidenciais; headings coerentes; escopo fechado; scanner/checks CI revisados e status reportado honestamente. **Aceite de mérito:** revisão/decisão do proprietário separada; PR pode permanecer Draft. PR não deve fazer merge automático.

## Frentes, responsabilidades e dependências

| Trilha/marco | Entregável futuro | Responsabilidade de execução | Dependência / decisão do proprietário |
|---|---|---|---|
| A / M0 | PR #17 candidata Web 2.6 + STATUS/Issue #24 corrigidos | Implementação futura com revisão independente | Nova execução/aceite, merge #17 específico |
| A / M0b | Links Drive substituídos em candidata própria | Revisão de segurança + source owner | Política de acesso na origem, merge separado |
| A / M1 | Builder versionado 2.6, ZIPs e host limpo | Maintainer + tester de host | Gate release 2.6 separado |
| B / pré-M2 | Esquemas evento/tarefa; oráculos de idempotência/privacidade | Owner dos contratos + revisor | Aprovação específica do núcleo |
| B / M2 | SQLite, CLI e Piloto 01 | Owner runtime de memória + QA independente | Projeto, retenção, local privado e merge |
| B / M3 | Content Repurposing (corte por timecodes primeiro) | Video/Media owner | Mídia com direitos, ferramentas se necessárias |
| B / M4 | Agentes Ads Specialist/Writer/Video Maker | Coordenação/Ads owner | Escopos e envelopes de autonomia |
| B / M5 | Workspace, painel, scheduler e notificações | Runtime/UI owner | Hospedagem, credenciais e canal |
| B / M6 | CRM e Leads/Outreach fictícios inicialmente | Comercial + privacidade | Dados reais, base legal, comunicação externa em gate próprio |
| C / QB1–QB4 | Benchmarks de produto, personagem, comercial/áudio, upscale/reframe | **Dono nominal a designar até M1** | Ativos, escopo e aprovação humana |
| D / S4→S5→M7 | Resiliência sintética → canário de fonte real → Intelligence conectada | Owner de Research/Intelligence | Gate 0, direitos, fonte, operação, credenciais e custo, nunca presumidos |

O papel identificado aqui é responsabilidade proposta, **não** nomeação de pessoa, agente autônomo ou autoridade concedida.

## Registro de decisões (pendentes, não delegadas)

| ID | Momento | Decisão necessária | Situação |
|---|---|---|---|
| D-A0-01 | Após revisar PR A0 | Aprovar/revisar ADR-0004 | OPEN |
| D-A0-02 | Antes de qualquer merge A0 | Autorizar squash merge documental | OPEN |
| D-M0-01 | Após revalidar #17 | Autorizar merge #17 | OPEN |
| D-M1-01 | Após builder + host T1–T7 | Aprovar release 2.6 | OPEN |
| D-P2-01 | Após checklist de schemas/oráculos | Aceitar núcleo evento/tarefa | OPEN |
| D-M2-01 | Antes de dados reais/execução M2 | Definir armazenamento, retenção, projeto e assets | OPEN |
| D-M2-02 | Após piloto e revisão | Aceitar/merge Memory v1 | OPEN |
| D-M4-01 | Antes de autonomia | Envelopes e limites dos agentes | OPEN |
| D-M5-01 | Antes de operação contínua | Hosting, credenciais e notificações | OPEN |
| D-D-01 | Antes de S4/S5 | Escopo sintético S4 e posterior Gate 0/S5 específico | OPEN |

**Nenhuma decisão OPEN se converte em permissão pela conclusão de testes ou pelo avanço de outra trilha.**

## Mudanças e evidências após cada marco

A preencher **somente quando executado e observado**: data; owner; issue/PR; base/head; artefatos; comandos/testes; PASS/FAIL/BLOCKED/NOT_RUN/UNVERIFIED; inspeção humana; custo; incidentes; decisões e próxima ação. Evidência privada não é anexada ao GitHub público.

## Handoff do A0

Condição para iniciar a implementação: proprietário revisa a ADR-0004 PROPOSED e os critérios de aceite; somente o escopo específico que ele aprovar será liberado. Handoff entre frentes preserva referências/cânone/direitos, **permissions_carried: NONE**. O pacote A0 não executa nenhuma fase futura.
