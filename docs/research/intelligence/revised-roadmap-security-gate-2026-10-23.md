# Ordem revisada de desenvolvimento e Security Gate · Intelligence · v0.1

**Data:** 2026-10-23  
**Estado:** PLANO DE CONTROLE PREVENTIVO · PROPOSTA NÃO CANÔNICA · S0 ENCERRADA POR DECLARAÇÃO DO PROPRIETÁRIO · SCANNER CANDIDATO NO PR #20 (AINDA NÃO INTEGRADO À MAIN)  
**Escopo:** PRs #18 e #19 e todos os futuros commits públicos da AI Creative Skill; alinhamento com ADR-0001 (código/documentação públicos, materiais privados fora do Git). O PR #17 pertence à sessão Claude Code de Web Experience e não deve ser modificado por esta frente.

## Atualização operacional: fase S0 encerrada por decisão do proprietário (23/10/2026)

O proprietário confirmou que os materiais de mídia sob sua responsabilidade foram **gerados com IA ou captados em fotografia/vídeo por ele**, e que os **textos são de sua autoria**. Solicitou o encerramento desta fase. A auditoria S0 fica `CLOSED_BY_OWNER_ATTESTATION_WITH_RESIDUAL_LIMITATIONS`, registrada no [relatório S0 do PR #20](https://github.com/bribeirobr25/ai-creative-skill/blob/proposal/reusable-development-security-gate-20261023/docs/security/S0-consolidated-text-exif-email-triage-2026-10-23.md). Isso não declara inspeção técnica integral, licença de eventuais materiais de terceiros, nem decisão específica de tornar público endereço de autoria Git.

A tabela abaixo preserva **a sequência planejada originalmente**, inclusive o trabalho que S0 exigia. Sua pendência administrativa de mídia/textos foi encerrada por atestação; a implantação de controles pré-publicação, adoção da ADR-0003 e Gate 0 de contratos/permissões **não foram aprovados automaticamente**. Para a frente Intelligence, a próxima execução é **S1/S2 (revisão técnica dos PRs #19/#18)** e o contrato `SOURCE_PERMISSION_PREFLIGHT`, sem fonte real/paid API. PR #17 permanece independente.

## 1. Decisão de sequenciamento

**Uma revisão cruzada real e um Security/Privacy Gate vêm ANTES de novos conectores e de qualquer tentativa de merge.** PRs experimentais continuam em Draft até que as condições aplicáveis sejam satisfeitas. CI verde comprova só os testes efetivamente executados, não valida o todo.

| Ordem | Tarefa | Owner / output | Gate |
|---|---|---|---|
| **S0: agora** | Inventariar possíveis informações privadas no repositório público, branches/PRs e commits/histórico relevante sem copiar conteúdos sensíveis para relatórios públicos; confirmar classificação | Responsável de segurança/documentação, relatório **privado** de exposição quando houver detalhes; sumário público sem segredos | Qualquer vazamento de credencial/URL assinada ativa contenção |
| **S1: agora** | Revisão cruzada do PR #19: `NO_RESULTS` vs `INSUFFICIENT_EVIDENCE`, seleção de snapshots, filtro repetido, validação inicial de `limit`, propagação de `requested_national_top`, vínculo `evidence_id`, testes | PR #19, testes unitários/adversariais; mantenha política sintética e não misture com runtime canônico | Revisão concluída e CI dos testes executáveis |
| **S2: paralelo** | Revisar contratos do PR #18 contra `RESEARCH_EVIDENCE_SYNTHESIS` e `HANDOFF_PACKET`, inclusive states/owners/independence, com foco em semântica de resultado vazio e cobertura | Documento v0.3 candidato, sem sobrescrever v0.1/v0.2 | Owner review + Gate 0 |
| **S3: antes de APIs reais** | Revisão de fonte, finalidade, direitos, retenção e aprovação Analytics & Reporting (quando aplicável); demonstrar fonte permitida e escopo real | `SourceCapabilityRecord` verificável e matriz de permissões | Sem uso derivado/persistente não autorizado |
| **S4: somente offline** | Melhorar estatística e teste sintético: seleção temporal determinística, coortes elegíveis, seeded/mutation/fault tests, Monte Carlo mais informativo com quotas/retries/correlação | Provas matemáticas sintéticas, limites de evidência, análise de sensibilidade | Sem tráfego externo; não extrapolar taxas simuladas |
| **S5: depois de S0–S4** | Preparar contrato executável mínimo/host adapter (reutilizar core), canary permitido e QA no host escolhido | Branch candidata separada; autorização aplicável antes de dados reais | Passar Gate 0 + direitos + testes |
| **S6: depois de canaries** | Integração regressiva, auditabilidade de resultados, revisão de privacidade e release gate; MCP continua opcional | Candidate/release sujeito a aceite | Nunca inferir release de PR draft |

**Dependência crítica:** S0 e controles preventivos devem existir antes de qualquer publicação/merge futuro. O levantamento de exposição pode ocorrer paralelamente à revisão de código, mas uma exposição efetiva de credencial é incidente que exige resposta imediata. O PR #17 fica na sua linha independente até o retorno planejado da sessão responsável em 27/10, salvo incidente de segurança.

## 2. Classificação de informação antes de publicar

**PUBLIC_OK**: código próprio sem segredos, testes e fixtures fictícias, método genérico, documentação e referências públicas permitidas.

**NEEDS_REVIEW**: nome de cliente/marca em contexto não aprovado; identificadores de Drive e paths que revelem estrutura interna; páginas de projetos, transcrições, screenshots, evidência de fornecedor, dados pessoais indiretos, prompts de cliente, links de compartilhamento estáveis, versões de contratos, relatórios reais.

**NEVER_PUBLIC**: chaves/tokens, cookies/sessões, passwords, credenciais OAuth, APIs com segredo, URLs assinadas/presigned contendo acesso, arquivos privados, mídia de cliente, documentos de cânone privado, dados de pessoas/contatos, respostas completas de APIs privadas, logs com tokens/cabeçalhos, datasets com direitos de redistribuição incertos.

Um nome público de marca **não é automaticamente** dado secreto, e uma URL do Drive **não é automaticamente** credencial. A classificação considera contexto, escopo de compartilhamento e se o link concede acesso. O relatório público de auditoria nunca deve reproduzir tokens, URLs assinadas ou fragmentos identificadores confidenciais.

## 3. Gate preventivo de pré-publicação (defesa em profundidade)

### Antes de salvar/publicar um novo commit

1. Revisar `git diff --cached` e nomes de arquivos por informação privada; quando usar GitHub connector para criar arquivos, fazer pré-verificação do **conteúdo completo que será enviado** antes da chamada.
2. Aplicar detecção local de segredos e padrões de URL assinada/identificadores privados com regras versionadas e placeholders; nunca confiar apenas em `.gitignore` porque arquivos rastreados continuam no histórico.
3. Usar fixtures `SYNTHETIC_FIXTURE`, IDs fictícios e referências opacas com resolução privada. Os dados privados permanecem fora do Git público (ADR-0001).
4. Revisar direitos de redistribuição de PDFs, imagens, vídeos, transcrições, capturas e logs antes de adicionar.
5. Para novos dados reais, verificar se não são logs de API, URLs com query string de segredo, cabeçalhos Authorization ou screenshots com dados pessoais.

### No PR / CI

6. Configurar revisão automatizada de segredos (p.ex. regras de scanner gratuito ou serviço aprovado); testes de links sensíveis e de dados não fictícios em pastas `experiments/`, `validation/fixtures/`, `docs/`. Respeitar falsos positivos e exigir revisor, não simplesmente tornar invisíveis alertas.
7. Fazer auditoria de diff e **histórico da branch**, não só do último snapshot. Uma chave removida de um commit posterior continua potencialmente acessível.
8. O CI não é a primeira barreira: no repositório público, dados enviados anteriormente já podem ser copiados por terceiros. Inspeção **pré-push e pré-criação via connector** é obrigatória.
9. Antes de merge: confirmar owner, aprovação, scanner sem achados críticos não resolvidos, segurança/privacidade, licenças, regressão e status explicitamente registrado; CI verde não comprova ausência total de vazamentos.

### Resposta caso exista exposição real

10. Interromper novos pushes contendo o material; classificar impacto **sem colar os segredos no chat ou no Git**.
11. Para chave, token, URL assinada ou cookie com acesso: revogar/rotacionar na origem primeiro, revisar logs/acessos e comunicar o responsável conforme a gravidade.
12. Remover referências do código e, quando houver necessidade, tratar **histórico Git, forks, caches e logs** com procedimento de segurança específico e coordenação do proprietário. Apagar a linha atual ou fechar um PR **não** desfaz exposição pública anterior.
13. Registrar no Git público apenas referência opaca ao incidente e status de contenção, nunca o material original.

**Implementação deste gate (estado de 23/10/2026):** o [PR #20](https://github.com/bribeirobr25/ai-creative-skill/pull/20) implementa um **candidato** de guard/CI, auditoria histórica e triagem privada com 81 testes de segurança aprovados no [HEAD verificado](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40012658633). O guard foi reforçado para classificar também diffs binários sem cabeçalho textual. **Ainda não foi integrado à main nem instalado como controle pré-publicação local obrigatório**. S0 já está ENCERRADA administrativamente com limitações. Caso surja evidência concreta, abrir análise pontual de incidente, sem reabrir automaticamente S0. Não alterar PR #17 sem coordenação.

## 4. Contratos do laboratório a rever antes de expansão

- `NO_RESULTS` é um **resultado da fonte** (cobertura negativa concluída) e não determina sozinho `COMPLETE` ou `INSUFFICIENT_EVIDENCE` do trabalho. Testar conclusão para pedido de existência/ausência vs pedido de ranking de itens existentes.
- `derived_permission=True` no laboratório é **somente controle de fixture sintética**, jamais autoridade real de API. Futuro Policy Gate usa fonte, finalidade, transformação, campo, retenção e escopo.
- Baselines históricos: uma publicação contada uma vez, com escolha declarada de snapshot, registro de idade, janela e missing/censoring; rejeitar apenas casos genuinamente ambíguos/insuficientes.
- Validar `limit`, geografia e solicitação nacional **antes** de tentar ranking; propagar essas condições pelo bridge. Exigir teste de ponta a ponta.
- Remover filtros duplicados sem alterar algoritmo; testes de regressão para a mesma coorte e derivação.
- Simulações: do toy model (consistência/reprodutibilidade) para hipóteses explícitas de quotas, retries, erros correlacionados, fontes/geo incompatíveis, custos e percentis. Comparar resultados analíticos e testar extremos determinísticos.

## 5. Critérios de saída

A sequência revisada é válida como **plano**, não como implementação concluída. Antes de seguir ao primeiro conector real é necessário demonstrar: auditoria S0 registrada em local apropriado; controles pré-publicação ativos e testados; PR #19 revisado, invariantes de autoridade/cobertura corrigidos; PR #18 harmonizado; fonte/permissão estabelecida para cada operação planejada.

**Este plano não reproduz nem valida segredos ou dados privados.** A auditoria S0 foi executada em etapa separada e, posteriormente, encerrada administrativamente por declaração do proprietário, com limitações e riscos residuais documentados no PR #20. Não equivale a certificação de privacidade geral.
