# Scenario 2 · Video Director → script → Production

**Type:** conceptual compatibility check. Uses the [Video Director v0.1](../../agents/video-director-v0.1/README.md) design **unchanged**; nothing here modifies or re-evaluates it. Fictional product ad. The script writer in variant B is a role assumed only for this check.

**Question:** do the generic contracts carry direction, references, limits and approved versions from the Director to Production, and settle who writes the script?

## Variant A · short product ad, simple script

| # | Step | Owner | Knowledge | Delegation | Records | Authority |
|---|---|---|---|---|---|---|
| 1 | Brief arrives; the Director fills its `request` | video-director | Video Direction Core + one card | — | task; assumptions as `open_questions` | — |
| 2 | Director writes the 15-second script itself | video-director | Script pack loaded (`packs_loaded`) | None: no trigger applies | direction v1 `proposed`; closing check | — |
| 3 | User approves direction v1 | — | — | — | `direction` approval | User |
| 4 | Director drafts execution scope v1, with the spend limit the user stated | video-director | — | — | scope v1 draft | — |
| 5 | Production quotes the scope and builds the package for it | production | Production tool knowledge (dated) | `permission` | `quote_ref` attached; package `built_for` scope v1, `inputs` = approved direction and reference versions | — |
| 6 | Approval of scope v1 is requested (v1 is now fixed); the package gets a readiness review | reviewer | Review criteria | `independent_review` | `approval_request`; review B `READY` | — |
| 7 | User approves scope v1 | — | — | — | `execution_scope` approval | User |
| 8 | Production generates within the scope | production | — | — | EC §9 attempts; assets with tool, rights, `package_ref` | Scope v1 only (AU7) |
| 9 | Independent review of the clips | reviewer | — | `independent_review` | review C: observed acceptance, linked to the package | — |

## Variant B · campaign where the words decide the result

Same flow, but at step 2 the Director delegates the script to a script writer with trigger `quality` and the reason recorded ("the claims and the hook carry the campaign"). The request carries the approved facts, the brand voice version and the direction; the handoff returns the script with `explicit_unknowns` and `permissions_carried: NONE`. The Director keeps ownership of the direction and integrates the script. For a series the trigger would be `authority_owner`: Story owns the script as canon, and the Director directs from the approved version.

## Mapping the Director's design

| Video Director | Core |
|---|---|
| `direction_package` | Deliverable (asset of kind `document`); lifecycle from project-context.md |
| `dimension_policy` latitudes preserve / bounded variation / open exploration | The scope's `preserve`, `vary` (with ranges) and `open` lists |
| `proposed_execution_scope` fields | Execution scope fields of the same names; `executor_roles` defaults to production |
| Stored `status`, `approval_ref` | Derived from approval records |
| `references[]` (source, tool, rights, version) | Assets and entities with rights; `stable_entities` in handoffs |
| `authorities` (brand, products, claims, budget) | Project `authorities`, `facts` and budgets |
| "Changes after approval" table | AU1 (exact version; changes the approved fields allow) |
| "v0.1 cannot record approvals" | AU2 (only the host records, from a person's act) |

## Gaps found

| Gap | Class | Note |
|---|---|---|
| The Director's scope has no `budget_ref`, `schedule`, `triggers`, `stop_condition` | Accepted limitation | Optional, or filled when the scope is recorded; the Director's design stays as it is |
| Production's package format and readiness criteria per route | Domain extension | Production's own schema under `extension` and its packs |
