# S3 · Source Permission Preflight · revisão offline · 2026-10-23

**Veredito restrito:** `S3_OFFLINE_SYNTHETIC_PASS / REAL_ACCESS_NOT_APPROVED / NO_CONNECTORS / NO_MERGE`.

**Evidência de execução:** [GitHub Actions (S2+S3)](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40022017507), commit `6b0637d65b74fb57e2a7a717ad91c7762706c6c5`: **113 testes PASS**, divididos em 42 S2 e 71 S3. A execução usou Python stdlib com fixtures exclusivamente fictícias. Não houve cliente HTTP, tokens, dados terceiros, geração, publicação, armazenamento ou compras.

## 1. Implementação

- `policy_gate.py`: validadores de pedido e `SourceCapabilityRecord` candidato, com decisões `BLOCKED` / `SIMULATION_ELIGIBLE`, razões sanitizadas e capacidades de acesso real/armazenamento real/gasto/publicação sempre `false`.
- `provider_templates.py`: **três hipóteses** documentais: YouTube search público, YouTube derived analytics, Meta Ad Library. Registro `NOT_VERIFIED`, sem direitos, sem credenciais e sem quota operacional. Não afirmar permissão ou cobertura empírica.
- `s2_projection.py`: projeção explícita `intelligence_query` S2 → requisição S3 com **exatamente uma plataforma**, preservando operation, country, geobasis, timebasis, início inclusivo e fim exclusivo, além de exigir `purpose` e `project_id` separados. Nenhuma autoridade acompanha o payload.
- `retention_verdict`: TTL e revogação de **fixtures**, com indicação de invalidação/purge, mas nenhuma exclusão real ou escrita.
- `test_*.py`: gates sintéticos de acesso, operação, finalidade, escopo de projeto/país/geografia/tempo, campos e direitos de derivação, transformação e divulgação, retenção, quota, expiração, revogação, pagamento, mídia crua, coleta recorrente, formatos inválidos, importações de rede, projeção S2.
- CI executa S2 e S3 na mesma branch empilhada, mas isto **não substitui** um teste de integração do host canônico ou da ponte PR #19.

## 2. Garantias específicas do canário

| Dimensão | Resultado S3 sintético | Limite |
|---|---|---|
| Fonte/operação/finalidade | Escopo exato obrigatório | Não consulta autorizações reais |
| País, geo, tempo, janela | Sem fallback silencioso; datas explícitas, fim exclusivo | Disponibilidade histórica verdadeira ainda não demonstrada |
| Campo e transformação | READ+PROCESS e permissões específicas de DERIVE/PERSIST/REDISTRIBUTE | Direitos fictícios são **apenas** fixture |
| Validade da política | reviewed_at, expires_at, revocation e quota simulados | Sem sincronização externa nem revogação efetiva |
| Retenção | TTL fictício e purge/invalidate calculados | Nenhum armazenamento/exclusão operacional |
| Gasto | Pedido pago sempre bloqueado; refs não liberam | Paid Research Binding + Ledger **não implementados** |
| Fonte real | `may_access_real_source=false` sempre | Credenciais por si só não alteram esse resultado |
| Handoff | S2 preserva `permissions_carried: NONE` | Rechecagem de autoridade downstream continua obrigatória |

## 3. Documentação oficial verificada como referência, não como licença

- [YouTube Developer Policies Guide](https://developers.google.com/youtube/terms/developer-policies-guide): o regime adicional para métricas derivadas não equivale a permissão de toda API key.
- [YouTube Derived Metrics](https://developers.google.com/youtube/terms/derived-metrics-policy): scores/ratios, leaderboards e retenção ampliada podem fazer parte de uso analítico **expressamente aprovado**; os prazos dependem do tipo de dado e da autorização.
- [YouTube quota](https://developers.google.com/youtube/data/determine_quota_cost): quota real deve ser verificada no Google Cloud da conta. Nenhum valor de quota do fixture é quota de projeto Google.
- [Meta Ad Library API](https://www.facebook.com/ads/library/api/) e [Meta Graph ads_archive](https://developers.facebook.com/docs/graph-api/reference/ads_archive/): planos de discovery e categorias/regiões estão **NOT_VERIFIED** para nossa conta. Não se presume dados de ads comerciais BR/US ou métricas de conversão por existir uma página da biblioteca.

Referências verificadas documentalmente nesta data; termos e escopos podem mudar e terão revisão pontual antes do primeiro canário real.

## 4. Preparação segura das contas (a cargo do proprietário)

| Fonte | Passos de preparação sem segredos | Estado que pode ser compartilhado no chat |
|---|---|---|
| Google Cloud / YouTube | Projeto na conta autorizada, Data API habilitada, credencial restrita via secret manager/runtime, confirmar cota, endpoints e identidade do responsável | `PROJECT_CONFIGURED`, `DATA_API_ENABLED`, `CREDENTIAL_STORED_PRIVATELY` |
| YouTube Analytics & Reporting | Revisar requisitos, preparar aplicação e autorização adicional quando necessária para métricas derivadas de terceiros | `APPLICATION_NOT_SUBMITTED/PENDING/APPROVED` com **escopo textual não secreto** |
| Meta Developer / Ad Library | Configurar app, concluir verificações exigidas, confirmar regiões, categorias e campos de `ads_archive` efetivamente habilitados | `APP_CREATED`, `ACCESS_PENDING`, `SCOPE_VERIFIED` sem app secret/token |

**Não publicar ou enviar** chaves de API, OAuth tokens, client secrets, cookies, screenshots com credenciais, URLs assinadas ou materiais de contas privadas. Links públicos de política são seguros; IDs, ACL e logs de acesso devem ser minimizados e só compartilhados quando estritamente necessários e sob canal privado.

## 5. Gates seguintes

- **S3-real (pendente):** validar autorização efetiva por operação, finalidade, campo, transformação, classe de dado, retenção/refresh/deleção, país/cobertura, quota, rate limits, compatibilidade RGPD/GDPR, termos de redistribuição e proprietário do projeto. **Sem inferir direito a score proprietário pela simples existência da Data API.**
- **S4 (pendente):** injeção de falhas sintéticas, quotas, retries, expiração concorrente, custos e Monte Carlo mais representativo. Sem extrapolar disponibilidade do mundo real.
- **PR #19 bridge (pendente):** adequar Evidence Record versus Evidence Cluster e os campos de `MetricObservation` definidos em S2, antes de chamar integração canônica.
- **S5 (não autorizado):** primeira consulta read-only pequena em fonte realmente elegível, depois de credencial/escopo confirmados e consentimento de execução aplicável.
- **PR #20:** auditoria S0 foi encerrada por declaração do proprietário, mas guard continua Draft; revisar pré-publicação em futuras alterações.

**Linhas preservadas:** PR #17 Web intocado, PR #18 arquitetura Draft, PR #19 laboratório Draft, PR #20 segurança Draft, PR #21 S2 Draft, PR #22 S3 Draft. `main` e release V2.5 não são alteradas por esta frente. Sem merge automático.
