# AI Creative Skill · Specialist Method · Buyer Research · Pre-v0.3

## Status

```text
METHOD ID = BUYER_RESEARCH
VERSION = Pre-v0.3
DATE = 2026-10-07
PARENT_DOCUMENT = AI_Creative_Skill_Specialist_Method_System
LAST_VALIDATED_AGAINST = AI_Creative_Skill_Specialist_Method_System_Pre-v0.8.md
STATUS = DESIGN METHOD · NOT INSTALLED
```

This method deepens the Ads Work Profile's purchase-situation research. It is provider-neutral and source-agnostic. Pre-v0.2 delegates generic retrieval/query/fusion/freshness mechanics to `RESEARCH_EVIDENCE_SYNTHESIS` and keeps buyer interpretation, purchase-situation evidence and creative implications here.

---

# 1. Trigger

Required when a commercial task needs a grounded buyer basis and none of the following is adequate and current:

```text
fresh inspected research
valid reusable research
authoritative supplied evidence
```

For a new ad creative:

```text
NEW_AD_CREATIVE
→ GROUNDED_AUDIENCE_BASIS REQUIRED
```

A bounded edit, resize, repair or script-only request may reuse existing valid audience evidence when the requested change does not depend on new buyer facts.

---

# 2. Inputs

Useful inputs:

```text
offer / SKU / service
market / language
known alternatives
client hypotheses
first-party observations
product specifications
existing research and date
commercial objective
```

Client-declared audience is a hypothesis, not independent confirmation.

---

# 3. Research Question

Do not begin with demographic decoration.

Begin with:

```text
What changes at the moment of purchase?
What progress is the buyer trying to make?
What do they use instead, including doing nothing?
What makes them hesitate?
What proof would reduce that hesitation?
```

Segment only when materially different situations, outcomes or barriers change the creative implication.

When external research is required, invoke `RESEARCH_EVIDENCE_SYNTHESIS` for query planning, source outcomes, dedupe, independent corroboration and freshness verification. Buyer Research owns the **buyer meaning** of that evidence, not the retrieval engine.

---

## 3.1 Buyer-specific signal quality

Do not rank buyer evidence by mention count alone. Evaluate what the observation can actually support.

Useful distinctions include:

```text
direct observed purchase/use experience
traceable first-party product / offer fact
independent discussion with concrete context
measured first-party research, when methodology is known
category commentary / analysis
promotional or affiliate copy
```

These are not universal numeric weights. A source can be strong for one proposition and weak for another. Repeated promotional copy does not outrank one well-supported contradictory observation merely because it appears more often.

---

# 4. Evidence Matrix

Maintain a compact matrix:

```text
source / coverage / date
→ buyer language or faithful paraphrase
→ situation / trigger
→ desired outcome
→ current alternative
→ hesitation
→ offer fit / poor fit
→ required proof
→ creative implication
```

Keep observation, interpretation and hypothesis separate.

A seller page supports what the seller states. It does not independently prove efficacy, popularity or sales.

Repeated syndicated reviews or duplicated press material do not count as independent evidence.
Copies surfaced by several subqueries, locales, embeds or aggregators also do not become independent corroboration when they trace to the same underlying origin.

---

# 5. Source Diversity

When available, combine different evidence classes, for example:

```text
exact product / offer specifications
retailer or marketplace reviews
independent user discussions / forums
first-party data or interviews
comparable offers
category-level context
```

For reviews, inspect recency, incentive context, variant identity and actual content rather than search snippets alone.

A "verified purchase" badge is useful context, not proof of authenticity.

---

# 6. Coverage

Coverage is proportional to task importance.

For a deep run, a practical starting target is roughly:

```text
~20 useful observations
across at least two source types
per major finalist / priority segment when evidence exists
```

This is a coverage heuristic, not statistical representativeness and not a quota that authorizes weak sources.

Stop when:

```text
requested depth is met
AND
targeted searches produce little new decision-relevant evidence
```

Report actual inspected coverage and material gaps.
Where retrieval was external, carry forward the complete canonical source outcome from `RESEARCH_EVIDENCE_SYNTHESIS` by reference. Do not maintain a Buyer-specific subset enum. Only canonical `NO_RESULTS` represents successful negative coverage; payment/authentication/configuration failures and every other non-success outcome must not be paraphrased as “no buyer evidence exists.”

---

# 7. Counterevidence and Poor Fit

Every priority buyer synthesis should include:

```text
positive observations
negative / mixed observations
counterexamples
poor-fit conditions
```

Research that only confirms the preferred angle is incomplete.

Counterevidence may narrow the claim, change the audience priority or invalidate the concept.

---

# 8. Buyer Language

Use exact wording only when wording itself matters and quotation rights/limits permit it. Otherwise preserve meaning through faithful paraphrase.

Do not turn hooks into fake buyer language.

Record language that reveals:

```text
trigger
alternative
friction
desired progress
proof vocabulary
terms buyers use for the problem
```

---

# 9. Output

Return:

```yaml
research_id:
offer_ref:
market:
research_date:
research_execution_ref:
coverage:
source_outcomes:
priority_buyer_situations:
  - trigger:
    desired_progress:
    current_alternative:
    hesitation:
    supporting_observations:
    counterevidence:
    poor_fit:
    buyer_language:
    required_proof:
    creative_implication:
unknowns:
recommended_priority:
priority_rationale:
freshness:
freshness_verdicts:
```

---

# 10. Acceptance Rubric

Pass only if the synthesis can answer:

```text
WHO, in a meaningful situation?
WHY NOW?
WHAT ARE THEY USING INSTEAD?
WHAT DO THEY WANT TO CHANGE?
WHAT STOPS THEM?
WHAT EVIDENCE WOULD MATTER?
WHAT SHOULD THE CREATIVE DO DIFFERENTLY BECAUSE OF THIS?
```

Reject or narrow output that collapses into generic demographics, generic pain points or invented motivations.

---

# 11. Reuse and Freshness

Reuse research when:

```text
same materially relevant offer / market / buyer situation
source age remains acceptable for the decision
no contradictory new evidence is known
```

Refresh when price, product, market, buyer context, platform environment or decision-critical evidence changed materially.
For volatile claims that could materially change the creative or offer, use the shared research method's point freshness verification instead of assuming the original research date is sufficient.

---

# 12. Calibration Examples

Weak:

```text
Women 25–44 want convenience and quality.
```

Acceptable:

```text
People buying after a specific trigger compare this offer with X and hesitate because of Y.
```

Excellent adds:

```text
observed buyer language
actual alternative behavior
counterevidence
poor-fit conditions
required proof
specific creative implication
```

The transferable principle is situational evidence, not a fixed segment count.
