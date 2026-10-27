# A0 · Checklist pré-M2, M2 e Piloto 01 — memória confiável

**Data:** 2026-10-27  
**Status:** proposta de critérios fechados para revisão; não é autorização para criar banco, executar fluxo, usar ativos privados, instalar infraestrutura ou alterar src/.  
**Gates próprios:** pré-M2 → autorização do núcleo → M2 em branch isolada → testes/Piloto 01 → revisão independente → eventual merge autorizado. Independente do gate da release 2.6.

## Pré-M2 — contratos mínimos, antes do código de memória

- [ ] P2-01. Confirmar owners: contratos EC §§2.2/2.3 (versionamento/revisão), §10/10.1 (linhagem/invalidação), Project Profile (cânone), Calibration (experiência) e ADR-0002 (operação independente). Não registrar todo conceito novo como alias EC §1.1.
- [ ] P2-02. Especificar esquema de evento versionado: event_id, idempotency_key, schema_family/schema_version, project_id, event_kind, event_type, object_type/object_id, revisions esperada/resultante, actor, authority_ref, causation_id/correlation_id, evidence_refs, supersedes, privacy_class/retention_policy_ref, personal_data_refs, occurred_at/recorded_at. Tipos de evento são propostos até aprovação.
- [ ] P2-03. Especificar esquema mínimo de tarefa: id, chave de idempotência, projeto, origem, executor, capacidade, entradas, dependências, estado, revisão, prazo, conclusão, limite de autoridade e permissions_carried: NONE; reconciliar vocabulário com contratos existentes.
- [ ] P2-04. Definir projeção atual e regras de aceite: OBSERVED não equivale a DECISION_RECORDED; autoridade não inferida; record revision monotônica; contradição e dados obsoletos falham fechado. Definir migração de esquema com STOP_SCHEMA_MIGRATION_REQUIRED.
- [ ] P2-05. Testar idempotência (mesma operação lógica, duas tentativas → um efeito de estado); revisões conflitantes → STALE_WRITE_REJECTED; causalidade; evento inválido/sem autoridade → rejeição; mudanças concorrentes em projetos diferentes → isolamento.
- [ ] P2-06. Modelar minimização, classificação, retenção, apagamento e backups: identificadores, timestamps, caminhos e logs também podem identificar; testes fictícios para exclusão, índice e expiração de cópias.
- [ ] P2-07. Definir dualidade stateless/stateful: mesmo executor de capacidade com input suficiente não importa memória; stateful recebe contexto pre-resolvido e emite eventos que só L3 autorizado pode persistir.
- [ ] P2-08. Revisão de segurança e escopo dos schemas; sem mudança canônica ou dependência no build V2.5/2.6. Aprovação explícita do proprietário do **núcleo** antes do M2.

**Exit pré-M2:** esquemas revisados e testados (versão exata e fixtures), fronteira/autoridade documentada, sem novas permissões, aceite específico do proprietário. Se faltar, M2 BLOCKED.

## M2 — implementação mínima em SQLite

- [ ] M2-01. Criar runtime isolado de memória local, com SQLite transacional, constraints/índices, controle otimista e migrações determinísticas. Nada em src/; nada em bancos remotos.
- [ ] M2-02. Implementar CLI para registrar evento autorizado, consultar projeto/objetos, recuperar contexto suficiente, inspecionar decisões atuais e listar refs de ativos com hashes/linhagem; export JSONL apenas para auditoria sanitizada.
- [ ] M2-03. Gravar eventos de forma idempotente, transacional, com chave lógica separada de event_id; reconstruir projeções e reabrir após reinício sem perda/duplicação.
- [ ] M2-04. Atuar somente sobre decisões com authority_ref verificável; testes para aprovação e revogação; invalidação seletiva EC §10.1 por dependencies de revisão, nunca por estar na mesma sessão.
- [ ] M2-05. Preservar assets como referências estáveis a armazenamento autorizado, não URLs temporárias como autoridade. Confirmar inexistência de inclusão de mídia privada no banco/repo público.
- [ ] M2-06. Implementar separação e política minimizada de dados pessoais **com fixtures**, considerando vazamento via metadados/logs, backups e índices; sem prometer apagamento total só por nulificar uma referência.
- [ ] M2-07. Antes do primeiro arquivo operacional: .gitignore + regra BLOCK no scanner para banco/log real, inclusive git add -f e caminho fora do diretório previsto; permitir **apenas fixtures fictícias explicitamente classificadas**. Testar a própria regra, com exemplos que falham e exemplos permitidos.
- [ ] M2-08. Testar fronteiras: src/ não importa apps/ ou experiments/; Workspace não exige GitHub/Drive/provedores para funcionar com fixture; nenhuma ação externa, custo ou publicação.
- [ ] M2-09. Registro de falhas e tempos; revisão independente das garantias de concorrência, exclusão e reprocessamento. Merge exige autorização específica.

## Piloto 01 — oito cenários obrigatórios

- [ ] T01. Registrar decisões aprovadas e referências de ativos com provenance e autoridade explícitas; manter exemplos de eventos OBSERVED e CHANGE_REQUESTED não promovidos.
- [ ] T02. Encerrar processo, iniciar outra sessão e recuperar o estado correto (incluindo dados obsoletos/revogados excluídos da projeção atual).
- [ ] T03. Executar uma capacidade independente usando contexto stateful recuperado e inputs autorizados.
- [ ] T04. Registrar entrega e vínculo a original/derivado com asset_id/hash/timecodes quando aplicáveis, sem transformar QA técnico em aprovação humana.
- [ ] T05. Revogar decisão; garantir que não volte como vigente em buscas, projeções ou resumos.
- [ ] T06. Executar a **mesma** capacidade com input explícito em modo stateless; output comparável e nenhuma chamada ao serviço de memória.
- [ ] T07. Interromper antes da confirmação e retomar; nenhum evento/tarefa/asset lógico duplicado. O teste local não promete idempotência de ações externas.
- [ ] T08. Alterar/revogar referência aprovada usada por derivados: **somente dependentes reais** recebem ACCEPTANCE_INVALIDATED; independentes mantêm aceitação.

**Casos adicionais obrigatórios:** duas escritas com expected_revision idêntico → segunda recebe STALE_WRITE_REJECTED; projeto A nunca lê ou afeta B; tentativa de publicar banco/log operacional em PR → scanner BLOCK; fixture fictícia passa; exclusão com dados fictícios alcança conteúdo, metadados/índices/expiração ou documentação honesta da limitação de backup. Reexecução produz resultados reproduzíveis.

## Fronteira de efeitos externos, antes de M4/M5

- [ ] Criar depois um simulador de job externo que aceite solicitação mas perca confirmação; o Coordinator consulta identidade/status do mesmo job e não reenvia cegamente, com registro de UNKNOWN, tentativas e reserva de custo quando aplicável. Não usar provedores reais nesse teste.
- [ ] Orçamento, publicação, contatos e coleta de dados reais continuam bloqueados sem os gates canônicos.

## Condições de saída

M2 só é considerado útil quando há um projeto que **recupera o estado correto, executa uma capacidade concreta e reinicia sem perder nem duplicar trabalho**. Artefatos do piloto: comandos de reprodução, schemas, banco fictício isolado, registro sanitizado, diff, matriz dos 8 cenários, bloqueios/resíduos, revisão humana e resumo de aprendizado. Dados do projeto real ficam privados e não entram em evidência pública.

**Pendências reservadas ao proprietário:** aprovação ADR-0004 e núcleo pré-M2, projeto real/ativos autorizados, armazenamento privado, retenção e eventual merge. Este checklist não concede essas aprovações.
