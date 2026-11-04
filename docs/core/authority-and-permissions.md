# Authority and permissions

**Sources:** ADR-0006 D3, D5, D6, D7, D8; decisions `tool-levels`, `user-journey`, `check.C2`; ADR-0004 I3, I4 and two-level idempotency (kept by ADR-0005 D2); ADR-0002; V2.5 EC §3 (approval contract), §4 (budget ledger), `AUTONOMY_ENVELOPE`, §26; ARCH §2 (authority order), §5.1.2, §16.1; Route Recipe Spec §4 (secret boundary); the Video Director contract ("Approval points the contract produces").

This file defines who may approve, how an approval is recorded, and the limits inside which agents act on their own. It restates ADR-0006 D6 only where needed; the ADR is the authority.

## Who holds authority

- **The user.** For an agency, the agency user and, where the user designates one, the **end client's approver**. The designation is itself an approval record.
- **Recorded decisions.** Approved facts, canon, brand rules and scopes bind until superseded.
- **Never an agent.** Leads coordinate; owners propose. No agent grants, holds or passes on a permission (ADR-0006 D3; ADR-0004 I3 `permissions_carried: NONE`).

Order when sources disagree (ARCH §2, summarized): law, safety and platform rules; the user's explicit governance; approved project authorities and canon; the current task's request; packs; generic defaults. A casual request inside a task does not change governance.

## Approval kinds

| Kind | Approves | Example |
|---|---|---|
| `direction` | A creative or strategic direction version | Concept 2, creative direction v3 |
| `execution_scope` | An execution scope version, with its spend limit | 12 frames, 3 attempts each, limit 40 USD |
| `authority_change` | A new version of a fact, canon entity or brand rule | Character costume v2 becomes canon |
| `outward_action` | One publication, send, listing, ad launch or contact | Publish the landing page |
| `standing_permission` | A named outward action the user pre-approves, with limits | Post weekly to one channel |
| `budget` | A project or operating budget | Operating budget for this project |
| `designation` | An approver for an end client | The client's marketing lead approves directions |

## Approval record

```yaml
approval:
  approval_id:      # required
  kind:             # required (table above)
  subject_ref:      # required: the exact record and version approved
  scope:            # required: what the approval covers, and what it does not
  approved_by:      # required: the person, by role
  authority_ref:    # required: evidence of the person's act (their message ref, a signed form, a PR merge for this repository)
  granted_at:       # required
  expires_at:       # optional
  conditions: []    # optional
  supersedes:       # optional: earlier approval it replaces
```

Rules:
1. **A1 · Exact version.** An approval binds to the exact version it names. Any change makes a new version needing a new approval, except changes the approved fields already allow (Video Director change table).
2. **A2 · Evidence or nothing.** An approval exists only with `authority_ref` to a verifiable act of the person. An agent may acknowledge an approval it was told about, says once that it must be recorded, and never records one itself.
3. **A3 · Approval is not acceptance.** Approving a direction does not authorize generation; approving a scope does not publish; passing review does not approve (ARCH V2.4 addendum).
4. **A4 · Noting is not recording.** After an approval, an agent may note it in its own deliverable document without asking (decision `check.C2`); that note is not the approval record, and images, video, paid tools, publication and contact still need a request.

## Permission levels

The levels, read, spend, act outward and credentials, are defined by ADR-0006 D6 and decision `tool-levels`. Per project they are expressed as an **autonomy envelope** (EC `AUTONOMY_ENVELOPE`), one entry per action class:

```yaml
autonomy_envelope:
  revision:
  action_classes:
    <action_class>:          # e.g. read.web, spend.media_generation, spend.research_data, act.publish
      disposition:           # AUTO_ALLOWED | ASK_BEFORE | FORBIDDEN_OR_OUTSIDE_AUTHORITY
      scope:                 # where it applies
      budget_or_limit:
      source_authority:      # the approval that set it
```

A standing permission is an `AUTO_ALLOWED` entry whose `source_authority` is a `standing_permission` approval; it is re-checked on every effect and never carried by delegation. Having a tool connected changes nothing (ARCH §5.1.2).

## Execution scope

The envelope for an operation that spends or acts, generalized from the Video Director's `proposed_execution_scope` beyond media:

```yaml
execution_scope:
  scope_id:            # required
  version:             # required
  status:              # lifecycle (project-context.md): proposed until a recorded approval
  approval_ref:        # set only by an approval record
  owner_role:          # required: who proposed it
  executor_roles: []   # required: who may run it
  permitted_operations: []   # required
  deliverables: []     # required
  preserve: []         # what must stay fixed
  vary: []             # each with its range; an entry without a range counts as preserve
  open: []             # left to the agents' choice
  quantities:          # items per deliverable
  attempts_per_item:
  tool_classes: []     # kinds of route, never a single vendor as authority
  spend_limit:         # from the user's budget; agents never set it
  quote_ref:           # dated quote; required before approval when money is spent
  schedule:            # optional: for scheduled or recurring work (when, how often)
  stop_condition:      # required for recurring or event-driven work
  max_delegation_depth: 2   # optional; the default unless the scope says otherwise
  valid_until:         # required
```

It binds like EC §3 `BATCH_TEMPLATE`: the approved template plus what is preserved and varied, counts, attempts, tool classes and spend limit. **Money left in a budget never authorizes anything outside the scope.** Each paid attempt is attributable; a partial batch is never blindly resubmitted; an `UNKNOWN` result is reconciled first (EC §4, §6, §9).

## Budgets

| Budget | Covers | Approved by |
|---|---|---|
| **Project budget** | Spend on tools for the project's deliverables: generation, paid data, ad spend | The user, per project |
| **Project operating budget** (*new here*) | The agents' own work on the project: model usage, delegation, tool calls | The user, per project |
| **System operating budget** | Shared scheduled work outside any project: learning, knowledge refresh (ADR-0006 D5) | The owner |

Rules: **B1** a budget bounds consumption and authorizes no operation; **B2** available = authorized − confirmed − open reservations (EC §4); **B3** cost is estimated before and reported after; usage appears in the status view; **B4** a project budget is never used for system work, nor the reverse; **B5** when an operating budget is exhausted, work waits for the user.

*New here:* the project operating budget. Agent model usage costs money even when nothing is generated, and no existing decision says who pays for it.

## Continuous and scheduled work

1. Scheduled work defaults to read-level research and reminders. Any other scheduled effect needs an execution scope that names it, with `schedule`, `stop_condition` and `valid_until` (ADR-0006 D6).
2. Every effect re-checks the current authority; a scope that expired, was superseded or whose dependencies were invalidated no longer applies.
3. An outward action that may have run is never repeated blindly (ADR-0004 two-level idempotency).
4. Recurring work without a goal, a budget and a stop condition is not authorized, whatever its cost.

## Credentials

Never in the repository or the project context. Records hold only a secret locator (Route Recipe Spec §4), resolved by the host or the user's own secret store. Choosing that store is a step-2 decision.
