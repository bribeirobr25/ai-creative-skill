# Slice 01 · Research → offer → landing page (plan)

**Status:** plan for the vision's step 4. Merging it approves the plan only. Each phase below starts only on the system owner's explicit go for that phase; one go does not carry over to the next (AGENTS.md). Nothing in this plan publishes, sends, contacts, connects an account or spends outside the owner's Claude plan.

**Sources:** the [vision](../vision/README.md) sequence steps 2 and 4; [ADR-0006](../decisions/ADR-0006-system-direction-agent-teams.md) D3, D6, D9; [ADR-0005](../decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md) D2, D6; the [Shared Core v0.1](../core/README.md), including its "Settled by the system owner" list; [scenario 01](../core/scenarios/01-research-offer-landing.md) (the reference playbook); the [benchmark log](../benchmarks/benchmark-log.md) checks C1–C9; the four-axis rubric in [creative-quality/evaluation.md](../research/creative-quality/evaluation.md).

## What the owner settled for this slice (2026-11-05)

| Question | Answer |
|---|---|
| Playbook | Research → offer → landing page, as in scenario 01 |
| Project | The system owner's own business. Single user, single tenant, no named approvers. Its name and data live only in the private half |
| Host | Claude Code subagents (decision `shared-core`) |
| Public system parts | This repository, in a new top-level `system/` folder: agent definitions, packs, the playbook, record templates, hooks, evaluation cases. Never project data. `src/` stays frozen |
| Private half | A private GitHub repository the owner holds; its locator is kept outside this repository. Plus an offline backup |
| Operating budget | The agents' own work runs within the owner's existing Claude plan; no metered API use |
| Tool spend | None. Every execution scope in this slice has `spend_limit: 0` |
| Evaluation | Automated readiness pipeline before v1; the owner rates v1 on the real project (below) |

## What the slice tests

On one real project, end to end (vision step 4): intake, handoffs, pack loading (KP2), freshness of research findings, the memory scenarios T01–T08 (check C8), the permission levels, and the Shared Core contracts used by scenario 01: task and message records, the derived lifecycle, independent review at boundary C, repair rounds, and continuation after results.

## Host mapping

Facts below are from the Claude Code documentation as checked on 2026-11-05. Each is re-verified in phase 0 before anything relies on it.

| Core contract | In Claude Code |
|---|---|
| Project lead | The main session. It plans and assigns. It holds no authority (collaboration.md) |
| Specialist roles | Subagents in `system/agents/`, one file per role: research, sales, visual-brand, reviewer, growth |
| Knowledge packs | Plain files in `system/packs/`, read by the role at start; each read is recorded in `packs_loaded` |
| Delegation depth 2 | Plan assignments are main → subagent (depth 0). The host allows nesting up to three layers below the main session, which matches depth 0–2. The host limit is a backstop; the recorded depth is the rule |
| Read-only review | The reviewer's `tools` allowlist names read-only tools only. The documentation describes this as removing tools from the subagent; phase 0 tests it |
| Records | Plain YAML/JSONL files in the private half, following project-context.md. Host memory is not the project's source of truth (ADR-0005 D5) |
| Limits enforced by hooks | `PreToolUse` hooks deny writes outside the project folder, deny any subagent write to approval records, and deny publishing, sending, deploy and account tools. Hook input names the subagent (`agent_type`), so the checks run per role |
| Approvals | The owner types the approval in the main session, and the main session records it. The host cannot attest that a person, not an agent, typed it (finding `FND-AUDIT2-AGENT-IDENTITY`). For a single-user slice where every outward action is manual, this is an accepted risk, recorded as such |
| Scheduling | Not used. The `research_due` reminder and the measurement step start when the owner asks |
| Cost | Runs use the Claude plan's login. A pre-run check confirms that no API key is set in the environment, because an API key takes precedence and would bill metered use. Usage is read from the host's usage view and recorded per phase |

## Phases

### Phase 0 · Groundwork (no real data)

1. The owner backs up the private repository offline, and keeps that backup current while the slice runs.
2. Set up the private-half layout in the private repository: `projects/<project-id>/` with `records/`, `assets/`, `snapshots/` and `exports/`, plus a README that repeats the privacy rules.
3. **Host check** (ADR-0005 D6), run on a fictional project. It covers the kept contract (I1–I5, I8, I9, privacy and erasure, two-level idempotency), T01–T08, the reviewer's read-only tools and each hook. The result goes in the benchmark log as a new entry, together with the host version.
4. No secret store yet: the slice uses no credentials. Choosing one comes back when a connection is planned (vision step 6).
5. **Rights review:**
   - Competitor pages and public reviews are read, never copied: patterns, not copies.
   - Snapshots stay in the private half and are kept only as platform terms allow.
   - The page uses only assets the owner holds the rights to.
   - Any new name or logo gets a mark check.
   - Lead capture, if the page has it, needs consent text and a retention rule before it goes live.

### Phase 1 · Build to v1 (agents build; fictional cases only)

Agents write `system/`:
- the five role definitions;
- the packs: buyer research and evidence synthesis, offer, websites with copy, review criteria, measurement;
- the playbook record;
- record templates;
- hooks;
- the evaluation cases.

Each pack item carries its layer, tag, strength and source (knowledge-packs.md), and stays `unproven` until it earns its place. A **generalist baseline** is fixed before any comparison: the same host and model, with no packs and no role files, running in one session from the same brief.

**Readiness pipeline**, run on fictional cases only:

1. **Rule checks**, mechanical where possible. They re-instrument C1, C2, C3 and C5, plus core invariants:
   - no unasked generation (C1);
   - after an approval, acknowledgement only (C2);
   - claims only from the facts sheet (C3);
   - an injected note never overrides an approved record (C5);
   - records valid against their contracts;
   - depth and caps respected;
   - no write by a subagent to approval records;
   - every finding has `checked_at`;
   - every closing check is present.
   
   One rule failure blocks v1, whatever the judges say.
2. **Blinded AI judges.**
   - Two judges, each in a fresh context with read-only tools.
   - The judges score the outputs of the system and of the baseline, labelled A and B in random order, on the four axes (aesthetic, fidelity, technical/functional, efficiency).
   - The page is judged from a local render at desktop and phone sizes.
   - Limitation: the judges come from the same model family as the producers, so judging is not independent of the model.
3. **Held-out cases.**
   - Ten fictional businesses are written at the start. Six are used while building, and four are sealed until the final readiness run.
   - The sealed cases are never shown to the agents that build or tune `system/`. This guards against tuning to the judge.
4. **v1 bar.** The bar is fixed before the final run:
   - all rule checks pass on all ten cases;
   - on the four sealed cases, the system is preferred or tied by both judges on at least 3 of 4, and never loses on fidelity (claims and facts);
   - the host check passed.
   
   A pack or role that does not beat the baseline stays `unproven`. It is removed, or kept only when the judges' reasons point to a specific gap it fixes.

The pipeline's design, cases, scores and limits go in the benchmark log as a new entry. Private material (outputs of real projects) never does.

### Phase 2 · Real project (owner's go required)

The playbook runs on the owner's business, with these checkpoints (scenario 01):
- the plan is shared (no approval needed);
- `direction` approval of the offer;
- `direction` approval of the page direction;
- independent review at boundary C, with at most 1 repair round before escalation;
- the owner publishes the page by hand: no agent deploys or posts.

Spend stays at zero. A step that would need paid generation, paid data or a connection stops with a request to the owner.

### Phase 3 · Measure and rate (owner's go required)

1. After two to four weeks, the owner exports the page's analytics and puts the file in the private half's `exports/`. Growth reads it as `external_result` data and proposes the next iteration. Nothing changes without a new `direction` approval.
2. **Owner rating of v1.** The owner rates each deliverable (the market brief, the offer, the page) on the four axes, 1–5, with one line of reasons. The owner also rates whether the guidance saved them work against doing it with a generalist session.
3. Rating summaries go in the benchmark log and Brain observations, with no project data. Ratings and results decide which packs and roles earn their place (ADR-0006 D9). An observation never becomes a rule by itself (Brain contract rule 4).

## Exit criteria and records

The slice closes when either of these holds:
- phase 3 is rated;
- the owner stops it.

It leaves:
- benchmark log entries for the host check, the readiness run and the owner's ratings;
- Brain observations of what worked and what failed, and findings for defects;
- decision records only for what the owner decides from the results.

The next slice or the learning loop (vision step 5) is a separate plan.

## Risks

| Risk | Mitigation |
|---|---|
| A judge from the same model family shares the producers' blind spots | Rule checks are mechanical; sealed cases; the owner's rating at v1 is the final word |
| Tuning to the evaluation | Sealed cases never reach the building agents; the v1 bar is fixed before the final run |
| Real business data reaches the public repository | The publication guard and CI scan; `system/` holds only domain-neutral files; the project lives in the private repository |
| Metered API billing by accident | Pre-run check that no API key is set; usage recorded per phase |
| Approval typed by an agent under the owner's session | Single user and manual publication; hooks deny subagent writes to approval records; recorded as an accepted risk (FND-AUDIT2-AGENT-IDENTITY) |
| Host behaviour differs from its documentation | Phase 0 tests every host fact this plan relies on before use |

## Amendments

**2026-11-05 (owner).** The slice's project is the owner's own brand, named only in the private half. Owner's answers:
- **Host check data:** it runs on that project's real text records, not on a fictional project.
- **Reading in place:** project sources are read in place at a pinned commit. They are never copied into the private half; records carry the path, commit and SHA-256.
- **Read-only sources:** the project's own repository and storage are never written to.
- **Excluded:** media, real recordings and real people. Earlier pilot material is not resumed.

Approvals, revocations and changes that the host check makes are test fixtures (`test: true`). They never stand for the owner's decisions.
