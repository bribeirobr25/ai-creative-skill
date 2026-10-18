> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Implementation Validation Plan · Pre-v0.13-V2.4-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
IMPLEMENTATION / CANARY VALIDATION PLAN

VERSION
=
Pre-v0.13-V2.4-CANDIDATE

DATE
=
2026-10-16

PARENT_DOCUMENT
=
AI_Creative_Skill_Architecture_Spec

LAST_VALIDATED_AGAINST
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.16-V2.3-CANDIDATE.md

CONTRACT_AUTHORITY
=
AI_Creative_Skill_Execution_Contracts

LAST_VALIDATED_CONTRACT
=
AI_Creative_Skill_Execution_Contracts_Pre-v0.19-V2.2-CANDIDATE.md

STATUS
=
PLANNED VALIDATION
NOT EXECUTED
```

Z2/Z3 hardening branch (2026-10-10): Pre-v0.9-V2.1-CANDIDATE extends the V2 zero-cost regression/canary plan with mandatory callback job-correlation/authenticity checks, duplicate/out-of-order callback resistance, explicit cancellation mapping and provider-extension conflict tests. Existing V2 regression targets remain in force. These tests validate design/runtime contracts; they do not replace host/provider canaries.

Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.10-V2.2-CANDIDATE makes creative-freedom regression mandatory for future creative hardening: diversity/mode-collapse, risk-ladder authority isolation, task-relative creative latitude, writer/visual/voice continuity, user override precision, canon-promotion boundaries and longitudinal canon anchoring. These remain model-based until empirical canaries exist.

E4 empirical-hardening branch (2026-10-11): Pre-v0.11-V2.2.1-CANDIDATE adds a narrow temporal-observability acceptance gate and makes requested open creative dimensions independently reviewable from identity/continuity success. It also adds regression coverage that an unattributed account-balance movement cannot be treated as job-level confirmed cost. These are validation rules only; Execution Contracts remain the transactional authority and Calibration retains the existing generic `creative_latitude_utilization` diagnostic.


This document separates implementation questions so one canary does not pretend to prove the whole system.

Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.7 puts the §2.1 subheadings at the correct level; states that the complete §2.1 pre-check requires a chosen host and that a host-neutral package check is only a structural pre-check that does not satisfy §2.1; and completes the §9.1 scenario schema with `NOT_RUN`, host/runtime, session and execution-time fields so a specified-but-unexecuted scenario cannot be reported as tested; a run outside a fresh session is recorded but does not count as acceptance evidence. No canary scope changes.

Pre-v0.6 strengthens the clean-package pre-check with version/reference/self-containment validation and adds a fresh-session behavioral regression suite for routing, authority, coercion and dependency-invalidation behavior. Existing paid/craft canaries remain unchanged.

---


## Conformance Authority

This plan may reference conformance cases by purpose, but the canonical numbered CT matrix and required behavior live only in the current `AI_Creative_Skill_Execution_Contracts`, with the version resolved by the Current Design Manifest.

# 1. Validation Principle

```text
ONE CANARY
=
ONE PRIMARY QUESTION
```

A pass is evidence only for the conditions actually tested. Every canary must record what passing **does not** prove.

---

# 2. Common Evidence Retention

Every real paid canary should retain, as applicable:

```text
request / task id
resolved authority / profile references
Execution Route + Execution Route Recipe version
model/provider/operation/version
quote / approval / reservation
attempt / provider job id
compiled execution spec / parameter snapshot
input/reference asset ids
output asset id + hash + sidecar
review verdict / inspection coverage
confirmed cost
observed defects / repairs
runtime timestamps
```

Do not retain secrets in evidence records.

---

## 2.1 Packaging Pre-check · Clean Package Load Canary

### Primary question

```text
CAN THE CHOSEN HOST DISCOVER AND LOAD THE DECLARED PACKAGE FROM A CLEAN COPY?
```

### Scope

This is a **zero-spend packaging pre-check**, not a new numbered Architecture/Contracts execution slice. It should run after a concrete host/runtime and package shape exist, before Slice 1A / the first paid execution canary.

Use a clean clone, checkout, copied release artifact or equivalent isolated package instance. Do not validate only from the working/editing directory.

The complete pre-check depends on the chosen host: steps 4 (install/load), 5 (host syntax) and 11 (activation case), and host resolution in step 6, cannot run before a host/runtime is selected. Before that, only a host-neutral **structural** check of the package artifact is possible (identity/version agreement, file presence, hashes, file-reference resolution, secret scan). Record it as:

```text
STRUCTURAL PACKAGE PRE-CHECK
≠
§2.1 CLEAN PACKAGE LOAD CANARY
```

A structural pass does not satisfy §2.1, does not exercise behavior and must not be reported as a §2.1 PASS. §2.1 remains not executed until the chosen host runs it.

### Procedure

```text
1. identify exact package source version / revision / release artifact
2. when one canonical package version is declared in multiple manifests/entry points, verify that declarations agree
3. create an isolated clean copy
4. install/load through the selected host's documented mechanism
5. verify host-required manifest/frontmatter/config syntax
6. verify declared package references resolve without reaching back into the working directory
7. verify required runtime rule/reference files are reachable from a declared entry point or explicitly classified non-runtime/historical
8. for independently installable modular units, verify required references stay within the declared package boundary
9. verify required files are present and JIT-loadable
10. verify no secret value was packaged as configuration/content
11. exercise one bounded activation/discovery case with no provider spend
12. record package version + host/runtime version + result
```

### PASS requires

```text
package is discoverable by the selected host
required entry metadata is valid for that host
required references/files resolve from the clean copy
version declarations agree where one canonical package version is intentionally shared
no accidental runtime rule/reference orphan is shipped
independently installable units are self-contained within their declared package boundary
no undeclared working-directory dependency is required
no secret value is embedded in the package
activation reaches the expected bounded router entry without provider execution
```

### FAIL / BLOCK examples

```text
works only from developer/working folder
missing referenced method/profile/rule file
conflicting canonical package versions across manifests/entry points
accidental orphan runtime rule/reference file with no declared owner/entry point
independently installable unit reaches outside its declared package boundary
host rejects manifest/frontmatter/config
installed copy points to absolute local paths
secret value appears in packaged content
package version/source revision cannot be identified
```

### Passing does NOT prove

```text
provider execution works
paid approval/accounting works
creative quality
async recovery
all activation intents or overlaps are correct
future host/plugin update behavior is safe
```

---

# 3. Slice 1A · Basic Execution Canary

## Primary question

```text
CAN THE SYSTEM SAFELY EXECUTE, INGEST AND ACCOUNT FOR ONE REAL ASSET?
```

## Scope

Use one external non-Higgsfield static-image route. A synchronous route is allowed and may be preferable for isolating basic execution mechanics.

## Prerequisites

```text
one route selected under normal eligibility rules
minimal verified/draft-for-canary Execution Route Recipe
current quote mechanism
single-job approval
reservation capacity
project-controlled output location
```

## Procedure

```text
1. receive one simple bounded production request
2. resolve route + recipe + freshness
3. quote
4. obtain explicit approval
5. reserve maximum authorized amount
6. submit exactly one logical paid attempt
7. receive/retrieve result
8. durable ingest
9. write sidecar / immutable provenance refs
10. review
11. reconcile confirmed cost / release reservation remainder
12. end task
```

## PASS requires

```text
no spend before approval/reservation
route identity explicit
recipe/binding usable
attempt attributable
result becomes project-controlled asset
hash + sidecar exist
review verdict exists
cost reconciles
no unauthorized adjacent work
```

## FAIL / BLOCK examples

```text
cannot prove which route ran
secret leaked into recipe/log
result remains only on temporary provider URL
cost cannot be reconciled
sidecar cannot point to execution provenance
provider swap occurs silently
```

## Passing does NOT prove

```text
async recovery
job reconciliation after interruption
specialist craft quality
reference-heavy fidelity
provider parity
talking persona / voice / lipsync
```

---

# 4. Slice 1B · Async / Recovery Canary

## Primary question

```text
CAN THE SYSTEM SURVIVE INTERRUPTION WITHOUT DUPLICATE PAID SUBMISSION?
```

## Scope

Use one genuinely asynchronous route with a provider-visible job/task identifier.

## Prerequisites

```text
Execution Route Recipe maps submit / status / completion / result retrieval
job state and retrieval state persistence
reconcile/resume path
idempotency strategy where provider supports it
cancel mapping when the route exposes cancellation
callback job-correlation mapping when the route uses callbacks
callback authenticity mapping when the provider exposes an authenticity mechanism
duplicate/out-of-order callback policy when callbacks exist
```

## Procedure

```text
1. quote / approve / reserve
2. submit
3. persist provider job id immediately
4. observe SUBMITTED / PENDING
5. interrupt or intentionally resume from persisted state
6. reload attempt
7. reconcile/poll the same provider job
8. when callbacks exist, exercise at least one valid callback plus duplicate/out-of-order handling
9. when feasible, inject/replay one mismatched or unauthenticated callback and verify it cannot mutate canonical state
10. when cancellation exists, exercise CANCEL_REQUESTED → CANCELED or COMPLETED_AFTER_CANCEL according to provider evidence
11. retrieve same completed job
12. durable ingest
13. review / cost reconcile
```

A controlled simulation of local interruption is acceptable; do not sabotage the provider itself.

## PASS requires

```text
same provider job survives local interruption
no second paid submission is created
UNKNOWN triggers reconciliation rather than regeneration
DOWNLOAD_FAILED retrieves same job
known result TTL/retrieval deadline is respected
callback with mismatched job correlation cannot mutate state
callback failing the declared authenticity check cannot mutate state
duplicate callback is idempotent
out-of-order callback cannot regress canonical job state
CANCEL_REQUESTED is not treated as CANCELED without provider evidence
late completion is not automatically accepted/delivered
```

## Passing does NOT prove

```text
quality parity across providers
policy-failure handling on every provider
all network-failure variants
batch recovery
```

---

# 5. Slice 1C · Static Craft Canary

## Primary question

```text
DO SPECIALIST METHODS MATERIALLY IMPROVE DECISION / OUTPUT QUALITY?
```

## Scope

One bounded static task with enough difficulty to exercise multiple craft methods without introducing video/audio complexity.

Candidate stack:

```text
buyer/evidence basis when required
Ads or Organic strategy
Image Direction
Typography / Layout
Route Compilation
QA · Evidence & Rights
QA · Realism & Performance
Localized Repair if needed
```

## Comparison

Where practical:

```text
BASELINE
same route + same source assets + generic specification

vs

SPECIALIST
same route + same source assets + specialist method stack
```

Use the same acceptance rubric and review coverage.

## PASS evidence

A pass should show observable improvement in one or more agreed dimensions without violating authority/cost/scope, for example:

```text
commercial/message clarity
product/reference fidelity
composition / hierarchy
exact-text handling
fewer known failure modes
better review verdict
less repair cost / fewer retries
```

A single win does not prove universal superiority. Record the causal hypothesis and counterexamples.

---

# 6. Slice 2 · Critical Provider-Independence / Talking Persona Canary

## Primary question

```text
CAN A HARD RECURRING-PERSONA DEPENDENCY MOVE TO AN ALTERNATIVE ROUTE WITHOUT LOSING REQUIRED QUALITY/AUTHORITY?
```

## Required dimensions

```text
identity fidelity
PT-BR naturalness
spoken-text fidelity
required voice identity or exact approved audio handling
lipsync
mouth / teeth / jaw integrity
eye / face naturalness
project environment / reference constraints where applicable
final-resolution acceptance
cost / reproducibility
```

Use the Project Profile authority. Do not invent a missing recurring voice or change canon to make a route pass.

## Progressive validation

```text
smallest technically valid CTA / short clip
→ review
→ only then longer / multipart production
```

A route that passes short talking-head speech does not automatically pass long duration, multipart continuity or all personas.

---

# 7. Route Invalidation Test

This is a regression/conformance exercise, not necessarily a paid generation.

Test or simulate a route fact becoming stale:

```text
model id removed
endpoint changed
schema changed
recipe deliberately marked STALE
```

Expected behavior:

```text
no material submission using stale binding
route/recipe state updated
facts refreshed/revalidated
creative method not blamed for upstream invalidation
possible prior submission still reconciled before fallback
```

---

# 8. Naming / Provenance Check

For each produced asset verify:

```text
human-readable filename is useful but non-authoritative
asset_id remains stable if the file is renamed
hash identifies exact bytes
sidecar resolves route/model/provider/job/execution spec
parameter snapshot can be recovered
references/parents remain traceable
```

---

# 9. Evidence Promotion Rule

```text
CANARY PASS
≠
UNIVERSAL APPROVAL
```

Promotion examples:

```text
single pass
→ PROJECT_EMPIRICAL for tested scope

repeated benchmark pass
→ may justify APPROVED_DRAFT for defined capability/project scope

master/final-quality approval
→ requires the corresponding final-resolution / project-specific rubric
```

Route evidence/approval states remain governed by Execution Contracts and the Provider Registry.

---

# 9.1 Behavioral Scenario Regression Suite

Canaries prove concrete execution paths; a scenario suite protects user-visible orchestration behavior across package revisions. Run important scenarios in fresh/clean sessions so hidden conversation state does not make a broken package look healthy.

Each scenario records:

```yaml
scenario_id:
package_revision:
user_request:
expected_authority_or_profile:
expected_activation_and_routing:
expected_gates_or_stop:
expected_deliverable:
forbidden_behavior:
host_runtime_and_version:
fresh_session:  # YES | NO
executed_at:
result:  # PASS | PARTIAL | FAIL | NOT_RUN
failure_mode:
time_to_result_if_useful:
```

A scenario that has not been executed on the tested host records `result: NOT_RUN`; a written scenario is a regression specification, not evidence that the package behaves as expected. An executed scenario records `fresh_session: YES` or `NO`; a run with `fresh_session: NO` stays in the record but does not count as acceptance or regression evidence. Include both single-capability and chain/overlap cases. Add or update a scenario when a real bug is found, a material behavior changes, or a new public capability ships. Test what the user would observe, not internal logging trivia. Do not import external numeric regression thresholds as universal law; compare revisions and investigate material regressions under project/runtime risk.

Required regression scenarios should include at least:

```text
UNKNOWN/NAMED ROUTE OR MODEL
→ verify/discover; never invent the capability

BROAD THIRD-PARTY ACTIVATION OVERLAP
→ current project authority retains ownership; no paid execution without delegation/approval

PROVIDER COERCES HARD OUTPUT PARAMETER
→ effective value is retained and mismatch is surfaced/replanned/stopped

UPSTREAM APPROVED AUTHORITY REVISION CHANGES
→ only recorded dependents are reopened/invalidated; unrelated accepted state remains accepted
```

A scenario pass is scoped evidence for that package revision and tested host/runtime; it is not universal provider/model approval.

---

# 9.2 Zero-Cost Contract-Model Regression Suite

Before a candidate design is promoted or a paid canary is run, execute a deterministic suite against the candidate contracts. At minimum cover:

```text
fixed conformance oracle
property-based / fuzz invariants
job × retrieval state model checks
canonical serialization / fingerprint equivalence
approval-binding mutation tests
concurrency interleavings / stale-write rejection
schema migration including ambiguous legacy records
corrupted-state recovery
cross-project isolation
constraint propagation across specialists
large-batch / chunking / lineage
synthetic temporal video/audio coverage fixtures
authority-laundering mutations
false-provider-success separation
```

Each run records seed, candidate document versions, case counts, invariants, failures and known limits. A model-based PASS proves consistency of the tested contract model only; it does not prove installed runtime behavior.

New mandatory regression targets from the 2026-10-10 validation round:

```text
APPROVAL ↔ EXACT SNAPSHOT/FINGERPRINT
STALE CONCURRENT WRITE REJECTED
AMBIGUOUS SCHEMA MIGRATION STOPS
COMPOSITE REFERENCE AUTHORITY REMAINS SCOPED
CANCEL_REQUESTED ≠ CANCELED
LATE COMPLETION ≠ ACCEPTED/DELIVERED
STATE CORRUPTION BLOCKS RESUME/EXECUTE/DELIVER
CROSS-PROJECT ASSET REUSE REQUIRES EXPLICIT TRANSFER
BATCH CHUNKING DOES NOT RESET GLOBAL SEMANTICS
CALLBACK JOB / ATTEMPT CORRELATION REQUIRED BEFORE STATE MUTATION
CALLBACK AUTHENTICITY FAILURE / REQUIRED-BUT-UNVERIFIED AUTH BLOCKS STATE MUTATION
DUPLICATE / STALE CALLBACK DOES NOT REGRESS STATE
ASYNC CANCEL MAPPING IS EXPLICIT WHEN SUPPORTED
PROVIDER EXTENSION CANNOT SHADOW PROTECTED GENERIC SEMANTICS

Z4 / Z4.1 CREATIVE-BALANCE REGRESSION:
CREATIVE RISK NEVER RELAXES FACTUAL / RIGHTS / IDENTITY / APPROVAL / SAFETY AUTHORITY
DISTINCT-CONCEPT REQUESTS DO NOT COLLAPSE INTO COSMETIC PARAPHRASES WHEN OPEN DIMENSIONS EXIST
CONTROLLED VARIANTS ARE NOT PENALIZED FOR INTENTIONAL PRESERVATION
TASK-RELATIVE PRESERVE / BOUNDED / OPEN POLICIES REMAIN SEPARATE FROM PRIORITY
USER PRESERVE / EXPLORE OVERRIDES AFFECT ONLY NAMED LEGITIMATE DIMENSIONS
WRITER / PERSONA VOICE CAN STAY STABLE WHILE AUTHORIZED HOOK / TITLE / EXAMPLE / STRUCTURE VARIES
CHARACTER / WORLD / ART DIRECTION CAN STAY STABLE WHILE AUTHORIZED CAMERA / LIGHT / BLOCKING / CONCEPT VARIES
VOICE IDENTITY CAN STAY STABLE WHILE AUTHORIZED EMOTION / PACE / PAUSE / BREATHING / EMPHASIS VARIES
LONGITUDINAL IDENTITY-BEARING STATE ANCHORS TO CURRENT CANON / APPROVED AUTHORITY, NOT DERIVATIVE CHAIN ALONE
REPEATED GENERATED EXPRESSION DOES NOT AUTO-PROMOTE TO CANON
CONSISTENCY IS NOT EQUATED WITH REPETITION; CREATIVITY IS NOT EQUATED WITH RANDOMNESS
```

---

## 9.3 E4 Empirical Hardening Regression

The E4 empirical canaries exposed two validation gaps without changing the underlying transactional or creative-authority ownership.

### Temporal observability gate

When a verdict depends on a material temporal state, object condition or temporal invariant, record whether the relevant state was sufficiently observable under the declared inspection coverage.

```text
UNOBSERVED
!=
PRESERVED
```

```text
MATERIAL TEMPORAL STATE
+ SUFFICIENT OBSERVATION
+ STATE SATISFIES AUTHORITY
→ PASS MAY BE AVAILABLE FOR THAT ASSERTION

MATERIAL TEMPORAL STATE
+ INSUFFICIENT OBSERVATION
→ REVIEW / UNVERIFIED / INSUFFICIENT_EVIDENCE
→ NOT PASS
```

Absence of a visible violation is not evidence that a hidden state remained correct.

### Independent review of requested open dimensions

Identity/continuity success must not substitute for compliance with a materially requested `OPEN_EXPLORATION` dimension. When an open dimension is part of the task objective, use the existing Calibration `creative_latitude_utilization` semantics or an implementation-equivalent review to determine whether the legitimate creative space was meaningfully used.

```text
IDENTITY PASS
!=
CAMERA / MOTION / OTHER OPEN-DIMENSION PASS
```

Do not create a universal requirement for more movement or novelty. A deliberately stable dimension remains valid when requested or functionally appropriate.

### Cost-attribution conformance regression

The current Execution Contracts remain the only transactional cost authority. Add the following regression target without creating a second ledger:

```text
UNATTRIBUTED ACCOUNT-BALANCE MOVEMENT
!=
JOB-LEVEL CONFIRMED COST
```

A cost assertion passes only through the existing attempt-attributable quote / reservation / confirmed-cost / reconciliation semantics. Account-balance movement may be retained as diagnostic evidence by an implementation, but it does not become confirmed job spend merely because it occurred in the same observation window.

New mandatory regression targets:

```text
UNOBSERVED MATERIAL TEMPORAL STATE DOES NOT PASS
IDENTITY / CONTINUITY PASS DOES NOT AUTO-PASS A MATERIALLY REQUESTED OPEN DIMENSION
UNATTRIBUTED BALANCE DELTA DOES NOT BECOME JOB-LEVEL CONFIRMED COST
```

---

# 10. Stop / Learn Loop

After every canary:

```text
persist evidence
record defects / trade-offs / repair
update scoped failure memory if justified
update Execution Route Recipe / Registry facts only where evidence supports it
add regression test for reusable failure mode
```

Do not immediately add new infrastructure merely because it would be aesthetically pleasing. Add controls when a real execution demonstrates the need.


---

# V2.3 Architecture-Reactivation Validation Addendum

## Objective

Validate that reactivating `RESEARCH_ONLY` and adding the narrow `PRODUCT_MARKETPLACE_INTELLIGENCE` candidate improves real-user coverage without stealing Ads/Organic ownership or weakening current state/authority invariants.

## Real-User Regression Corpora

### U1 · Commerce-to-Creative · 45 turns

Must verify:
- turns 1–28 remain negative for primary Creative ownership;
- turns 29–37 remain research/strategy/project-state work unless a creative deliverable is requested;
- turn 38 activates Organic/Image when profile media is requested;
- turns 39–41 preserve accepted-state/local-repair behavior for bio/copy iteration;
- turns 42–45 activate Organic/Video as appropriate;
- selecting Higgsfield changes execution route only;
- exact product/entity identity survives Research → Creative handoff;
- commerce evidence transfers without procurement/purchase authority.

### U2 · Autonomous Venture · 19 turns

Must verify:
- persistent project objective survives bounded task completion;
- standalone research routes to RESEARCH_ONLY;
- creative tasks route to current Creative Work Profiles;
- tool connection changes capability availability, not authority;
- negative Git scope persists;
- non-commercial validation can remain separate from monetization gates;
- language/brand changes invalidate only affected current/future state;
- publishing/deployment remain separately authorized actions;
- broad autonomy maps to action-class envelope, not unlimited authority;
- analytics evidence returns to project state without seizing ownership.

## Static Pre-Branch Pack Already Completed

```text
owner / routing fixtures               36 / 36 PASS
authorization fixtures                  8 / 8 PASS
handoff packet completeness             4 / 4 PASS
handoff zero authority transfer         4 / 4 PASS
creative routing regression canaries   24 / 24 PASS
mixed-request research subtask cases    6 / 6 PASS

TOTAL ASSERTIONS = 82
FAILURES = 0
```

This is design validation only, not implementation/runtime proof.

## Required Candidate-Branch Regression Families

A. Owner Resolution
B. Handoff Integrity
C. Project / Task Separation
D. Selective Invalidation
E. Product / Marketplace Method Ablation
F. Supplier Specialist Non-Creation Regression
G. Authority Orthogonality
H. Existing Creative Inheritance

Key precedence:

```text
standalone research
→ RESEARCH_ONLY

research + final ad
→ ADS final owner
→ RESEARCH_ONLY bounded support

research + final organic post/video
→ ORGANIC_CONTENT final owner
→ RESEARCH_ONLY bounded support
```

Every material cross-profile handoff must validate stable entity/source refs, evidence class/confidence/freshness, explicit unknowns, accepted/protected state, zero implicit permissions transfer and action-authorization recheck.

V2.3 remains candidate unless U1/U2 routing/state regressions and inherited affected-family V2.2.1 regression remain green.

## V2.3 Candidate-Branch Validation Result · 2026-10-11

Inherited V2.2.1 regression harness reused against this candidate:

```text
checks = 3,610,432
failures = 0
status = PASS
```

V2.3-specific reactivation fuzz ZR22–ZR29:

```text
checks = 1,350,000
failures = 0
status = PASS
```

Static design + branch-integrity assertions:

```text
82 + 74 = 156
failures = 0
```

Current candidate validation total:

```text
4,960,588 checks / assertions
0 failures
```

Scope note: the historical full 33M Z2/Z3 suite was not rerun for V2.3 and must not be claimed as V2.3 validation.

These results justify continued candidate testing. They do not by themselves promote V2.3 to `00_ACTIVE`.


---

## V2.4 real-world hardening — real-world completeness, guidance and creativity regression

Use source-linked Della/Influencer cases as scenario fixtures and a clean-session *held-out* run, not as bundled answer keys in the installed skill. Minimum matrix: (1) new 8-field full character Bible vs names-only negative control; (2) ten per-item Bia ideas with hooks and evidence-vs-hypothesis; (3) Nina leading supertopmodel premise not downgraded by secondary brand mission; (4) storyboard-first multi-chapter and optional accepted storyboard reuse; (5) editorial one-shot skip; (6) continuous PCN direction vs required deterministic motion graphic timeline; (7) one canonical Della printed pouch not edible croissant; (8) two characters and prop transfers, counts, delayed reveal across chapter seams; (9) local video repair preserves audio/camera or FAIL; (10) project next-action guidance does not authorize paid generation/publishing; (11) source evidence and connected-tool accessibility are verified; (12) versioned JIT loading/fresh session in Work and other hosts.

Structural/seeded fuzz and adversarial fixtures test **only deterministic invariants**, not artistic quality, provider results, loaded skill behavior or causality. Run original C1–C8 ownership/authority canaries in fresh sessions before promotion; no claim that inherited 4,960,588 V2.3 checks were reexecuted unless actually run. Smoke-test package discovery after installation; then one provider canary under approved budget. Record baseline V2.3 alongside V2.4 for first-pass completeness and user intervention comparison.

