# Roles

**Sources:** V2.5 SMS §13 (Role Contract), §16 (Growth Rule); RA §5 ("ownership ≠ capability availability"); ADR-0004's Agent Role contract (not kept by ADR-0005; raw material); ADR-0006 D3, D6; the Video Director definition.

A role is a bounded responsibility, **not necessarily a permanent agent** (SMS §13). The same role can run in three forms:

| Form | What it is | When |
|---|---|---|
| `pack` | Knowledge another agent loads to do the work itself | The default |
| `agent` | A separately invoked agent with its own fresh context | When a delegation trigger applies ([collaboration.md](collaboration.md#when-to-delegate)) |
| `capability` | A shared service with routes and tools, used by many roles | Production; independent review |

A role becomes a standing agent only when it earns its place against a generalist doing the same job (ADR-0006 D3), measured as D9 decides. Until then every role is `unproven`.

## Role contract

```yaml
role:
  role_id:            # required, stable, e.g. video-director
  area:               # required: an area id, e.g. research, visual-brand, story, growth, sales, production, shared (not a closed list)
  version:            # required
  status: unproven    # required: unproven | earned | retired (only a system-owner decision changes it)
  purpose:            # required, one or two sentences
  receives: []        # required: inputs, by record type
  decides: []         # required: what it chooses on its own
  delivers: []        # required: deliverable types, each with its "done" (playbook or pack)
  may_not_decide: []  # required: what it must leave to others or to the authority (RO1)
  knowledge:          # required
    always: []        # pack ids always loaded
    on_demand: []     # pack ids loaded per task
  permissions:        # required, least privilege; may be empty
    - action_class:   # e.g. read.web, spend.media_generation, spend.research_data, act.publish
      level:          # read | spend | act_outward (ADR-0006 D6; credentials are not a role level)
  forms_allowed: []   # required: pack | agent | capability
  reads: []           # required: access classes it may read (project-context.md#access)
  extension: {}       # optional, see README "Extensions"
```

## Rules

1. **RO1 · No authority.** `decides` covers only choices inside existing authority. Approvals, budgets, canon and authority changes, publication, contact and **commercial commitments** (prices, discounts, refunds, contract terms beyond an approved offer version) are always in `may_not_decide` (ADR-0006 D3, D4).
2. **RO2 · Least privilege.** `permissions` lists only the action classes the job needs. A connected tool never widens them (ARCH §5.1.2). A research role cannot post; a script writer cannot spend.
3. **RO3 · Owning is not executing.** A role can own a deliverable whose media another role generates. Production owns media generation and its post-production; other areas use their own permitted tools (paid research data, ad budgets, commercial tools) under their own scopes.
4. **RO4 · Knowledge comes first from the model.** Packs add what the model cannot know or reliably skips (ADR-0006 D2); a role's definition never restates general craft.
5. **RO5 · New roles must be justified.** A new role, or splitting one into several agents, needs at least one SMS §16 reason: an existing role cannot express the needed depth, repeated failures show a distinct discipline, a medium has a different grammar, or calibration evidence justifies it.
6. **RO6 · One canonical definition.** Each role has one definition file; copies installed in a host are generated, not edited (frozen ledger §13.4).

## Shared roles every project uses

| Role | Purpose | Notes |
|---|---|---|
| `project-lead` | Turns the user's goal into a plan from a playbook, assigns owners, tracks dependencies and reads the status view | Coordinates; holds no authority. Owns no creative deliverable |
| `reviewer` | Independent review of finished deliverables | A capability: fresh context, read-only, no stake in the verdict ([review.md](review.md)) |
| `production` | Media generation and its post-production | A capability with routes, split by pipeline only when that proves worth it (Video Director README) |

## Example

The [Video Director v0.1](../agents/video-director-v0.1/definition.md) maps onto this contract without changes to its design: it `receives` its request contract, `delivers` a direction package and a *proposed* execution scope, `may_not_decide` generation, spend, publication, approvals or canon, and its `permissions` are empty (it plans; Production executes). Field mapping in [scenarios/02-director-script-production.md](scenarios/02-director-script-production.md).
