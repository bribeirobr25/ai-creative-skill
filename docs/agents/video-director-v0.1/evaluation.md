# Video Director v0.1 · Evaluation protocol

**Status:** proposal, revised 2026-11-03 with the owner's adjustments. Nothing has been run. The comparison needs an owner decision first, because the evaluation-method decision in force rules out live blind studies (see "Authority"). Running then needs the owner's approval of the cost option. It costs model usage only: no generation, publication, spend outside the approved option, or external services.

**Question:** does the Director's specialized guidance add meaningful creative and planning value over a generalist given the same model, facts, binding rules and tools?

## Authority

- **In force:** DEC-2026-10-30-evaluation-method: "No further live blind benchmark studies; questions are evaluated by simulation … over recorded evidence." A comparison with new runs and a hidden-label review is the kind of study it rules out. ADR-0006 D9 leaves the evaluation design open and proposes owner ratings on real work.
- **Proposed:** DEC-2026-11-03-evaluation-method-r2 restates that decision unchanged and adds one bounded exception: this comparison, under this protocol at a named commit, run once. It is in its own small PR so the owner can decide it without merging this one.
- **What the exception does not do:** it does not decide ADR-0006 D9, does not allow other studies, and does not make the Director ready for production. If this protocol changes after the record names its commit, the record must be updated before the owner's merge, or a new one added after it.
- **No run** until that record is merged.

## What this can and cannot show

- **It can show:** how each arm understands a goal, develops a concept, asks for what is really missing, makes useful decisions, adapts to the user, and hands over a direction someone could execute.
- **It cannot show:** final video quality. A good direction does not prove a good video (see "Later: final production quality").
- **Its weight:** 12 simulated conversations are exploratory evidence for one of four recommendations. They are not a statistical result. The earlier container test (benchmark log BL-2026-10-29-01) found no owner-visible difference between its arms; an inconclusive result here is a real possibility and an acceptable one.
- **Merging and use are separate decisions.** Merging PR #56 records a candidate definition. Using the Director on real work is a later owner decision informed by this result. Neither establishes proven production readiness.

## Set-up

- **Same model for every role**, recorded with its effort setting.
- **Two arms, one difference.** Both get the same harness instructions (role as a video creative assistant, no tools, reply with the next message only, a closing `NEXT STEP:` line), the same scenario facts and materials, and the same binding rules: the `rule` items C5, C7, C13, C16 and C17 from `knowledge-packs.md`, as written at the freeze commit.
  - **Generalist:** that and nothing else.
  - **Director v0.1:** that, plus `definition.md`, `contract.md` and Packs 1–3. The Production tool register is excluded.
- **Freeze.** The Director's files are frozen at a named commit before the scenarios are written. No change to them, or to the shared instructions, until all 12 runs are done.
- **Each turn is a fresh call** with the whole conversation so far in its prompt, as in the post-approval test (`post-approval-test-2026-11-03-turn.py`, extended to take an arm and a scenario). No relay tool that adds text around messages.
- **Roles:**
  - a simulated user per scenario, which sees only its character sheet and the conversation;
  - the agent under test;
  - an AI reviewer, after all runs, which sees transcripts without arm labels.
- **Order:** the 12 runs are interleaved in a seeded random order, so one arm is not run entirely before the other.

## Scenarios

Three fresh scenarios replace the reserved A, B and C. Those were written with the packs and resembled the smoke-test scenarios, so they were not held out (their text is in git history at `3d3108f`).

| # | Type | What it should exercise |
|---|---|---|
| S-pro | A professional with a clear brief and real materials | Staying light; a strong concept inside an established brand; finding the one thing really missing |
| S-new | A beginner with a vague goal and few materials | Inferring and stating assumptions; good defaults; teaching without interrogating; an idea the user did not think of |
| S-con | A constrained creative task (for example a fixed duration, format, budget or material limit) | Creative quality under limits; honest trade-offs; one post-approval change sequence |

**The post-approval sequence** (in S-con only, or in S-pro if the writer judges it a better fit): after the agent's proposal, the user approves it and then asks for two changes, one that the proposal allows and one that it does not. At most three extra user turns. The other scenarios end at the proposal.

**Who writes them, and isolation.** A hash shows that materials were not changed later; it does not keep them from being seen. So:
- **Preferred:** the owner writes the three scenarios and character sheets.
- **Otherwise:** a separate writer session that receives only the writer brief below. It sees no Director file, pack, test, earlier scenario or report.
- The materials are kept in the private folder. No session that edits the Director reads them before the freeze. The orchestrator first reads them when the runs start, after the freeze.
- They are fictional (brands, people, products) and are published with the results.

**Writer brief (the whole of it):** "Write three short video-direction requests a real client might bring to a creative director: a professional with a clear brief and real materials; a beginner with a vague goal; and a constrained creative task. For each, write the client's opening message, a one-page character sheet (who they are, what they want, what they know, how they talk, what they will say if asked, what they will not volunteer), and written descriptions of any materials they bring. In the constrained one, add an approval followed by two change requests: one the agent's plan could easily allow, and one that would need a new plan. Use fictional brands and people only. Do not design the requests around any particular rulebook."

**Stop rule (both arms):** a run ends when the agent delivers its proposal for the deliverable the user asked for, or after six user turns, plus the post-approval sequence where it applies. The simulated user follows its sheet and does not steer the agent.

## Measures

### Primary: the owner's judgment

The owner reads each scenario's four transcripts (two per arm), labelled W, X, Y and Z at random, before the labels are revealed.

| # | Measure | Owner records |
|---|---|---|
| O1 | **Creative quality**: is there a real concept that fits this goal and audience, distinct and not generic? | 1–5 and one sentence |
| O2 | **Usefulness of the direction**: could a producer execute it as handed over, with the decisions that matter made? | 1–5 and one sentence |
| O3 | **User experience**: did it understand the goal, ask only what was missing, adapt to this user, and keep the effort proportionate? | 1–5 and one sentence |
| O4 | **Preference**: rank the four transcripts by "which would I rather work with on this job" | rank and one sentence |

O1 and O2 are the main measures. O3 matters, but a better experience does not make up for a weaker direction.

### Minimum requirements (pass or fail, per transcript)

These are floors, not substitutes for creative quality. The AI reviewer flags them and the owner confirms.

| # | Requirement |
|---|---|
| M1 | No invented facts, products, interfaces, results or testimonials presented as real |
| M2 | Rights and consent handled for the people, brands, voices and materials involved |
| M3 | Stops before production or spend and asks for the approval it needs |
| M4 | Post-approval sequence only: the allowed change is accepted without a new approval, and the other is raised as a new version for approval, without stretching what was approved |

### Secondary: the AI reviewer

- **When:** after all 12 runs, one call per scenario with that scenario's four unlabelled transcripts, in random order.
- **Rubric:** the planning criteria P1–P12 below, plus flags for M1–M4.
- **Limits:** it is the same model family as the agents, so it may favour their style. It is a guide; the owner's judgment decides. A reviewer from another model family would need another provider and is not part of this bounded comparison.
- **Sealed:** its raw output is hashed before the owner reads the transcripts, and the owner sees it only after recording O1–O4.

### Planning criteria (AI reviewer)

Each criterion is scored 0, 1 or 2 per transcript, or `N/A` when it does not apply to the deliverable requested.

| # | Criterion | 2 means |
|---|---|---|
| P1 | Objective understood | States the goal, audience and desired effect correctly, including what was implied |
| P2 | Questions and assumptions | Asks only what is missing and matters; states the other assumptions for confirmation |
| P3 | Calibrated to the user | Guidance fits the user's level; a simple task stays simple |
| P4 | Reference review | Finds every reference gap that matters and says what to supply and why |
| P5 | Authorities and rules | Handles facts, consent, testimonials and interfaces correctly |
| P6 | Planning depth | Chooses a depth that fits, and says why; neither bureaucratic nor thin |
| P7 | Creative direction | Clear enough for another professional to execute; a real concept, not generic |
| P8 | Proactivity with ownership | Where a real opportunity exists, proposes an improvement with a reason and the user keeps the decision. `N/A` when the brief leaves no material opportunity; 0 when a proposal overrides what the user asked |
| P9 | Sequence | Shot plan or storyboard is coherent: purpose per shot, continuity, timing that fits the duration. `N/A` when the deliverable stops before a sequence |
| P10 | Executable handoff | A proposed execution scope with eligible routes (not one provider), quantities, attempts, cost estimate and risks; stops before spend. `N/A` unless the deliverable is a production plan or beyond |
| P11 | Deliverable boundary | Stops at the deliverable requested |
| P12 | Freedom | Not formulaic; beats and techniques are chosen for this job; alternatives are distinct when offered |

**Operational:** turns and words to the proposal, reported as the cost of using each arm.

## Blinding and leakage (stated in advance)

This is not fully blind. The report lists every known leak, including these:
- The Director's format (scope versions, preserve and vary, the closing check) is recognisable, and the owner has read the earlier transcripts. Outputs are not rewritten to hide it, because rewriting could change their quality.
- The orchestrator designed the Director, runs the comparison and writes the report.
- Every role uses the same model family.
- Under the subscription option (below), the host may add context of its own (earlier runs showed account details reaching the simulated user). Any such text seen in an output is reported.
- The simulated users are cooperative by design, which flatters both arms.

## Outcome

The result supports one of four recommendations. None follows automatically from a count. Each claim must cite transcript passages.

| Recommendation | Evidence that supports it |
|---|---|
| **Advance v0.1 as a candidate for real-world use** | The owner prefers the Director's direction for reasons of creative quality or usefulness across the scenarios, and the Director has no M1–M4 failure that the generalist avoided. It is then used on real work as an unproven candidate (ADR-0006 D9), not as a proven agent. |
| **Simplify specific guidance** | Named parts of the guidance add length, questions or formula without better O1–O2 judgments. The named items are removed. |
| **Revise specific weaknesses** | A demonstrated weakness, such as a minimum-requirement failure or a pattern of weak concepts, traced to the guidance or its absence. Targeted change; any re-test uses new scenarios. |
| **Inconclusive; defer promotion** | Preferences split, or the two runs of one arm differ as much as the arms do, or leakage undermines the reading. Always an acceptable result. |

The recommendation, with the owner's decision, is recorded as a decision record in its own PR.

## Stop conditions

- **Before the runs:** the authority record is not merged; the cost option is not approved; any pre-registered file differs from its hash; the Director's files changed after the freeze.
- **During the runs:**
  - a failed call is retried once; if it fails again, the run is marked failed and one replacement run is allowed for that slot; both are reported;
  - a run where the host's own context or test-awareness shows in an output is kept, marked as leaked and reported; if more than two of the 12 leak, the runs stop and the report says so;
  - under the paid option, the runs stop when the approved cap is reached;
  - nothing is tuned between runs, and no run is repeated to change a result.
- **After:** the owner's O1–O4 are recorded before the labels and the AI review are revealed.

## Pre-registration (committed before the first run)

- the freeze commit of the Director's files;
- the shared harness instructions and both arms' exact prompts;
- the run script with its flags, the model and effort, and the seeded run order;
- SHA-256 hashes of the scenarios, character sheets and materials, which stay private until the runs end;
- the AI reviewer's prompt;
- the owner's rating sheet (O1–O4, M1–M4).

**Kept and published after the runs:** every raw output with its SHA-256, the scenario materials, the label mapping, the AI reviewer's raw output, the owner's ratings, and a list of every place the report departs from the reviewer.

## Cost estimate

Measured inputs: the Director's bundle is about 34,000 characters (about 10,000–13,000 tokens); earlier transcripts reached 8,000–15,000 characters; runs took five to seven agent turns. The main uncertainty is thinking tokens.

| Part | Input tokens | Output tokens (with thinking) |
|---|---|---|
| Director arm, 6 runs × about 6 calls | about 540,000 | about 145,000 |
| Generalist arm, 6 runs × about 6 calls | about 160,000 | about 145,000 |
| Simulated users, 12 runs × about 6 calls | about 290,000 | about 110,000 |
| AI reviewer, 3 calls | about 60,000 | about 30,000 |
| **Total** | **about 1.05 million** | **about 430,000** |

Two ways to run it:
- **Subscription (the earlier tests' method, `claude -p` on the owner's plan):** no per-token charge; it uses plan quota. Isolation is weaker, because the host may add context of its own.
- **API key with a clean, bare host session:** cleaner isolation. At the published Claude Opus 5.5 rates ($4 per million input tokens, $20 per million output tokens; checked 2026-11-03) the estimate is about **$13**, likely range $10–30 depending on thinking. Proposed hard cap: **$40**, including replacement runs.

**Owner time:** reading and rating 12 transcripts of about 1,500–2,500 words each, about two to three hours.

## Acceptance criteria

- **Ready to run:** the authority record is merged; the scenarios exist, written under the isolation rule; pre-registration is committed; the cost option (and cap, if paid) is approved.
- **Valid run set:** 12 transcripts, or replacements reported as such, each from fresh calls, with raw output and hash; every deviation and leak listed.
- **Complete evaluation:** the owner's ratings for all 12, recorded before unblinding; the AI review published; one of the four recommendations, with cited passages; a proposed decision record stating that the result is exploratory and that merging and real-world use remain separate decisions.

## Later: final production quality

These criteria apply only after an authorized production run of an approved plan, and are not part of v0.1:

| # | Criterion |
|---|---|
| Q1 | Fidelity of product, interface and characters to the references |
| Q2 | Continuity across shots |
| Q3 | Motion and physical plausibility |
| Q4 | Legible, correct text and numbers |
| Q5 | Sound and voice quality |
| Q6 | Editing and pacing |
| Q7 | Fit with the objective (commercial or communicative) |
| Q8 | Artistic quality |
| Q9 | Delivery specifications met (duration, formats, captions) |
| Q10 | Rights and consent record complete |
| Q11 | Cost and attempts within the approved execution scope |

The comparison planned for that stage: the same deliverable produced from the Director's plan and from a generalist plan, judged by the owner. A second cut made from the same assets tests repurposing.
