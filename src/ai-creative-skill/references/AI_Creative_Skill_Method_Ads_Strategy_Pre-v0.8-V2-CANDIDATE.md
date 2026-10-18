# AI Creative Skill · Specialist Method · Ads Strategy · Pre-v0.8-V2-CANDIDATE

## Status

```text
METHOD ID = ADS_STRATEGY
VERSION = Pre-v0.8-V2-CANDIDATE
DATE = 2026-10-10
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.11-V2-CANDIDATE.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

GPT validation hardening branch (2026-10-10): Pre-v0.8-V2-CANDIDATE adds controlled experiment-design fields for variant families when the user's goal is learning/optimization rather than merely producing aesthetic alternatives. Existing persuasion/evidence rules remain unchanged.


This method converts grounded buyer/evidence inputs into a commercial hypothesis and executable concept. Validator correction round (operator-agreed window, 2026-10-09): Pre-v0.7 only moves the Pre-v0.6 dominant-commercial-tension sentence in §10 to after the traceability chain it had interrupted; no rubric content changes. Pre-v0.6 adds a bounded-asset focus rule around one dominant commercial job/problem and makes format selection explicitly subordinate to the commercial problem, available evidence and placement constraints rather than provider preset availability. Pre-v0.5 TVM-derived message-knowledge-state and mechanism → consequence behavior remains in force. It does **not** import fixed awareness levels, copy-length laws, numerical scores, urgency incentives or performance-uplift claims.

---

# 1. Trigger

Use when the task requires:

```text
new commercial concept
ad copy / script
commercial variation with a changed persuasion mechanism
creative strategy diagnosis
```

Do not reopen strategy for a bounded mechanical edit unless the requested change invalidates the existing commercial logic.

---

# 2. Six Required Decisions Before Copy

Before writing final copy, resolve:

```text
1. PURCHASE SITUATION / JOB
2. DESIRED OUTCOME + RELEVANT OBSTACLE
3. PRODUCT / SERVICE MECHANISM + ONE SUPPORTED DIFFERENCE THAT MATTERS
4. MAIN OBJECTION + EVIDENCE / TRUTHFUL EXPLANATION
5. REAL OFFER: PRICE / INCLUSIONS / CONDITIONS / DESTINATION / NEXT ACTION
6. MEASURABLE HYPOTHESIS: WHAT SHOULD CHANGE, FOR WHOM, AND WHAT RESULT WOULD SUPPORT OR REJECT IT
```

If any material decision is unknown, narrow the strategy rather than inventing it.

## 2.1 Message Knowledge State · conditional

When reliable buyer evidence materially changes how much explanation or proof the message needs, record a **message knowledge state**. This is an evidence-grounded planning bridge, not a demographic stereotype and not a mandatory five-level awareness taxonomy.

Resolve only what the evidence supports:

```yaml
message_knowledge_state:
  what_buyer_already_knows:
  what_still_needs_explanation:
  what_requires_proof:
  what_can_be_stated_directly:
  supporting_evidence_refs:
```

Use it to decide message depth, sequencing and proof burden. For example, a buyer already familiar with the problem but unfamiliar with the offer may need little problem education and more mechanism/proof; a buyer already comparing the offer may need direct differentiation and current terms.

```text
LOWER FAMILIARITY
!=
AUTOMATICALLY LONGER COPY

HIGHER FAMILIARITY
!=
AUTOMATICALLY HARDER SELL
```

Format, attention window, task objective and evidence still govern execution. If the knowledge state is unknown, leave it unknown and do not infer it from age, gender, platform or other decorative demographics.

---

## 2.2 Dominant commercial job / problem per bounded asset

For a bounded ad asset or creative execution, choose **one dominant commercial job, problem or tension**. Secondary details may support it, but they should not compete as independent persuasion theses unless the chosen format explicitly requires a sequence.

```text
ONE BOUNDED AD ASSET
→ ONE DOMINANT COMMERCIAL TENSION
→ ONE COHERENT HOOK / MECHANISM / PROOF / CTA CHAIN
```

This is a focus discipline, not a universal ban on multi-step explainers, comparison narratives or longer formats. If two materially different purchase situations need independent persuasion chains, treat them as separate concepts/assets rather than hiding both inside one short execution.

When several candidate problems exist, prioritize with evidence-grounded factors such as buyer relevance, consequence, frequency, supported surprise/non-obviousness, visual/audible demonstrability and fit with the actual offer. Do not manufacture a dramatic problem merely because it is easy to visualize.

---

## 2.3 Experiment Design for Learning-Oriented Variants · conditional

When a variant family is intended to learn rather than merely provide choices, declare:

```yaml
experiment_hypothesis:
learning_question:
comparison_family_ref:
preserved_dimensions:
varied_factors:
factor_levels:
primary_metric_or_observation:
invalidating_confounds:
```

Prefer variants that cover declared factor levels without accidental duplicates or simultaneous uncontrolled changes. This is a planning discipline, not a promise of statistical significance or business uplift.

---

# 3. Persuasion Chain

```text
BUYER SITUATION
→ BUYING MOTIVE
→ OBJECTION
→ SUPPORTED DIFFERENCE / REASON TO BELIEVE
→ PERSUASION HYPOTHESIS
→ VISIBLE / AUDIBLE SUPPORT
→ CONCEPT FAMILY
→ CTA / DESTINATION
→ FAILURE HYPOTHESIS
```

A wrapper change is usually a variant. A materially different reason-to-believe or persuasion mechanism is a new concept.

---

# 4. Specificity Standard

Challenge generic strategic language that could fit almost any product. As an operational check, ask whether the line could move unchanged to a competitor, another product or another category without losing much meaning. If yes, require a supported product/buyer-specific fact, mechanism, consequence, constraint or judgment when the concept depends on specificity.

```text
PORTABLE LANGUAGE
= REVIEW FOR SPECIFICITY
!= AUTOMATIC FAILURE
```

Do not invent a detail merely to make copy more specific.

Examples of generic strategic language to challenge:

```text
premium quality
unlock your potential
game-changing
effortless transformation
best-in-class
```

A feature earns space only when it explains a buyer-relevant benefit or proof mechanism.

## 4.1 Mechanism → consequence check

When a feature or mechanism is strategically important, test whether the creative can trace it to an actual buyer-relevant consequence:

```text
SUPPORTED FEATURE / MECHANISM
→ OBSERVABLE OR PLAUSIBLE CONSEQUENCE SUPPORTED AT THE RIGHT SCOPE
→ BUYER-RELEVANT OUTCOME / REASON TO CARE
```

Ask the equivalent of “so what?” only until the chain reaches a meaningful supported consequence. Do not keep climbing into invented emotional benefits, fabricated outcomes or universal claims merely to make the copy sound stronger.

If the consequence cannot be supported, narrow the promise or remove the feature from the persuasion chain.

---

# 5. PROOF and QUEST

Use PROOF for product/e-commerce when useful:

```text
Promise
Receipts
Offer
Objection
First step
```

Use QUEST for services when useful:

```text
Qualify
Understand
Educate
Stimulate
Transition
```

These are reasoning frameworks, not mandatory visual templates.

---

# 6. Format ↔ Evidence Contract

Choose the format family from the commercial job/problem, available evidence and placement constraints. Provider preset availability does not decide the strategy.

```text
COMMERCIAL JOB / PROBLEM
+ AVAILABLE SUPPORTING EVIDENCE
+ PLACEMENT / ATTENTION CONSTRAINTS
→ FORMAT FAMILY
```

Common product families require different proof:

| Family | Required evidence |
|---|---|
| CALLOUT / DIAGRAM | visible verified feature + supported benefit |
| REVIEW-LED | traceable genuine review/testimonial with allowed attribution |
| OFFER-LED | current product, price, inclusions and material terms |

Common service families:

| Family | Required evidence |
|---|---|
| QUIZ | truthful self-assessment and real next step; no fake diagnosis |
| CASE STORY | documented starting point, intervention and supported result |
| DIRECT OFFER | real scope, terms and CTA |

If evidence is missing, change the concept or clearly mark an unfinished blueprint. Do not manufacture proof to preserve a format.

---

# 7. Packaging and Unboxing Truth

An unboxing or offer reveal must match verified packaging and included items.

Without evidence, do not invent:

```text
gift box
extra accessory
warranty card
quantity
capacity
compliance badge
```

Use an honest product/offer reveal instead.

---

# 8. Localization

Localization is not literal translation.

Recheck for every market:

```text
buyer context
spelling
units
currency
offer eligibility
cultural meaning
voice timing
line breaks
claims
typography
pacing
destination
```

A concept may transfer while execution changes materially.

---

# 9. Output

```yaml
strategy_id:
buyer_situation_ref:
offer_ref:
message_knowledge_state:
job:
dominant_problem_or_tension:
desired_outcome:
obstacle:
supported_difference:
main_objection:
answering_evidence:
persuasion_hypothesis:
concept_family:
format_family:
exact_offer:
visible_support:
cta:
destination:
primary_metric:
failure_hypothesis:
experiment_hypothesis:
learning_question:
preserved_dimensions:
varied_factors:
comparison_family_ref:
localization_requirements:
```

---

# 10. Acceptance Rubric

A strategy is strong when a reviewer can trace:

```text
EVIDENCE
→ BUYER NEED / SUPPORTED MESSAGE KNOWLEDGE STATE WHEN MATERIAL
→ PROMISE
→ PROOF
→ EXECUTION
→ CTA
```

A strong bounded asset also has one dominant commercial tension. If the reviewer cannot tell which problem/job the asset is trying to resolve, split or narrow the execution before adding more copy.

Reject concepts whose visual treatment is unrelated to the claimed reason-to-believe or whose evidence does not support the promise. When a message knowledge state is used, its explanation/proof assumptions must trace to evidence. Material feature-led persuasion should also survive the mechanism → consequence check without inventing the final benefit.
