# ADR-0005 · Container decision and the disposition of ADR-0004

**Date:** 2026-10-30
**Status:** ACCEPTED.
- D1 was accepted by the owner on 2026-10-29.
- D2–D7 were accepted when the owner merged PR #33 on 2026-10-30.
- The filename keeps `-PROPOSED` so existing links stay stable.

> **Amendment (owner, 2026-10-30): evaluation method.** No more live blind benchmark studies like Stage 1 are planned.
> - Future questions are evaluated with simulations (for example Monte Carlo) and similar techniques, using the evidence already recorded.
> - This replaces the entry cadence in D1.4. The benchmark log stays as the record of what was observed.
> - The durable checks stay active, because their retirement rule needed new entries.
> - Recorded as `DEC-2026-10-30-evaluation-method` in the Project Brain.

**Supersedes in part:** [ADR-0004](ADR-0004-PROPOSED-agent-workspace-durable-memory.md) (PROPOSED, never accepted). Its text stays unchanged as a historical record.
**Leaves unchanged:** ADR-0001, ADR-0002, and ADR-0003 (still PROPOSED).
**Does not authorize:** merges, releases, changes to `src/`, paid APIs, use of private data, or external operations. Each still needs its own owner authorization.

## Context

Models and hosts improve faster than a prescriptive how-to package can be refreshed. Two examples: image templates in ChatGPT, and motion video in Claude.

The owner questioned whether a skill package is the right container. Three options were defined:
- **(a)** keep the skill package;
- **(b)** a short guide covering what, sequence, quality bar and limits, with techniques as dated suggestions;
- **(c)** no artifact, plus a dated benchmark log.

The question was tested before deciding. See [benchmark log entry BL-2026-10-29-01](../benchmarks/benchmark-log.md#bl-2026-10-29-01-container-test-stage-1).

**Test design**
- Three arms: none, the current skill (a), and a 6,500-character guide (b).
- Two hosts: Claude and ChatGPT.
- 30 runs: a copy task and an image task (3 replicates each), plus four behaviour probes.
- The protocol and decision rule were frozen before the first run. The run order was seeded.
- The owner was the blind judge. Two blind LLM judges, sealed before the owner's verdict, served as a cross-check.

**Result**
- **The owner saw no quality difference between the arms.** Under the pre-registered rule this gives a clear (c).
- The LLM judges also found no arm clearly better than none.
- The skill was enabled in all 5 Claude runs of its arm, but the host never showed it being read.
- The only behaviour difference went against the skill: unasked image generation in turn 1 happened in 2 of 3 runs, against 1 of 3 for the guide and 0 of 3 for none.

## Decisions

### D1 · Container: (c) no artifact plus a dated benchmark log (owner-accepted 2026-10-29)

1. **No new release line for the skill package.**
   - The `v2.5.0` reference and its hashes stay immutable and verifiable.
   - The `2.6.0-dev` candidate is parked, not released.
   - `src/` is neither deleted nor moved; any such change would be a separate owner decision.
2. **No new methods or technique content go into `src/`.** A technique worth keeping becomes a dated, host- and model-scoped observation in the benchmark log, with a review-by date.
3. **Durable rules become checks, not instructions.** The durable rules are: no unasked generation, spend, publication or contact (editing the assistant's own deliverable document is allowed, per the owner's ruling of 2026-10-30); claims only from the facts; flag conflicting inputs; keep product identity. They live as pass/fail criteria in benchmark entries and, later, as Project Brain gates. They are not prompt text.
   - A rule is retired when the current hosts pass it with no artifact in two consecutive benchmark entries.
4. **The benchmark log is the evidence trail** (`docs/benchmarks/benchmark-log.md`).
   - An entry is added when a major host or model change matters to the owner's work, and at least every 6 months while the work continues.
   - Every entry states its date, hosts, model labels, design, judge, n and limits.
   - Private study material (outputs, client media, account state) stays outside the repository.

### D2 · ADR-0004 is partially superseded

**Kept as contract**
- Invariants I1–I5, I8 and I9:
  - one authority per subject;
  - bounded, independently completable operations;
  - `permissions_carried: NONE`;
  - autonomy per action class;
  - fact, request and decision kept separate;
  - private data outside the public repository;
  - maturity, validation and authorization kept separate.
- Privacy and erasure: references do not anonymize, and erasure promises are honest.
- Two-level idempotency: a duplicate-record key is not proof that an external action ran once, and nothing is resubmitted blindly after an UNKNOWN result.
- The memory scenarios T01–T08, kept as the acceptance test for **any** memory, host-native included.

**Changed**
- **I6 (Growth Rule):** moot for new methods under D1.
- **I7 (candidate inventory for `src/`):** applies unchanged to any remaining `src/` change, including D4.

**Withdrawn**
- The L3 engine build (the SQLite event store, i.e. M2) and the L4 Agent Workspace.
- Milestones M4 (agent trio), M5 (dashboards, scheduler, notifications) and M6 (CRM).
- M6 also conflicts with the canon's "not promoted" list: prospecting, outreach and CRM. Withdrawing them from this repository is a scope decision; it is not a judgement that the business need is absent.

### D3 · Tracks and milestones

| Item | Disposition | Re-open trigger |
|---|---|---|
| M0 (#17 + reconciliation) | **Overtaken.** #17 merged 2026-10-27. M0-11 (Intelligence STATUS), M0-12 (Issue #24) and M0-13 (Issue #4) carry over as housekeeping. | — |
| M0b (Drive links) | **Kept, widened** as D4 | — |
| M1 (2.6 builder, clean-host ZIPs, release gate) | **Dropped:** no package release under D1. ADR-0002 journeys T1–T7 are kept as benchmark checks. | Owner reverses D1 |
| pre-M2 (schemas) | **Reduced** to the decision-record contract in D5 | — |
| M2 (Memory v1, SQLite) | **Deferred** | Host memory plus plain files fail T01–T08 on a real project |
| M3 (repurposing) | **Deferred** to the first real project that needs it | A real project needs it |
| M4, M5, M6 | **Withdrawn** (D2) | New ADR |
| Track C (quality benchmarks) | **Promoted:** it is the D1 benchmark log | — |
| Track D / M7 (Intelligence) | **Deferred**; Gate 0 status unchanged (`GATE_0_NOT_PASSED`) | Owner decision on method, source and rights |

### D4 · Public-exposure redaction stays the one planned `src/` change

`src/` still contains:
- Google Drive links in 3 files;
- Drive path references in 7 files (148 lines);
- owner-environment details noted by the 2026-10-28 inventory.

Replacing them with neutral logical IDs or wording is a privacy fix, not a content change. It goes through a separate candidate under I7, with its own owner authorization. Git history keeps the old text; whether to accept that is the owner's decision.

### D5 · Memory: one contract, separate instances, no new engine

**The decision/state record contract**

Fields:
- `kind`: OBSERVED, CHANGE_REQUESTED or DECISION_RECORDED;
- `authority_ref`: required for decisions;
- `evidence_refs`;
- `supersedes`;
- `scope`: host, route, model or version;
- `occurred_at` and `recorded_at`;
- `review_by`;
- `privacy_class`.

Rules:
- the emitter is not the persister;
- superseded or revoked records are never current;
- contradictions fail closed;
- nothing is promoted automatically.

**Instances**
1. **The Project Brain** is the first instance: public and developer-facing.
   - Its state is derived on read from GitHub, not committed.
   - A decision's status changes only through an act attested by the owner.
2. **The Brain's private half** (pilot canon, client brands, account state) lives outside the repository, wherever the owner chooses.
3. **Per-creative-project memory** uses what the host offers, or plain files, evaluated with T01–T08. No home-built engine unless the D3 trigger fires.

### D6 · Host-native features are adopted against the kept contract

Host memory, delegation, scheduling and artifacts are preferred over home-built infrastructure. Before relying on one for real data, check it against D2's kept contract: authority, privacy and erasure, idempotency, and T01–T08. Record the check in the benchmark log.

### D7 · Names

- The memory scenarios called "Piloto 01" in ADR-0004 are renamed **memory scenarios T01–T08**. This avoids a collision with the Pilot 01 persona work.
- The A0 decision IDs are settled as follows:

| ID | Disposition |
|---|---|
| D-A0-01 | Answered by this ADR |
| D-M0-01 | Overtaken |
| D-M1-01 | Dropped |
| D-P2-01 | Reframed as D5 |
| D-M2-01 | Kept as "where private state lives, retention and erasure" |
| D-M2-02 | Deferred |
| D-M4-01 | Kept as action-class envelopes for any delegate |
| D-M5-01 | Deferred |
| D-D-01 | Deferred |
| D-A0-02 (PR #30) | Closed without merge by the owner on 2026-10-30. Its branch is preserved by the evidence-branch ruleset, and ADR-0004's text is carried here unchanged. |

## Consequences

- **The repository's role changes:**
  - from an installable package under active method growth;
  - to a record of decisions, evidence and benchmarks, plus a frozen historical package.
- **The cost of keeping up with new models falls:**
  - no candidate, rebuild or reinstall cycle;
  - benchmarks cost owner judging time and image budget.
- **Risk: rules nobody checks rot on paper.** Mitigation: D1.3 keeps durable rules only as checks that a benchmark or the Brain actually runs.
- **Risk: a host regresses on a retired rule.** Mitigation: the next benchmark entry re-tests it, and retirement is reversible.
- **Limits of the evidence:**
  - Stage 1 covered one copy task, one image task and four probes, at n = 3 per quality cell, with one human judge.
  - It says nothing about video, long projects or live research. Those need their own benchmark entries before any container is reconsidered for them.

## Next steps (each separately authorized)

1. The owner reviews and accepts this ADR (D2–D7) in its pull request.
2. Public-exposure redaction candidate (D4).
3. Project Brain skeleton (D5.1).
4. Housekeeping M0-11, M0-12 and M0-13.
5. Next benchmark entry, when D1.4 triggers.
