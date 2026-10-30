# AI Media Provider Registry · v0.12

## Status

```text
DOCUMENT TYPE
=
LIVE / VOLATILE PROVIDER + ROUTE KNOWLEDGE REGISTRY

VERSION
=
v0.12

DATE
=
2026-10-09

SUPERSEDES
=
AI_Media_Provider_Registry_v0.11.md
```

This registry stores changing execution facts.

It does not define creative method and does not approve a route merely because it is listed.

v0.10 preserves the provider/model facts from v0.9 and adds Remotion 4.0.533 as a **DOCUMENTED / UNTESTED local deterministic finishing candidate**. The reviewed source is the official Remotion repository at the probable pre-ZIP revision; exact ZIP↔commit byte identity could not be proven because the 584.8 MB Drive archive exceeds the connector download ceiling. Runtime installation, license eligibility, Route Recipe and production approval remain unresolved and must be rechecked before execution.

v0.11 is a narrow correction applied by the independent validator at the operator's request: §24 now names the commit that was on `main` when the ZIP was made, and §24.2 records the headcount wording of the Remotion FAQ and Terms. All other facts are unchanged from v0.10.

v0.12 · Validator correction round (operator-agreed window, 2026-10-09): §15.6 records the Pilot 01 Phase 10B Seedance 2.5 connector execution failures as `PROJECT_EMPIRICAL` evidence scoped to the current MCP connector configuration, and §15.7 records the conflicting third-party Seedance 2.5 output-resolution claims for recheck before any use; §12 points to §15.7. No price, limit or route-approval fact is added or changed.

---

# 1. Evidence Classes

```text
OFFICIAL_PUBLIC
PROJECT_EMPIRICAL
OPERATOR_REPORTED
THIRD_PARTY
UNVERIFIED
```

Every material fact should carry:

```yaml
value:
scope:
checked_at:
evidence_class:
source:
observed_surface:
observed_section:
retrieval_mode:
observation_snapshot_ref:
notes:
```

A provider row with no value/date/source is not treated as a verified fact merely because it carries an evidence label.

For dynamic public pages, `observed_surface` / `observed_section` should identify what was actually visible during the check. `retrieval_mode` records how the page was observed when material. `observation_snapshot_ref` may be null/`NOT_RETAINED`; do not invent a snapshot after the fact. If two official surfaces or readers expose materially different current values, preserve both observations with scope/date instead of silently overwriting one. Execution-time quote/metering remains authoritative for spend.

---

# 2. Execution Vocabulary Authority

Canonical definitions for:

```text
route evidence state
production approval state
job state
retrieval state
stop labels
benchmark record semantics
```

live in:

```text
AI_Creative_Skill_Execution_Contracts_Pre-v0.9.md
```

This Registry stores current **instances** of those states and current provider/model/route facts.

---

# 3. Architecture Vocabulary

```text
MODEL
=
provider-independent model family knowledge

PROVIDER
=
execution company/service

EXECUTION ROUTE
=
model × provider × operation × endpoint/mode × version
```

Same model name across providers does not prove parity.

```text
EXECUTION ROUTE RECIPE
=
versioned runtime binding for one concrete Execution Route
```

A recipe is not a quality verdict and is not a second source of provider truth. It points back to current Registry facts/docs, carries its own recipe state, and records only the route-freshness snapshot/evidence against which it was validated.

---

# 4. Integration Status

```text
HOST_NATIVE
DIRECT_API
OFFICIAL_MCP
COMMUNITY_MCP
MANUAL_UI
NOT_VERIFIED
```

Integration state is a fact about access, not a quality verdict.

## 4.1 Execution Route Recipe / Freshness State

Current route instances may store:

```yaml
route_recipe_ref:
route_recipe_relation_state:
  # ABSENT | DRAFT | VERIFIED | STALE | INVALIDATED
route_freshness_state:
  # FRESH | RECHECK_REQUIRED | STALE | INVALIDATED
recipe_last_verified:
```

Canonical relation-state and route-freshness meanings live only in `AI_Creative_Skill_Execution_Contracts_Pre-v0.9.md`. The existing-recipe object schema lives in `AI_Creative_Skill_Route_Recipe_Spec_Pre-v0.3.md`.

`ABSENT` is a route-to-recipe relationship state, not a state stored inside an existing recipe object. `VERIFIED` means the recipe matched its tested execution scope; it does not mean the route is approved for every project/capability or that output quality passed every rubric.

```text
CURRENT route_freshness_state
=
this Registry's current Execution Route instance
under Execution Contract semantics
```

An Execution Route Recipe stores only the freshness snapshot/evidence against which it was validated. If that snapshot conflicts with the current Registry state, the current Registry/Execution Route state governs execution.

---

# 5. Provider Comparison Criteria

Filter first by:

```text
required capability
project permission
input/reference support
privacy / rights constraints
route evidence state
production approval state
freshness
reliability
```

Then compare:

```text
quality
latency
current quoted cost
credit expiry / subscription overhead
retention
data handling
support
supply-chain transparency
effective cost per accepted asset
```

No permanent `KIE → fal → WaveSpeed` ordering exists.

## 5.1 Derived Approved Route Index

A runtime may derive a compact operational view:

```text
capability / task class
→ project-permitted routes
→ APPROVED_DRAFT / APPROVED_MASTER state
→ recipe/freshness state
→ current benchmark scope
```

The index must be computed from current Registry + Execution Route Contract + Project Profile state. It is not maintained as a separate manual truth table. If a route becomes stale, invalidated, disallowed or deprecated, the derived view must stop presenting it as currently approved.

---

# 6. Current Provider Summary

| Provider | Role candidate | Integration status | Route evidence | Production approval |
|---|---|---|---|---|
| OpenAI API | image generation/edit | DIRECT_API | DOCUMENTED | UNTESTED |
| Google Gemini/Veo | high-end video | DIRECT_API | DOCUMENTED | UNTESTED |
| fal | broad model aggregator | DIRECT_API + OFFICIAL_MCP | DOCUMENTED | UNTESTED |
| WaveSpeedAI | multi-model aggregator candidate | DIRECT_API + OFFICIAL_MCP | DOCUMENTED | UNTESTED |
| KIE.ai | cost-optimized aggregator candidate | DIRECT_API; MCP NOT_VERIFIED | DOCUMENTED | UNTESTED |
| Runway Dev | multi-model production API/router | DIRECT_API | DOCUMENTED | UNTESTED |
| Replicate | open/specialized model lab | DIRECT_API | DOCUMENTED | UNTESTED |
| ElevenLabs | audio / voice transform | DIRECT_API | DOCUMENTED | UNTESTED for recurring locked voice |
| Remotion | local deterministic finishing/reframe candidate | NOT_VERIFIED | DOCUMENTED | UNTESTED |
| Higgsfield | empirical workflow baseline | existing project workflow/UI/integration | PROJECT_EMPIRICAL | baseline only |

`WaveSpeedAI` is a **candidate**, not a preferred route until our benchmarks justify preference.

---

# 7. OpenAI API · Current Image Facts

## GPT Image 2

Checked: `2026-10-07`

Official source:
`https://developers.openai.com/api/docs/guides/image-generation`

Revalidated observation: the current official image-generation guide still shows the canonical GPT Image 2 examples below and states that total request cost also depends on input/output token usage.

Official canonical-size output-cost examples for `gpt-image-2`:

| Output | Low | Medium | High |
|---|---:|---:|---:|
| 1024×1024 | $0.006 | $0.053 | $0.211 |
| 1024×1536 | $0.005 | $0.041 | $0.165 |
| 1536×1024 | $0.005 | $0.041 | $0.165 |

Underlying current rates shown by OpenAI for GPT Image 2 / 2.5 include:

```text
image input   $8 / 1M tokens
cached image  $2 / 1M tokens
image output  $30 / 1M tokens
text input    $5 / 1M tokens
cached text   $1.25 / 1M tokens
```

OpenAI notes that actual per-image cost varies with token consumption, resolution and quality.

Evidence:

```text
OFFICIAL_PUBLIC
```

Route state:

```text
DOCUMENTED
UNTESTED BY OUR SYSTEM
```

---

# 8. Google · Veo 3.1

Checked: `2026-10-07`

Official source:
`https://ai.google.dev/gemini-api/docs/pricing`

Revalidated observation: the current official pricing table still lists the Veo 3.1 Standard/Fast/Lite model IDs and paid-tier per-second prices below.

Current paid-tier pricing listed by Google:

| Model | Resolution | Price / second |
|---|---|---:|
| Veo 3.1 Standard with audio | 720p / 1080p | $0.40 |
| Veo 3.1 Standard with audio | 4K | $0.60 |
| Veo 3.1 Fast with audio | 720p | $0.10 |
| Veo 3.1 Fast with audio | 1080p | $0.12 |
| Veo 3.1 Fast with audio | 4K | $0.30 |
| Veo 3.1 Lite with audio | 720p | $0.05 |
| Veo 3.1 Lite with audio | 1080p | $0.08 |

Current model IDs shown include:

```text
veo-3.1-generate-preview
veo-3.1-fast-generate-preview
veo-3.1-lite-generate-preview
```

Google also states paid-tier inputs/outputs are not used to improve products on that pricing table, while free-tier treatment differs.

Evidence:

```text
OFFICIAL_PUBLIC
```

Route state:

```text
DOCUMENTED
UNTESTED BY OUR SYSTEM
```

---

# 9. fal

Checked: `2026-10-07`

## 9.1 Credit expiry

Official Terms last updated 2026-09-08 state:

```text
paid purchased credits expire 365 days from purchase
free/promotional credits expire after 90 days
```

Source:
`https://fal.ai/legal/terms-of-service`

Evidence:

```text
OFFICIAL_PUBLIC
```

## 9.2 Official hosted MCP

fal's official blog documents a hosted MCP endpoint:

```text
https://mcp.fal.ai/mcp
```

with model discovery, schema, pricing, upload, execution and job-status tools.

Source:
`https://blog.fal.ai/connect-your-ai-to-1-000-models-with-the-fal-mcp-server/`

Integration:

```text
DIRECT_API
OFFICIAL_MCP
```

## 9.3 GPT Image 2 on fal

Revalidated on `2026-10-07` against the official model page. The page currently lists text-to-image projections including:

| Output | Low | Medium | High |
|---|---:|---:|---:|
| 1024×1024 | $0.006 | $0.053 | $0.211 |
| 1920×1080 | $0.005 | $0.040 | $0.158 |
| 3840×2160 | $0.012 | $0.101 | $0.401 |

Source:
`https://fal.ai/models/openai/gpt-image-2`

The page also exposes queue submission/status/result handling, so async execution is available even though convenience clients can present a blocking `subscribe` flow.

Route state:

```text
DOCUMENTED
UNTESTED BY OUR SYSTEM
```

---

# 10. WaveSpeedAI

Checked: `2026-10-06`

## 10.1 Billing / credit policy

Current official WaveSpeed pages state:

```text
pay as you go
no monthly membership required
paid/top-up credits do not expire
```

Sources:
`https://wavespeed.ai/higgsfield-api`
`https://wavespeed.ai/higgsfield-alternative`

Evidence:

```text
OFFICIAL_PUBLIC
```

## 10.2 Current starting prices

Current English pricing page lists starting prices:

| Model | Starting price |
|---|---:|
| GPT Image 2 | $0.01 / image |
| Nano Banana 2 | $0.045 / image |
| Nano Banana Pro | $0.14 / image |
| Seedance 2.5 | $0.18 / second |
| Wan 3.0 | $0.05 / second |
| Kling 3.0 Std | $0.084 / second |
| Veo 3.1 Fast | $0.10 / second |
| InfiniteTalk | $0.03 / second |

Source:
`https://wavespeed.ai/pricing`

These are starting prices; exact cost depends on route parameters such as resolution, duration and references.

Localized/stale pages can show different historical values. Execution should therefore use current route-level quote rather than a copied registry number.

## 10.3 Official MCP

WaveSpeedAI's official GitHub organization currently pins an MCP server for the live catalog, with schema introspection, file upload, price quotes and prediction recovery.

Sources:
`https://github.com/WaveSpeedAI`
`https://github.com/WaveSpeedAI/mcp-server`

Integration:

```text
DIRECT_API
OFFICIAL_MCP
```

Route state:

```text
DOCUMENTED
UNTESTED BY OUR SYSTEM
```

Role:

```text
MULTI-MODEL AGGREGATOR CANDIDATE
not
PRIMARY / PREFERRED UNTIL BENCHMARKED
```

---

# 11. KIE.ai

Checked: `2026-10-07`

## 11.1 Credit / retention facts

KIE's official site currently states:

```text
credits do not expire
```

Its official getting-started documentation states:

```text
generated media retention = 14 days
log/text/metadata retention = 2 months
all generation tasks are asynchronous
successful submission returns task_id
final result requires webhook or polling
```

Sources:
`https://kie.ai/`
`https://kie.ai/getting-started`
`https://docs.kie.ai/`

Evidence:

```text
OFFICIAL_PUBLIC
```

## 11.2 GPT Image 2 current KIE pricing

KIE's official GPT Image 2 page was revalidated on `2026-10-07` and currently lists:

```text
1K = $0.03
2K = $0.05
4K = $0.08
```

Source:
`https://kie.ai/gpt-image-2`

## 11.3 Integration / continuity

```text
DIRECT_API = DOCUMENTED
OFFICIAL_MCP = NOT_VERIFIED
```

Do not convert creator speculation about KIE's upstream supply method into fact.

Continuity/supply-chain risk remains:

```text
UNASSESSED
```

not “high” or “low”. It requires evidence.

Route state:

```text
DOCUMENTED
UNTESTED BY OUR SYSTEM
```

Operational rule:

```text
KIE RESULT
→ DURABLE INGEST IMMEDIATELY
```

because provider media retention is 14 days.

---

# 12. Runway Dev

Checked: `2026-10-06`

Official source:
`https://docs.dev.runwayml.com/guides/pricing/`

Current API credit value:

```text
1 credit = $0.01
```

Selected current video pricing:

| Model | Price |
|---|---:|
| `wan3` 480p | 5 credits/s |
| `wan3` 720p | 10 credits/s |
| `wan3` 1080p | 20 credits/s |
| `seedance2_5` 480p output | 20 credits/s |
| `seedance2_5` 720p output | 30 credits/s |
| `seedance2_5` 1080p output | 68 credits/s |
| `veo3.1_fast` with audio | 15 credits/s |
| `veo3.1_fast` without audio | 10 credits/s |
| `veo3.1` with audio | 40 credits/s |
| `veo3.1` without audio | 20 credits/s |

For Seedance 2.5, input/reference video is additionally billed at 10/15/34 credits/s for 480p/720p/1080p respectively; reference images/audio are listed as free and a minimum generation cost applies.

The `seedance2_5` rows describe Runway's listing as checked on 2026-10-06. Seedance 2.5 output-resolution claims on other surfaces conflict (§15.7); recheck the current Runway listing before relying on any resolution row.

Runway's Model Router reports selected model and realized cost.

Evidence:

```text
OFFICIAL_PUBLIC
```

Route state:

```text
DOCUMENTED
UNTESTED BY OUR SYSTEM
```

---

# 13. Replicate

Role candidate:

```text
OPEN-MODEL LAB
SPECIALIZED MEDIA OPERATIONS
FALLBACK WHERE A SPECIFIC MODEL/ROUTE FILLS A GAP
```

No broad provider-level price is recorded because pricing is model-specific.

Route state:

```text
UNTESTED
```

---

# 14. ElevenLabs

Checked: `2026-10-07`

Official sources:

```text
https://elevenlabs.io/pricing/api
https://elevenlabs.io/text-to-speech-api
https://elevenlabs.io/v4
```

Current ElevenAPI rate card observations:

| Capability | Current public rate | Evidence note |
|---|---:|---|
| TTS Multilingual v2 / v3 | $0.10 / 1K characters | current API pricing page |
| TTS Flash / Turbo | $0.05 / 1K characters | current API pricing page |
| Voice Changer | $0.12 / minute | current API pricing page |
| Sound Effects | $0.12 / minute | current API pricing page |
| Music | $0.15 / minute | current API pricing page |
| Dubbing v1 | $0.33 / minute | current API pricing page; watermark/plan details may vary |
| Dubbing v2 | $2.20 / minute | current API pricing page |

The current API pricing page does **not** present `v3 Conversational` as a separate $0.05/1K-character TTS line, so v0.8 removes that older registry row instead of carrying an unconfirmed alias forward.

Current product/model pages also show Eleven v4 and Eleven v4 Turbo as API-available. Their product-page estimates are approximately:

```text
Eleven v4       ≈ $0.08 / minute
Eleven v4 Turbo ≈ $0.04 / minute
```

Those are product-page approximate per-minute figures, not a replacement for the character-based API rate card above and not budget authority. Execution-time quote/metering remains authoritative for spend.

Dynamic pricing surfaces may differ by region, account, promotion or rendering path. If another official surface exposes a materially different rate/unit, record it as a separate scoped observation with date/surface/section rather than silently replacing this observation.

The official pricing page also lists Scribe v2 at $0.22/hour and Scribe v2 Realtime at $0.39/hour; these matter only when STT is selected as a route capability.

Candidate capabilities:

```text
voice_generate
voice_transform
speech_to_text
dubbing
sound_effects
music
```

Evidence:

```text
OFFICIAL_PUBLIC
```

Route state for our recurring locked-voice requirement:

```text
DOCUMENTED
UNTESTED BY OUR SYSTEM
```

No claim is made yet that ElevenLabs Voice Changer, Eleven v4, v4 Turbo or any TTS route preserves the Pilot's locked voice/timing to the required standard. That needs a benchmark.

---

# 15. Higgsfield · Project Empirical Baseline

Higgsfield is not the architectural system of record. It remains an empirical comparison baseline because Pilot 01 has completed production and test records there.

## 15.1 Marketing Studio canary

```text
duration ≈ 12 s
cost = 42 credits
status = completed provider job
evidence_class = PROJECT_EMPIRICAL
```

## 15.2 D-01 cost semantics

Do not bind all D-01 cost measures to one source. Current source status is recorded per measure:

| Measure | Value | Source binding | Evidence state |
|---|---:|---|---|
| final D-01 round actual spend | 63.04 credits | `P01_DonaVera_D01_Final_1080p_Run_Record_CC_2026-10-03.md` | PROJECT_EMPIRICAL |
| D-01 two-part reference cost without repeats | 106.5 credits | `p01/phase10/P01_Phase10_Validated_Production_Method_v1.0.md` · section “Custo de referência (D-01, duas partes, sem repetições)”; corroborated in `p01/00_COMO_FUNCIONA.md` | PROJECT_EMPIRICAL |
| Phase 10 accumulated spend before D-02 | 667.36 credits | `p01/00_ACTIVE_AUTHORITY.md` · arithmetic later summarized as `849.36 = 667.36 + 182`; also recorded in `P01_10G_DonaVera_Run_Record_D02_2026-10-03.md` §13 | PROJECT_EMPIRICAL |

Rules:

```text
63.04
=
confirmed final-round spend from the named D-01 Run Record

106.5
=
reference cost for the D-01 two-part method without repeats
≠
final-round actual spend

667.36
=
Phase 10 accumulated spend before D-02
≠
"whole D-01 canary spend"
```

Do not collapse these three measures into one D-01 cost label. They answer different accounting questions.

## 15.3 D-02 cost semantics

Named project source:

```text
P01_10G_DonaVera_Run_Record_D02_2026-10-03.md
```

```text
approved cap = 250 credits
actual spend = 182 credits
reference/no-repeat spend = 94 credits
```

Evidence class:

```text
PROJECT_EMPIRICAL
```

## 15.4 Wan 3.0 exact-audio / lipsync evidence

Named project sources:

```text
P01_Operator_Review_DonaVera_Wan3_CTA_Lipsync_2026-10-02.md
P01_Dona_Vera_Voice_Pipeline_Canary
```

Short CTA scope:

```text
duration ≈ 4 s
test state = EMPIRICAL_PASS
operator review date = 2026-10-02
```

Full D-01 scope:

```text
duration ≈ 23 s
submission = failed at input
charge = refunded
```

Therefore:

```text
SHORT-CTA SCOPE
=
EMPIRICAL_PASS

FULL-LENGTH EXACT-AUDIO SCOPE
=
UNRESOLVED
```

A failed/refunded input submission does not prove that the underlying model would fail after successful execution.

## 15.5 Accepted current production baseline

```text
low-res talking generation
→ Mabel voice replacement
→ mandatory speech verification
→ low-res operator acceptance
→ complete low-res preview
→ upscale accepted source clip(s)
→ final-resolution mobile review
→ final assembly
```

This is a capability/quality baseline, not a permanent vendor requirement.

## 15.6 Seedance 2.5 · Phase 10B connector execution evidence

Named project source:

```text
p01/phase10/runs/P01_Phase_10B_Dona_Vera_Run_Record_v0.8.md
§35.5 (first submission) and §39 (one operator-authorized controlled retry)
```

```text
route = Seedance 2.5 via the current Higgsfield MCP connector
configuration = mode omni_reference · 720p · approved reference audio
result = 2 technical failures
net credit charge = 0
decision = route stopped after 2 technical failures; no further paid retry
evidence_class = PROJECT_EMPIRICAL
```

Scope:

```text
CURRENT MCP CONNECTOR / THIS CONFIGURATION
=
EMPIRICAL_FAIL (technical execution failure)

SEEDANCE 2.5 CAPABILITY FOR THIS WORKFLOW ON OTHER SURFACES / CONFIGURATIONS
=
UNTESTED
```

The run record classifies this as an execution failure of the current connector, not a general claim that Seedance 2.5 cannot perform the workflow elsewhere. It does not establish model quality.

## 15.7 Seedance 2.5 output resolution · conflicting third-party claims

```text
evidence_class = THIRD_PARTY
state = CONFLICTING · RECHECK BEFORE USE
```

| Claimed output resolution | Surface | Observed text |
|---|---|---|
| 720p | isolated skill `seedance-clean` v2.5 (`prompt-builder-2-5`), `SKILL.md` line 156 | "Note: 2.5 renders at 720p" |
| up to 1080p | official `higgsfield-ai/skills` repository v0.13.0 (commit `f83af0bc1d937c8119099a11f8ebbf5e6fb99819`), `higgsfield-generate/references/model-catalog.md` line 50 (also lines 129 and 205) | "Supports 4–30s output up to 1080p"; "Seedance 2.5 tops out at 1080p" |
| 1080p output row | Runway Dev pricing (§12, checked 2026-10-06) | `seedance2_5` 1080p output |
| "4K" requested in a prompt | Higgsfield blog post `ai-vs-vfx`, prompt blocks linked to `model=seedance_2_5` (lines 134 and 139 of the validator's raw capture) | "Photoreal. 16:9. 6s. 4K." |

The Runway row is `OFFICIAL_PUBLIC` for Runway's own route and does not establish another provider's output; the other three are third-party statements about Higgsfield surfaces. The blog prompt's "4K" is a request inside a prompt, not a documented output resolution, and the isolated skill itself treats such words as "detail intent, not output size". The Pilot 01 Phase 10B submissions (§15.6) used 720p and do not resolve the maximum. Verify the current output resolution on the selected surface before compiling a Seedance 2.5 route; none of these values is a method default.

---

# 16. Higgsfield Exit Coverage Matrix

This table is the single authority for current provider-independence coverage.

| Capability | Higgsfield baseline | Alternative candidates | Current alternative evidence | Exit-ready |
|---|---|---|---|---|
| Static image | available | OpenAI / fal / WaveSpeed / KIE | DOCUMENTED, untested | no |
| Image edit | available | OpenAI / fal / aggregators | DOCUMENTED, untested | no |
| Character/reference image | available | direct / aggregator image routes | untested | no |
| Reference-heavy video | available | Veo / Kling / Seedance / Wan routes | documented candidates | no |
| Talking character | empirical baseline exists | specialized talking/lipsync routes | benchmark pending | no |
| Locked voice replacement | empirical baseline exists | ElevenLabs / other voice-transform routes | benchmark pending | no |
| Exact-audio lipsync | Wan 3.0 short CTA ≈4 s: EMPIRICAL_PASS; ≈23 s full submission failed/refunded, full-length unresolved | specialized lipsync routes | alternative benchmark pending | no |
| Upscale | empirical baseline exists | Topaz / API / aggregator routes | benchmark pending | no |
| Finishing/reframe | available | Remotion / local deterministic-editor routes | Remotion DOCUMENTED, UNTESTED; implementation pending | no |

```text
EXIT_READY = YES
```

only after an alternative route passes the required project benchmark and approval.

---

# 17. Benchmark Priority

Recommended order:

```text
1. static image infrastructure smoke test
2. image/edit route benchmark
3. reference-heavy video benchmark
4. talking/lipsync benchmark
5. voice-replacement benchmark
6. upscale benchmark
7. provider parity where strategically useful
```

The talking/voice path is the critical proof for meaningful workflow independence.

## 17.1 Canonical Benchmark Case Binding

Provider/model comparisons should reuse fixed benchmark cases where possible so differences are not inferred from unrelated prompts. Initial case families may include:

```text
BENCH-STATIC-01
product identity + exact text + hierarchy

BENCH-REF-01
recurring character + reference preservation

BENCH-ACTION-01
single controlled physical interaction

BENCH-TALK-01
short PT-BR talking clip + exact script / voice requirement

BENCH-CONTINUITY-01
two linked shots with explicit end/start state
```

Every stored benchmark instance should retain `benchmark_case_id`, fixed input version, route/model/provider/version, date, attempt count, confirmed cost, output refs, rubric and verdict. A pass remains scoped to the case and tested conditions.

## 17.2 Scoped Failure / Mitigation Memory

Record provider/model/route failures with enough scope to avoid turning one anecdote into a universal rule:

```text
route / model / provider / version
operation
input conditions
observed defect
probable cause
mitigation tried
result after mitigation
confidence
last observed
```

Prompt notes and mitigations may guide Route Compilation only when their evidence scope matches the current task closely enough. Contradictory observations remain visible.

Current external-method heuristic retained from `utils/generate-skill-guide.pdf`:

```text
WHEN exact face/logo identity matters
AND an authoritative permitted reference exists
AND the selected route supports reference binding correctly
→ prefer the real authoritative reference over textual reconstruction
```

Evidence class for this heuristic:

```text
evidence_class = THIRD_PARTY
source_role = METHOD_REFERENCE
NOT PROJECT_EMPIRICAL
```

Project restrictions, reference contamination risk or route behavior may override it. Pilot 01, for example, can prohibit visible brand/logo/readable text in generation references even when a generic method would otherwise prefer a real reference.

## 17.3 Expected Progress Window

If a route has a known normal queue/completion range, it may record an expected progress window used for recovery. Route instances/recipes may also record observed or documented concurrency, polling and retry-after behavior. Do not hard-code one universal timeout, poll cadence or concurrency limit across providers.

```text
NO PROGRESS BEYOND ROUTE-SPECIFIC EXPECTED WINDOW
→ preserve state
→ poll / reconcile
→ report pending/unknown when necessary
→ do not create a duplicate paid submission blindly
```

---

# 18. Endpoint Parity Rule

Before treating two providers as interchangeable for the same model, compare where feasible:

```text
model/version
input/reference support
exposed parameters
resolution / quality
async behavior
prompt adaptation
output quality
cost
failure behavior
known failure / mitigation memory
benchmark case / fixed input parity
```

```text
SAME MODEL MARKETING NAME
≠
SAME ROUTE BEHAVIOR
```

Benchmark record semantics live in `AI_Creative_Skill_Execution_Contracts_Pre-v0.9.md`.

---

# 19. Provider Trust / Supply-Chain Criteria

Where material, track:

```text
official upstream relationship
authorized/reseller status if documented
model-version transparency
terms stability
billing reliability
API reliability
support
data-use transparency
```

Unknown is an acceptable result.

Do not fabricate a trust score from vibes, unverified community claims or affiliate marketing material.

---

# 20. Privacy / Data Handling

Provider comparison should track when available:

```text
input retention
output retention
log retention
training / data-use policy
deletion controls
region / DPA where material
temporary URL lifetime
project-controlled archival requirement
```

Local custody does not by itself determine usage rights or provider data-use terms.

---

# 21. Procurement Preference

Current procurement preference:

```text
PAYG / TOP-UP
+
AVOID MONTHLY USE-IT-OR-LOSE-IT CREDIT STRUCTURES
```

This is a cost preference, not a quality verdict.

Total cost can include:

```text
unit generation cost
subscription overhead
unused-credit loss
retries
post-production
storage / infrastructure
```

The comparison target is eventually:

```text
EFFECTIVE COST PER ACCEPTED ASSET
```

not sticker price alone.

---

# 22. Freshness Rule

Before material spend, recheck the exact route for:

```text
model/version availability
endpoint/schema
price / quote
credit policy
retention
reference support
resolution
duration
audio behavior
rate limits / concurrency
polling / Retry-After behavior where applicable
result URL TTL / retrieval urgency where documented
Execution Route Recipe relation state / schema compatibility
integration availability
known route failures / mitigation freshness where material
expected progress window where known
```

Pricing should be same-day for material spend.

The registry is evidence and planning support; the execution-time quote is the spend authority input.

---

## 22.1 Upstream Route Invalidation Signals

Treat the following as route-maintenance signals rather than creative-quality evidence:

```text
MODEL_NOT_FOUND
MODEL_VERSION_REMOVED
ENDPOINT_REMOVED
SCHEMA_CHANGED
ROUTE_RECIPE_STALE
```

On a proven pre-submission invalidation, mark the relevant recipe/route stale or invalidated, refresh official/current facts and revalidate before material spend. If submission may have occurred, the Attempt/Job state machine still governs and reconciliation comes first.

---

# 23. Current Registry Decision

```text
NO PROVIDER IS CURRENTLY THE UNIVERSAL DEFAULT
```

Selection remains:

```text
PROJECT PERMISSION
→ CAPABILITY FIT
→ ROUTE EVIDENCE / APPROVAL
→ APPLICABLE BENCHMARK / FAILURE MEMORY
→ PRIVACY / RIGHTS / TRUST
→ CURRENT COST / LATENCY
```

The first implementation can choose one route for the smoke test without prematurely declaring it the permanent winner. Route/model knowledge should become more precise through fixed benchmarks and scoped experience memory, not through unversioned prompt folklore.

---

# 24. Remotion · Local Deterministic Finishing Candidate

Checked: `2026-10-08`

Source-of-record archive:

```text
private-archive://influencer/utils/remotion-main.zip
Drive ID = 16v0STtI8ugeaNK7WH74k7La7b4CTr8OI
size = 584836895 bytes
```

The archive exceeds the connected Drive raw-download ceiling, so its exact SHA-256 and byte equivalence to an upstream commit are **not available**. Source inspection was reconciled against the official repository:

```text
repository = remotion-dev/remotion
probable revision = 328178a68a8031167649273405f2405028bd2305
revision basis = last commit on main's first-parent history before the Drive ZIP modified time (2026-10-06T00:46:56Z)
probable revision commit time = 2026-10-05T16:59:22Z
core package version = 4.0.533
ZIP ↔ commit byte equivalence = NOT_PROVEN
official repository snapshot = https://github.com/remotion-dev/remotion/tree/328178a68a8031167649273405f2405028bd2305
license source = LICENSE.md at the same revision
```

v0.10 named `15806b71e54cbb6654678d4b54f6560b7d673430` as the probable revision. That commit belongs to the `studio-caption-style` branch and reached `main` only on 2026-10-07T20:49:54Z (PR #12022), after the ZIP was made, so it cannot be the content of `remotion-main.zip`. The core package version (4.0.533), `LICENSE.md` and the skill files are identical at both commits, so no adjudication changes.

Evidence for repository/version/license facts:

```text
OFFICIAL_PUBLIC
with source-reconciliation limitation retained above
```

## 24.1 Candidate role

```text
ROLE
= LOCAL DETERMINISTIC VIDEO FINISHING / COMPOSITING / REFRAME CANDIDATE

ROUTE EVIDENCE
= DOCUMENTED

PRODUCTION APPROVAL
= UNTESTED

INTEGRATION STATUS
= NOT_VERIFIED / NOT INSTALLED

ROUTE RECIPE RELATION
= ABSENT

ROUTE FRESHNESS STATE
= RECHECK_REQUIRED
```

Observed capabilities at the reviewed probable revision include code-addressable composition/timeline structure, exact controlled text/captions, source media assembly, preview/still/selected-frame rendering and final video export. These are documented capabilities, not project validation.

A future executable route would require a code-capable runtime and a pinned recipe for its actual Node/React/browser/render stack. Do not infer that Remotion is available merely because the repository is documented here.

## 24.2 License boundary

The reviewed `LICENSE.md` uses a custom Remotion license rather than a standard permissive open-source license. At the reviewed revision it permits free use for individuals, nonprofits/not-for-profits, evaluation, and for-profit organizations with up to 3 employees; other for-profit use requires a Company License under the stated terms. The same license file announces a planned license change for Remotion 5.0.

The license FAQ and Terms at the same revision word the free tier as "an organization or team of individuals with up to 3 people", not employees. The Terms count everyone who operates the same Remotion project, including freelancers; a client that only receives finished media does not count. The FAQ also states that Remotion is source-available, not open source. Use the stricter reading until the current terms are rechecked.

```text
LICENSE ELIGIBILITY
= EXECUTION-TIME / ORGANIZATION-SPECIFIC CHECK

DOCUMENTED HERE
≠
CURRENT LEGAL ELIGIBILITY APPROVED
```

Before installing or using Remotion for commercial production, recheck the **current official license/terms** and the operator/entity's actual eligibility. Do not copy a historical eligibility statement into runtime authorization.

## 24.3 Current route disposition

```text
REMOTION RUNTIME INSTALLATION
= DEFERRED

REMOTION EXECUTION ROUTE RECIPE
= DEFERRED UNTIL AN ACTUAL ROUTE IS SELECTED / VALIDATED

NEW STAGE-9 SPECIALIST METHOD
= DEFERRED UNDER THE GROWTH RULE
```

The source supports deterministic finishing as a coherent execution surface but does not, by itself, justify adding runtime infrastructure or a new Specialist Method. Representative-frame previews and explicit output metadata already fit current Route Compilation / QA semantics; route-specific React/CLI/frame mechanics belong in a future Recipe if this candidate is exercised.
