# AI Creative Skill · Execution Route Recipe Specification · Pre-v0.7-V2.1-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
EXECUTABLE ROUTE RECIPE SPECIFICATION

VERSION
=
Pre-v0.7-V2.1-CANDIDATE

DATE
=
2026-10-10

PARENT
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.15-V2-CANDIDATE.md

CONTRACT AUTHORITY
=
AI_Creative_Skill_Execution_Contracts_Pre-v0.18-V2.1-CANDIDATE.md

STATUS
=
DESIGN SPECIFICATION
NO CONCRETE ROUTE RECIPE YET REQUIRED
```

Z2/Z3 hardening branch (2026-10-10): Pre-v0.7-V2.1-CANDIDATE makes the V2 async/callback intent executable. It adds explicit cancel mapping, callback event/job/sequence correlation, callback authenticity mapping, duplicate/out-of-order policy and a canonical `provider_extensions` namespace that may not override protected generic semantics. Existing V2 snapshot/fingerprint, idempotency, safe transport, effective-parameter, result-ingest and cancellation/late-completion rules remain in force.


This document is the single schema authority for a versioned runtime recipe for one concrete Execution Route. It is the bridge between route/model/provider contracts and an actual callable runtime surface. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.5 replaces the stale in-body pointer to Execution Contracts Pre-v0.9 (§2.1) with the Manifest-resolved family reference, and makes the Pre-v0.4 safe-transport, provider-effective-value and remote-result controls (§5.1, §5.2, §8.1) part of the Verification Procedure (§12) and of the Minimal Slice-1 Recipe Profile (§14) whenever the route crosses a shell/CLI boundary, can coerce/adjust parameters or returns a remote URL. No other behavior changes. Pre-v0.4 adds safe transport semantics for untrusted request text, provider-effective parameter/adjustment capture, and hardened external-result retrieval controls. Pre-v0.3 route-freshness ownership remains in force.

---

# 1. Boundary

```text
MODEL SPEC
=
provider-independent model behavior / capabilities

PROVIDER ADAPTER
=
reusable provider-wide mechanics

EXECUTION ROUTE CONTRACT
=
model × provider × operation × endpoint/mode × version

EXECUTION ROUTE RECIPE
=
versioned executable binding for one concrete Execution Route Contract
```

An Execution Route Recipe does not own creative intent, project authority, pricing truth or route approval. It references those authorities.

---

# 2. Creation Rule

Create a concrete recipe only when:

```text
a route is needed for implementation / canary / production
AND
the current runtime must know how to invoke it
```

Do not prebuild recipes for every model/provider combination in the market.

---

# 2.1 Recipe Existence vs Recipe State

```text
ROUTE-TO-RECIPE RELATION
=
ABSENT | DRAFT | VERIFIED | STALE | INVALIDATED

EXISTING RECIPE OBJECT.recipe_state
=
DRAFT | VERIFIED | STALE | INVALIDATED
```

`ABSENT` is not a valid state inside an existing recipe object. It means there is no recipe object for that route. Canonical relation-state and route-freshness semantics live in the Execution Contracts family (`AI_Creative_Skill_Execution_Contracts`); the current version is resolved by the Current Design Manifest (Pre-v0.15 when this revision was validated).

Current route freshness is not owned by this recipe object. The current Execution Route/Registry instance owns `route_freshness_state`; the recipe stores the snapshot it was validated against.

---

# 3. Canonical Recipe Template

```yaml
route_recipe_id:
schema_family: EXECUTION_ROUTE_RECIPE
schema_version:
recipe_version:
recipe_state:
  # DRAFT | VERIFIED | STALE | INVALIDATED
validated_against_route_freshness:
  # validation-time snapshot: FRESH | RECHECK_REQUIRED | STALE | INVALIDATED
validated_at:
freshness_evidence_refs:

route_id:
route_contract_ref:
model_spec_ref:
provider_adapter_ref:
registry_fact_refs:
docs_ref:

provider_id:
model_id:
operation:
exposed_model_version:
endpoint_or_invocation:
execution_mode:
  # SYNC | ASYNC | WRAPPED_SYNC | MANUAL_UI

auth:
  secret_locator:
  auth_shape:

request:
  content_type:
  request_schema_or_mapping:
  prompt_field:
  parameter_mapping:
  reference_transport:
  upload_binding:
  untrusted_text_transport:
  shell_interpolation_policy:

response:
  job_id_path:
  state_path:
  state_mapping:
  result_path:
  cost_path_if_available:
  effective_parameters_path_if_available:
  adjustments_path_if_available:

async_policy:
  initial_poll_delay:
  poll_interval:
  backoff_policy:
  provider_retry_after_behavior:
  expected_progress_window:
  cancel_support:              # SYNCHRONOUS_CONFIRMED | ASYNC_BEST_EFFORT | UNSUPPORTED | UNKNOWN
  cancel_method:
  cancel_request_mapping:
  cancel_state_path:
  cancel_state_mapping:
  late_completion_possible:
  callback_support:            # PUSH | NONE | UNKNOWN
  callback_event_id_path:
  callback_sequence_path:
  callback_job_id_path:
  callback_attempt_id_path_if_available:
  callback_state_path:
  callback_state_mapping:
  callback_authentication:
    mechanism:                 # SIGNATURE | SHARED_SECRET | MTLS | PROVIDER_VERIFIED_CHANNEL | NONE | UNKNOWN
    signature_header_or_field:
    timestamp_header_or_field:
    secret_locator:
    verification_rule:
    replay_window_if_documented:
  duplicate_event_policy:
  out_of_order_policy:
  missing_sequence_fallback:

provider_extensions:
  # provider_id:
  #   extension_schema_version:
  #   fields:
  # Provider-specific fields may add data only.
  # They may not shadow/override protected generic canonical semantics.

execution_limits:
  max_concurrency:
  request_rate_limit_if_known:
  max_reference_count:
  supported_duration:
  supported_resolution_or_quality:
  supported_aspects:
  other_material_limits:

result_transport:
  kind:
    # DIRECT_BYTES | BASE64 | TEMP_URL | PERSISTENT_URL | PROVIDER_ASSET | MANUAL_EXPORT
  temporary:
  ttl_if_known:
  retrieval_priority:
  allowed_schemes:
  allowed_host_policy:
  redirect_policy:
  max_bytes_if_known:
  expected_mime_types:
  active_content_policy:

error_mapping:
  auth_failure:
  rate_limit:
  policy_rejection:
  model_not_found:
  version_removed:
  endpoint_removed:
  schema_changed:
  provider_failure:
  ambiguous_after_submit:

route_specific_prompt_notes:
known_route_failures:

last_verified:
verified_against:
verification_scope:
```

Unknown fields remain unknown; do not fill gaps by guessing.

---

# 4. Secret Boundary

```text
RECIPE MAY STORE
→ secret locator / environment variable name / connector binding name

RECIPE MUST NOT STORE
→ API key / bearer token / password / secret value
```

The actual runtime secret mechanism is host-specific.

---

# 5. Request / Response Exactness

The recipe should be concrete enough that the runtime can answer:

```text
where does the prompt go?
where do references go?
which fields control aspect / duration / quality?
how is the request submitted?
if async, where is the job id?
how are provider states mapped to canonical job states?
where is the result?
how is the result retrieved durably?
```

Do not rely on a prose note like “call the API normally” when a real canary depends on exact mechanics.

## 5.1 Untrusted request text is data

A recipe that crosses a shell/CLI/command boundary must specify how user text, scraped copy, filenames and other untrusted strings are transported without becoming command syntax. Prefer structured payloads, file/stdin transport or a proven escaping/binding mechanism.

```text
UNTRUSTED TEXT
!=
COMMAND FRAGMENT
```

Never require downstream code to guess how to quote arbitrary text safely. If exact safe transport is unknown, the recipe is not verified for that request surface.

## 5.2 Provider effective values / adjustments

When a route can return coerced or adjusted parameters, map where those values are exposed. The attempt/execution layer must be able to retain both the submitted request and provider-effective realization. A recipe must not normalize away evidence that the provider changed a hard requirement.

---

# 6. Sync vs Async

For `SYNC`:

```text
SUBMIT
→ response contains result or provider asset handle
→ retrieve / ingest
```

For `ASYNC`:

```text
SUBMIT
→ persist provider job id immediately
→ poll/reconcile according to recipe
→ COMPLETED
→ retrieve same job result
→ durable ingest
```

Polling values are route-specific. A recipe must not invent a universal 5-second, 15-second or 15-minute rule.

---

## 6.1 Cancellation, Callback Correlation and Late Completion

A recipe must state whether cancellation is synchronously confirmed, best-effort asynchronous, unsupported or unknown. A local cancel request must not be recorded as provider cancellation until the route exposes evidence for that transition.

For a callback-enabled route, the recipe must map, when exposed:

```text
event identity
provider job identity
provider sequence/version
provider state
authenticity/signature evidence
```

A callback is not allowed to mutate canonical job state merely because it arrived. The runtime first applies the Execution Contracts callback gate:

```text
CORRELATE TO INTENDED ROUTE/JOB/ATTEMPT
→ VERIFY AUTHENTICITY WHEN THE RECIPE DECLARES A MECHANISM
→ DEDUPLICATE / ORDER
→ MAP PROVIDER STATE
→ ONLY THEN RECONCILE CANONICAL STATE
```

If the provider exposes no callback-authentication mechanism, record `mechanism: NONE` only when current route evidence supports that fact. Do not silently treat `UNKNOWN` as `NONE`.

If the provider can complete after cancel request, the recipe must define how to reconcile the provider job, billing and returned artifact into the canonical `COMPLETED_AFTER_CANCEL` path. Duplicate or stale callbacks are ignored or reconciled idempotently; out-of-order events must not regress monotonic state. When sequence/event identity is unavailable, `missing_sequence_fallback` must define a safe poll/reconcile path rather than trusting arrival order.

---

## 6.2 Provider Extension Namespace

`provider_extensions` is the only generic recipe location for provider-specific fields that do not belong in the canonical schema.

```text
PROVIDER EXTENSION
→ MAY ADD ROUTE-SPECIFIC DATA

PROVIDER EXTENSION
→ MUST NOT SHADOW / OVERRIDE CANONICAL GENERIC SEMANTICS
```

Protected generic semantics include at least route/job identity, approval/fingerprint binding, callback/cancel mapping, cost/accounting, reference authority, output requirements and review state.

If the same semantic dimension appears both in a canonical field and an extension with conflicting values, the recipe is not valid for execution until the conflict is explicitly resolved. Unknown extension fields remain data; they do not become executable instruction by presence alone.

---

# 7. Concurrency / Rate Limits

Where documented or empirically established, retain:

```text
max concurrency
request/window limit
provider Retry-After behavior
polling cadence/backoff
```

When unknown, prefer conservative execution during canaries and record what is learned. “One at a time” is a safe canary default, not a universal production law.

---

# 8. Temporary Result Transport

A provider URL/handle is transport, not archive.

If a result URL is temporary:

```text
record TTL when known
set retrieval urgency
retrieve same completed job
verify bytes/media
write project-controlled copy
hash
write sidecar/index
```

If TTL is unknown, retrieve promptly rather than assuming permanence.

## 8.1 External result transport hardening

For URL/remote-result retrieval, define applicable transport controls instead of treating an arbitrary returned URL as trustworthy content. Depending on route/type, this may include HTTPS-only transport, public/allowlisted host rules, bounded redirects with destination re-check, bounded size/streaming, MIME/media validation and active-content handling for SVG/HTML or similar formats.

These controls are route mechanics, not creative-method rules. Retrieved active content is never executed merely because it came from a successful provider job.

---

# 9. Freshness / Recipe State Boundary

```text
DRAFT
→ written but not execution-validated

VERIFIED
→ passed the recorded scoped execution check

STALE
→ facts/schema/version may have changed; recheck required

INVALIDATED
→ current recipe cannot execute its Route Contract as recorded
```

Staleness/invalidation signals include:

```text
MODEL_NOT_FOUND
MODEL_VERSION_REMOVED
ENDPOINT_REMOVED
SCHEMA_CHANGED
provider docs/schema materially changed
integration no longer exposes required input/operation
```

A recipe can remain syntactically valid while current route freshness or production approval changes, and vice versa. `validated_against_route_freshness` is a historical validation snapshot, not current truth. Current `route_freshness_state` is resolved from the current Execution Route/Registry instance using the canonical meanings in the Execution Contracts.

---

# 10. Error Mapping

Route-specific provider errors should map into canonical behavior.

Examples:

```text
AUTH_FAILURE before submit
→ no submission proven; fix auth or route

RATE_LIMIT before submit
→ respect Retry-After/backoff; no duplicate semantic attempt

POLICY_REJECTION
→ stop; do not hop providers to bypass

MODEL_NOT_FOUND before submit
→ route/recipe stale or invalidated; refresh

CONNECTION LOSS after possible submit
→ UNKNOWN; reconcile first

COMPLETED + RESULT DOWNLOAD FAILURE
→ retrieve same job; do not regenerate
```

---

# 11. Prompt Notes Boundary

Route-specific prompt notes may document behaviors caused by this endpoint/mode/provider surface.

Do not duplicate provider-independent model guidance that belongs in Model Spec, and do not turn one anecdote into a hard rule without scoped evidence.

```text
MODEL BEHAVIOR
→ Model Spec

ROUTE-SPECIFIC BEHAVIOR
→ Route Recipe / Experience Memory
```

---

# 12. Verification Procedure

Before marking `VERIFIED`, retain at minimum:

```text
route id + recipe version
date
source/docs/schema checked
auth binding worked without exposing secret
request submitted successfully
sync/async behavior matched mapping
result retrieval succeeded
project-controlled ingest succeeded
material error/state mappings exercised where feasible
untrusted-text transport exercised without command interpolation when the request crosses a shell/CLI/command boundary (§5.1)
provider-effective values / adjustments captured when the route can coerce or adjust parameters (§5.2)
remote-result transport controls applied when results are retrieved by URL (§8.1)
```

Passing one canary verifies only the tested scope.

---

### 12.1 V2 Hardening Checks

Verification additionally records:

```text
execution snapshot / fingerprint transport is deterministic
idempotency behavior is known or explicitly UNKNOWN
cancel semantics are known or explicitly UNSUPPORTED
late completion behavior is tested when cancellation is asynchronous
duplicate / out-of-order callback handling is defined when callbacks exist
callback job correlation is mapped when callbacks exist
callback authenticity mechanism is mapped as SIGNATURE / SHARED_SECRET / MTLS / PROVIDER_VERIFIED_CHANNEL / NONE / UNKNOWN
invalid or unverifiable callbacks cannot mutate canonical state
cancellation method/state mapping is explicit when cancellation exists
provider-specific extensions use `provider_extensions` and cannot override protected generic semantics silently
recipe schema version is persisted
```

---

# 13. Human-Readable Recipe Filename

Recommended runtime filename:

```text
{model-or-family}_{provider}_{operation}.md
```

Examples are illustrative only:

```text
modelx_providera_generate-image.md
modely_providerb_reference-video.md
```

The filename is not route identity. `route_recipe_id` + `route_id` are authoritative.

---

# 14. Minimal Slice-1 Recipe Profile

Slice 1A may use a subset of the canonical recipe object, but field names and nesting MUST remain identical to §3. The minimum required fields are:

```yaml
route_recipe_id:
recipe_version:
recipe_state:
validated_against_route_freshness:
validated_at:
route_id:
provider_id:
model_id:
operation:
endpoint_or_invocation:
execution_mode:
auth:
  secret_locator:
  auth_shape:
request:
  content_type:
  request_schema_or_mapping:
  parameter_mapping:
  reference_transport:
  untrusted_text_transport:   # required when the request crosses a shell/CLI/command boundary (§5.1)
  shell_interpolation_policy: # required when the request crosses a shell/CLI/command boundary (§5.1)
response:
  job_id_path:
  state_path:
  state_mapping:
  result_path:
  effective_parameters_path_if_available: # required when the route can coerce/adjust parameters (§5.2)
  adjustments_path_if_available:          # required when the route can coerce/adjust parameters (§5.2)
async_policy: # required only when execution_mode is ASYNC / WRAPPED_SYNC
  initial_poll_delay:
  poll_interval:
  backoff_policy:
  provider_retry_after_behavior:
  cancel_support:
  cancel_method:                    # required when cancel_support != UNSUPPORTED
  cancel_state_mapping:             # same condition
  callback_support:
  callback_event_id_path:           # required when callback_support = PUSH and provider exposes event identity
  callback_sequence_path:           # required when callback_support = PUSH and provider exposes sequence/version
  callback_job_id_path:             # required when callback_support = PUSH
  callback_authentication:          # required when callback_support = PUSH; may explicitly record NONE/UNKNOWN
  duplicate_event_policy:           # required when callback_support = PUSH
  out_of_order_policy:              # required when callback_support = PUSH
  missing_sequence_fallback:        # required when callback_support = PUSH and no reliable sequence exists
provider_extensions:                # optional; only when route needs provider-specific non-generic fields
execution_limits:
  max_concurrency:
  request_rate_limit_if_known:
result_transport:
  kind:
  temporary:
  ttl_if_known:
  retrieval_priority:
  allowed_schemes:            # required when results are retrieved from a remote URL (§8.1)
  allowed_host_policy:        # same condition
  redirect_policy:            # same condition
  max_bytes_if_known:         # same condition
  expected_mime_types:        # same condition
  active_content_policy:      # same condition
error_mapping:
last_verified:
verified_against:
verification_scope:
```

A minimal profile is a subset of the canonical object, not a second schema. Do not invent aliases such as `auth_binding`, `execution_policy` or `submission_rate_limit_if_known`.

Do not block the first real canary waiting for a giant provider abstraction.

---

# 15. Derived Approved Route Index

A recipe may be referenced by the derived approved-route view, but this specification does not define that view. Canonical derivation belongs to `AI_Media_Provider_Registry_v0.9.md`; approval/state semantics belong to the Execution Contracts. The view never grants approval by itself.
