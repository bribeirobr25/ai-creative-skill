# Intelligence · Status da proposta (não canônico) · 2026-10-30

**Estado de Gate 0: `GATE_0_NOT_PASSED / OWNER_ACCEPTANCE_PENDING`.**
**Estado de implementação: `SYNTHETIC_LAB_REVIEW_ONLY / NO_CANONICAL_INTEGRATION / NO_RELEASE`.**
Estes são registros de revisão, não autorização formal. A versão v0.3 é uma proposta de harmonização, não um contrato adotado.

**Atualização 2026-10-30:**
- Os PRs #20 (proposta do Security Gate), #18 (candidata v0.3) e #23 (laboratório consolidado S1–S3) foram integrados à `main` em 2026-10-26. Integração ao histórico não é aceite do Gate 0, da v0.3 nem da ADR-0003, que continua PROPOSED.
- A [ADR-0005](../../decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md) adia a Trilha D / M7 (Intelligence), sem alterar o estado do Gate 0.

## Sequência S0–S6

| Fase | Resultado e situação |
|---|---|
| S0 | Encerrada administrativamente por atestação do proprietário, com limites residuais. O link Drive em `src/` foi substituído por ID lógico na candidata `privacy-redaction-v1` (PR #35, 2026-10-30); o histórico Git mantém o texto antigo |
| S1 | Motor estatístico anterior #19: histórico; substituído pelo laboratório consolidado do PR #23 (integrado em 2026-10-26) |
| S2 | Validador de contratos anterior #21: histórico; substituído pelo laboratório consolidado do PR #23 (integrado em 2026-10-26) |
| S3 | Preflight de permissões anterior #22: histórico; substituído pelo laboratório consolidado do PR #23 (integrado em 2026-10-26) |
| S1–S3 consolidados | [PR #23](https://github.com/bribeirobr25/ai-creative-skill/pull/23), integrado em 2026-10-26 como laboratório sintético offline (`experiments/intelligence/`); não é capacidade canônica nem release. Número de testes e estado devem ser conferidos no CI da `main` |
| S4 | Resiliência avançada, hipóteses e testes por planejar; não iniciada |
| S5 | Primeiro canário real somente após direitos, credenciais privadas e autorização específica; NÃO autorizado |
| S6 | Integração em `src/` e release: NÃO autorizado; exige coordenação com versão do PR #17 e Manifest |

## Decisões sob controle do proprietário

- Aprovar ou rejeitar Gate 0, versão v0.3 e entrada do laboratório isolado no histórico da `main`; não presumir `CONDITIONAL` como aceito.
- Definir owner de métricas: emenda versionada do Research Evidence Synthesis (rever §§3, 13 e 17) versus novo Specialist Method sob a Growth Rule (§16). `engagement_observed` já existe e deve ser reconciliado, sem assumir fórmulas, thresholds ou watchlists por simples referência.
- Confirmar SourceCapabilityRecord sob §24, aliases da §1.1, vínculo a `MetricObservation`, `STOP_POLICY_REJECTION` e `STOP_REQUIRED_AUTHORITY_MISSING`.
- A ativação futura de §24.1 DATA-SOURCE CONNECTORS é Gate separado. A seção é `NOT CURRENT CAPABILITIES`; citá-la não a implementa.
- Fonte real inicial, licenças/permissões de dados próprios e externos, host das credenciais, histórico permitido e custos.
- Aceite da ADR-0003 (Security Gate). O PR #20 foi integrado, mas a ADR continua PROPOSED. A proteção da `main` já está ativa por ruleset; as lacunas restantes são acompanhadas na Issue #24.
- Decidir, antes de S6, quem governa a identidade de criadores, canais e publicações de terceiros; não confundir com `publication_id` das próprias campanhas.
- Confirmar direitos por operação/campo/fonte para comparações com YouTube, métricas derivadas e redistribuição; aprovação específica de Analytics & Reporting permanece não demonstrada.

## Guardrails permanentes

A `main`/V2.5 ficam intocados até merge autorizado. PR #17 é independente. O laboratório #23 é offline e não implementa API real, armazenamento real, publicação ou autorização financeira. Um retorno `SHAPE_CHECK_PASSED_SYNTHETIC_ONLY` jamais autoriza execução. As versões v0.1/v0.2 e referências PR #19/#21/#22 são história, não status vigente.

**Evidência de testes sintéticos não equivale a direitos de fonte nem a aprovação do Gate 0.** A entrada independente e conclusão da futura capacidade exigem [ADR-0002](../../decisions/ADR-0002-capability-bounded-invocation.md) e seus cenários T1–T7, vinculados à [Issue #1](https://github.com/bribeirobr25/ai-creative-skill/issues/1).

## Limites documentados de cobertura (consulta de referência · outubro de 2026)

- Meta Ad Library: a descoberta oficial de anúncios comerciais de terceiros está vinculada à cobertura de transparência na UE/Reino Unido; anúncios comerciais exibidos apenas no Brasil não ficam disponíveis como catálogo comercial geral. Campos de gastos, impressões e estimativas variam por tipo de anúncio e região; verificar o endpoint e a documentação atual antes de afirmar cobertura.
- TikTok Commercial Content API: a cobertura é centrada no território europeu e varia segundo endpoint/região. Não assumir gastos ou impressões exatas como disponíveis; o acesso aprovado à API não prova direitos para todo campo, país ou transformação.
- YouTube: a política geral limita criação de métricas próprias e combinação de dados; determinados usos de Analytics & Reporting e retenção ampliada dependem de aprovação específica. `search.list` utiliza cota própria documentada de 100 chamadas/dia na configuração padrão, sujeita a alterações.
- Alemanha oferece fontes oficiais parciais para pesquisa de anúncios comerciais; Brasil não dispõe, nessas APIs de biblioteca, de cobertura geral para anúncios comerciais de terceiros exibidos exclusivamente no país. Dados próprios autorizados são uma categoria distinta.

Esses fatos de cobertura são referências de planejamento verificadas em outubro de 2026, não autorizações operacionais, garantias de disponibilidade ou contratos de direitos para S5.
