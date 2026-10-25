# Intelligence · laboratório offline de contratos e evidência

**Natureza:** experimentos sintéticos e auditáveis. Não é código de produção, módulo canônico, cliente de API, servidor, gerenciador de credenciais, autorização de gastos ou publicação.

## Verificação reproduzível

```sh
python -m unittest discover -s experiments -t . -p 'test_*.py' -v
python -m validation.release_integrity
python -m validation.candidate_integrity
python -m validation.candidate_tests
```

O workflow instala `validation/requirements.txt` antes da validação de release. Todos os fixtures são totalmente fictícios. Testes verdes não comprovam direitos de provedores externos nem substituem revisão independente.

## Ownership and flow

- `engine.py`: métricas estatísticas sintéticas (tempo UTC e DST, deduplicação, ranking restrito por cobertura).
- `vocabulary.py`: referência a enums que continuam pertencendo ao método Research Evidence Synthesis.
- `policy_gate.py`: preflight exclusivamente de **formato** e de direitos simulados, sem autoridade de ação. `SourceCapabilityRecord` não armazena aprovação de projeto nem estado de autorização de API. IDs de `source_id`, `platform` e `channel_id` das fixtures usam o namespace ASCII `fixture-*`.
- `research_bridge.py`: construtor `research_execution` em ambiente isolado. Exige decisão explícita de preflight, propaga `BLOCKED` a `SKIPPED_UNCONFIGURED` e `STOP_POLICY_REJECTION`; uma pesquisa bloqueada não pode declarar `COMPLETE`.
- `contract_canary.py`: valida estados, Evidence Records/Clusters, métricas, cobertura, campos permitidos e proíbe referências reais em Evidence de fixtures.
- `s2_projection.py`: transporta métrica, base geográfica, país, timezone IANA, limites e janela sem trocar silenciosamente o significado.
- `provider_templates.py`: apenas hipóteses descritivas de YouTube e Meta, sem direitos verificados, sem conexão.
- `test_remediation.py`: cenários adversariais para falso positivo de cobertura, fonte real mascarada, derivados não autorizados, retenção impossível e coerência das fases.

A única decisão positiva do laboratório é `SHAPE_CHECK_PASSED_SYNTHETIC_ONLY`. Mesmo com resultado positivo, `may_access_real_source`, `may_spend`, `may_store_real_data` e `may_publish` sempre são `false`. O relógio injetado é **somente de teste**, não um relógio de confiança para produção. O retorno não deve ser usado como autorização. Um adaptador real precisará consultar os donos canônicos: Research Evidence Synthesis, Project Profile, AUTONOMY_ENVELOPE e Execution Contracts.

## Interfaces que continuam NÃO implementadas

Nenhum armazenamento persistente, purga real, OAuth, Google/TikTok/Meta/YouTube API, rate limit ao vivo, análise real de vídeo, canal/credencial, orçamento, endpoints internos, criação de conteúdo, dashboard ou MCP. Não há uma segunda governança de Research. `engagement_observed` e a definição do especialista estatístico exigem decisão formal e versão do método. Quota, TTL e retenção de provedores reais não podem ser derivados de fixtures.

A arquitetura proposta está em `docs/research/intelligence/architecture-v0.3.md` no candidato documental correspondente; somente após aprovação e testes T1–T7 da Issue #1 uma capacidade pode ser integrada à skill. Código de produção em `src/` **não** deve importar `experiments/`.

Esta documentação é uma descrição técnica de laboratório, não um pedido de ação para agentes, plano de merge nem declaração de aceite.

## Before any real-source integration (S5)

The synthetic `validate_fixture_verdict` is a shape validator only. It does not bind the decision to the actual query or source capability. A real authorization decision must be bound to the exact request, source, operation, purpose and capability through canonical authority, and the fixture validator must never be reused as production permission.

`redistribute_output` describes the intent to distribute provider-derived results externally; private transient analysis is not automatically redistribution. Rights are checked per provider and operation. No current synthetic fixture grants redistribution or real execution.
