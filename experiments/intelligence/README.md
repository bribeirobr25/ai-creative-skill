# Intelligence · laboratório único de revisão · 2026-10-24

**Status:** `SYNTHETIC_ONLY / NO_CANON / NO_REAL_SOURCE / DRAFT / NOT_RELEASE_APPROVED`.
**Branch:** PR #23, **based on main**, replacing experimental PRs #19 (metrics), #21 (contract canary) and #22 (policy-shape canary). Old PRs remain open as history until independent CC review and owner-approved closure. No PR #17 files touched.

## Executable checks

```sh
python -m unittest discover -s experiments -p 'test_*.py' -v
python -m validation.release_integrity
python -m validation.candidate_integrity
python -m validation.candidate_tests
```

The consolidated workflow installs the existing `validation/requirements.txt` and runs the tests **without custom PYTHONPATH** on a full Git checkout; canonical `validate.yml` also runs because this PR targets `main`. A green test is scope-limited evidence of synthetic code, never a provider authorization or release decision.

## Reconciled shape

- `engine.py`: explicit `source_kind=SYNTHETIC_FIXTURE`, rejects real platform labels, UTF-8/NFC-stable IDs, UTC-normalised timestamps across DST, bounded counters, stable snapshot selection, view velocity, age-cohort outliers and raw ranking with coverage restrictions and tie disclosure.
- `research_bridge.py`: mirrors the Research Evidence Synthesis `research_execution`. Outputs **Evidence Clusters** that refer to **Evidence Records**; individual metrics contain `research_execution_id`, `evidence_id`, `source_outcome_ref` and typed context. The separate `fixture_evidence_index` is explicitly a **test-only map**, not a second provenance authority; production research owns actual Evidence Records.
- `contract_canary.py`: one contract validator; `COMPLETE` cannot be inferred from `AUTH_FAILED` or incomplete sources, nor from `OK` without evidence. National ranking requires strict bool flags, complete synthetic coverage and numeric evidence. Authority fields are forbidden inside the analytics extension. Checks Evidence Record/Cluster independence, timestamps, typed window/geo and HANDOFF_PACKET.
- `vocabulary.py`: one fixture reference to canonical source outcomes/statuses/envelope keys. The parity test reads the actual Research Evidence Synthesis Markdown rather than comparing two copies of hard-coded constants.
- `policy_gate.py`: one **synthetic shape preflight**, rather than S2 and S3 competing gates. It rejects real provider IDs disguised as fixtures, validates metric support and required transformations, field rights, data class and retention policy references, time windows, policy expiry/revocation, quota, TTL, storage and purpose. **Project authority is not kept on SourceCapabilityRecord**; only Project Profile/AUTONOMY_ENVELOPE can approve real project actions.
- `s2_projection.py`: transmits the exact S2 operation, platform, geo/time meaning, calendar window and requested ranking metric into S3, with cross-stage tests preventing derived analytics being labelled DISPLAY_NATIVE.
- `provider_templates.py`: YouTube Data search, YouTube derived analytics and Meta Ad Library documentation templates carry **no usable rights** or credentials.

**Even if shape validation succeeds, every permission signal about real APIs, real storage, external publishing and payments is always `false`.** Success is explicitly named `SHAPE_CHECK_PASSED_SYNTHETIC_ONLY`. The caller-provided test clock is NOT a trusted production clock.

## Canonical authority not usurped

- Core Stage 0 / Research Work Profile / Project Profile / AUTONOMY_ENVELOPE: task and action authority.
- RESEARCH_EVIDENCE_SYNTHESIS: source outcomes, Evidence Records/Clusters, final research state and uncertainty.
- AD_FUNNEL_INTELLIGENCE: ad observations and variant methods; PRODUCT_MARKETPLACE_INTELLIGENCE: product/seller identity.
- Execution Contracts §23.1: publication/performance lineage; §24: provider onboarding; §§3–4.1: spend/approval/ledger.
- Deterministic analytics here is a **helper**, not an independently accepted specialist or replacement for research.
- HANDOFF_PACKET transfers evidence but never approval.

## What must still be resolved outside this lab

1. **Architecture v0.3/STATUS** in PR #18 requires owner and independent CC acceptance.
2. **Security PR #20** requires independent final review, owner approval of slim ADR-0003 and actual local pre-publication deployment. S0 closure is recorded with residual limits.
3. A currently published stable Drive locator in three source media docs/registries requires **versioned source-inventory/Manifest migration**, coordinated with PR #17's separate 2.6 changes; it was not touched by this lab.
4. **No source credentials** in repo. YouTube/Meta policies, scope, history and retention must be officially verified before any S5 read-only live call. Historical outlier comparisons are unavailable absent licensed snapshots.
5. S4 fault injection, quotas/retry/cost and empirical data validation are **not run**. They begin after CC accepts the reconciled boundaries.
6. This PR does not decide whether owner-authorized accounts or external datasets should be the first production route. Both need distinct permissions.

## Final independent CC review request

Audit actual HEAD and CI, reproduce P0/P1 fixes with negative/adversarial cases (Git parser, DST, spoof, failed-source COMPLETE, metric projection and cross-stage bridge), verify no default synthetic provenance, confirm semantic field ownership and license assumptions, compare combined `main + #20 + #18 + #23` with PR #17 in a throwaway worktree, and report remaining P0/P1/P2 separately. **Do not merge or mutate branches without separate owner authorization.**
