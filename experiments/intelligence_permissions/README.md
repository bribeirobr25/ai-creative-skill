# S3 · Source Permission Preflight · Offline candidate (2026-10-23)

**Status:** `S3_OFFLINE_POLICY_SHAPE_CANDIDATE / NO_CANON / NO_NETWORK / NO_CREDENTIALS / NO_REAL_RIGHTS / NO_MERGE`.

This candidate is stacked on [PR #21 (S2 contracts)](https://github.com/bribeirobr25/ai-creative-skill/pull/21), itself stacked on [PR #18 (architecture)](https://github.com/bribeirobr25/ai-creative-skill/pull/18). It neither modifies the S2 code nor merges into the AI Creative Skill. It is a small, pure Python standard-library laboratory with **no HTTP client, subprocess, network access, API keys, provider SDK, persistence or spending**.

Run S2+S3 in a stacked checkout: `PYTHONPATH=experiments/intelligence_contracts:experiments/intelligence_permissions python -m unittest discover -s experiments/intelligence_permissions -p 'test_*.py' -v`.

**S3+S2 CI:** [113/113 synthetic tests PASS](https://github.com/bribeirobr25/ai-creative-skill/actions/runs/40022017507), commit `6b0637d65b74fb57e2a7a717ad91c7762706c6c5` (42 S2 + 71 S3). [S3 review and safe owner setup checklist](S3-offline-review-2026-10-23.md). The CI checks test the proposed code only, never provider permission.

## Purpose

Before any external provider can be connected, the proposed SourceCapabilityRecord and request must agree on all of these **independent** dimensions:

| Dimension | S3 simulated condition |
|---|---|
| Identity & operation | Matching source, platform and specific operation, with explicit adapter/policy references |
| Project and purpose | Both must be independently in scope; research permission never implies media generation or publication |
| Geography and time | Country AND geographic meaning AND time basis; audience location cannot silently fall back to creator country or search locale |
| Field rights | Every requested field requires READ and PROCESS; missing fields deny eligibility |
| Transform | Exact transformation grant and, for derived ratios, per-field DERIVE right; output summaries also require REDISTRIBUTE right in this *conservative synthetic fixture* |
| Storage & TTL | NONE/TRANSIENT_ONLY cannot retain; PERSIST requires explicit field PERSIST right and a positive TTL within the maximum |
| Currency of authorization | Explicit reviewed_at/expires_at, with timezone; expired, future or revoked records block; no inferred approval from available docs |
| Quota & paid actions | Synthetic call estimate within declared quota; **all paid requests blocked** even if fake approval/reservation IDs are provided |
| Side effects & media | Raw media, background collection and all real external API access remain forbidden |

For a successful **synthetic** candidate the response is `SIMULATION_ELIGIBLE` with `may_access_real_source=false`, `may_spend=false`, `may_store_real_data=false`, `may_publish=false`. It is **not** an actionable real-source authorization. Invalid types fail with `InvalidContract`, and policy mismatches produce sanitized reason codes. Neither tokens, filenames, private URLs nor raw source data are logged.

`retention_verdict` only computes when a hypothetical fixture would need purge/invalidation. It does **not** create, refresh, delete or persist actual records. Rights tied to downstream derivatives need a future revocation workflow in S5/S6.

For a request passed from S2, `s2_projection.py` enforces exactly one platform and copies the operation, country, geography meaning, temporal meaning and exact **inclusive-start/exclusive-end** window without substitution. Provider templates carry no actual history coverage. The S3 candidate verifies synthetic request windows against explicitly simulated availability windows; its future real source rights must be separately checked. The date-window and provider TTL fixture values are **not** real platform policies.

## Provider templates: hypotheses, NOT approved profiles

`provider_templates.py` contains unverified plans for three operations:

1. YouTube public video search (separate from derived analysis).
2. YouTube advanced derived analytics, requiring the relevant express Analytics & Reporting approval before real derived metrics.
3. Meta Ad Library discovery, with commercial-ad categories, fields, geographies and app/access rights all **NOT VERIFIED**.

The templates have **zero rights grants, zero executable quota, no project IDs, no credentials and expired placeholders**. The tests prove they cannot become executable because of optimistic fixture settings. Source documentation is linked for human verification, **not** treated as evidence of account-specific approval.

Relevant official sources consulted on 2026-10-23:

- [YouTube Developer Policies Guide](https://developers.google.com/youtube/terms/developer-policies-guide) (its additional-metrics regime requires an audited developer and explicit approval, not any API key).
- [YouTube Additional Derived Metrics Policy](https://developers.google.com/youtube/terms/derived-metrics-policy) (sets conditional analytics rules, including selected extended-retention categories).
- [YouTube quota](https://developers.google.com/youtube/data/determine_quota_cost) (quotas are account/project-specific and can change, so no numeric limit is embedded as operational entitlement).
- [Meta Ad Library API](https://www.facebook.com/ads/library/api/) and [Graph API ads_archive reference](https://developers.facebook.com/docs/graph-api/reference/ads_archive/) (documentation must be reconciled with actual app permissions, region and ad category before first use).

**Do not reuse synthetic time-to-live or quota values as YouTube/Meta policy claims.** Fixture values are made up exclusively to exercise contract logic.

## Connection preparation, performed by the owner OUTSIDE GitHub

- **YouTube:** create a Google Cloud project under the intended account, enable the appropriate YouTube API, configure a restricted credential, inspect quota settings and document what scopes/endpoints the project actually possesses. Analytics & Reporting derived metrics must remain disabled until separate express approval is established.
- **Meta:** set up Meta for Developers access and the applicable Ad Library workflow, identity/app verification where requested, and confirm exactly which regions/categories, endpoints, fields and modes are available for the account.
- Store secrets only in a private secret manager/runtime environment, with minimum scopes and rotation. **Never paste API keys, OAuth tokens, cookies, Google Cloud project secrets or signed URLs into chat, GitHub, documents or CI logs.** Public PRs should contain only names of permissions and sanitized status.
- The owner can later provide nonsecret status such as `YOUTUBE_PROJECT_CONFIGURED`, `YOUTUBE_DATA_API_ENABLED`, `META_APP_CREATED`, `ACCESS_PENDING` and `ANALYTICS_APPROVAL_NOT_GRANTED`. Those status statements do not by themselves grant S5 execution authority.

## Follow-on gates

1. **S3 real-policy review:** evidence on precise operation, purpose, fields, geo/time meaning, derivative rights, storage/refresh/TTL, redistribution, price/quota and approved scope. Owner acceptance required.
2. **S4 resilience:** offline fault injection (quota exhaustion, retry, stale permission, revocation, race conditions, partial result, cost cap), verified without real source data.
3. **S5 read-only canary:** only an expressly allowed operation and an authenticated project, small quota budget, no unauthorized history/outlier metric or redistribution.
4. **S6 integration:** review the S2 mismatch between PR #19's evidence-as-cluster bridge and the canonical Evidence Record/Cluster distinction; do not treat S3 fixture success as merge approval.

**No action in this candidate authorizes API calls or money.** CI PASS will only prove the declared synthetic paths, not legal compliance, a real-access configuration, an API quota, or safe production behavior.
