> **V2.4 CANDIDATE SCOPE:** Modified version of this method family. Read the final section “V2.4 real-world hardening” for current candidate additions. Historical V2.3 discussion and prior-source pointers below remain provenance, not active version resolution.

# AI Creative Skill · Specialist Method · Script & Performance · Pre-v0.14-V2.4-CANDIDATE

## Status

```text
METHOD ID = SCRIPT_PERFORMANCE
VERSION = Pre-v0.14-V2.4-CANDIDATE
DATE = 2026-10-16
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.12-V2.2-CANDIDATE.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

GPT validation hardening branch (2026-10-10): Pre-v0.12-V2-CANDIDATE treats translation/localization of claims as semantic transformation, carries language/market/jurisdiction context where material, and adds protected `DO_NOT_TRANSLATE` references. It does not change script authority or exact-speech rules.

Z4/Z4.1 creative-balance hardening branch (2026-10-11): Pre-v0.13-V2.2-CANDIDATE consumes the cross-modal creative-latitude policy so writer/persona voice can remain stable while hooks, topics, titles, examples, analogies, structure and other authorized expression dimensions are explored without mechanical exemplar copying.


This method turns strategy or content intent into speakable, performable, timed writing. Pre-v0.11 makes route-generated or improvised speech explicitly non-authoritative until the actual spoken output is compared with applicable script/claim authority. It preserves canonical text-finding ownership and the timing-authority distinction for audio-led work; the Pre-v0.10 `timing_authority_ref` correction remains in force.

---

# 1. Trigger

Use for:

```text
video scripts
talking-persona scripts
voiceover
scene dialogue
talking points
organic spoken content
ad scripts
```

A text-only bounded request can stop after script QA and delivery.

---

# 2. Script Modes

```text
COMMERCIAL
ORGANIC / PERSONA
EDUCATIONAL / EXPLANATORY
STORY / COMMENTARY
```

The Work Profile and Project Profile determine objective, evidence and persona rules.

---

# 3. Beat Contract

For each beat resolve:

```text
FUNCTION
what must change in viewer understanding / emotion / action?

SPOKEN CONTENT
what is said?

VISIBLE CONTENT
what proves, illustrates or accompanies it?

PERFORMANCE TASK
what must the presenter physically do?

DURATION
can the speech and action fit naturally?

TRANSITION
why does the next beat follow?

END STATE
what must be true at the end?
```

A scene without a function should be removed or merged.

---

# 4. Opening

A strong opening may use:

```text
specific situation
unexpected but supported observation
visible action
clear problem / contrast
immediate value
persona-specific point of view
```

Avoid generic openings that could introduce any product or topic.

For commercial work, the hook must still connect to the actual offer or buyer situation.

For organic work, the opening should create a reason to continue without forcing ad structure.

---

# 5. Progression

The script should add information rather than restate the hook.

```text
OPEN
→ DEVELOP
→ PROVE / EXPLAIN / COMPLICATE
→ PAYOFF / DECISION / NEXT STEP
```

Each beat should earn its time.

Do not create a script whose visual sequence adds no new information while the camera merely changes angle.

---

# 6. Spoken Naturalness

Evaluate:

```text
sentence length
breathability
speech density
pause opportunities
conversational syntax
word choice
repetition
pronunciation risk
number / price readability
language naturalness
```

A script can be grammatically correct and still be unspeakable or artificial.

## 6.1 Text naturalness review

When the request requires natural, non-generic style aligned with the intended writer/persona, copy cleanup or a pre-delivery text review, inspect for generic model-writing patterns. Treat them as **signals**, not automatic defects.

Use the following canonical taxonomy. `default_strength` is a starting prior for review, not a verdict. Context, persona authority, reader context and task objective may narrow or dismiss a finding.

| `text_issue_class` | One-line definition | `default_strength` | Context / exception |
|---|---|---|---|
| `STAGED_CONTRAST` | contrast whose negative half adds little or no information | `STRONG_SIGNAL` | may be deliberate rhetoric |
| `THROAT_CLEARING_OR_FAUX_INSIGHT` | staged opener, false candor or setup before a routine point | `STRONG_SIGNAL` | oral persona markers may be intentional |
| `UNRAISED_OBJECTION` | argument against an objection the audience did not raise and the strategy did not establish | `STRONG_SIGNAL` | valid when grounded in buyer evidence |
| `CHATBOT_OR_DRAFTING_RESIDUE` | assistant wrapper, drafting note, process narration or unsolicited service language remains in final copy | `STRONG_SIGNAL` | none when clearly unintended residue |
| `KNOWLEDGE_LIMIT_GUESS` | uncertainty disclaimer is followed by an unsupported guess presented as useful content | `STRONG_SIGNAL` | uncertainty itself is not a defect |
| `CONTEXT_REEXPLANATION` | text re-states context already supplied by the reader/audience without adding interpretation | `CONTEXTUAL_SIGNAL` | can be necessary when distribution removes prior context |
| `INTERPRETIVE_METADISCOURSE` | tells the reader what the text means instead of making the point directly | `CONTEXTUAL_SIGNAL` | can aid genuinely complex explanation |
| `IMPORTANCE_PUFFERY` | inflates significance without adding mechanism, evidence or consequence | `CONTEXTUAL_SIGNAL` | supported strategic framing may be valid |
| `BORROWED_OR_WEASEL_AUTHORITY` | vague authority such as “experts say” or “studies show” without traceable support | `STRONG_SIGNAL` | also triggers Evidence & Rights review |
| `GENERIC_SALES_LANGUAGE` | interchangeable promotional language with weak subject specificity | `CONTEXTUAL_SIGNAL` | apply portability test before rewriting |
| `FORCED_TRIAD_OR_LIST_PATTERN` | repeated three-part or list rhythm that appears formulaic rather than functional | `CONTEXTUAL_SIGNAL` | may be intentional cadence |
| `REPEATED_OPENING_OR_ROBOTIC_SYMMETRY` | repeated sentence shape/opening creates mechanical rhythm | `CONTEXTUAL_SIGNAL` | may be deliberate parallelism |
| `DASH_HEAVY_RHYTHM` | repeated dash-led segmentation creates a mechanical cadence without functional need | `CONTEXTUAL_SIGNAL` | punctuation conventions and persona cadence vary by language/format |
| `STACKED_QUALIFIERS` | multiple hedges/intensifiers obscure the actual claim | `CONTEXTUAL_SIGNAL` | nuance may require qualification |
| `AGENT_OBSCURING_PHRASING` | passive/indirect wording hides responsibility or makes meaning unclear | `CONTEXTUAL_SIGNAL` | subject omission itself is not a defect |
| `SYNONYM_CYCLING` | repeated concept is renamed mainly to avoid repetition, reducing precision | `CONTEXTUAL_SIGNAL` | domain terminology may require lexical variety |
| `NEGATIVE_LISTING_OR_STACKED_PUNCH` | serial negatives/fragments create artificial punch without progression | `CONTEXTUAL_SIGNAL` | spoken performance may justify fragments |
| `RHETORICAL_SETUP_OR_SELF_ANSWER` | question/setup is used mechanically when a direct statement would carry more information | `CONTEXTUAL_SIGNAL` | rhetorical questions can be persona-native |
| `COLON_REVEAL_DRAMA` | punctuation/structure manufactures a reveal unsupported by the content | `CONTEXTUAL_SIGNAL` | punctuation conventions vary by language/format |
| `FAKE_PROFOUND_KICKER` | closing sentence adds significance or emotion without new meaning | `STRONG_SIGNAL` | genuine persona punchline/observation may be valid |
| `SUMMARY_RECAP_ENDING` | ending merely repeats the preceding point | `STRONG_SIGNAL` | recap can be useful in instructional formats |
| `DECORATIVE_FORMATTING` | formatting pattern is applied mechanically rather than serving comprehension | `CONTEXTUAL_SIGNAL` | platform-native formatting can be intentional |

`CONTEXT_REEXPLANATION` is deliberately `CONTEXTUAL_SIGNAL`, not a universal strong defect. The external pattern is useful, but distributed/social content may legitimately restate context that is absent from the viewer's entry point. Open a material finding only when the **actual reader/viewer context** already supplies the information and the re-explanation adds no useful interpretation, consequence or transition.

For PT-BR, examples such as `não é só X, é Y`, `A verdade é que...`, `Vamos lá...`, `E isso muda tudo.` or repeated three-part lists remain **ANALYST_HYPOTHESIS** review prompts, not validated Brazilian-audience findings and not banned forms. They originated in integration analysis, not in project empirical evidence.

```text
EXTERNAL STYLE SIGNAL
≠
AUTOMATIC DEFECT
```

A single `CONTEXTUAL_SIGNAL` should not trigger a rewrite by itself. A single `STRONG_SIGNAL` is sufficient to open a review finding, but it is **not** automatic authorization to edit. Compare the passage against locked wording, project/persona voice, curated exemplars, reader context, content objective and protected text.

```text
STRONG_SIGNAL
=
REVIEW FINDING MAY OPEN

STRONG_SIGNAL
!=
AUTOMATIC REWRITE / AUTOMATIC FAIL
```

`text_issue_class` identifies **what pattern is observed**. `text_evidence_strength` identifies **how strongly the observed instance supports a material writing-quality finding in context**. The taxonomy's `default_strength` is only the starting value.

### 6.1.1 Portability / specificity test

For a sentence, hook, claim or closing that feels generic, ask:

```text
COULD THIS PASSAGE MOVE UNCHANGED
TO A DIFFERENT PERSON / PRODUCT / COMPANY / TOPIC
WITHOUT LOSING MUCH MEANING?
```

If yes, inspect whether it is functional connective language or replaceable filler. When specificity is needed, prefer a supported subject-specific element such as:

```text
fact
mechanism
observable action
consequence
constraint
example
judgment that genuinely belongs to the persona / writer
```

Do not invent specificity. A concrete unsupported detail is worse than an honest general statement. Preserve useful numbers, names, mechanisms and other exact details instead of smoothing them into abstract importance.

## 6.2 Text review action

`text_review_action` is **derived from the task path plus wording authority**. It is not a free-standing user mode and must not create a second meaning of `EDIT`.

```text
REVIEW_ONLY TASK PATH
OR LOCKED / EXACT-APPROVED WORDING
OR NO AUTHORITY TO CHANGE WORDING
→ FINDINGS_ONLY

NEW_CREATIVE / EDIT / IMPROVE / ADAPT / VARIATE
WHEN THE CURRENT SCOPE AUTHORIZES WORDING CHANGES
→ AUTHORIZED_EDIT
```

If the current task path is not explicitly listed, use the authority test: no wording authority means `FINDINGS_ONLY`; explicit wording authority means `AUTHORIZED_EDIT` within scope.

Canonical text finding schema. `SCRIPT_PERFORMANCE` is the schema owner; consumer methods store `text_finding_ref` rather than publishing partial or renamed copies:

```yaml
text_finding_id:
text_issue_class:
quoted_span:
text_evidence_strength:  # STRONG_SIGNAL | CONTEXTUAL_SIGNAL
voice_or_canon_exception:
reader_context:
consequence:
smallest_repair:
```

Style-pattern findings must **not** be used to claim that AI authored the passage. They describe observable writing behavior, not provenance or authorship.

For `AUTHORIZED_EDIT`, preserve strong/distinctive material and change only what is necessary to resolve the actual defect. Do not normalize every paragraph, rhythm change, blunt phrase, digression or imperfection merely for consistency.

## 6.3 Voice precedence and protected text

For style review:

```text
EXACT APPROVED / CANONICAL WORDING, WHEN WORDING IS LOCKED
>
PROJECT / PERSONA VOICE AUTHORITY
>
CURATED PERSONA / WRITER EXEMPLARS
>
GENERIC TEXT-NATURALNESS HEURISTICS
```

Before editing, mark protected material where applicable:

```text
exact approved speech
quotes and attributed wording
names / dates / numbers
price / quantity / offer terms
claim-registry allowed wording
required disclosures
safety / legal notices
code / commands / paths / identifiers
```

If exact approved speech is already canonical, default to **review-only findings**. Rewriting requires explicit authority to reopen the text.

Do not add a personal reaction, lived experience or opinion merely to increase perceived naturalness unless the applicable Work/Project Profile authorizes that content.

## 6.4 Semantic fidelity after editing

After any rewrite, compare source and draft for unintended change to:

```text
facts
names
numbers
dates
quotes / citations
claim scope
rankings / comparisons
sequence or simultaneity
price / quantity / offer terms
persona experience claims
required disclosure / safety wording
```

An unsupported addition is an error. A lost material claim is an error unless the task explicitly authorizes removing it.

---

## 6.5 Localization and Claim-Strength Preservation

When text is translated or localized, record the source and target language separately from market/jurisdiction. Compare claim meaning and strength before and after the edit. A translation that strengthens certainty, scope, comparison, performance or eligibility requires new applicable evidence or must be narrowed.

Protected brand/product/shade names, legal phrases, mandatory disclosures and explicitly locked strings are referenced through `do_not_translate_refs` rather than being normalized for fluency.

---

# 7. Persona Voice

When a recurring persona exists, use Project Profile authority and curated exemplars.

Model:

```text
vocabulary
sentence rhythm
energy / seriousness
humor / profanity when authorized and characteristic
preferred transitions
relationship to audience
bluntness / uncertainty / digressions / self-interruptions when characteristic
forbidden behaviors / phrases if canonical
```

If no approved exemplar exists yet:

```text
1. use Project/Profile canonical voice constraints;
2. use authoritative operator/source material when available;
3. do not infer stable persona voice from a model-generated draft;
4. if authority remains insufficient, use neutral task-appropriate wording and mark persona-voice calibration UNVERIFIED.
```

Do not copy exemplar sentences mechanically. Extract voice patterns.

---

## 7.1 Writer / Persona Continuity vs New Expression

For recurring author, persona or project writing, preserve the dimensions that current authority says carry recognizable voice while allowing new expression in dimensions that remain open.

Typical **examples**, not universal locks:

```text
VOICE / AUTHORSHIP CONTINUITY MAY PRESERVE
→ characteristic vocabulary range
→ sentence rhythm / bluntness / uncertainty / humor when canonical
→ relationship to audience
→ stable point-of-view / persona boundaries

AUTHORIZED EXPRESSION MAY EXPLORE
→ topic angle
→ hook
→ title
→ analogy
→ example
→ explanatory route
→ scene / beat structure
→ rhetorical device
```

The task-relative `creative_latitude_ref` from the Specialist Method System decides the actual boundary. Do not infer that every prior phrasing pattern is identity-bearing, and do not copy exemplar sentences mechanically merely to maintain voice.

For longitudinal writing, resolve stable voice from Project/Profile authority and curated exemplars. The immediately previous generated paragraph/chapter may provide local continuity, but it does not become the sole voice authority merely because it is recent.

When several distinct approaches are requested, explore materially different approaches before selecting/developing. When the task asks for continuation in a tightly fixed form, preserve the applicable form instead of manufacturing novelty for its own sake.

---


# 8. Timing

Estimate speech against the actual route and target duration during planning. Treat word-count or words-per-minute guides only as provisional heuristics; language, persona, pause structure and performance can materially change real duration.

For audio-led work such as approved voiceover, once the actual audio/performance exists and its timing is accepted or otherwise authoritative:

```text
PLANNING DURATION ESTIMATE
→ SUPERSEDED FOR DOWNSTREAM TIMING BY
MEASURED / APPROVED AUDIO TIMING
```

Record the governing authority in `timing_authority_ref` and use it when mapping the final beat/scene windows. For audio-led work it points to the timing references owned by `AUDIO_VOICE_PERFORMANCE`: `measured_duration_ref` for total duration, and `speech_text_evidence_ref` when segment-level timing is needed. Otherwise it points to the project/task authority that governs timing. This method does not define a timing schema of its own. Do not keep forcing the audio to fit an obsolete script estimate.

This is conditional, not universal: native on-camera performance, music-led edits, exact performance transfer or other task classes may resolve timing from a different authority.

If the script exceeds route limits:

```text
shorten
OR
split at a meaningful semantic boundary
```

Do not compress speech into unnatural speed merely to preserve every sentence.

Multipart scripts must preserve continuity and part-specific completion conditions.

---

# 9. Exact Speech Authority

Where exact wording is required, mark it once in the execution spec and avoid duplicating dialogue in unrelated prompt sections unless the route requires it.

Known failure memory should be checked for prompt structures that cause repeated or altered speech.

---

## 9.1 Generated / improvised speech is not script authority

When a generation route invents or paraphrases spoken wording, the result is output content rather than an automatic extension of the approved script.

```text
GENERATED / IMPROVISED SPEECH
!=
EXACT APPROVED SPEECH
!=
APPROVED CLAIM WORDING
```

For commercial, factual, regulated or otherwise claim-bearing speech:

1. use exact approved wording when the route/task requires it; or
2. obtain eligible speech-text evidence from the actual output;
3. compare the spoken wording with script/claim authority;
4. treat additions, omissions and changed scope as findings rather than assuming semantic equivalence.

A route that cannot reliably honor an exact material line may still be useful for non-claim performance exploration, but it is not suitable for that exact-speech requirement without an approved downstream replacement/repair path.

---

# 10. Output

```yaml
script_id:
mode:
objective:
persona_ref:
creative_latitude_ref:
creative_risk_level:
concept_exploration_ref:
canon_anchor_refs:
exact_speech_required:
generated_speech_review_ref:  # when route output invents/paraphrases speech
beats:
  - beat_id:
    function:
    speech:
    visible_content:
    performance_task:
    target_duration:
    transition:
    end_state:
pronunciation_notes:
input_language:
output_language:
market_scope:
jurisdiction_scope:
do_not_translate_refs:
claim_translation_equivalence:
timing_notes:
timing_authority_ref:
text_review_action:  # FINDINGS_ONLY | AUTHORIZED_EDIT
text_naturalness_review:
text_findings:  # text_finding_id / canonical finding records
protected_text_refs:
semantic_fidelity_check:
change_delta_summary:
self_check:
  iterations:
  initially_failed_checks:
  repaired_checks:
  remaining_failed_checks:
  status:  # PASS | HANDOFF_WITH_FINDINGS | NOT_RUN
acceptance_criteria:
```

---

# 11. Acceptance Rubric

Pass when:

```text
every beat has a function
opening is specific
progression adds information
speech fits time
persona voice is credible
voice continuity does not collapse into mechanical copying when expression is open
distinct-concept requests materially diverge across authorized open dimensions rather than only paraphrasing one concept
claims match evidence
generated/improvised speech, when present, has been compared against applicable text/claim authority
spoken content is performable
CTA/payoff is earned
text style fits the intended writer/persona rather than a generic model default
no chatbot/drafting residue remains in delivered copy
portable/interchangeable language is justified or made subject-specific without invention
text findings describe observable behavior and do not infer AI authorship
any rewrite preserves protected facts, claims and exact-authority text
edit scope is proportional to the actual defect
```

Reject merely polished copy that remains predictable, repetitive or disconnected from visible action.


## 11.1 Method self-check before handoff

Before handing off edited text, evaluate the applicable acceptance criteria as observable pass/fail checks. If a check fails and the current authority permits repair, fix the smallest causal text surface and rerun the affected checks.

For this method, the default maximum is **2 local self-check repair passes** after the initial check. Stop earlier when all applicable checks pass. If material checks still fail after the bound, hand off the remaining findings rather than iterating indefinitely.

```text
METHOD SELF-CHECK
!=
INDEPENDENT FINAL QA
```

Record the result in `self_check` with iterations, initial failures, repaired checks, remaining failures and status. A producer checking its own work is useful, but must not be recorded as independent review.


---

## V2.4 real-world hardening — narrative script form and pre-handoff completeness

For story-led video use a **director-style continuous narrative** describing human action, dialogue, concurrent gestures, motivated framing, environmental activity and emotional arc, without a second-by-second timestamp table by default. Output sections: optional `Text on Screen`, `Setting & Atmosphere`, `Script & Creative Direction`, `Creative Invariants`, `Creative Open Zones` and overall technical constraints. Exact dialogue/claims, when user-approved, remain protected even when improvisation is allowed elsewhere. Do not create mandatory spoken hook when a visual hook works.

`CONCEPT` / idea selection ≠ script approval; storyboard is iterative planning object. For motion requiring exact synchronization, measured speech, UI click states or edits, use the appropriate beat/time fields and real authority. Check semantic and theatrical naturalness as well as structural presence; improve a missing beat rather than redoing already accepted work. A complete script must satisfy the Catalog's applicable contract; retain the method's bound of two local self-check repairs unless another authority narrows it.

