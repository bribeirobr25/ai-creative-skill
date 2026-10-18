# AI Creative Skill · Specialist Method · Ad & Funnel Intelligence · Pre-v0.4

## Status

```text
METHOD ID = AD_FUNNEL_INTELLIGENCE
VERSION = Pre-v0.4
DATE = 2026-10-07
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.9.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

This method studies current ads, destinations and funnel mechanics without pretending public observation reveals private conversion economics. Pre-v0.4 keeps generic retrieval/source outcomes in `RESEARCH_EVIDENCE_SYNTHESIS`, uses the canonical `video_inspection_evidence_ref` for material reference/competitor videos, and carries those evidence references forward in the intelligence handoff.

---

# 1. Trigger

Use when:

```text
live competitor / category creative research is requested
OR
current ad/funnel evidence is needed for a new commercial strategy
OR
an existing concept should be compared with current market execution
```

Do not force it into bounded edits or tasks whose strategy is already authoritative and adequate.

---

# 2. Inputs

```text
buyer synthesis
offer / market
known competitors / alternatives
platform / source scope
research depth
existing inspected evidence and date
video_inspection_evidence_ref, when applicable
```

Buyer synthesis should normally precede ad interpretation so observed executions are evaluated against real buyer situations rather than admired as visual trends.
When external retrieval spans multiple source classes, use `RESEARCH_EVIDENCE_SYNTHESIS` as the shared research layer and reference its execution/report rather than rebuilding generic search mechanics inside this method.

---

# 3. Ad Observation Record

For each distinct observation, capture where available:

```text
advertiser / page
ad or creative ID
country / market
observed status and dates
inspection date
format / placement cues
opening / hook
promise
visible proof / demonstration
offer
objection handling
CTA
concept family
variant relationship
visual progression
destination
inspection coverage
```

Separate observed execution from inferred persuasion strategy.

When a material observation depends on what happens inside an ad/reference video and direct inspection is not already adequate and traceable, stack `VIDEO_EVIDENCE_INSPECTION`. Store/reference it as `video_inspection_evidence_ref`; do not invent a local video-coverage schema. Ad/Funnel Intelligence remains responsible for interpreting the observed mechanism, not for redefining how video evidence was sampled or verified.

---

# 4. Variant Clustering

Do not count every translation, crop or minor hook change as an independent concept.

Cluster related assets by shared mechanism:

```text
CONCEPT FAMILY
→ localized version
→ hook variant
→ format variant
→ actor variant
```

Record both common mechanism and material differences.
Search fan-out does not create independent confirmation: the same ad, landing page, press item or underlying creative returned by multiple queries/sources should retain one underlying provenance identity.

Recurrence may justify inspection priority. It does not prove conversions, profitability, spend, targeting or platform preference.

---

# 5. Funnel Inspection

Where reachable, inspect:

```text
ad promise
→ destination
→ proof
→ offer
→ objections
→ CTA
→ checkout / lead form boundary
```

Record current price, shipping, subscription conditions, guarantees and eligibility when relevant.

Do not create accounts, purchase, submit real contact data or trigger external side effects merely to complete research.

Hidden steps remain unknown.
If official brand positioning is compared with current ads or public conversation, capture the current official wording separately and connect it only to evidence addressing the same proposition. Orthogonal conversation should remain orthogonal rather than being forced into a brand-positioning narrative.

---

# 6. Evidence Ladder

Use the Ads Profile ladder:

```text
L0 OBSERVED
L1 INFERRED
L2 MEASURED
L3 ECONOMIC
```

Public ad presence and longevity remain L0/L1 unless actual measured/economic data is available.

Never elevate recurrence into CPA, ROAS or profitability evidence.

---

## 6.1 Source outcome discipline

When live retrieval is used, retain the **complete canonical source-outcome vocabulary** from `RESEARCH_EVIDENCE_SYNTHESIS` by reference. Do not copy a subset into this method. `NO_RESULTS` means successful negative coverage; every other non-success outcome keeps its canonical meaning and must not be paraphrased as completed negative evidence.

Do not write “competitors are not doing X” merely because the relevant source failed, required payment/authentication, was unconfigured, or was only partially inspected.

---

# 7. Coverage

For a deep run, seek approximately:

```text
3 relevant advertisers
~20 distinct ad observations
```

when accessible and useful.

Report actual research coverage, duplicates and inaccessible sources. For structured video/audio inspection, reference the canonical `VIDEO_EVIDENCE_INSPECTION` coverage rather than restating it with local field names.

A failed access attempt is not a completed audit.

---

# 8. Adaptation Boundary

Extract:

```text
buyer problem
communication hierarchy
proof mechanism
pacing
funnel logic
concept structure
```

Do not copy distinctive scripts, layouts, brand assets, mascots, footage, customer evidence or other protected expression.

---

# 9. Output

```yaml
intelligence_id:
market:
source_scope:
inspection_date:
research_execution_ref:
video_inspection_evidence_refs:
coverage:
source_outcomes:
concept_families:
observed_mechanisms:
repeated_patterns:
contradictions:
funnel_findings:
useful_test_hypotheses:
unsupported_inferences_to_avoid:
access_limits:
```

---

# 10. Acceptance Rubric

A strong output explains:

```text
WHAT was observed
WHERE it was observed
HOW much was inspected
WHAT is repeated versus duplicated
WHAT mechanism may be worth testing
WHAT remains unknown
```

It must not claim private performance from public recurrence.
