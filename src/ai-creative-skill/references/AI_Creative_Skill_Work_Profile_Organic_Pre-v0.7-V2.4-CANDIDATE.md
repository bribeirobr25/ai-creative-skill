> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Work Profile · Organic Content · Pre-v0.7-V2.4-CANDIDATE

## Status

```text
DOCUMENT TYPE
=
ORGANIC CONTENT WORK PROFILE

VERSION
=
Pre-v0.7-V2.4-CANDIDATE

DATE
=
2026-10-07

PARENT_DOCUMENT
=
AI_Creative_Skill_Architecture_Spec

LAST_VALIDATED_AGAINST
=
AI_Creative_Skill_Architecture_Spec_Pre-v0.14.md

STATUS
=
DESIGN PROFILE
NOT INSTALLED
```

This profile prevents the generic Creative Core from treating every piece of persona/editorial content like a paid ad. Pre-v0.6 keeps conditional `RESEARCH_EVIDENCE_SYNTHESIS` and adds `VIDEO_EVIDENCE_INSPECTION` only when an existing/reference video must be inspected as structured evidence for a trend, format, claim or creative observation.

---

# 1. Scope

Use when the main objective is:

```text
organic social content
editorial / educational content
persona-led recurring content
community / audience development
non-paid platform-native content
```

Organic content can still have a commercial context. That does not automatically make every piece an Ads-profile task.

## 1.1 Default Specialist Method Stack

Depending on the bounded request, Organic may activate:

```text
RESEARCH_EVIDENCE_SYNTHESIS, when Stage-2 external/current research is active
VIDEO_EVIDENCE_INSPECTION, when material claims about an existing/reference video require structured inspection
ORGANIC_CONTENT_CRAFT
SCRIPT_PERFORMANCE
IMAGE_DIRECTION or VIDEO_DIRECTION
TALKING_PERSONA, when recurring visible speech applies
AUDIO_VOICE_PERFORMANCE, when speech/audio applies
TYPOGRAPHY_LAYOUT, when visible text matters
PLATFORM-specific method, when available and material
ROUTE_COMPILATION, before provider execution
QA_EVIDENCE_RIGHTS, when claims/disclosure/rights apply
QA_REALISM_PERFORMANCE
LOCALIZED_REPAIR, when needed
```

These are loaded just in time; this Work Profile remains authority for organic/editorial intent.

---

# 2. Inputs

Minimum relevant inputs may include:

```text
project profile
persona / presenter authority
content objective
content territory / theme
platform
language
script / talking points
format / duration
approved references
required disclosure
production budget / approval scope
```

No `offer` entity is required unless the piece actually contains an offer.

No PROOF/QUEST framework is required merely because the content might eventually support a business.

---

# 3. Organic Creative Intent

Typical intent classes:

```text
TEACH
EXPLAIN
ENTERTAIN
COMMENT
STORY
DEMONSTRATE
CONVERSATION
SERIES_EPISODE
COMMUNITY_RESPONSE
```

The profile should preserve the persona's established voice, behavior and content territory from the Project Profile/canon.

---

# 4. Social-Native Structure

A production brief may define:

```text
opening beat / hook
core idea
development beats
payoff / final observation
series continuity
optional CTA
visual behavior
camera / framing
presentation mode + audio binding contract
caption / text plan
```

The objective is natural platform-native communication, not automatic ad structure.

For each piece, resolve three craft questions:

```text
WHY WOULD SOMEONE STOP?
WHY WOULD THEY CONTINUE?
WHAT IS THE PAYOFF?
```

The answer may be utility, a specific observation, visible action, tension, persona point of view, story progression or another format-appropriate mechanism. Avoid empty pattern interrupts that do not connect to the content.

Pacing should balance speech density, visual change, pause/breathing room, caption load and complexity of the idea. Fast is not automatically engaging; slow is not automatically natural.

---

# 5. Research

Research is task-dependent.

Possible research classes:

```text
fact verification
current-topic research
platform/context research
audience-language research
trend / format observation
source-backed educational research
```

Do not force buyer research or competitor-ad research when the content does not need it. Reuse current research when it still matches the topic/market/platform context; refresh current-topic or platform evidence when staleness could change the content materially.
When external research is active, use `RESEARCH_EVIDENCE_SYNTHESIS` for query planning, source outcomes, evidence clustering, independent corroboration and decision-critical freshness checks. When trend/format research depends materially on an existing video, stack `VIDEO_EVIDENCE_INSPECTION` to prepare bounded visual/audio evidence and preserve its coverage by reference. Organic remains responsible for editorial/content intent and how the evidence becomes content. Trend discovery may validly return `INSUFFICIENT_EVIDENCE`; do not manufacture a trend because the content brief would be easier with one.

---

# 6. Evidence and Claims

For factual/editorial content:

```text
source-backed statement
personal/character opinion
fictional framing
inference
unknown
```

must remain distinguishable.

A fictional persona must not manufacture real-world personal experience as evidence.

Project-specific restrictions on finance, health, legal, product experience or other sensitive content remain controlled by the Project Profile/canon.

---

# 7. Persona Continuity

For recurring AI personas, evaluate:

```text
visual identity
age / defining features
voice identity
behavioral voice
recurring environment where relevant
content territory
relationship to audience
series continuity
```

A strong visual generation that behaves like a different character is not an accepted output.

Where approved project material exists, curate a small exemplar set for behavioral voice rather than loading the entire archive. Exemplars may cover different canonical modes such as explanation, story, reaction and commercial-adjacent mention. They teach voice patterns; they do not become copy templates.

---

# 8. Audio / Talking Content

Organic content separates how speech is presented from how audio identity is produced.

## 8.1 Presentation Mode

```text
ON_CAMERA_SPEECH
VOICEOVER
NO_SPEECH
```

## 8.2 Audio Binding Contract

Where speech exists, use one applicable Core contract:

```text
NATIVE_SPEECH
VOICE_REFERENCE
SEPARATE_TTS
EXACT_APPROVED_AUDIO
NATIVE_SPEECH_THEN_VOICE_REPLACEMENT
```

`NO_SPEECH` has no spoken-audio binding contract.

The Organic profile does not invent a persona voice. It receives voice authority and permitted audio-binding behavior from the Project Profile and passes the requirement to the Core/Execution layer.

Auxiliary music/SFX are specified separately. Recurring visible speech should also use the `TALKING_PERSONA` method so identity, behavioral voice, visible performance, voice identity and lipsync are reviewed independently.

---

# 9. Text and Graphics

Text on screen can be:

```text
NONE
CAPTION
SUBTITLE
HEADLINE
CALLOUT
END CARD
```

Where identity/reference contamination is a project risk, prefer clean generation and controlled finishing layers.

Text should not be generated merely because an example/reference image contained it.

---

# 10. CTA Logic

Organic CTA is optional.

Possible types:

```text
NONE
WATCH_NEXT
FOLLOW
COMMENT
SAVE
SHARE
VISIT_LINK
SOFT_COMMERCIAL
```

Do not inject a sales CTA into an editorial piece unless the task/profile calls for it.

---

# 11. Disclosure

Organic content may still require disclosure depending on context.

```text
AI DISCLOSURE
ADVERTISING / SPONSORSHIP DISCLOSURE
AFFILIATE DISCLOSURE
```

are separate requirements.

The Project Profile and current platform rules decide which apply.

---

# 12. Production Brief

Before execution, compile only what is needed:

```text
content objective
persona / authority refs
platform / format
hook / stop reason / continue reason / beats / payoff / final line
script or talking points
visual / acting direction
presentation mode + audio binding contract
reference bindings
text / graphics plan
active specialist method refs
acceptance criteria
```

No raw project archive should be dumped into the provider prompt.

---

# 13. Organic QA

Evaluate:

```text
persona consistency
factual support where applicable
spoken-content fidelity
specific opening / stop reason
progression / continue reason
payoff
social-native performance
voice / lip-sync where applicable
visual naturalness
continuity
text accuracy
platform format
technical file quality
```

Where relevant, also review in real-use context:

```text
thumbnail
first frame / first second
phone size
muted
crop / safe area
audio on
```

Performance quality and identity correctness are separate dimensions.

---

# 14. Learning

When performance learning is intended, define creative lineage before publication where possible:

```text
concept / episode intent
variant / asset ID
hook ID / opening type
platform / format
publication ID
```

When organic metrics are available, treat them as signals such as:

```text
retention
completion
rewatch
shares
saves
comments
profile visits
follows
```

They can inform the next hypothesis but do not automatically prove purchase intent or paid-ad effectiveness.

Organic success is not silently promoted into commercial conversion evidence.

---

# 15. Output of Organic Profile

The profile hands the generic Core/Execution layer:

```text
content objective
persona/project authority
concept / episode intent
script / beats
production spec
reference bindings
presentation mode + audio binding contract
acceptance criteria
active method outputs / refs
publication-learning identifiers when in scope
```

Execution then remains provider-agnostic and is compiled through the applicable Route Compilation method rather than by copying one generic prompt unchanged across tools.


---

## V2.4 real-world hardening — creator character/idea workflow

For complete persona-led project requests, route an `CHARACTER_BIBLE` deliverable through the Catalog's required identity/backstory/USP/canon requirements before optional visual generation; do not silently turn a supertopmodel into a product presenter because her supporting brand mission was emphasized. Distinguish `CONCEPT` and `CONTENT_IDEA` selection from production-ready `SCRIPT`. Recommend choosing ideas before drafting many fixed scripts in a new series; honor requests for direct bounded scripting, preserving approval scope. A complete per-idea `CONTENT_IDEA` must have hook, format/hold, setting, why (evidence vs hypothesis) and payoff/reader value. Creative extras are encouraged when canon-consistent.

At the end of a significant project stage, return completed state and one next useful, **unexecuted** recommendation only when needed; do not change Ads/Research ownership, sponsor disclosure, or publication authority.

