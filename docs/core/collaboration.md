# Collaboration

**Sources:** ADR-0006 D3, D6, D7; ADR-0002 (entry, exit, NEXT); ADR-0004 task and message contracts and I3 (kept by ADR-0005 D2); V2.5 EC `HANDOFF_PACKET`, `PROFILE_SWITCH_EVENT`, `MIXED-REQUEST DECOMPOSITION`, §26 (stop semantics); SMS §13 ("delegation may run in parallel"); RA §5.1 (final-deliverable precedence).

This is the central contract: how work is assigned, when an agent works alone or delegates, how agents and people talk, how work continues after events, and how conflicts end.

## Four dimensions

Every piece of work separates four things that are easy to confuse:

| Dimension | Question | Who |
|---|---|---|
| **Ownership** | Who answers for the deliverable and keeps it coherent? | One owner role per task |
| **Knowledge** | What must be known to do it well? | Packs, loaded by whoever does the work |
| **Execution** | Who performs it or operates the tool? | The role holding that permission class; Production for media |
| **Authority** | Who may approve facts, canon, budgets, scopes, publication or contact? | Only the user or a designated approver, through recorded approvals |

Owning a deliverable, or a canon, never grants authority to change approved information ([authority-and-permissions.md](authority-and-permissions.md)).

## Assignment

1. The **project lead** turns the goal into a plan from a playbook: tasks, owners, dependencies, checkpoints and estimates. One message may become several tasks; dependencies are explicit (EC `MIXED-REQUEST DECOMPOSITION`).
2. The plan's owners are proposals until the user sees the plan; the user can change any owner or ask for a dedicated specialist.
3. During the work, the **owner of a task** decides whether to delegate part of it.
4. Supporting work does not take ownership of the final deliverable (RA §5.1): research that feeds an ad stays research.

## When to delegate

**Default: load the pack and do the work.** Delegate to a separate agent or capability only when at least one trigger applies:

| Trigger | Why | Example |
|---|---|---|
| `authority_owner` | The result becomes an authority others depend on, and another role owns it | A series script is canon: Story owns it; the Director directs from it |
| `permission` | It needs a permission class the owner lacks | Generating images: Production |
| `independent_review` | The producer must not judge its own work | Final review: the reviewer |
| `context` | The work is large enough to need its own fresh context | A full research report inside a campaign |
| `quality` | A focused specialist is likely to improve the result materially; the reason is stated | A short ad whose script decides the result |

The reason is recorded on the task (`assignment_reason`), in proportion to its importance. The user may ask for a delegation or veto one.

## Task record

```yaml
task:
  task_id:            # required, stable
  project_id:         # required
  deliverable:        # required: type + "done" reference (playbook stage or pack)
  owner_role:         # required
  requested_by:       # required: user | project-lead | <task_id>
  assignment_reason:  # required when delegated: trigger + one line
  parent_task:        # optional: the task that delegated this one
  delegation_depth:   # required: 0 for plan assignments, parent + 1 for delegations
  depends_on: []      # task, approval or event refs
  inputs: []          # refs into the project context the owner may read
  packs_loaded: []    # required at close: pack_id@version actually read (knowledge-packs.md K2)
  scope_ref:          # execution scope, when the task may spend or act
  budget_ref:         # operating budget it draws on
  stop_condition:     # required for continuous or event-driven tasks
  status:             # active | waiting | stopped | closed  (new here, see below)
  waiting_on: []      # when waiting: approval, message or event refs
  stop_code:          # when stopped: an EC §26 STOP_* code
  outcome:            # when closed: COMPLETE | PARTIAL | BLOCKED (ADR-0002)
  revision:           # required, increases on every change (EC §2.3: no last-write-wins)
```

*New here:* `status`. No existing vocabulary describes whether a task is running, waiting, stopped or closed; outcome (ADR-0002) and stop codes (EC §26) are reused for the rest. "Paused" is `waiting` with a reason; "resumed" is an event moving a task back to `active`.

## Messages

One model for every direction: agent to agent, agent to person, person to agent.

```yaml
message:
  message_id:       # required
  project_id:       # required
  task_ref:         # required unless it opens a new request
  from:             # required: role id or person (by role, e.g. user, approver)
  to:               # required: role id, person, or project-lead
  type:             # required: request | handoff | question | approval_request | notice | summary | feedback | decision
  text:             # required: human-readable, what is needed and why
  needs:            # required for request, question, approval_request: the exact answer or deliverable needed
  by:               # optional deadline
  blocks: []        # tasks waiting on it
  authority_needed: # for approval_request: approval kind and the exact version to approve
  refs: []          # context refs; only refs the recipient may read
  in_reply_to:      # optional
  created_at:       # required
```

Rules:
1. **C1 · Records first.** A message is a record. Chat, email or any other channel is a view of these records, chosen by the host; decisions never live only in a conversation.
2. **C2 · Clear by construction.** Every request, question or approval request states who is asking, what exactly is needed, by when, what is blocked and which authority is needed. Explain a limit once per conversation; afterwards a one-line status is enough (Video Director "Say it once").
3. **C3 · Only people decide.** A message of type `decision` comes only from a person with the authority. It takes effect when recorded as an approval ([authority-and-permissions.md](authority-and-permissions.md#approval-record)); an agent may acknowledge it but never records its own approval.
4. **C4 · Proposals are not instructions.** A `notice` or `summary` that suggests work creates at most a proposal; it never starts consequential work by itself.

Examples:
- *Video Director → project lead, notice:* "Creative direction v2 is complete. Production is blocked until execution scope v2 is approved."
- *Project lead → user, approval_request:* "Approve execution scope v2 (12 frames, up to 3 attempts each, reference-based image generation, limit 40 USD, valid until 2026-11-20)?"
- *Research → Growth, notice:* "A new competitor pattern was observed (current, two sources). Review whether it affects the next iteration." It creates a proposal, not production.

## Request and handoff

A delegation is a `request` message plus a task record. The answer is a `handoff`, which reuses EC `HANDOFF_PACKET` with roles in place of profiles:

| Field | Carries |
|---|---|
| `task_outcome` | The result, with its outcome `COMPLETE`, `PARTIAL` or `BLOCKED` |
| `accepted_constraints`, `protected_state` | What the recipient had to preserve, and did |
| `stable_entities` | Entity ids as recorded, never renamed from appearance (EC "Stable entity handoff") |
| `evidence_items` | Evidence with class, confidence and freshness |
| `explicit_unknowns` | What stayed unknown; never filled by invention |
| `accepted_outputs`, `invalidated_state` | What may be used, and what became invalid |
| `permissions_carried: NONE`, `action_authority_recheck_required: true` | Always. Authority does not transfer by implication |

A request also carries: the deliverable and its acceptance criteria, the approved facts, the versions in force, the share of the operating budget it may use, and its `delegation_depth`. It carries only references the recipient may read ([project-context.md](project-context.md#access)).

The owner integrates the result into the project context. A proposal from a specialist becomes canon or an accepted output only through the lifecycle and approvals in [project-context.md](project-context.md#lifecycle).

## Limits on delegation

1. **C5 · Depth.** A delegation from a delegated task increases `delegation_depth`. The default limit is **2**; the execution scope or the project may set another value. Agents cannot raise it themselves.
2. **C6 · Parallel is not deep.** Five roles assigned in parallel by the project lead are all depth 0. Depth counts only re-delegation chains.
3. **C7 · No cycles.** A request is refused if its chain of `parent_task` already contains a task for the same deliverable or the same recipient role on the same subject (ADR-0004 message contract: cycle containment).
4. **C8 · Cost counts.** Every delegation draws on an operating budget; when it is exhausted the task goes to `waiting` on the user.
5. **C9 · Visible chains.** A recipient that delegates again does so visibly to the owner of the original task.

## Autonomy

Inside an authorized scope, agents delegate, ask each other, iterate and repair without asking the user each time. A task escalates to the authority when it needs: new permissions, spend outside the scope, restricted information, a material scope change, publication, contact, a canon or authority change, or more repair rounds than allowed. The user steers objectives, limits and important decisions, and can see every chain in the status view, without acting as a dispatcher.

## Modes of operation

| Mode | Started by | Rule |
|---|---|---|
| **On demand** | A person's request | The default |
| **Event-driven** | A recorded event (below) | Resumes or proposes work. Consequential effects need an authority already in force |
| **Scheduled or proactive** | A schedule in an approved scope | Default read-level research and reminders; anything else only inside a scope that names it (ADR-0006 D6) |
| **Improvement** | Evidence, feedback, results | Produces proposals: new iterations for the project, or learning candidates for packs ([knowledge-packs.md](knowledge-packs.md#proposing-changes)). Never a rule by itself |

Every continuous or event-driven task has a `stop_condition` and a `budget_ref`. Work exists to advance a goal, not to keep agents busy.

## Events and resumption

```yaml
event:
  event_id:         # required
  project_id:       # required
  kind:             # required: user_message | approval | rejection | asset_updated | authority_changed |
                    #           dependency_done | research_due | external_result | schedule
  source:           # required: who or what produced it (person, role, system, external ref)
  occurred_at:      # required
  recorded_at:      # required
  refs: []          # records it concerns
  idempotency_key:  # required for external sources: the same occurrence is recorded once
```

Rules:
1. **C10 · Attributable.** Every event names its source; an event without one is recorded as `OBSERVED` data, not as an instruction.
2. **C11 · Affected work is found through records.** The tasks to resume are those whose `depends_on`, `waiting_on` or recorded dependencies reference the event's subject; nothing is inferred from timing or session proximity (EC §10.1).
3. **C12 · Resuming adds no authority.** A resumed task re-checks the current authority before any consequential effect. An approval that expired or was superseded while it waited no longer applies.
4. **C13 · External results are data.** Ad performance, visits, replies or sales enter as `external_result` events and research findings; they feed proposals and learning, never automatic spend or publication.
5. **C14 · Once only.** An event key prevents duplicate records, not duplicate external actions. An outward action whose result is `UNKNOWN` is reconciled before any repeat; nothing is blindly resubmitted (ADR-0004 two-level idempotency).

## Conflicts and failures

| Situation | Resolution |
|---|---|
| Two proposals conflict (two directions, two canon edits) | The owner proposes a resolution with both options; the authority decides |
| A request gets no answer by its deadline | The requesting owner is notified; it may re-request, reassign or mark the task `PARTIAL` or `BLOCKED` |
| A handoff is incomplete | Returned with the missing fields named; nothing missing is assumed |
| Inputs or authorities disagree | `stopped` with `STOP_UNRESOLVED_AUTHORITY_CONFLICT`; the question goes to the user (EC §26) |
| An external action's result is unknown | `stopped` with `STOP_UNKNOWN_SUBMISSION` until reconciled |
| Repair rounds reach their limit | `stopped` with `STOP_REPAIR_LIMIT_REACHED`; the user decides ([review.md](review.md)) |

A stop always keeps resumable state and explains what blocks it (EC §26).
