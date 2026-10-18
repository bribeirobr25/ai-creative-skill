> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill Execution Contracts · Pre-v0.21-V2.4-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
IMPLEMENTATION CONTRACTS

VERSION
=
Pre-v0.21-V2.4-CANDIDATE

DATE
=
2026-10-16

PARENT
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.16-V2.3-CANDIDATE.md
```

Z2/Z3 hardening branch (2026-10-10): Pre-v0.18-V2.1-CANDIDATE is a **candidate branch revision**, derived from the validated V2 candidate and not promoted to `00_ACTIVE`. It adds executable callback correlation/authentication semantics and a protected provider-extension boundary confirmed as missing by the zero-cost adversarial runtime simulation. All V2 canonical execution serialization/snapshot, exact approval binding, revision control, schema migration, cancellation/late-completion, scoped-reference, integrity, cross-project, batch, decision-trace, idempotency, UNKNOWN reconciliation, same-job recovery, effective-parameter reconciliation, selective authority invalidation and PARTIAL batch semantics remain in force.


Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.16 adds §1.1 Canonical Names and Accepted Aliases as the single declaration of canonical field/state names and their accepted aliases (revised documents use canonical field and enum names, prose labels may stay descriptive where the table declares the equivalence, and a new document must not introduce a new alias without adding it to §1.1); renames the Reference Binding field `forbidden_inheritance` → `excluded_inheritance`; aligns the operator-feedback `unit_review_state` with the canonical Review Verdict vocabulary; names the dependency-invalidated acceptance state `ACCEPTANCE_INVALIDATED` (distinct from route/recipe `STALE`); moves the Operator Review / Repair Feedback Record out of the Extended QA Record to §22.1 under Repair Record (former §22.1–§22.2 become §22.2–§22.3); and replaces the outdated Route Recipe Spec Pre-v0.3 and Implementation Validation Plan Pre-v0.3 pointers with Manifest-resolved family references. No job/retrieval state machine, failover, budget or stop semantic changes.

Pre-v0.15 adds provider-reported effective-parameter reconciliation, selective invalidation of downstream assets when an approved upstream authority revision changes, and hardened result-ingest requirements for untrusted external transport. Pre-v0.14 operator review/repair feedback semantics and all existing state/stop semantics remain in force.

This document defines record/state semantics for the future skill.

It separates what Slice 1 actually needs from what can wait until real execution proves the need.

```text
MVP_REQUIRED
=
needed for the first external image smoke test

LATER
=
useful contract, not required before Slice 1
```


Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.19-V2.2-CANDIDATE adds only a portable `creative_latitude_ref` handoff and one isolation conformance case. Craft semantics remain owned by the Specialist Method System; transactional state does not become a competing creative authority.

---

# 1. Governance Boundary · MVP_REQUIRED

The new skill owns internally:

```text
authority resolution
approval state
budget state
job state
retrieval state
asset provenance
QA verdict
retry / failover / stop behavior
```

No external governance skill is required.

## 1.1 Canonical Names and Accepted Aliases

Some current design documents name the same concept differently. This table is the single declaration of the canonical name for each such concept and of the aliases accepted as equivalent. Documents revised in or after the 2026-10-09 validator correction round use the canonical name for field and enum names; prose labels in those documents may keep descriptive wording where this table declares the equivalence. Documents not revised in that round may keep a listed alias, which this table declares equivalent. One listed field alias remains in a revised document: the Extended QA Record defect locator `region_or_timestamp` (§21), which mirrors the QA Realism Performance defect record and stays the declared alias of `time_ref` + `spatial_ref` until both defect records are revised together. An accepted alias is never a second concept or a second field. A new document must not introduce a new alias without adding it here.

| Concept | Canonical name | Accepted aliases (where) | Equivalence / note |
|---|---|---|---|
| temporal invariant whose state may exist only inside a declared window | `WINDOW_SCOPED_EXISTENCE` (Video Direction temporal-invariant type) | none; `BOUNDED_WINDOW` (Video Direction Pre-v0.9 §9.1) is the retired name | `BOUNDED_WINDOWS` remains only the Video Direction timing-precision level; it is a different concept |
| source-media dimensions that must not change | `protected_dimensions` | `authoritative_dimensions` (Route Compilation Pre-v0.11 §7; Video Direction Pre-v0.9 §9.2) — same field, merged | `protected_dimensions` = Localized Repair §6 `PRESERVE`; `allowed_changes` = `VARY / FIX`; every other dimension = `FORBIDDEN CHANGE`. The Video Direction transition seam uses the same mapping: "must persist" = `PRESERVE`, "allowed to change" = `VARY / FIX` |
| blocking / layout map | reference role `COMPOSITION` (Image Direction §10); field `composition_ref` | `blocking_plan_ref` (Video Direction Pre-v0.9); "COMPOSITION / BLOCKING MAP"; "composition-map labels"; "control reference" (Route Compilation Pre-v0.11) | one artifact; its authority is the narrow `COMPOSITION` authority owned by Image Direction |
| identity authority | `identity_authority_ref` | `identity_authority` (Talking Persona Pre-v0.5) | reference to the approved identity authority, not a copy of it |
| voice authority | `voice_authority_ref` | `voice_authority` (Audio Voice Performance Pre-v0.10; Talking Persona Pre-v0.5) | reference to the approved voice authority, not a copy of it |
| approved range of contextual voice-delivery variation | `scene_adjustment_envelope_ref` | "approved performance envelope"; "allowed contextual variation"; "allowable performance envelope" | variation inside this envelope does not change the locked voice identity (Audio Voice Performance) |
| inheritance a reference must not contribute | `excluded_inheritance` | `forbidden_inheritance` (Architecture §12 example; Execution Contracts ≤ Pre-v0.15 §19) | positive counterpart: `allowed_inheritance` (Route Compilation §7) |
| per-unit review state in operator feedback | `unit_review_state` using the Review Verdict vocabulary `ACCEPTED \| REPAIR \| BLOCKED \| UNVERIFIED` (§12) | interface labels `REVIEW` / `FIX` / `ACCEPTED` (Execution Contracts Pre-v0.14–Pre-v0.15 §21.1; Motion OS UI "Review" / "Fix" / "Approved") | `REVIEW` = `UNVERIFIED` (not yet reviewed at adequate coverage); `FIX` = `REPAIR`; `ACCEPTED` = `ACCEPTED`; UI labels are presentation only |
| time / region locator of a finding or feedback item | `time_ref` + `spatial_ref` | `region_or_timestamp` (Extended QA Record §21 defects; QA Realism Performance) | `region_or_timestamp` is the combined form of the same locator; not a separate concept |
| accepted asset whose recorded authority dependency no longer matches current approved authority | `ACCEPTANCE_INVALIDATED` (§10.1; Asset Index `status`) | "current acceptance becomes stale" (Execution Contracts Pre-v0.15 §10.1) | distinct from route/recipe `STALE` (§5.3/§5.4), which describes route facts, not acceptance |
| variant execution vs variant comparison family | `variation_batch_id` (§13.1) for one bounded execution of N accepted variants; `variant_family_id` (Calibration §8.1) for a declared comparison/series family | none — two different concepts | a variant family may be produced by one or more variation batches; a variation batch need not be a calibration family. When a family is executed as a bounded batch, the family record references the `variation_batch_id` rather than duplicating its approval/budget/attempt state |
| third-party predictive / diagnostic tool score | `signal_origin_class = THIRD_PARTY_TOOL_DIAGNOSTIC` (Calibration) | "third-party diagnostic evidence" (Work Profile Ads §17.1) | diagnostic signal only; never measured performance or acceptance |

Section numbers in this table refer to the version named in the alias column, or to the current version resolved by the Current Design Manifest when no version is named.

---

# 2. Minimal Slice-1 State + Configuration

Slice 1 needs six persistent run/state concepts:

```text
1. APPROVAL
2. BUDGET / RESERVATION
3. EXECUTION ROUTE
4. ATTEMPT / JOB
5. ASSET SIDECAR / DURABLE INGEST
6. REVIEW VERDICT
```

It also requires one executable runtime configuration for the selected route:

```text
EXECUTION ROUTE RECIPE
```

The recipe is configuration reused across runs, not a seventh per-run state record. Other `LATER` contracts remain additive unless a selected route/canary explicitly needs them.

---

## 2.1 Canonical Execution Snapshot and Serialization · MVP_REQUIRED

Before an execution plan can be fingerprinted, approved or submitted, resolve an immutable canonical execution snapshot.

```yaml
execution_snapshot_id:
schema_family: EXECUTION_SNAPSHOT
schema_version:
project_id:
work_id:
operation:
route_id:
route_recipe_ref:
provider_id:
model_id:
creative_spec_ref:
prompt_or_compiled_spec_ref:
reference_binding_refs:
authority_revision_snapshot:
claim_evidence_refs:
exact_text_refs:
locale:
market_scope:
jurisdiction_scope:
output_requirements:
expected_output_count:
reservation_ref:
created_at:
canonical_serialization_version:
execution_fingerprint:
```

Canonical serialization rules:

```text
CANONICAL FIELD NAMES, NOT ALIASES
CANONICAL UNITS / ENUMS
INTEGER-EQUIVALENT NUMBERS NORMALIZE CONSISTENTLY
UNORDERED SETS SORT DETERMINISTICALLY
ORDERED SEQUENCES PRESERVE ORDER
ABSENT / UNKNOWN / EXPLICIT NONE ARE NOT SILENTLY COLLAPSED
NON-SEMANTIC METADATA IS EXCLUDED FROM THE FINGERPRINT
SEMANTIC REFERENCES RESOLVE TO STABLE ID + REQUIRED REVISION / HASH
```

Two snapshots that are semantically equivalent under the canonical rules must produce the same fingerprint. Any material difference that changes what is generated, represented, claimed, spent, routed or authorized must produce a different fingerprint.

The snapshot is immutable. Recompilation creates a new snapshot; it never rewrites the object that an approval already references.

---

## 2.2 Persisted Record Versioning and Migration · MVP_REQUIRED

Every persisted state record that may survive a process/session boundary carries:

```yaml
schema_family:
schema_version:
record_revision:
```

Load behavior:

```text
CURRENT SUPPORTED SCHEMA
→ read directly

SUPPORTED OLDER SCHEMA
→ explicit deterministic migration
→ preserve source record / migration provenance

AMBIGUOUS OR UNSUPPORTED SCHEMA
→ STOP_SCHEMA_MIGRATION_REQUIRED
→ do not guess missing semantics
```

A migration may rename or normalize a declared alias but may not invent authority, approval, provenance, locator meaning or state that the old record cannot establish.

## 2.3 Mutable-State Revision and Integrity · MVP_REQUIRED

Mutable current-state records use optimistic revision semantics or an implementation-equivalent concurrency control:

```text
READ revision N
→ WRITE with expected_revision = N
→ if current revision != N: STALE_WRITE_REJECTED
→ reload / reconcile before another write
```

Immutable snapshots, sidecars and historical evidence are never "fixed" by overwriting history.

Before `RESUME`, `EXECUTE`, `DELIVER` or final acceptance, a state-integrity check must reject impossible or corrupt relations such as negative spend, refund greater than confirmed spend, duplicate stable IDs where uniqueness is required, broken approval/attempt/parent references, missing provider job identity after a submitted async attempt, impossible job/retrieval combinations, hash mismatch, or `COMPLETE` batches below their accepted-count target.

---

# 3. Approval Contract · MVP_REQUIRED

```yaml
approval_id:
scope:
  # SINGLE_JOB | BATCH | BUDGET_CAP
currency:
max_cost:
max_attempts:
allowed_operations:
allowed_routes_or_classes:
approval_binding_mode:  # EXACT_EXECUTION | BATCH_TEMPLATE | SPEND_ENVELOPE_ONLY
execution_snapshot_ref:
execution_fingerprint:
batch_template_ref:
created_at:
expires_at:
notes:
```

Rules:

```text
QUOTE ≠ APPROVAL
```

An approval may authorize one job, a batch or a monetary cap.

`SPEND_ENVELOPE_ONLY` authorizes a monetary ceiling but is **not by itself** authorization to submit an arbitrary concrete execution plan. A concrete paid submission must resolve either an `EXACT_EXECUTION` binding or a `BATCH_TEMPLATE` binding that covers the submitted item.

For `EXACT_EXECUTION`, the current canonical `execution_fingerprint` must equal the fingerprint recorded by the applicable approval immediately before submission. Material semantic change makes the approval relation `APPROVAL_STALE` until re-authorized.

For `BATCH_TEMPLATE`, the approval binds to the canonical template plus its declared `preserve`, `vary`, count, attempt, route-class and spend envelope. A child item outside that envelope is not authorized merely because budget remains.

A Project Profile may require a stricter cadence.

---

# 4. Budget Ledger · MVP_REQUIRED

Core formula:

```text
available_balance
=
authorized_cap
- confirmed_spend
- open_reservations
```

Before a new paid action:

```text
new_maximum_reservation <= available_balance
```

Ledger entry:

```yaml
cost_entry_id:
work_id:
attempt_id:
currency:
quoted:
reserved:
confirmed:
refunded:
status:
  # RESERVED | CONFIRMED | RELEASED | REFUNDED | UNKNOWN
source:
checked_at:
```

Never report estimate as confirmed spend.

Reservation discipline:

```text
ONE LOGICAL PAID ATTEMPT / OUTPUT TARGET
↔
ONE IDENTIFIABLE RESERVATION / COST ENTRY
```

A batch may be authorized as one approval scope, but each paid attempt must remain individually attributable. A partially completed batch is not blindly resubmitted as a whole.

## 4.1 Paid Research / Inspection Binding · LATER

Any paid research source, paid transcription/video-inspection route or other paid evidence action uses the same approval and budget machinery as production execution. A method-level field such as `paid_source_authorization_ref` or `paid_processing_authorized` is not itself a spend ledger. Before a paid evidence action:

```text
APPLICABLE APPROVAL
+
IDENTIFIABLE RESERVATION / COST ENTRY
+
AUTHORIZED ROUTE / OPERATION
→ PAID EVIDENCE ACTION MAY PROCEED
```

If the source requires payment but no applicable approval/reservation binding exists, the method must return/retain a blocked or `PAYMENT_REQUIRED` source outcome as appropriate and must not consume credits automatically.

---

# 5. Execution Route Contract · MVP_REQUIRED

The executable technical unit is an Execution Route, not merely a model name.

```yaml
route_id:
model_id:
provider_id:
operation:
endpoint_or_mode:
exposed_model_version:
adapter_version:

required_inputs:
supported_refs:
output_type:
resolution_or_quality:
duration_if_applicable:
audio_support:
execution_mode:
  # SYNC | ASYNC | WRAPPED_SYNC | MANUAL_UI

route_evidence_state:
  # DOCUMENTED | INTEGRATION_EXPOSED | UI_ONLY | EMPIRICAL_PASS
  # EMPIRICAL_FAIL | BLOCKED_BY_INTEGRATION | UNTESTED

production_approval_state:
  # UNTESTED | EXPERIMENTAL | APPROVED_DRAFT | APPROVED_MASTER | DEPRECATED | REJECTED

registry_fact_refs:
route_recipe_ref:
route_recipe_relation_state:
  # ABSENT | DRAFT | VERIFIED | STALE | INVALIDATED
route_freshness_state:
  # FRESH | RECHECK_REQUIRED | STALE | INVALIDATED
docs_ref:
last_verified:
```

Price is not duplicated here if the Registry already owns the volatile fact.

## 5.1 Canonical Route Evidence State

```text
DOCUMENTED
INTEGRATION_EXPOSED
UI_ONLY
EMPIRICAL_PASS
EMPIRICAL_FAIL
BLOCKED_BY_INTEGRATION
UNTESTED
```

Meanings:

- `DOCUMENTED`: current provider documentation says the route/capability exists.
- `INTEGRATION_EXPOSED`: the current integration exposes the required operation/inputs.
- `UI_ONLY`: known in provider UI but not in the current programmatic integration.
- `EMPIRICAL_PASS`: our project executed the stated test scope and passed its acceptance rubric.
- `EMPIRICAL_FAIL`: our project executed the stated test scope and failed it.
- `BLOCKED_BY_INTEGRATION`: upstream capability may exist but the current integration cannot execute the required contract.
- `UNTESTED`: no project execution evidence exists for the stated scope.

Empirical state is always scoped by test case. A short-duration pass does not imply a longer-duration pass.

## 5.2 Canonical Production Approval State

```text
UNTESTED
EXPERIMENTAL
APPROVED_DRAFT
APPROVED_MASTER
DEPRECATED
REJECTED
```

Approval is route + capability + project + test-scope specific.

## 5.3 Execution Route Recipe Relation State

This is the state of the relationship between an Execution Route and its runtime recipe:

```text
ABSENT
DRAFT
VERIFIED
STALE
INVALIDATED
```

Meanings:

- `ABSENT`: no runtime recipe exists for the route yet.
- `DRAFT`: a recipe exists but has not passed scoped execution validation.
- `VERIFIED`: the recipe exists and passed its recorded scoped execution check.
- `STALE`: the recipe exists, but material facts/schema/version may have changed and require refresh before material execution.
- `INVALIDATED`: the current recipe can no longer satisfy the Execution Route Contract as recorded.

`ABSENT` is a relationship state. An existing recipe object's own `recipe_state` therefore uses only `DRAFT | VERIFIED | STALE | INVALIDATED`.

Recipe relation state does not upgrade route quality or production approval by itself.

## 5.4 Canonical Route Freshness State

```text
FRESH
RECHECK_REQUIRED
STALE
INVALIDATED
```

Meanings:

- `FRESH`: required volatile route facts were checked within the applicable freshness window and no material invalidation signal is known.
- `RECHECK_REQUIRED`: the route may still work, but at least one material volatile fact must be refreshed before material spend or production use.
- `STALE`: current route facts are no longer sufficiently reliable for execution without refresh/revalidation.
- `INVALIDATED`: a known upstream or integration change means the recorded Execution Route Contract cannot currently be satisfied as recorded.

```text
STALE
≠
INVALIDATED
```

A stale route may recover after refresh. An invalidated route requires a changed/revalidated contract or another eligible route.

### 5.4.1 Current Freshness Ownership

```text
CURRENT route_freshness_state
=
current Execution Route state
maintained as the volatile route instance in the Provider Registry
```

The Execution Contracts define the field and semantics; the Registry stores the current volatile instance. This is not two competing authorities. An Execution Route Recipe must **not** maintain an independent current freshness truth. It records only the freshness state/evidence against which that recipe was validated plus the validation timestamp.

If a recipe snapshot says `FRESH` but the current Registry/Execution Route instance is now `RECHECK_REQUIRED`, `STALE` or `INVALIDATED`, the current route state governs execution.

## 5.5 Minimal Execution Route Recipe Requirement · MVP_REQUIRED

The first real canary needs one concrete recipe conforming to the canonical schema in:

```text
AI_Creative_Skill_Route_Recipe_Spec
(current version resolved by the Current Design Manifest; the safe-transport and effective-parameter recipe fields this document relies on in §9 and §11 require Pre-v0.4 or later)
```

For Slice 1, the recipe may use that specification's **Minimal Slice-1 Recipe Profile**. This document intentionally does not redeclare recipe fields.

```text
CURRENT MINIMAL RUNTIME
=
EXECUTION ROUTE RECIPE

REUSABLE PROVIDER-WIDE ABSTRACTION
=
PROVIDER ADAPTER
=
LATER
```

Secrets are never stored in route/recipe records.

---

## 5.6 Provider-Specific Extension Boundary · CONDITIONAL_MVP

Provider-specific fields may be carried only through the canonical `provider_extensions` namespace defined by the current Route Recipe Specification.

```text
GENERIC CANONICAL SEMANTICS
>
PROVIDER EXTENSION
```

An extension may add route-specific data that has no generic canonical field. It may not silently shadow, replace or reinterpret protected generic semantics such as route identity, approval/fingerprint binding, job state, callback correlation/authentication, reference authority, cost state, output requirements or review state.

If a provider extension conflicts with a canonical field or would change the meaning of a protected generic field:

```text
EXTENSION CONFLICT
→ RECIPE / ADAPTER INVALID FOR THAT MAPPING
→ EXPLICIT REMAP OR SCHEMA REVISION REQUIRED
```

Unknown provider-specific data remains data. Its presence does not authorize execution behavior.

---

# 6. Job State Machine · MVP_REQUIRED

```text
PREPARED
   ↓
SUBMITTING
   ↓
SUBMITTED
   ↓
PENDING
   ↓
COMPLETED

Cancellation / late-result states:
CANCEL_REQUESTED
COMPLETED_AFTER_CANCEL

Exceptions / terminal outcomes:
FAILED
CANCELED
UNKNOWN
```

`UNKNOWN` means the system cannot prove whether execution occurred.

`CANCEL_REQUESTED` means cancellation was requested but the system cannot yet prove that the remote execution stopped. It must not be treated as `CANCELED`.

`COMPLETED_AFTER_CANCEL` means the provider completed after cancellation was requested. The resulting asset may be durably ingested for accounting/provenance if authorized, but it is not automatically accepted, delivered or published. Cost state follows actual provider billing evidence.

`NO_SUBMISSION` is **not** a job state. It is a proven failover condition meaning submission did not occur.

---

## 6.1 Callback Event Correlation and Authentication · CONDITIONAL_MVP

A callback/webhook is untrusted external input until it is correlated to the intended route/job/attempt and any route-declared authenticity check has passed.

Canonical callback event record:

```yaml
callback_event_record_id:
schema_family: CALLBACK_EVENT
schema_version:
route_id:
attempt_id:
provider_job_id:
provider_event_id:
provider_sequence:
payload_hash:
received_at:
authentication_state:  # VERIFIED | FAILED | NOT_SUPPORTED | UNVERIFIED
correlation_state:     # MATCHED | MISMATCHED | UNRESOLVED
ordering_state:        # APPLICABLE_IN_ORDER | APPLICABLE_NEWER | DUPLICATE | STALE_OLDER | UNKNOWN
mapped_provider_state:
decision:              # APPLIED | DUPLICATE_IGNORED | STALE_IGNORED | REJECTED | HELD_FOR_RECONCILIATION
evidence_refs:
```

Rules:

```text
CALLBACK ARRIVAL
≠
STATE AUTHORITY

CORRELATION != MATCHED
→ MUST NOT MUTATE CURRENT JOB STATE

AUTHENTICATION = FAILED
→ MUST NOT MUTATE CURRENT JOB STATE

AUTHENTICATION = UNVERIFIED
AND route recipe declares an authenticity mechanism
→ MUST NOT MUTATE CURRENT JOB STATE

DUPLICATE / STALE_OLDER EVENT
→ IDEMPOTENT IGNORE OR RECONCILE
→ MUST NOT REGRESS MONOTONIC STATE
```

`NOT_SUPPORTED` is valid only when the verified Route Recipe establishes that the provider exposes no callback-authentication mechanism for the route. It does not waive correlation to the intended route/job/attempt.

When sequence or event identity is unavailable, the recipe must explicitly say so and define the safe reconciliation fallback. Arrival order alone is never evidence that an event is newer.

A callback may move state only through the canonical job-state reconciliation rules. It cannot itself grant approval, relax an output requirement, accept an artifact or authorize publication.

---

# 7. Retrieval State · MVP_REQUIRED

Retrieval is independent from provider job state.

```text
NOT_STARTED
RETRIEVING
RETRIEVED
DOWNLOAD_FAILED
VERIFIED
```

Examples:

```text
JOB = COMPLETED
RETRIEVAL = DOWNLOAD_FAILED
```

means:

```text
retrieve the same job again
not
generate another asset
```

---

# 8. Failover Contract · MVP_REQUIRED

```text
NO_SUBMISSION confirmed
→ alternate eligible route may be selected

CONFIRMED_PROVIDER_FAILURE
→ alternate eligible route may be selected

UNKNOWN after submit
→ reconcile first

POLICY_REJECTION
→ do not automatically route around

COMPLETED_BAD_OUTPUT
→ QA / repair decision

DOWNLOAD_FAILED
→ retrieve the same provider job
```

Every provider/route swap is recorded and surfaced.

## 8.1 Upstream Route Invalidation

The following errors are execution-routing facts, not creative-quality failures:

```text
MODEL_NOT_FOUND
MODEL_VERSION_REMOVED
ENDPOINT_REMOVED
SCHEMA_CHANGED
ROUTE_RECIPE_STALE
```

Required behavior:

```text
PROVEN PRE-SUBMISSION INVALIDATION
→ mark Execution Route Recipe relation / route freshness stale or invalidated
→ refresh official/current route facts
→ update binding / recipe
→ revalidate
→ select another eligible route only after normal routing/approval rules

POSSIBLE SUBMISSION OCCURRED
→ UNKNOWN
→ reconcile first
→ no blind fallback
```

An upstream route change does not count as evidence that the creative method failed.

---

# 9. Attempt Record · MVP_REQUIRED

One object per real submission attempt:

```yaml
attempt_id:
work_id:
route_id:
approval_id:
execution_snapshot_ref:
execution_fingerprint:
schema_family: ATTEMPT
schema_version:
record_revision:
provider_job_id:
idempotency_key:
callback_event_log_ref:
last_applied_callback_event_id:
last_applied_callback_sequence:
submitted_parameter_snapshot_ref:
effective_parameter_snapshot_ref:
provider_adjustments_ref:

job_state:
retrieval_state:
submitted_at:
updated_at:
cancel_requested_at:
cancel_confirmed_at:
late_result_disposition:  # NOT_APPLICABLE | RETAIN_UNACCEPTED | DISCARD_IF_SAFE | OPERATOR_REVIEW

quoted_cost:
reserved_cost:
confirmed_cost:

error_class:
error_detail:
upstream_error_class:

result_transport:
result_available_at:
result_expires_at:
retrieval_deadline:
retrieved_asset_id:
```

For manual/UI routes, do not invent provider job IDs. Record the provider-visible task/run identifier when one exists; otherwise record `manual_no_job_id` explicitly. `result_expires_at` / `retrieval_deadline` remain unknown when the provider exposes no reliable TTL; absence of a known TTL is not permission to postpone durable ingest.

---

# 10. Asset Sidecar · MVP_REQUIRED

Portable provenance next to or logically linked to each produced asset:

```yaml
asset_id:
project_id:
work_id:
version:

model:
provider:
route:
provider_job_id:

prompt_or_request_ref:
execution_spec_ref:
parameter_snapshot_ref:
reference_ids:
parent_assets:
authority_dependency_refs:
authority_revision_snapshot:

human_filename:
created_at:
file_hash:
technical_metadata:

review_verdict:
approval_status:
```

`human_filename` is convenience metadata. Stable `asset_id`, lineage, hash and immutable provenance references remain authoritative. `execution_spec_ref` and `parameter_snapshot_ref` should resolve to immutable/versioned records or content-addressed snapshots when implemented.

This remains deliberately small for Slice 1.

## 10.1 Authority dependency revision snapshot

When an accepted asset materially depends on mutable approved authority, record the dependency identity and revision/state that was in force when the asset was accepted. Examples include identity, environment, product/package reference, logo, palette, typography, voice or other Project/Profile authority.

```text
UPSTREAM AUTHORITY CHANGES
→ COMPARE RECORDED DEPENDENCIES
→ REOPEN / INVALIDATE ONLY ACTUAL DEPENDENTS
→ PRESERVE UNRELATED ACCEPTED STATE
→ REBUILD / RE-REVIEW / RE-APPROVE AFFECTED OUTPUTS
```

Do not infer dependency merely because two assets were created in the same session. Do not discard unrelated accepted assets. Historical sidecars/provenance remain immutable even when current acceptance is invalidated. Record that current state as `ACCEPTANCE_INVALIDATED` on the affected asset (Asset Index `status` when implemented; otherwise the current approval/acceptance record for that asset), never by rewriting the historical sidecar or review verdict. `ACCEPTANCE_INVALIDATED` means the asset must be re-reviewed/re-approved before it is reused as accepted; it is distinct from route/recipe `STALE` (§5.3/§5.4). If an authority revision is required to prove validity and its state cannot be recovered, stop for authority resolution rather than treating conversation memory or generation recency as approval.

The logical asset index can grow later.

---

# 11. Durable Ingest Contract · MVP_REQUIRED

Provider completion is not enough.

```text
provider result located
→ download / materialize
→ media readable
→ expected type confirmed
→ write project-controlled copy
→ hash
→ sidecar
→ RETRIEVAL = VERIFIED
```

Temporary provider URLs do not become archival authority.

When retrieval crosses an external/untrusted transport boundary, the selected route recipe must define enough controls to prevent the transport itself from becoming executable authority. At minimum, where applicable:

```text
allowed scheme / host policy
redirect limit with destination re-check
maximum acceptable size or bounded streaming policy
expected content/media type verification
active-content policy for SVG / HTML / similar formats
no execution of retrieved scripts/content merely because a provider returned them
```

Downloaded filenames, scraped copy, prompt text and other untrusted strings are data. They must not be interpolated into shell/command surfaces without an explicit safe transport/escaping strategy owned by the route recipe.

## 11.1 Provider-effective parameter reconciliation

If the provider reports adjusted/coerced/effective parameters after submission, persist them with the attempt and compare every material hard requirement against the submitted/authorized request.

```text
REQUESTED / COMPILED PARAMETER
→ PROVIDER EFFECTIVE VALUE
→ COMPARE BEFORE ACCEPTANCE
```

A provider silently changing a hard duration, aspect, resolution, reference count or other material requirement is not a harmless success. The run must either be re-planned through an authorized deterministic transform/eligible route, explicitly accepted under a changed requirement, or stopped. Never hide the swap by storing only the originally requested parameter snapshot.

---

# 12. Review Verdict · MVP_REQUIRED

Minimal Slice-1 record:

```yaml
review_id:
asset_id:
reviewer_type:
  # HUMAN | MODEL | TECHNICAL | MIXED
verdict:
  # ACCEPTED | REPAIR | BLOCKED | UNVERIFIED
notes:
```

For later project/media types, dimensions can be added without changing the core verdict vocabulary.

---

# 13. Work Card · LATER

Useful after Slice 1 proves the execution path:

```yaml
work_id:
project_profile:
work_profile:
method_stack:
mode:
request_summary:
entry_point:
exit_point:
completion_condition:
deliverables:
reuse_assets:
required_new_assets:
authority_refs:
approval_scope:
production_budget:
open_jobs:
blockers:
```

The Work Card is a current execution snapshot, not a second canon.

## 13.1 Variation Batch Contract · LATER

Use when one bounded request asks for multiple accepted variants derived from an accepted asset or concept. This contract is not required for Slice 1.

```yaml
variation_batch_id:
work_id:
source_asset_id:
source_concept_id:
target_accepted_count:
max_attempts:
preserve:
  # identity / composition / format / timing / other declared invariants
vary:
  # hook / opening visual / presenter / execution style / audio / aspect / offer emphasis / CTA / other authorized dimensions
acceptance_criteria:
approval_id:
production_budget:
attempt_ids:
accepted_asset_ids:
status:
  # PLANNED | RUNNING | PARTIAL | COMPLETE | BLOCKED | CANCELED
notes:
```

Canonical distinction:

```text
TARGET_ACCEPTED_COUNT
≠
MAX_ATTEMPTS
```

Rules:

- every candidate variant receives its own review verdict;
- `COMPLETE` requires `accepted_asset_ids` to satisfy `target_accepted_count`;
- rejected candidates consume attempts/cost according to their actual execution state but do not count toward the accepted target;
- the engine may make additional attempts only while approval, budget, route validity and `max_attempts` allow;
- reaching a cost, attempt, policy, authority or route stop returns `PARTIAL` or `BLOCKED` with resumable state rather than retrying indefinitely;
- preserved attributes remain binding invariants for each candidate;
- variation dimensions must remain inside the declared `vary` set and applicable project/work authority.

---

### 13.1.1 Batch Chunking and Variant Merge

Chunking is execution packaging only. It must not reset or redefine:

```text
variation_batch_id
approval binding
accepted-count target
max attempts / spend
preserve / vary constraints
variant family lineage
per-item authority / evidence bindings
```

A branch/merge variant that combines selected attributes from two accepted variants creates a new child variant with explicit parent refs and a field-level merge plan. It does **not** inherit every claim, offer, authority mutation, provider assumption or incidental property of either parent.

---

## 13.2 Specialist Method Stack Contract · LATER

Use when runtime needs an explicit record of which craft methods are active for a bounded request.

```yaml
method_stack_id:
work_id:
resolved_methods:
  - method_id:
    version:
    trigger_reason:
    required_or_optional:
    input_refs:
    output_ref:
reused_method_outputs:
missing_required_methods:
resolved_at:
```

Rules:

- load only methods required by the bounded request;
- Project/Work authority overrides method defaults;
- a method may be satisfied by still-valid prior output;
- adding a method does not authorize adjacent deliverables or spend.

### 13.2.1 Creative Latitude Handoff · LATER

The transactional layer may carry a portable reference to the task-relative creative policy, but it does not own the craft judgment that produced it. Canonical semantics live in the current Specialist Method System.

```yaml
creative_latitude_policy_id:
work_id:
task_scope:
dimension_policies:
  - dimension:
    priority:
    creative_latitude:  # PRESERVE | BOUNDED_VARIATION | OPEN_EXPLORATION
    authority_ref:
    envelope_ref:
    canon_promotion_ref:
creative_risk_level:    # SAFE | BALANCED | BOLD | EXPERIMENTAL | null
concept_exploration_ref:
user_override_refs:
resolved_by_method_refs:
```

Rules:

- priority/authority and creative latitude remain separate axes;
- a user override changes only the named dimension(s) within current authority;
- `OPEN_EXPLORATION` never weakens claims, rights, identity, product truth, exact text, approval, policy or safety;
- a generated expressive choice does not become canon merely through repetition;
- downstream methods may narrow latitude for a documented feasibility/continuity reason, but may not silently broaden protected dimensions.

---


## 13.3 Task Canary Contract · LATER

Use before scaling when a costly task depends on a high-risk unvalidated capability.

```yaml
canary_id:
work_id:
uncertainty:
smallest_valid_test:
route_id:
approval_id:
reservation_id:
acceptance_criteria:
result_asset_id:
verdict:
  # PASS | FAIL | UNVERIFIED | BLOCKED
scale_authorized:
notes:
```

```text
HIGHEST-RISK UNKNOWN
→ LOWEST-COST VALID TEST
→ REVIEW
→ ONLY THEN SCALE
```

A canary is task-specific validation and does not automatically become general route approval.

---

## 13.4 Decision Trace Index · LATER

A compact audit index may link the already-authoritative records without duplicating their truth:

```yaml
decision_trace_id:
work_id:
authority_refs:
research_refs:
strategy_refs:
production_spec_refs:
route_decision_ref:
execution_snapshot_ref:
approval_ref:
attempt_refs:
qa_refs:
repair_refs:
final_asset_refs:
```

The trace is navigation/audit metadata. The referenced owner record remains authority for each domain.

---

# 14. Microtask Contract · LATER

Use roughly ten fields when task decomposition becomes necessary:

```yaml
task_id:
objective:
trigger:
inputs_and_authority:
dependencies:
operation_and_capability:
output:
acceptance_criteria:
authorization_and_cost:
state_resume_failure:
```

Do not add fields merely because a schema can be made longer.

---

# 15. Model Spec · LATER

Provider-independent knowledge:

```yaml
model_id:
model_family:
capabilities:
input_modalities:
output_modalities:
reference_behavior:
known_strengths:
known_weaknesses:
prompt_notes:
```

No provider auth or endpoint belongs here.

---

# 16. Reusable Provider Adapter · LATER

Provider-wide reusable mechanics. Slice 1 does not require this full abstraction because §5.5 defines the minimum route-specific recipe requirement needed for real execution.

Reusable provider-wide mechanics:

```yaml
provider_id:
auth_method:
secret_locator:
catalog_discovery:
schema_discovery:
upload_binding:
quote_method:
submit_method:
status_method:
callback_support:
cancel_method:
result_retrieval:
cost_reporting:
known_error_classes:
last_verified:
```

Secrets are never stored in this record.

---

# 17. Production Request · LATER

```yaml
production_request_id:
work_id:
concept_id:
scene_or_asset_id:
creative_spec_ref:
creative_latitude_ref:
prompt_ref:
route_id:
route_recipe_ref:
reference_bindings:
exact_text:
presentation_mode:
audio_binding_contract:
auxiliary_audio_requirements:
output_requirements:
acceptance_criteria:
execution_snapshot_ref:
execution_fingerprint:
approval_id:
reservation_id:
```

---

# 18. Prompt Provenance · LATER

```yaml
prompt_id:
role:
  # ORCHESTRATION | COMPILED_EXECUTION | EXTERNAL_EXECUTION_SPEC
  # ADAPTATION | POST_PRODUCTION | EVALUATION
origin:
  # USER | COMPILED | IMPORTED | MANUAL_EDIT | HANDOFF
creative_spec_ref:
compiler_version:
route_id:
modified_after_compile:
modification_notes:
```

Prompt provenance is useful, but it is not allowed to block the first canary merely because a 12-field record is not yet implemented.

---

# 19. Reference Binding · LATER

```yaml
binding_id:
reference_id:
stable_asset_id:
reference_mode:
  # CREATE | PRESERVE | TRANSFORM | STYLE_ONLY
authority:
reference_scope:
  # WHOLE_ASSET | SEMANTIC_REGION | SPATIAL_REGION | SUBJECT | PANEL
reference_locator:
  # semantic label / subject ID / panel ID / bounded spatial locator; null only for WHOLE_ASSET
source_project_id:
cross_project_reuse_authority_ref:
excluded_inheritance:
route_asset_id:
temporary_handle:
binding_checked_at:
```

Provider handles never replace stable project asset IDs.

A binding from another project is not eligible as current authority by default. Cross-project reuse requires an explicit import/reuse authority that names the source asset and intended role. Historical accessibility is not authorization.

For composite assets, authority and inheritance attach to the declared `reference_scope`, not automatically to the whole image. A `PANEL`, `SUBJECT`, `SEMANTIC_REGION` or `SPATIAL_REGION` locator must identify the smallest reliable authoritative surface.

---

# 20. Asset Index · LATER

Folder layout is implementation detail.

```yaml
asset_id:
current_path_or_uri:
media_type:
version:
status:
  # GENERATED | IN_REVIEW | ACCEPTED | ACCEPTANCE_INVALIDATED | REJECTED | SUPERSEDED
parents:
children:
sidecar_ref:
review_ref:
```

The index, not a flat folder, becomes logical authority when scale justifies it.

---

# 21. Extended QA Record · LATER

```yaml
qa_id:
asset_id:
reviewer_type:
reviewer_independence:
  # INDEPENDENT | SELF_REVIEW | MIXED | UNKNOWN
  # semantic owner: Specialist Method System § Review Independence
inspection_scope:
  artifact_scope:
  full_resolution_checked:
  target_display_checked:
video_inspection_evidence_ref:  # canonical reference to VIDEO_EVIDENCE_INSPECTION when structured video evidence is used
speech_text_evidence_ref:  # canonical reference to AUDIO_VOICE_PERFORMANCE speech-text evidence when speech verification is used, including audio-only sources
unverified_dimensions:
dimensions:
  factual:
  commercial_clarity:
  identity:
  product:
  anatomy_physics:
  continuity:
  audio_voice:
  spoken_text:
  lipsync:
  performance:
  typography:
  legibility:
  technical:
  claim_visual_support:
defects:
  - region_or_timestamp:
    defect:
    consequence:
    severity:  # canonical defect severity owned by QA_REALISM_PERFORMANCE
    smallest_repair:
    text_finding_ref:  # canonical reference to a SCRIPT_PERFORMANCE text finding when the defect is textual
overall:
  # ACCEPTED | REPAIR | BLOCKED | UNVERIFIED
notes:
repair_task_ids:
```

No dimension is passed merely because the prompt requested it. A dimension that was not inspectable at adequate coverage remains `UNVERIFIED`. For video, `VIDEO_EVIDENCE_INSPECTION` owns the canonical modality/coverage schema; this contract stores only the evidence reference and downstream unverified dimensions rather than a second coverage vocabulary. The same rule applies to speech and text: `AUDIO_VOICE_PERFORMANCE` owns the speech-text evidence schema and `SCRIPT_PERFORMANCE` owns the text-finding schema; this record stores `speech_text_evidence_ref` and `text_finding_ref` only and does not redeclare their fields.

---

# 22. Repair Record · LATER

```yaml
repair_id:
repair_plan_ref:
source_asset_id:
operator_feedback_record_ref:
feedback_item_refs:
repair_target_locator:
  unit_ref:
  time_ref:
  spatial_ref:
  source_locator_ref:
defect:
root_cause:
repair_surface:
primary_change:
operation:
preserved_components:
accepted_state_at_risk:
reopened_accepted_units:
weakly_anchored_state:
regression_risk:
regression_mitigation:
affected_dependents:
repair_round_limit:      # resolved by LOCALIZED_REPAIR; stored here, not owned here
repair_round_number:
repair_rounds_used:
completion_criteria_ref:
escalation_state:       # NOT_REQUIRED | OPERATOR_REQUIRED | RESOLVED
stop_reason:
result_asset_id:
review_ref:
```

Rules:

- prefer the smallest causal repair surface;
- when repair originates from operator feedback, preserve the feedback record/item references and resolve any timestamp/region/unit/source locator to the actual evidence surface before semantic repair;
- declare accepted state that may regress before a generative retry;
- if an accepted sub-surface must be reopened, record the affected unit and causal reason, then re-review that scope;
- prefer one primary causal intervention per diagnostic retry when practical;
- preserve the resolved repair-round limit, round number, completion criterion and escalation state for each iterative repair;
- `LOCALIZED_REPAIR` owns how `repair_round_limit` is resolved; this contract records the resolved value and must not create a competing default;
- do not regenerate accepted upstream state to fix a deterministic downstream layer.

Use only when real repair lineage makes this worthwhile.

---

## 22.1 Operator Review / Repair Feedback Record · LATER

Use when operator feedback must survive a review→repair handoff as addressable project data rather than an unstructured chat paraphrase. This record does not make a tool-specific player, timeline or source-code format canonical.

```yaml
operator_feedback_record_id:
artifact_or_version_ref:
review_scope_ref:
created_by:
created_at:
feedback_items:
  - feedback_item_id:
    unit_ref:              # stable scene / segment / element / layer ref when available
    time_ref:              # timestamp or range when applicable
    spatial_ref:           # point / box / region when applicable
    source_locator_ref:    # provider-neutral source/config locator when available
    feedback_kind:         # EXACT_EDIT | SEMANTIC_NOTE | STATUS
    before_value:
    after_value:
    note:
    unit_review_state:     # ACCEPTED | REPAIR | BLOCKED | UNVERIFIED (Review Verdict vocabulary, §12; see §1.1 for interface-label mapping)
preserve_units:
repair_units:
notes:
```

Rules:

- prefer stable `unit_ref` values across repair versions when the selected deterministic/editing surface can preserve them; if identity cannot be preserved, record a new mapping or leave it unresolved rather than pretending continuity;
- `EXACT_EDIT` may become an absolute deterministic target only when the requested field/value is within current authority and still applies to the current artifact state;
- `SEMANTIC_NOTE` is task data requiring evidence resolution and diagnosis before repair; it is not executable merely because it came from the operator;
- `STATUS` records review state without inventing a defect;
- a unit marked `ACCEPTED` belongs in the protected/preserved scope by default; if a causal repair requires reopening it, record why the acceptance scope was reopened and re-review the affected unit;
- `preserve_units` and `repair_units` must be explicit enough to prevent a local note from silently authorizing whole-asset regeneration;
- source-specific coordinates, file/line locators or typed properties are retained only when the current route exposes them reliably; absence of such instrumentation must not be fabricated.

This record is an execution/handoff contract. QA findings, speech evidence and text findings remain owned by their existing schemas and are referenced rather than copied.

---

## 22.2 Experience / Failure Memory Record · LATER

```yaml
experience_id:
method_or_capability:
route_id:
operation:
input_conditions:
spec_before_ref:
output_before_ref:
defect_or_observation:
probable_cause:
primary_change:
spec_after_ref:
output_after_ref:
improved:
regressed:
mitigation:
confidence:
last_observed:
```

One observation remains scoped evidence. It does not become a universal model rule automatically.

## 22.3 Creative Preference Record · LATER

```yaml
preference_id:
scope:
statement:
explicit_operator_statement:
evidence_examples:
repeated_pattern:
confidence:
last_confirmed:
```

Keep separate:

```text
OBJECTIVE DEFECT
≠
PROJECT / PERSONA RULE
≠
OPERATOR CREATIVE PREFERENCE
```

One rejection does not automatically become permanent preference authority.

---

# 23. Benchmark Contract · LATER

Benchmark types:

```text
CREATIVE_EXPLORATION
MODEL_BENCHMARK
PROVIDER_PARITY_BENCHMARK
PRODUCTION_BENCHMARK
```

Minimal benchmark record:

```yaml
benchmark_id:
mode:
benchmark_case_id:
fixed_input_version:
capability:
model:
provider:
route:
checked_at:
test_case:
input_refs:
output_target:
rubric:
review_blinding:
attempt_count:
confirmed_cost:
results:
operations:
verdict:
notes:
```

The Provider Registry stores benchmark **instances/status**, while this document owns the schema/meaning. Comparisons should reuse canonical benchmark cases where possible so model/provider differences are not inferred from unrelated tasks.

---

## 23.1 Publication / Performance Interface · LATER

Use only when distribution/performance learning is in scope.

```yaml
publication_id:
asset_id:
concept_id:
variant_id:
hook_id:
opening_type:
platform:
account_or_property:
post_or_ad_id:
published_at:
campaign_context:
audience_context:
performance_source:
metrics:
  retention:
  completion:
  rewatch:
  shares:
  saves:
  clicks:
  leads:
  purchases:
  revenue:
  spend:
  cpa_cac:
  roas:
attribution_window:
observed_at:
```

Performance attaches to the publication context, not abstractly to the asset. Define creative identifiers before publication when learning is intended.

---

# 24. Provider Onboarding Contract · LATER

```text
OFFICIAL DOCS
→ CANDIDATE ADAPTER / ROUTE
→ SCHEMA VALIDATION
→ DRY RUN / RECORDED RESPONSE TEST
→ LOW-COST CANARY
→ BENCHMARK
→ APPROVE / REJECT
```

```text
DOCS INGESTED
≠
ADAPTER VALIDATED
```

---

# 25. Economic Comparison Boundary · LATER

This document owns execution-budget arithmetic and reservation semantics.

Provider-market economics such as subscription overhead, unused-credit loss, provider markup, retention cost and effective cost per accepted asset are recorded in:

```text
AI_Media_Provider_Registry_v0.9.md
```

Do not duplicate volatile provider economics in execution contracts.

---

# 26. Stop Semantics · MVP_REQUIRED

Execution engine recognizes:

```text
STOP_COST_CAP_REACHED
STOP_UNKNOWN_SUBMISSION
STOP_POLICY_REJECTION
STOP_OPERATOR_REJECTION
STOP_REQUIRED_AUTHORITY_MISSING
STOP_REQUIRED_VERIFICATION_UNAVAILABLE
STOP_ROUTE_INVALIDATED
STOP_REPAIR_LIMIT_REACHED
STOP_UNRESOLVED_AUTHORITY_CONFLICT
STOP_SCHEMA_MIGRATION_REQUIRED
STOP_STATE_INTEGRITY_FAILURE
STOP_APPROVAL_STALE
```

A stop must preserve resumable state and explain the blocking condition.

---

# 27. Critical Conformance Matrix

The following numbered CT matrix is the canonical conformance-case authority. Architecture and validation documents may summarize categories but must not maintain a divergent numbered copy.

The following cases are required regression targets as implementation grows:

| ID | Case | Required behavior |
|---|---|---|
| CT-01 | New action would exceed authorized cap | stop before submission |
| CT-02 | Timeout/connection loss after possible submit | mark UNKNOWN and reconcile; no blind duplicate |
| CT-03 | Provider job completed but result download fails | retry retrieval of same job |
| CT-04 | Provider returns policy refusal | stop; do not hop providers to bypass |
| CT-05 | Required canonical reference/voice/environment is missing | stop for authority |
| CT-06 | Route lacks a mandatory input/capability | invalidate route before spend |
| CT-07 | Repeated wrong-language/systematic route defect | stop/invalidate according to project rule |
| CT-08 | Prompt attempts unsupported testimonial/review/claim | block or rewrite before generation |
| CT-09 | Price/offer fact conflicts with authority | stop for authority resolution |
| CT-10 | Exact approved text/audio is required | preserve exact authority and verify output |
| CT-11 | Route/provider swap occurs | record and surface the swap |
| CT-12 | Localized defect in accepted asset | repair minimum causal surface; preserve accepted upstream state |
| CT-13 | Final-resolution review fails after low-res acceptance | repair/upscale path first; do not silently regenerate accepted performance |
| CT-14 | Bounded request reaches its requested deliverable, e.g. “write a script” | deliver the accepted result and end at the resolved exit point; do not trigger provider selection, generation, spend, adjacent deliverables or unsolicited next-stage offers |
| CT-15 | User requests `N` accepted variants from an accepted asset/concept | preserve declared invariants, vary only authorized dimensions, review each candidate independently, distinguish accepted-count target from attempt count, complete only when target is met or return partial/blocked at an authorized stop; never exceed approval, budget or max attempts |
| CT-16 | Compiled paid request matches an applicable known failure pattern | mitigate, change route/spec, or explicitly preserve the risk state before submission; do not repeat a known preventable defect blindly |
| CT-17 | Costly batch depends on an unvalidated high-risk capability | run the smallest valid task canary first unless operator explicitly authorizes scale with the risk; canary pass remains scoped |
| CT-18 | Repair can regress accepted state | declare accepted state at risk, preserve/anchor it where possible, and review for regression after repair |
| CT-19 | Reviewer lacks adequate inspection coverage for a dimension | mark that dimension UNVERIFIED; do not issue unconditional acceptance for unseen motion/audio/lipsync/etc. |
| CT-20 | Recorded model/version/endpoint/schema disappears or no longer matches the verified Execution Route Recipe | mark Execution Route Recipe relation / route freshness stale or invalidated, refresh and revalidate before material spend; do not classify as creative failure or blindly retry/fallback after a possible submit |
| CT-21 | Async job is submitted and local execution is interrupted before retrieval | recover the stored attempt/provider job identity, reconcile/poll the same job and retrieve it without duplicate paid submission |
| CT-22 | Operator feedback names a timestamp, region or stable unit for repair | preserve the feedback reference, resolve the addressed evidence/unit before interpretation, compile an authorized exact edit to an absolute target where possible, diagnose semantic notes before repair, and preserve accepted units outside the causal repair scope |
| CT-23 | Provider reports an adjusted/coerced effective value for a material hard parameter | persist requested/submitted and provider-effective values; treat material mismatch as capability/route incompatibility or an explicitly re-authorized change, not silent success |
| CT-24 | An approved/canonical upstream authority revision changes after dependent assets were accepted | identify dependents from recorded authority-dependency revisions, reopen/invalidate only affected acceptance, preserve unrelated accepted state, and require affected outputs to be re-reviewed/re-approved |
| CT-25 | Concrete paid execution plan differs materially from the snapshot/template bound to its approval | mark approval relation stale / stop before submission; re-authorize the new snapshot |
| CT-26 | Two writers attempt to update the same mutable state revision | reject stale write and reconcile; never last-write-wins across conflicting revisions |
| CT-27 | Persisted record requires an unsupported or ambiguous schema migration | preserve source state and stop for migration; do not guess semantics |
| CT-28 | Composite reference supplies authority only for a panel/subject/region | bind authority/inheritance to that locator; do not promote the whole asset |
| CT-29 | Cancellation is requested but provider completion races or arrives late | keep cancellation pending until resolved; late completion is not automatic acceptance/delivery |
| CT-30 | State-integrity validator finds impossible/corrupt persistent relations | stop before resume/execute/deliver and surface the integrity failure |
| CT-31 | Callback/webhook has wrong job correlation, failed authenticity, duplicate identity or stale sequence | reject/ignore/hold as applicable; do not mutate current job state and do not regress monotonic state |
| CT-32 | Provider-specific extension conflicts with a protected canonical generic field | reject the mapping/recipe until explicitly remapped or schema-revised; extension does not silently win |
| CT-33 | User asks to preserve or explore one named creative dimension | change only that legitimate dimension policy; unrelated hard/forbidden/protected dimensions remain unchanged and no authority is broadened |

Project Profiles may add stricter cases.

---

# 28. Slice-1 Acceptance Tests

## 28.1 Slice 1A · Basic Execution Canary

The first implementation slice passes only if one external non-Higgsfield static generation can demonstrate:

```text
route selected explicitly
Execution Route Recipe resolved under the Minimal Slice-1 Recipe Profile
route freshness checked
quote observed
approval bound
reservation made
submission recorded
result retrieved/received without blind resubmit
project-controlled copy written
file hash / sidecar written
review verdict recorded
confirmed cost reconciled
```

A synchronous route may pass Slice 1A. Passing does not prove async recovery.

## 28.2 Slice 1B · Async / Recovery Canary

A separate asynchronous canary passes only if it demonstrates:

```text
real provider job identity persisted
SUBMITTED / PENDING state preserved
local interruption or resume condition exercised
reconciliation/poll resumes against the same provider job
no duplicate paid submission
result retrieved before expiry where a TTL is known
durable ingest completes
```

No gallery, benchmark database, style library or giant asset graph is required to pass Slice 1A or 1B.

Canonical multi-slice validation scope lives in the `AI_Creative_Skill_Implementation_Validation_Plan` family; its current version is resolved by the Current Design Manifest.

# 29. Growth Rule

```text
IMPLEMENT MINIMUM
→ RUN REAL CANARY
→ OBSERVE MISSING CONTROL
→ ADD CONTRACT
```

Avoid adding new record types before a real execution or control requirement demonstrates their value.


---

# V2.3 Cross-Profile Project Contracts

## HANDOFF_PACKET

A cross-profile handoff is explicit state transfer between bounded task owners. Conversation proximity is not a substitute for the contract when material entity identity, evidence limits, accepted state or authorization boundaries matter.

Minimum schema:

```yaml
handoff_packet:
  project_id: string
  from_task_id: string
  to_task_id: string | UNKNOWN
  from_profile: string
  to_profile: string
  task_outcome: object
  accepted_constraints: [string]
  stable_entities:
    - entity_id: string
      entity_type: string
      canonical_label: string | UNKNOWN
      source_refs: [string]
  evidence_items:
    - evidence_ref: string
      evidence_class: OBSERVED | USER_PROVIDED | VERIFIED | INFERRED | UNKNOWN
      confidence: HIGH | MEDIUM | LOW | UNKNOWN
      freshness: object | UNKNOWN
  explicit_unknowns: [string]
  accepted_outputs: [string]
  protected_state: [string]
  invalidated_state: [string]
  permissions_carried: NONE
  action_authority_recheck_required: true
```

Invariants:

```text
STATE / EVIDENCE MAY TRANSFER
AUTHORITY DOES NOT TRANSFER BY IMPLICATION

permissions_carried
=
NONE
```

If the target task requires publication, deployment, spend, purchase, contact, signature, security/ownership mutation or another side effect, authorization is re-evaluated for that action even if the prior owner was authorized for a different action.

## PROFILE_SWITCH_EVENT

```yaml
profile_switch:
  project_id: string
  closing_task_id: string
  closing_profile: string
  target_profile: string
  handoff_packet_ref: string
  project_state_revision_before: string
  project_state_revision_after: string
  reason: string
```

A switch is valid only when:
1. the current task is complete or a bounded delegation boundary is explicit;
2. the next owner is resolved from the requested deliverable;
3. a handoff packet exists when material state/evidence must cross the boundary;
4. the target owner consumes only relevant scoped state;
5. side-effect authority is rechecked independently;
6. the project-state revision is recorded.

## PROJECT_CONTINUITY_STATE

A bounded task may close while the persistent project remains active.

Durable project state may include:

```yaml
project_continuity:
  objective: object
  constraints: [object]
  negative_authority: [object]
  resource_envelope: object
  autonomy_envelope_ref: string | UNKNOWN
  accepted_decisions: [object]
  stable_entities: [object]
  accepted_outputs: [object]
  evidence_refs: [string]
  explicit_unknowns: [object]
  gates: [object]
  experiment_state: object | UNKNOWN
  next_actions: [object]
  revision: string
```

Task-local style or convenience instructions remain task/local-scope unless promoted by explicit authority.

## AUTONOMY_ENVELOPE

This is a project-governance representation over existing approval/budget/side-effect contracts.

```yaml
autonomy_envelope:
  action_classes:
    <action_class>:
      disposition: AUTO_ALLOWED | ASK_BEFORE | FORBIDDEN_OR_OUTSIDE_AUTHORITY
      scope: object
      budget_or_limit: object | UNKNOWN
      source_authority: string
      revision: string
```

The envelope never supersedes system/safety/platform restrictions.

Examples of action classes may include research/read-only inspection; draft creation; generation inside an approved credit envelope; publish/schedule; deploy; purchase/order; new paid subscription; contract/signature; money transfer/withdrawal; destructive account mutation; security/ownership mutation; explicitly excluded repositories/data scopes.

## STABLE ENTITY HANDOFF

When exact identity matters, downstream owners must use `stable_entities` rather than re-name the object from appearance alone.

```text
EXACT PRODUCT SELECTED DURING RESEARCH
+
CREATIVE VIDEO GENERATED LATER
→
SOURCE PRODUCT ENTITY / LABEL REMAINS TRACEABLE
```

A creative nickname may be added only as a presentation label when it cannot be mistaken for the source identity. The source/canonical entity remains preserved separately.

## MIXED-REQUEST DECOMPOSITION

One user message may produce multiple bounded work units.

```text
MESSAGE
!=
SINGLE TASK
```

Dependencies are explicit. Supporting research can finish and hand off into Ads/Organic without turning RESEARCH_ONLY into owner of the final creative deliverable.


---

## V2.4 real-world hardening — deliverable completeness binding, project guide and physical-scene handoff

Before declaring a FULL deliverable COMPLETE, a verifier must check the Manifest-current deliverable contract and each item in a batch; preserve `method_version_refs`, scoped source authority, required/conditional status and remaining findings. A rubric attached to a method is **not** proof of execution. The supplemental `deliverable_check_id` in the Catalog is bound to the bounded `work_id`, not a competing Review Verdict; a structural test alone cannot claim semantic or independent review. If host tools cannot execute a deterministic validator, perform bounded explicit self-check and mark independence `SELF_REVIEW`.

`PROJECT_NEXT_ACTION` belongs to existing project-continuity state/next-action register and is an advisory output only; it cannot promote `AUTO_ALLOWED` or mutate a task's approved `exit_point`. Track whether a step is recommended vs already approved vs actually executed. Never collapse `TASK COMPLETE` into `PROJECT COMPLETE`.

For physical multi-chapter scenes, a lightweight `scene_state_ref` may map stable `object_id`, owner/source/destination, hand/contact state, visibility status (`OBSERVED`, `OFFSCREEN_UNVERIFIED`, `CONFIRMED_ABSENT`), count, and dependency to next scene; do not treat offscreen as missing. The Video Direction method owns physical interpretation; this contract carries stable references only. User approved output remains approved unless a true critical invariant failure is observed and scoped repair authorized.

Every external job retains quote vs provider-billed vs account-balance movement as distinct evidence. An external capability can be used only after actual authorization and current route evidence; a UI tool showing a provider does not automatically authorize paid rendering.

