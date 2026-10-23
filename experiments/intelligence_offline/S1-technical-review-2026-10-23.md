# S1 · Revisão técnica consolidada do laboratório sintético · 23/10/2026

**Estado:** `S1_OFFLINE_REVIEW_COMPLETED_WITH_EXPLICIT_LIMITATIONS` · PR #19 **Draft** · não canônico · sem merge, produção, APIs ou dados reais.

**Base de avaliação:** revisão do motor `engine.py` e de `research_bridge.py`; 56 testes existentes + 12 testes adversariais novos. A execução de [68 testes offline aprovados](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40017781052/job/120634192975) refere-se ao commit `5efb2ebe361c7f66edc3c642f867724ac45cdef4`. Outros checks devem ser consultados no commit de cada alteração.

## 1. Falhas de contrato encontradas e corrigidas

| ID | Problema observado no código anterior | Proteção implementada | Evidência de regressão |
|---|---|---|---|
| S1-01 | Uma solicitação de ranking nacional poderia ser tratada como coberta usando somente `population_coverage_verified=True` e fonte `OK`, sem cobertura de fonte efetiva | No *bridge*, ranking nacional exige `population_coverage_verified` **e** `source_coverage_verified` e `source_outcome=OK`; caso contrário, `INSUFFICIENT_EVIDENCE` sem referências ranqueadas | `test_national_top_needs_both_population_and_source_coverage`; `test_rate_limited_source_cannot_qualify_as_exhaustive_national_rank` |
| S1-02 | Mesmo com população declarada coberta, uma métrica desconhecida podia deixar um item real fora do topo sem alerta suficiente | Ranking nacional por views agora rejeita qualquer contador desconhecido; resultado `NATIONAL_RANKING_UNDETERMINED` | `test_national_top_fails_when_any_counter_is_unknown`; `test_national_top_with_missing_counts_is_not_definitive` |
| S1-03 | IDs concatenados com `:` poderiam colidir entre `platform` e `publication_id`, comprometendo a vinculação de Evidence/Metric | Codificação individual e reversível das partes do ID via percent-encoding; referências mantêm `evidence_id` e `source_outcome_ref` | `test_composite_evidence_ids_cannot_collide_when_source_ids_have_colons` |
| S1-04 | Identidade inconsistente do mesmo vídeo em snapshots de diferentes instantes podia ser descartada pelo filtro de coorte antes da checagem de conflito | Verificação global de `channel_id`, `content_type` e `published_at` por `platform/publication_id` **antes** da seleção do baseline | `test_cross_snapshot_channel_conflict_not_hidden_by_cohort_filter`; `test_target_publication_conflict_cannot_be_silently_excluded` |
| S1-05 | Velocidade de views não verificava se dois snapshots tinham o mesmo formato de conteúdo | Proibir comparação `short` versus `long` mesmo com publicação, canal e origem aparentemente iguais | `test_velocity_rejects_cross_format_observations` |
| S1-06 | Identificadores vazios de espaços/tipos estranhos, datetimes não tipados, valores booleanos como parâmetros estatísticos, `seed` e contagem de trials mal tipados | Validação explícita de tipos, timezone e intervalos antes de qualquer cálculo | `test_malformed_identity_and_datetime_fail_with_validation_error`, `test_outlier_rejects_boolean_and_malformed_comparator_options`, `test_monte_carlo_rejects_boolean_or_malformed_parameters` |

O caso positivo de `test_synthetic_complete_scope_remains_explicitly_not_real_market` passou a exigir também `source_coverage_verified=True`. Isso não converte uma *fixture* em pesquisa de mercado real: `coverage.actual_scope=SYNTHETIC_FIXTURE_ONLY` e `report_is_real_market_research=False` permanecem.

## 2. O que os testes efetivamente provam

- Invariantes determinísticos exercitados nas entradas sintéticas usadas pela suíte.
- Falhas explícitas quando faltam campos, cobertura ou comparabilidade para rankings nacionais.
- Integridade de referências e tratamento distinto de ausência, falha da fonte e valor `UNKNOWN`.
- Nenhuma alteração no `src/`, no método canônico, no V2.5, no PR #17 ou na `main`.

**Não provam:** cobertura de países, amostragem não enviesada, qualidade de resultados de anúncios, políticas de YouTube/Meta, licenciamento real, desempenho do host, aprovação de armazenamento de dados de terceiros ou precisão preditiva comercial. `derived_permission=True` continua **exclusivamente uma trava de fixture sintética**, nunca autoridade de uso de fonte externa.

## 3. Pendências expressamente transferidas, não escondidas

| Destino | Itens fora do escopo concluído em S1 |
|---|---|
| **S2 · PR #18** | Tipo/validador executável para `research_execution`, `MetricObservation`, Evidence e policy decisions; sem duplicar o owner de pesquisa nem chamar esse bridge de runtime canônico |
| **S3 · Permission Gate** | Contrato verificável por operação, finalidade, campo, transformação, retenção e autorização; `default deny` para scores/armazenamento real sem licença adequada |
| **S4 · Resiliência/estatística** | Censura de snapshots, amostragem/sampling bias, coortes temporais, quotas e retries, falhas correlacionadas, custos, latência e Monte Carlo informativo |
| **S5/S6** | Conector read-only efetivamente autorizado, cobertura empírica, host e integração regressiva, revisão separada de merge e release |

## 4. Segurança e segregação de trabalho

A S0 foi encerrada **administrativamente por declaração do proprietário**, registrada no PR #20, sem transformar essa declaração em inspeção técnica ou licença geral para qualquer material futuro. O controle preventivo do PR #20 segue Draft e separado da `main`; novas publicações exigem inspeção prévia do conteúdo. PR #17 permanece reservado à sessão de Web Experience.

**Decisão:** encerrar a **revisão técnica offline S1**, mantendo PR #19 Draft e sem integração. Prosseguir para S2 de contratos e, paralelamente quando apropriado, S4 de testes de resiliência sintéticos. Nenhuma autorização de fonte real é inferida.
