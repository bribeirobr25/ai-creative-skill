# Roles

**Sources:** V2.5 SMS §13 (Role Contract), §16 (Growth Rule); RA §5 ("ownership ≠ capability availability"), §12.3 (separately invokable units); ADR-0004 Agent Role (kept as contract by ADR-0005 D2); ADR-0006 D3, D6; the Video Director definition.

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
  area:               # required: research | visual-brand | story | growth | sales | production | shared
  version:            # required
  status: unproven    # unproven | earned | retired (only an owner decision changes it)
  purpose:            # required, one or two sentences
  receives: []        # required: inputs, by record type
  decides: []         # required: what it chooses on its own
  delivers: []        # required: deliverable types, each with its "done" (playbook or pack)
  may_not_decide: []  # required: what it must leave to others or to the authority
  knowledge:          # required
    always: []        # pack ids always loaded
    on_demand: []     # pack ids loaded per task
  permissions:        # required, least privilege; levels from ADR-0006 D6
    - action_class:   # e.g. read.web, spend.media_generation, act.publish
      level:          # read | spend | act_outward
  forms_allowed: []   # pack | agent | capability
  reads: []           # access classes it may read (project-context.md#access)
  extension: {}       # optional, see README "Extensions"
```

## Rules

1. **R1 · No authority.** `decides` covers only choices inside existing authority. Approvals, budgets, canon changes, publication and contact are always in `may_not_decide` (ADR-0006 D3).
2. **R2 · Least privilege.** `permissions` lists only the action classes the job needs. Having a tool connected never widens them (ARCH §5.1.2). A research role cannot post; a script writer cannot spend.
3. **R3 · Owning is not executing.** A role can own a deliverable whose media another role generates. Production owns media generation and execution; other areas use their own permitted tools (paid research data, ad budgets, commercial tools) under their own scopes.
4. **R4 · Knowledge comes first from the model.** Packs add what the model cannot know or reliably skips (ADR-0006 D2); a role's definition never restates general craft.
5. **R5 · New roles must be justified.** A new role needs a distinct deliverable, a stable input/output boundary and a reason an existing role cannot cover it (SMS §16; RA §12.3). Splitting a role into several agents needs the same reason.
6. **R6 · One canonical definition.** Each role has one definition file; copies installed in a host are generated, not edited (the Multiplayer Skills lesson in the frozen ledger, §13.4).

## Shared roles every project uses

| Role | Purpose | Notes |
|---|---|---|
| `project-lead` | Turns the user's goal into a plan from a playbook, assigns owners, tracks dependencies and keeps the status view current | Coordinates; holds no authority. Owns no creative deliverable |
| `reviewer` | Independent review of finished deliverables | A capability: fresh context, read-only, no stake in the verdict ([review.md](review.md)) |
| `production` | Media generation, editing, post-production, rendering | A capability with routes, split by pipeline only when that proves worth it (Video Director README) |

## Example

The [Video Director v0.1](../agents/video-director-v0.1/definition.md) fits this contract unchanged: `receives` its request contract, `delivers` a direction package and a *proposed* execution scope, `may_not_decide` generation, spend, publication, approvals or canon, and its `permissions` are empty (it plans; Production executes). See [scenarios/02-director-script-production.md](scenarios/02-director-script-production.md).
