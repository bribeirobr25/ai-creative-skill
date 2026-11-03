# Video Director v0.1 (proposal)

**Status:** draft for the owner's review. Not adopted and not formally evaluated; smoke and targeted runs only (below). No Brain decision yet. It authorizes nothing: no generation, external service, spend or change to the frozen `src/`.

The first specialist under the [system vision](../../vision/README.md) and [ADR-0006](../../decisions/ADR-0006-system-direction-agent-teams.md): an audiovisual creative director that turns an idea, goal or brief into a clear creative direction and an executable production plan. It is also the first concrete use of the shared parts later agents will reuse: a role definition, an input/output contract, knowledge packs with evidence tags, and an evaluation protocol fixed in advance.

| File | What it holds |
|---|---|
| [definition.md](definition.md) | Role, scope, responsibilities, boundaries, freedom, working with the user, phases, the four information categories, planning depth, repurposing, kinds of quality, relations, learning |
| [contract.md](contract.md) | Input (objective, type, medium, techniques, specifications, authorities, references, user experience, deliverable level) and output (the direction package) |
| [knowledge-packs.md](knowledge-packs.md) | Direction Core, format and medium cards, professional motion reference library, Production's tool register, and what was not adopted |
| [evaluation.md](evaluation.md) | The comparison with a generalist: authority, three fresh scenarios, owner-judged creative quality as the main measure, minimum requirements, four possible recommendations, stop conditions, cost; production-quality criteria for later |
| [smoke-test-plan.md](smoke-test-plan.md) | Five exploratory scenarios with fixed user sheets, procedure and criteria, written before running |
| [smoke-test-report-2026-10-31.md](smoke-test-report-2026-10-31.md) | Results of the five runs (assisted role-play), the problems found and the fixes made; transcripts in `smoke-test-2026-10-31/` |
| [smoke-test-regression-report-2026-10-31.md](smoke-test-regression-report-2026-10-31.md) | Regression run of the same five scenarios after the fixes (file-scoped isolation, harness context present), with corrections from the 2026-11-03 audit; transcripts and the user sheets as used in `smoke-test-2026-10-31-regression/` |
| [post-approval-test-2026-11-03.md](post-approval-test-2026-11-03.md) | Targeted test of changes after an approval: plan, results and validity limits; the transcript, the reviewer's output and the run script sit beside it |

## Design choices

- **One Director, not one agent per video type or technique.** Type, medium and technique are knowledge the Director loads; execution is Production's. Production starts as capabilities and is split by pipeline only when that proves worth it (likely candidates: code-based motion graphics, and avatars).
- **The owner's four game changers are information categories, not mandatory documents.** Their depth follows the job.
- **Freedom by default.** Each dimension of a job is preserve, bounded variation or open exploration, set by the authorities; everything else is open, and an execution scope lists its open dimensions explicitly. Approvals, the spend limit, rights, consent, the closing check and independent review are never skipped.
- **Evidence tags on every item,** so a hypothesis from a research chat cannot pass as a rule.

## Sources

- **The owner:** the description of the agent and the notes on the four information categories and brief parameters (2026-10-31).
- **The frozen V2.5 methods**, cited by section.
- **This project's research records:** the photoshoot study, the 2026-10-22 audit and the benchmark log.
- **Four AI-assistant research conversations, kept privately** with checksums. Only distilled points and source links are published here.

## Decided in review (2026-10-31)

1. **Location:** `docs/agents/` stays as the provisional home until the vision's step 2 decides where agent material lives.
2. **Formal comparison:** two runs per arm per scenario, with the owner reviewing all 12 transcripts unlabelled and in random order (not fully blind; see `evaluation.md`).
3. **Scenarios:** the three fictional scenarios in `evaluation.md` are reserved for that comparison and not used for tuning. *Replaced 2026-11-03 by three fresh scenarios written outside the Director's development (see `evaluation.md`).*
4. **Next:** after the Director's evaluation, a small, controlled motion-graphics Production route, under separate authorization.

Before the formal comparison, a five-scenario exploratory smoke test with different briefs checks the whole flow ([smoke-test-plan.md](smoke-test-plan.md)).

## Readiness (2026-11-03)

**Not ready for the formal comparison.**

What the runs show:
- The Director catches most high-stakes traps.
- It keeps the user in charge and can apply the change-after-approval rule.

What they don't show:
- **Reliability.** Every scenario ran once or twice with cooperative simulated users, and most "fixed" verdicts repeat the fix's own wording.
- **The edges hold up.** One run stretched a range across dimensions, invented a product detail, widened a scope beyond the request and repeated the same caveat about six times.

Changed after the 2026-11-03 audit, and not re-run, so that the five smoke scenarios are no longer used for tuning:
- explicit `open` dimensions in a scope;
- a defined closing check, and independent review of the finished deliverable;
- `quote_ref` before approval;
- the D8 items: asset `tool`, captions, handing off what needs a human professional;
- scenario-tagged rules removed;
- C7 restated;
- labels kept internal unless they change what the user is asked;
- the reports corrected.

Before the comparison (revised 2026-11-03, see `evaluation.md`):
1. **Authority.** The owner decides the proposed record DEC-2026-11-03-evaluation-method-r2, which allows this one comparison as an exception to the evaluation-method decision.
2. **Scenarios.** Three fresh scenarios, written by the owner or by a separate writer session that has not seen the Director.
3. **Pre-registration**, then the owner approves the cost option.
