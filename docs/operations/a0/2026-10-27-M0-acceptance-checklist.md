# A0 · Checklist de aceitação M0 e fronteira M0b/M1

**Data:** 2026-10-27  
**Status:** checklist PROPOSED; nenhum item abaixo equivale a execução concluída.  
**Base congelada para este planejamento:** main 23c6dd641d5554178da67698c0008c8934811be4; PR #17 head 0baac348d94aa8006bde7ae374de331d5cfeaff7 (estado deve ser atualizado ao executar).  
**Escopo desta PR A0:** escrever critérios, não modificar #17, seus testes/código, a main, os issues, os manifests, o scanner nem o builder.

## Objetivo / fora de escopo

Preparar e aceitar uma integração futura da candidata Web Runtime 2.6 (PR #17), reconciliar documentação de status e verificar o ruleset, **sem aprovar a release**. M0b é uma candidata separada para referências Drive em src/. M1 exige builder/empacotamento 2.6 próprio e ensaios de host limpo.

### M0 — aceitação fechada da PR #17

- [ ] M0-01. Registrar head/base atuais de #17 e main; atualizar a branch estritamente pelo caminho de integração autorizado. Preservar mudanças e evidências históricas; não resolver conflitos mudando contratos sem novo escopo aprovado.
- [ ] M0-02. Congelar diff e inventário de 17 arquivos da candidata na revisão; confirmar candidate inventory v2 e escopo cumulativo v1→v2, fonte protegida e todos os registros históricos imutáveis.
- [ ] M0-03. Reexecutar python -m validation.release_integrity: integridade V2.5 preservada, sem modificar hashes históricos.
- [ ] M0-04. Reexecutar python -m validation.candidate_integrity e python -m validation.candidate_tests no head atualizado; anotar exact SHA, ambiente, status e logs.
- [ ] M0-05. Executar **de verdade** as sete verificações de navegador que podem ser puladas no CI. Registrar Playwright/Chromium e versões, evidências por caso, 1440/390/320 quando pertinentes, imagem colapsada, lazy-loading, ausência de servidor (file://) e caso de infinite scroll/limite de varredura. Não contabilizar SKIP como PASS.
- [ ] M0-06. Executar python -m validation.harness --profile candidate --host --check; reportar PASS/FAIL/BLOCKED/NOT_RUN/UNVERIFIED **separadamente**, inclusive defeitos esperados não corrigidos.
- [ ] M0-07. Verificar na PR, no head exato, os jobs Immutable V2.5 integrity, Boundary hardening candidate e scan-publication-diff; revalidar updates após qualquer mudança de head.
- [ ] M0-08. Verificar proteção ativa, squash-only, required checks e PR up-to-date; audit/proteção de dados antes de qualquer push. Corrigir sem alargar o escopo da #17.
- [ ] M0-09. Revisão independente focada nas mudanças Web 2.6 (roteamento sem falso positivo; paths privados; records TODO; UI/QA de imagens; método de etiqueta; direitos; limites da qualidade). Registrar defeitos residuais ou justificativa de aceite.
- [ ] M0-10. Aprovação específica do proprietário para squash merge da #17; confirmar novo head de main e CI pós-merge. **Nunca inferir merge autorizado a partir deste documento.**
- [ ] M0-11. Em mudança documental própria, atualizar docs/research/intelligence/STATUS.md: #20/#18/#23 integradas, S1–S3 como laboratório sintético, Gate 0 ainda não aprovado; não alterar condições de S4–S6.
- [ ] M0-12. Atualizar Issue #24 com evidências do ruleset aplicado e checagens ainda não comprovadas (revisores independentes, proteção nativa de segredos, history audit, tag protection); não fechar a Issue apenas porque os três checks são obrigatórios.
- [ ] M0-13. Registrar Issue #4 como pendente de classificação dos ZIPs mistos sem excluir mídia autorizada. Não realizar limpeza neste marco.

**Exit M0:** #17 integrada somente após autorização, CI do novo head green, sete testes browser efetivamente demonstrados, resultados limitados interpretados corretamente, STATUS/Issue #24 reconciliados. Bloqueios e exceções exigem decisão explícita; nenhum status PASS é presumido.

### M0b — correção separada de referência Drive

- [ ] Inventariar e recontar no head de trabalho três arquivos hoje identificados: media/README_PTBR.md e media/registry/provider_capabilities_v0.2.json / v0.3.json sob src/ai-creative-skill/. Não repetir no relatório público URLs/IDs reais.
- [ ] Classificar o recurso na origem (permissões, acesso histórico incerto, ação exigível), sem afirmar vazamento provado; considerar histórico/forks/caches independentemente da correção em HEAD.
- [ ] Substituir a referência por IDs lógicos aprovados em candidata versionada própria, **depois da #17**; candidate inventory, regressões, scanner e revisão independentes.
- [ ] Solicitar autorização de merge separada. Não fazer reforma do histórico público sem escopo e permissão específicos.

### M1 — fronteira da release 2.6 (não incluída em M0)

- [ ] Projetar e revisar **build/release 2.6 separado**: packaging/build.py atual é reprodutor imutável da V2.5; não alterar/remover seu gate histórico para empacotar a candidata.
- [ ] Validar fonte/manifests/hashes dos ZIPs 2.6 Agent Skill e Plugin; confirmar conteúdo consistente entre ambos e inexistência de dependência obrigatória do Workspace/Drive/GitHub.
- [ ] Instalar os **ZIPs reais** em host limpo; executar ADR-0002 T1–T7 em Web, Research e direção de produto com evidência, contexto e estado por rota/host/versão.
- [ ] Verificar QA de navegador, acessibilidade e edição localizada em cenário autorizado; distinguir adequação funcional, avaliação criativa e aprovação humana.
- [ ] Submeter gate de release 2.6 ao proprietário como decisão separada, mesmo após eventual merge #17.

## Evidência mínima / bloqueadores

Para cada teste: identificador, SHA de código, comando, versão do host/browser, insumo autorizado/sintético, resultado bruto, evidência e classificação. Sem evidência confiável: NOT_RUN/UNVERIFIED ou BLOCKED; não converter em PASS. Nenhum dado privado em anexos públicos.

**Bloqueadores do merge de #17:** checks obrigatórios falhos/ausentes, escopo ou inventário violado, integridade histórica alterada, publicação insegura, QA obrigatório não realizado sem exceção formal, autoridade de merge ausente. 

**Handoff para M1:** entregar heads, artefatos de QA, defeitos, versão candidata, dependências de build e restrições; permissions_carried: NONE.
