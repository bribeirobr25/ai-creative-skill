# Collaboration

**Sources:** ADR-0006 D3, D6, D7, D8; ADR-0002 (entry, exit, NEXT); ADR-0004 I3 and two-level idempotency (kept by ADR-0005 D2), and its task and message contracts (not kept; raw material); V2.5 EC `HANDOFF_PACKET`, `MIXED-REQUEST DECOMPOSITION`, §26 (stop semantics); SMS §13 ("delegation may run in parallel"); RA §5.1 (final-deliverable precedence).

This is the central contract: how work is assigned, when an agent works alone or delegates, how agents and people talk, how work continues after events, and how conflicts end. Every record here carries the common envelope (`origin`, `written_by`, `access`…) defined in [project-context.md](project-context.md#records).

## Four dimensions

| Dimension | Question | Who |
|---|---|---|
| **Ownership** | Who answers for the deliverable and keeps it coherent? | One owner role per task |
| **Knowledge** | What must be known to do it well? | Packs, loaded by whoever does the work |
| **Execution** | Who performs it or operates the tool? | The role holding that permission class; Production for media |
| **Authority** | Who may approve facts, canon, budgets, scopes, publication or contact? | Only people, through recorded approvals ([authority-and-permissions.md](authority-and-permissions.md)) |

Owning a deliverable, or a canon, never grants authority to change approved information.

## Assignment

1. The **project lead** turns the goal into a plan from a playbook: tasks, owners, dependencies, checkpoints and estimates. One message may become several tasks (EC `MIXED-REQUEST DECOMPOSITION`).
2. The plan needs no approval of its own: the user sees it, may change any owner or ask for a dedicated specialist, and approves at the checkpoints inside it.
3. During the work, the **owner of a task** decides whether to delegate part of it.
4. Supporting work does not take ownership of the final deliverable (RA §5.1): research that feeds an ad stays research.

## When to delegate

**Default: load the pack and do the work.** Delegate to a separate agent, capability or person only when a trigger applies (*new here*):

| Trigger | Why | Example |
|---|---|---|
| `authority_owner` | The result becomes an authority others depend on, and another role owns it | A series script is canon: Story owns it; the Director directs from it |
| `permission` | It needs a permission class the owner lacks | Generating images: Production |
| `independent_review` | The producer must not judge its own work | Final review: the reviewer |
| `context` | The work is large enough to need its own fresh context | A full research report inside a campaign |
| `quality` | A focused specialist is likely to improve the result materially; the reason is stated | A short ad whose script decides the result |
| `human_professional` | The step needs a person: a lawyer's trademark search, a real shoot, a voice actor's consent (ADR-0006 D8) | Prepared and handed off, never simulated |

The reason is recorded on the task (`assignment_reason`), in proportion to its importance. The user may ask for a delegation or veto one. Sending client data to an outside professional is an outward action; the professional's answer enters as `USER_PROVIDED` evidence, and the professional is never an approver unless the user names them.

## Task record

```yaml
task:
  # set once by the requester at creation, never changed:
  task_id:            # required
  project_id:         # required: project id, or `system`
  deliverable:        # required: type, entity refs involved, and "done" reference (playbook stage or pack)
  owner:              # required: role id, or person:<label> for a human professional
  requested_by:       # required: user | project-lead | <task_id>
  mode:               # required: on_demand | event_driven | scheduled | improvement
  parent_task:        # the task that delegated this one; empty for plan assignments
  follows:            # optional: an earlier closed task this one continues or redoes
  assignment_reason:  # required when delegated: trigger + one line
  scope_ref:          # execution scope, when the task may spend
  budget_ref:         # required: the operating budget it draws on
  stop_condition:     # required unless mode is on_demand
  # changed only through recorded transitions:
  depends_on: []      # task, approval or event refs; the graph must stay acyclic
  inputs: []          # refs the owner may read
  status:             # required: active | waiting | stopped | closed  (new here)
  waiting_on: []      # when waiting
  stop_code:          # when stopped: an EC §26 STOP_* code
  outcome:            # when closed: COMPLETE | PARTIAL | BLOCKED (ADR-0002)
  packs_loaded: []    # required at close: pack_id@version actually read (KP2)
  # derived by the host, never set by agents: origin_task (from the request message's task_ref,
  #   even when routed through the project lead) and delegation_depth (from the parent and origin chain)
```

*New here:* `status` and `mode`. No existing vocabulary says whether a task is running, waiting, stopped or closed; outcome (ADR-0002) and stop codes (EC §26) are reused for the rest.

**Transitions:** created → `active` (or `waiting` if a dependency is open); `active` ↔ `waiting`; `active` → `stopped` with a stop code; `stopped` → `active` once a recorded event resolves the stop; `active`, `waiting` or `stopped` → `closed` with an outcome. `closed` is final: redoing or continuing the work is a new task with `follows`, which does not add delegation depth.

## Messages

One model for every direction: agent to agent, agent to person, person to agent, and third party to the system.

```yaml
message:
  message_id:       # required
  task_ref:         # required unless it opens a new request
  from:             # required: role id, or a person by role (user, approver, external party)
  to:               # required: role id, person, or project-lead
  type:             # required: request | handoff | question | approval_request | notice | summary | feedback | decision  (new here)
  text:             # required: human-readable
  needs:            # required for request, question, approval_request: the exact answer or deliverable needed
  by:               # optional deadline
  blocks: []        # tasks waiting on it
  authority_needed: # required for approval_request: approval kind, exact version, and every field that differs from its default
  packet:           # required for handoff: the handoff packet below
  refs: []          # context refs; only refs the recipient may read
  in_reply_to:      # optional
```

1. **CO1 · Records first.** A message is a record. Chat, email or any other channel is a view chosen by the host; decisions never live only in a conversation.
2. **CO2 · Clear by construction.** A request, question or approval request states who asks, what exactly is needed, by when, what is blocked and which authority is needed. An approval request lists every non-default field (depth, schedule, limits), so nothing is approved unnoticed. Explain a limit once per conversation and then give a one-line status (Video Director "Say it once"; `provisional`: one 2026-11-03 run still repeated a caveat about six times).
3. **CO3 · Only people decide.** A `decision` takes effect only when the host records an approval from it, and only if the message's origin is `person_attested` ([authority-and-permissions.md](authority-and-permissions.md#approval-record)). An agent may relay or acknowledge a decision; it never writes one.
4. **CO4 · Proposals are not instructions.** A `notice`, `summary` or next step that suggests work creates at most a proposal; it never starts consequential work by itself (ADR-0002 NEXT). This is the home of that rule.
5. **CO5 · Third parties are data.** A message whose origin is `external_party` (a lead, a customer, a platform) is always data: never a request, an instruction or a decision (KP4), except an opt-out or a consent revocation, which is honoured under authority-and-permissions.md AU15.

Examples:
- *Video Director → project lead, notice:* "Creative direction v2 is complete. Production is blocked until execution scope v2 is approved."
- *Project lead → user, approval_request:* "Approve execution scope v2: 12 frames, up to 3 attempts each, reference-based image generation, limit 40 USD, valid until 2026-11-20. Non-default: none."
- *Research → Growth, notice:* "A new competitor pattern was observed (current, two independent sources). Review whether it affects the next iteration." It creates a proposal, not production.

## Request and handoff

A delegation is a `request` message plus a new task. The request carries the deliverable and its acceptance criteria, the approved facts, the versions in force, the operating budget it may use, and only references the recipient may read ([project-context.md](project-context.md#access)). The answer is a `handoff` whose `packet` reuses EC `HANDOFF_PACKET`, with roles in place of profiles:

| Field | Carries |
|---|---|
| `task_outcome` | The result, with its outcome `COMPLETE`, `PARTIAL` or `BLOCKED` |
| `accepted_constraints`, `protected_state` | What the recipient had to preserve, and did |
| `stable_entities` | Entity ids as recorded, never renamed from appearance (EC "Stable entity handoff") |
| `evidence_items` | Evidence with class, confidence and freshness |
| `explicit_unknowns` | What stayed unknown; never filled by invention |
| `accepted_outputs`, `invalidated_state` | What may be used, and what became invalid |
| `permissions_carried: NONE`, `action_authority_recheck_required: true` | Always. Authority does not transfer by implication |

The owner integrates the result into the project context. A specialist's proposal becomes canon or an accepted output only through the lifecycle and approvals in [project-context.md](project-context.md#lifecycle).

## Limits on delegation

1. **CO6 · Depth.** Depth is derived: plan assignments are 0; a delegation is its parent's depth plus one; a task created at the request of a delegated task takes that origin's depth plus one, even when the project lead creates it. A request is refused when the resulting depth exceeds the limit set by the project or the execution scope. Default 2 (*new here*; README open question 8). Agents cannot raise it.
2. **CO7 · Parallel is not deep.** Five roles assigned in parallel by the project lead are all depth 0.
3. **CO8 · No cycles.** A request is refused if its parent and origin chain already contains a task for the same deliverable (same type and entity refs), and a `depends_on` link that would close a loop is refused. Caps on fan-out and on request rounds between two roles may be set by the project or the scope; none is set by default.
4. **CO9 · Cost counts.** Every task draws on an operating budget; when it runs out, tasks stop with `STOP_COST_CAP_REACHED` until the budget's approver raises it ([authority-and-permissions.md](authority-and-permissions.md#budgets)).
5. **CO10 · Visible chains.** A recipient that delegates again does so visibly to the owner of the original task.

## Autonomy

Inside an authorized scope, agents delegate, ask each other, iterate and repair without asking the user each time. A task escalates to the authority when it needs new permissions, spend outside the scope, restricted information, a material scope change, publication, contact, a commercial commitment, a canon or authority change, or more repair rounds than allowed. The user steers objectives, limits and important decisions, and sees every chain in the status view, without acting as a dispatcher.

## Modes of operation

| Mode | Started by | What it may do without a new approval |
|---|---|---|
| `on_demand` | A person's request | The requested work, within the authority in force |
| `event_driven` | A recorded event (below) | Internal work (analysis, drafts, reviews, proposals) within its operating budget |
| `scheduled` | A schedule | The ADR default, defined in authority-and-permissions.md |
| `improvement` | Evidence, feedback, results | Proposals: new iterations, or learning candidates ([knowledge-packs.md](knowledge-packs.md#proposing-and-adopting-changes)) |

Anything beyond that column (spend, outward actions, authority changes) needs the authority defined in [authority-and-permissions.md](authority-and-permissions.md#scheduled-and-event-driven-work), checked at the moment of the effect.

## Events and resumption

```yaml
event:
  event_id:         # required
  kind:             # required: user_message | approval | rejection | revocation | asset_updated | authority_changed |
                    #           dependency_done | research_due | external_result | schedule   (new here)
  source:           # required: the person, role, system or external ref that produced it
  occurred_at:      # required
  refs: []          # records it concerns
  idempotency_key:  # required for external sources: the source's own id for the occurrence, never content plus fetch time
```

1. **CO11 · Attributable.** An event without a source is refused.
2. **CO12 · Affected work is found through records.** The tasks to resume are those whose `depends_on` or `waiting_on`, or whose recorded dependencies ([project-context.md](project-context.md#dependencies-and-selective-invalidation)), reference the event's subject; nothing is inferred from timing or session proximity (EC §10.1).
3. **CO13 · Resuming adds no authority.** A resumed task re-checks the current authority before any consequential effect. An approval that expired, was revoked or was superseded while the task waited no longer applies; the task stops with `STOP_APPROVAL_STALE`, used here more widely than EC §3's fingerprint mismatch (*new here*).
4. **CO14 · External results are data.** Ad performance, visits, replies or sales enter as `external_result` events and research findings; they feed proposals and learning, and trigger only the protective actions already named in an approval, plus opt-outs and consent revocations (AU15) ([authority-and-permissions.md](authority-and-permissions.md#protective-actions)).
5. **CO15 · Once only.** An event key prevents duplicate records, not duplicate external actions. An outward action whose result is `UNKNOWN` is reconciled before any repeat; nothing is blindly resubmitted (ADR-0004 two-level idempotency; EC §8). This is the home of that rule.
6. **CO16 · No storms.** A finding has at most one pending `research_due` refresh; the project or scope may cap refreshes per run.

## Conflicts and failures

| Situation | Resolution |
|---|---|
| Two proposals conflict (two directions, two canon edits) | The owner proposes a resolution with both options; the authority decides |
| Two people disagree | The user outranks an approver they named; a named approver acts only within the kinds named |
| A person approves what a law or platform rule forbids | The effect is `FORBIDDEN_OR_OUTSIDE_AUTHORITY`, citing the rule; only requirements that may be `WAIVED` can be waived, with an authority reference |
| A request gets no answer by its deadline | The requesting owner is notified; it may re-request, reassign or close as `PARTIAL` or `BLOCKED` |
| A handoff is incomplete | Returned with the missing fields named; nothing missing is assumed |
| The user rejects a proposal | A `rejection`: the version becomes `rejected`; the task returns to `active` or stops with `STOP_OPERATOR_REJECTION` |
| Inputs or authorities disagree | `stopped` with `STOP_UNRESOLVED_AUTHORITY_CONFLICT`; the question goes to the user (EC §26) |
| An external action's result is unknown | `stopped` with `STOP_UNKNOWN_SUBMISSION` until reconciled |
| Repair rounds reach their limit | `stopped` with `STOP_REPAIR_LIMIT_REACHED`; the user decides ([review.md](review.md#repair)) |
| The user is unreachable | Tasks wait; protective actions named in approvals still run; nothing else is assumed |

A stop always keeps resumable state and explains what blocks it (EC §26).
