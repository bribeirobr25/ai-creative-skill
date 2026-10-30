# ADR-0004 · Evolução modular: capacidades, memória durável e Agent Workspace

> **Status note (2026-10-30):** this proposal was never accepted.
> - [ADR-0005](ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md) proposes to supersede part of it.
> - The text below is unchanged from PR #30 (commit `dfe39ca`) and is kept as a historical record.

**Data:** 2026-10-27  
**Status:** PROPOSED — decisão do proprietário pendente.  
**Autoridade:** proposta de evolução v1.1 de 2026-10-26; complementa ADR-0001, ADR-0002 e a ADR-0003 ainda proposta, sem substituí-las.  
**Escopo desta ADR:** arquitetura-alvo e invariantes. Não aprova implementação, alteração canônica, Gate 0 de Intelligence, merge, release, dados reais, envio externo, credenciais, gasto ou publicação.

## Problema e objetivo

A AI Creative Skill possui uma árvore canônica portátil (src/ai-creative-skill), métodos criativos, contratos, controles e algumas rotas locais. Projetos longos precisam de estado recuperável, ativos relacionados, colaboração entre profissionais e visibilidade operacional. A resposta proposta **não** é replicar métodos, permissões ou memórias por agente, nem obrigar o usuário de uma operação simples a instalar uma plataforma multiagente.

**Objetivo testável:** um projeto recupera o estado vigente, executa uma capacidade independente e pode ser retomado após interrupções, com e sem serviço de memória.

## Decisão proposta: quatro camadas lógicas

| Camada | Responsabilidade | Não é dona de |
|---|---|---|
| L1 — Core da skill | Stage 0, Work Profiles, Specialist Methods, Execution Contracts, Research Evidence Synthesis, critérios de QA e manifests | Dados de clientes, estado de projetos ou credenciais |
| L2 — Capacidades invocáveis | Entrada/saída/status de operações independentes (Web, Research, Ads, imagem, vídeo, áudio, upscale, reframe, repurposing e, futuramente, Intelligence) | Banco de memória ou agendador obrigatório |
| L3 — Estado e memória, opcional | Event Store, projeções de projeto, decisões, ativos e linhagem, experiências, estado operacional e recuperação | Regras canônicas de criação ou autorização implícita |
| L4 — Agent Workspace, opcional e com versão própria | Papéis, Coordinator, tarefas, mensagens, agenda, notificações e interfaces/CRM | Métodos próprios, aprovação substituta ou banco concorrente de verdade |

**Dependências:** L2 conhece apenas contratos de dados; não importa L3. No modo stateless recebe contexto suficiente da requisição e entrega o resultado. No modo stateful recebe contexto recuperado pelo chamador e **propõe/emite** eventos; o serviço L3 verifica e persiste, quando autorizado. L4 usa as mesmas capacidades de L2; painel e CRM são projeções de L3, não bases paralelas. A skill permanece distribuível e utilizável sem L3/L4.

**Quatro responsabilidades transversais, não quatro servidores:**
- [C] Contratos versionados: evento, tarefa, mensagem, Capability Registry e Agent Role Contract.
- [G] Governança: Project Profile, AUTONOMY_ENVELOPE, Approval/Budget Ledger, STOP, HANDOFF_PACKET, direitos, privacidade, Security Gate e CI.
- [A] Adaptadores elegíveis: ferramentas locais, provedores criativos, Drive, transcrição, e-mail, calendário e APIs, com onboarding sob EC §24 quando apropriado.
- [V] Validação: inventário de candidatas, gates V2.5/2.6, harness, ADR-0002 T1–T7, QA contextual e benchmarks humanos.

## Invariantes e autoridade

1. Uma autoridade por assunto. Core da skill (L1) e cânone de cada projeto (estado L3) são distintos. O projeto não reescreve a skill; a skill não inventa o cânone do projeto.
2. Toda capacidade e suboperação com valor próprio pode iniciar, executar, fazer QA proporcional e parar sem executar fases adjacentes. A sugestão de continuação não autoriza execução (ADR-0002).
3. Delegação transfere referências e tarefa, não permissões: **permissions_carried: NONE**, verificação de autoridade em cada efeito.
4. Autonomia é por classe de ação e contexto: criar/propor pode ser permitido; acesso a dados, gasto, contato com terceiros, publicação, modificações canônicas e ações irreversíveis dependem dos gates aplicáveis, incluindo base legal quando necessária.
5. Eventos distinguem **fato observado**, **mudança solicitada** e **decisão autorizada**. A observação, o feedback, o teste sintético ou a aprovação de um único ativo não promove automaticamente uma regra permanente.
6. Conceito novo exige owner, definição/contrato e justificativa. EC §1.1 só registra aliases para o mesmo conceito; métodos novos exigem a Growth Rule do Specialist Method System §16.
7. Mudanças em src/ usam candidate inventory versionado. A referência histórica V2.5 permanece imutável e verificável. O A0 não altera src/.
8. Dados privados, mídia de clientes, bancos, logs operacionais e segredos ficam fora do repositório público.
9. Maturidade técnica, validação em contexto e autorização são eixos distintos. Um relatório sintético aprovado não certifica host/produção nem concede direitos.

## Contratos [C] e persistência (decisões de desenho; não implementados neste A0)

A ADR fixa somente os limites abaixo. Os esquemas detalhados de cada marco serão revisados e aprovados separadamente.

**Evento — núcleo pré-M2:** event_id (registro único); idempotency_key (operação lógica); schema_family/schema_version; project_id; event_kind (OBSERVED, CHANGE_REQUESTED, DECISION_RECORDED); object_type/object_id; event_type (acontecimento específico); expected_revision/resulting_revision; actor; authority_ref obrigatório para decisões; causation_id/correlation_id; evidence_refs; supersedes; privacy_class/retention_policy_ref; personal_data_refs; occurred_at/recorded_at. Compatibilizar os nomes e os estados com os proprietários existentes antes da aprovação dos esquemas. O emissor não obtém automaticamente o direito de persistir um evento ou autorizar uma decisão.

**Tarefa:** task_id e chave de idempotência, project_id, capacidade, solicitante/responsável, entradas/referências, estado, dependências, prazo opcional, revisão, conclusão verificável, autorização aplicável e permissions_carried: NONE. **Mensagem:** conversation, task_request ou handoff; delegações executáveis resultam em tarefas rastreáveis, com contenção de ciclos. **Agent Role:** objetivo, capacidades/ferramentas, memória permitida, limites de autonomia/delegação/concorrência/tentativas/custo, escalonamento e contexto temporário não canônico.

**Capacidade:** registro derivado do Manifest/Registry e das evidências, não novo adjudicador de autorização. Separar maturidade técnica, evidência de validação por host/rota/versão/caso e permissão efetiva no projeto. Primeiro canário pode executar como experimento explicitamente autorizado sem alegar validação prévia.

**Durabilidade:** SQLite transacional para Memory v1 local; JSONL para exportação de auditoria; PostgreSQL apenas com demanda real. Estado atual materializado a partir de eventos verificáveis; prevenção de duplicações e gravações obsoletas (EC §§2.2–2.3). Ativos com asset_id/hash/proveniência e dependências revisionadas. Mudança de autoridade invalida somente os derivados efetivamente dependentes (EC §10.1), preservando o registro histórico.

**Privacidade e apagamento:** event store minimizado; dados identificáveis em armazenamento apagável separado quando aplicável. *Somente referências* não garantem anonimização: actor, IDs, timestamps, caminhos, logs, exportações, índices e backups podem identificar pessoas. Estabelecer acesso, retenção, exclusão verificável e política de backup/expiração antes de dados pessoais reais; exceções legais são explicitadas. Nunca prometer apagamento absoluto apenas pela deleção de uma linha de conteúdo.

**Dois níveis de idempotência:** uma chave de evento evita duplicação de registros, **não** garante que uma ação externa foi executada uma única vez. Rotas com efeitos externos usam identidade durável da tentativa/job, approval binding, reserva de custo quando aplicável e reconciliação de resultado UNKNOWN antes de qualquer repetição, conforme Execution Contracts. Nenhuma segunda submissão automática após confirmação perdida. Exercitar com simulador antes de habilitar provedores reais.

**Portabilidade dos contratos:** fonte canônica única dos schemas e hashes. Durante M2, implementação isolada em apps/agent-workspace ou schemas/ não é parte do pacote portátil. Contratos necessários à skill distribuída só poderão ingressar em src/ por candidata posterior a 2.6, acompanhada de testes de inclusão e hashes dos dois formatos de build.

## Fronteiras de segurança e distribuição

- O Workspace é opcional e versionado independentemente. src/ não importa apps/ nem experiments/; testar a fronteira.
- .gitignore é comodidade, **não bloqueio de publicação**. Antes de incluir armazenamento operacional, ampliar o Security Gate com bloqueio adequado para bancos, logs e diretórios privados mesmo com git add -f, preservando fixtures sintéticas permitidas e verificáveis.
- A publicação pública exige preflight antes do primeiro push; checks de PR são defesa adicional, não desfazem vazamento histórico.
- A release 2.6 exige **um builder/versionamento novo e independente** para os pacotes 2.6: o packaging/build.py existente está propositalmente preso à V2.5, com hashes históricos. Não afrouxar nem substituir esse gate; testar os dois pacotes 2.6 efetivamente gerados em host limpo.
- Gate 0 de Intelligence permanece GATE_0_NOT_PASSED / OWNER_ACCEPTANCE_PENDING; S1–S3 são laboratório sintético já integrado, S4 só sob escopo sintético aprovado, S5 fontes reais com direitos/credenciais/autorizações separados.

## Roteiro em quatro trilhas

- **A — Core/distribuição:** M0 (#17 + reconciliação documental) → M0b (links Drive em candidata separada) → M1 (host limpo, ADR-0002 T1–T7, builder 2.6 e gate de release).
- **B — Memória/experiência:** pré-M2 (esquemas testados) → M2 (SQLite + Piloto 01) → M3 (repurposing, primeiro timecodes) → M4 (trio de agentes piloto sob demanda) → M5 (painéis/agendador) → M6 (CRM fictício antes de dados reais).
- **C — Qualidade real:** QB-1 produto, QB-2 personagem, QB-3 comercial/áudio, QB-4 upscale/reframe; cada benchmark guarda evidências, aceitação humana e recomendações versionadas.
- **D — Intelligence:** decisões de método/fonte/direitos e Gate 0 → S4 sintético aprovado → S5 canário real estritamente autorizado → M7 Intelligence conectada.

Gates da release 2.6 e do Memory v1 **independentes**; pré-M2/M2 podem progredir em branch isolada sem alterar src/ enquanto M0/M1 avançam. M4 exige fundamentos M1/M2; M5 exige coordenação M4; dados reais M6 exigem políticas de privacidade; M7 exige decisões D/S5. Cada marco oferece demonstração útil, QA proporcional, retrospectiva curta e aprovação de merge separada.

## Alternativas rejeitadas / adiadas

- Redesenhar o Core, impor Workspace a cada tarefa, conceder autoridade a agentes, duplicar bancos por perfil, promover experimentos como produção.
- Microserviços, broker, vetores como fonte da verdade e autonomia contínua antes de teste de retomada/delegação.
- Envio de outreach, gastos, publicação ou acesso a API real apenas porque um método/fixture existe.

## Aceitação desta ADR

Esta ADR só deixa **PROPOSED** após aceite explícito do proprietário, verificação com ADR-0001/0002/0003 e contratos atuais e avaliação dos limites. Sua aprovação arquitetural futura **não** autoriza execução de marcos posteriores, acesso externo, migração canônica, merge ou release. Os critérios operacionais encontram-se nos checklists A0. Os resultados dos pilotos deverão atualizar evidências e, se apropriado, motivar ADR/candidata versionada — sem reescrever este registro histórico.

## Referências

- docs/decisions/ADR-0001-source-of-truth.md; ADR-0002-capability-bounded-invocation.md; ADR-0003-PROPOSED-development-review-and-publication-safety.md.
- src/ai-creative-skill/references/: Architecture Spec, Execution Contracts, Calibration and Experience Memory, Specialist Method System, Work Profile Organic (source-derived atomization).
- docs/research/intelligence/architecture-v0.3.md; docs/research/intelligence/STATUS.md; experiments/intelligence/README.md.
- Origem de planejamento: **PROPOSTA-EVOLUCAO-v1.1-2026-10-26.md** (anexo do proprietário, ainda não commitado aqui).
