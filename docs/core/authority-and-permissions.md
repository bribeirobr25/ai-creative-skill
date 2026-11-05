# Authority and permissions

**Sources:** ADR-0006 D3, D4, D5, D6, D7, D8; decisions `tool-levels`, `user-journey`, `business-scope`, `check.C2`; ADR-0002; ADR-0004 I3, I4 and two-level idempotency (kept by ADR-0005 D2); V2.5 EC §3 (approval contract), §4 (budget ledger), §8, §9, `AUTONOMY_ENVELOPE`, §26; ARCH §2 (authority order), §5.1.2, §16.1; Route Recipe Spec §4 (secret boundary); the Video Director contract ("Approval points the contract produces").

Who may approve, how an approval is recorded, and the limits inside which agents act on their own. ADR-0006 D6 and decision `tool-levels` are the authority for the permission levels; this file cites them and adds only what records need.

## Who holds authority

- **The user.** For an agency, the agency user. The user may **name an approver** (for example the end client's marketing lead) for stated approval kinds on one tenant (*new here*; settled by the system owner, see README). A naming is itself an approval of kind `designation`, evidenced by the user's own `person_attested` message naming the person, the tenant, the kinds and `expires_at`. It may cover `direction`, `authority_change` and `outward_action` only: never `designation`, `budget`, `execution_scope` or `standing_permission`, which stay with the user (decisions `agent-teams`, `tool-levels`). The user always outranks the approver they named.
- **Recorded decisions.** Approved facts, canon, brand rules and scopes bind until superseded or revoked.
- **Never an agent.** Leads coordinate; owners propose. No agent grants, holds or passes on a permission (ADR-0006 D3; ADR-0004 I3 `permissions_carried: NONE`).

When sources disagree (ARCH §2, summarized): law, safety and platform rules; the user's explicit governance; approved project authorities and canon; packs; external methods, third-party skills and provider defaults last. A casual request inside a task does not change governance ("casual task request ≠ operator governance change", ARCH §2). An approval cannot authorize what a higher source forbids ([collaboration.md](collaboration.md#conflicts-and-failures)).

## Approval record

| Kind (*new here*) | Approves | Example |
|---|---|---|
| `direction` | A creative or strategic direction version | Concept 2, creative direction v3 |
| `execution_scope` | An execution scope version, with its spend limit | 12 frames, 3 attempts each, limit 40 USD |
| `authority_change` | A new version of a fact, canon entity, brand rule, or a pack's core item or rule | Character costume v2 becomes canon |
| `outward_action` | One publication, send, listing, ad launch or contact | Publish the landing page |
| `standing_permission` | A named outward action other than publication that the user pre-approves, with limits and holders | Reply to booking inquiries with the approved template |
| `budget` | A project budget or the system operating budget | Tool spend for this project |
| `designation` | An approver for stated kinds on one tenant | The client's marketing lead approves directions |

```yaml
approval:                 # plus the record envelope (project-context.md#records)
  kind:                   # required (table above)
  decision:               # required: approve | reject | revoke  (new here)
  subject_ref:            # required: the exact record and version decided on
  covers:                 # required: what the approval covers and what it does not
  decided_by:             # required: the person, by role
  designation_ref:        # required when decided_by is not the user
  authority_ref:          # required: the person_attested record of their act (a message, a signed form)
  expires_at:             # required for outward_action, standing_permission and designation
  canon_promotion:        # authority_change only, when a choice is promoted to canon: CAL §6.1 canon_promotion_ref fields
  conditions: []          # optional, e.g. protective actions
  consumed_by:            # outward_action only: the action record that used it (once only)
  supersedes:             # optional
```

1. **AU1 · Exact version.** An approval binds to the exact version it names. A change makes a new version that needs a new approval, except changes the approved fields already allow (Video Director change table).
2. **AU2 · Attested or nothing.** An approval exists only when the host records it from a `person_attested` act named in `authority_ref`. An agent may relay or acknowledge an approval, says once that it must be recorded, and never writes one. Whether the host can prove that a person, not an agent using the person's identity, made the act is open (finding `FND-AUDIT2-AGENT-IDENTITY`). For this repository, the system owner's PR merge stays the authority for decisions (brain/CONTRACT.md).
3. **AU3 · Tenant-bound.** An approval is valid only for its own tenant and, when `decided_by` is a named approver, only while that designation is in force and covers the kind.
4. **AU4 · Approval is not acceptance.** Approving a direction does not authorize generation; approving a scope does not publish; passing review does not approve (ARCH V2.4 addendum).
5. **AU5 · Once only.** An `outward_action` approval is consumed by the one action it authorized. A revoke takes effect at once for every task (collaboration.md CO13).
6. **AU6 · Noting is not recording.** After an approval, an agent may note it in its own deliverable document without asking (decision `check.C2`); that note is not the approval record, and images, video, paid tools, publication and contact still need a request.

## Permission levels and the autonomy envelope

The levels (read, spend, act outward, credentials) are those of ADR-0006 D6. Per project they are expressed as an autonomy envelope (EC `AUTONOMY_ENVELOPE`), one entry per action class:

```yaml
autonomy_envelope:
  action_classes:
    <action_class>:          # e.g. read.web, spend.media_generation, spend.research_data, act.publish
      disposition:           # required: AUTO_ALLOWED | ASK_BEFORE | FORBIDDEN_OR_OUTSIDE_AUTHORITY
      holder_roles: []       # required: the roles that may use it (new here)
      scope:                 # required: where it applies
      budget_or_limit:       # optional
      source_authority:      # required: the approval that set it
      revision:              # required
```

A standing permission is an `AUTO_ALLOWED` entry whose `source_authority` is a `standing_permission` approval: usable only by its `holder_roles`, re-checked on every effect, never carried by delegation. A connected tool changes nothing (ARCH §5.1.2).

## Execution scope

The envelope for **spending**, generalized from the Video Director's `proposed_execution_scope` beyond media. Outward actions need an `outward_action` approval or a standing permission; a scope never authorizes them.

```yaml
execution_scope:       # plus the record envelope
  version:             # required
  owner_role:          # required: who proposed it
  executor_roles: []   # optional; default production for media generation
  budget_ref:          # required: the budget its spend draws on
  permitted_operations: []   # required
  deliverables: []     # required
  preserve: []         # required: what must stay fixed
  vary: []             # each with its range; an entry without a range counts as preserve
  open: []             # left to the agents' choice
  quantities:          # required
  attempts_per_item:   # required
  tool_classes: []     # required: kinds of route, never a single vendor as authority
  spend_limit:         # required: the amount the user states; agents ask for it and never invent it
  quote_ref:           # required before approval is requested
  schedule:            # optional: for scheduled spending (when, how often)
  stop_condition:      # required with a schedule or a trigger
  triggers: []         # optional: event kinds that may start spending under this scope
  max_delegation_depth:  # optional; default 2
  valid_until:         # required
  # derived on read, never stored: lifecycle state, approval
```

It binds like EC §3 `BATCH_TEMPLATE`: the approved template plus what is preserved and varied, counts, attempts, tool classes and spend limit. **Money left in a budget never authorizes anything outside the scope** (decision `tool-levels`).

1. **AU7 · No confused deputy.** An executor runs a package only if the requesting task references the scope, the package's deliverable is listed in it, and its inputs are the approved versions it depends on.
2. **AU8 · Attributable spend.** Each paid attempt is an EC §9 attempt record; cost is estimated before and reported after (decision `tool-levels`). Repeats follow collaboration.md CO15.

## Budgets

```yaml
budget:                # plus the record envelope
  class:               # required: project | system_operating
  currency:            # required
  authorized:          # required: from its budget approval
  approval_ref:        # required
  ledger_ref:          # required: EC §4 ledger (confirmed, reserved)
  valid_until:
```

| Class | Covers | Approved by |
|---|---|---|
| `project` (*new here* as a record; README open question 5) | Spend on tools for the project's deliverables: generation, paid data, ad spend | The user |
| `system_operating` | One monthly budget for the agents' own work on every project (model usage, delegation, tool calls) and for shared scheduled work outside any project: learning, knowledge refresh (ADR-0006 D5). There is no per-project operating budget (settled by the system owner) | The system owner |

1. **AU9** A budget bounds consumption and authorizes no operation.
2. **AU10** Available = authorized − confirmed − open reservations (EC §4). An ad launch needs both an `outward_action` approval and an execution scope for its spend; spend the platform makes after launch is reserved in full when the scope is approved, and bounded by a platform-side cap stated in it.
3. **AU11** Tool spend for a project's deliverables draws only on that project's budget; the agents' own work draws only on the operating budget.
4. **AU12** When a budget runs out, the tasks drawing on it stop with `STOP_COST_CAP_REACHED` until its approver raises it.

## Scheduled and event-driven work

This is the home of the rule. The default, from ADR-0006's header on ADR-0002: scheduled work is read-level research and reminders. Event-driven work may do internal work and proposals (collaboration.md "Modes of operation"). D6 authority extends either one only in these ways:
- **Spend** on a schedule or a trigger: only under an approved execution scope that names the `schedule` or `triggers`, with a `stop_condition` and `valid_until`.
- **Outward actions** on a schedule or a trigger: only under a standing permission that names the action. A standing permission never covers publication: every publication, recurring or not, needs its own `outward_action` approval, which keeps the "no auto-publishing" limit (decision `business-scope`; settled by the system owner).
- Every effect re-checks the current authority; work without a goal, a budget and a stop condition is not authorized, whatever its cost.

## Protective actions

Pausing an ad, stopping a campaign, suppressing a contact who opted out, cancelling queued sends and taking down content whose consent was revoked reduce exposure (*new here*).
1. **AU13** Every approval of an ongoing outward action (an ad launch, an outreach sequence, a standing permission) names its protective actions and their conditions in `conditions`, such as kill rules on results. Scaling up is never protective and needs its own cap in the approval.
2. **AU14** Named protective actions run without a new approval, even when a budget is exhausted or the user is unreachable, and are reported at once.
3. **AU15** Honouring an opt-out or a consent revocation is always part of the approved action itself (ADR-0006 D8), named or not.

## Required elements at every outward action

Before any outward effect, including one under a standing permission, the action is checked at the moment of the effect for: rights for every asset, a mark check for any new logo or name, consent for any real likeness or voice, accessibility (WCAG for websites, captions for videos, alt text for images), AI-disclosure rules, the platform's ad or listing policies, and outreach consent and anti-spam law in the recipient's country (ADR-0006 D8; decision `rights-and-trust`). Outward content commits only terms from an approved offer version (roles.md RO1).

## Credentials

Never in the repository or the project context. Records hold only a secret locator (Route Recipe Spec §4), resolved by the host or the user's own secret store. Choosing that store is a step-2 decision.
