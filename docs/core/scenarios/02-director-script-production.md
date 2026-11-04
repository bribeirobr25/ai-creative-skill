# Scenario 2 · Video Director → script → Production

**Type:** conceptual compatibility check. Uses the [Video Director v0.1](../../agents/video-director-v0.1/README.md) contract **unchanged**; nothing here modifies or re-evaluates it. Fictional product ad.

**Question:** do the generic contracts carry direction, references, limits and approved versions from the Director to Production, and settle who writes the script?

## Variant A · short product ad, simple script

| # | Step | Owner | Knowledge | Delegation | Records | Authority |
|---|---|---|---|---|---|---|
| 1 | Brief arrives; the Director fills its `request` | video-director | Video Direction Core + one card | — | task; assumptions as `open_questions` | — |
| 2 | Director writes the 15-second script itself | video-director | Script pack loaded (`packs_loaded`) | None: no trigger applies | direction package `proposed` | — |
| 3 | User approves direction v1 | — | — | — | `direction` approval | User |
| 4 | Director proposes execution scope v1 | video-director | — | — | `execution_scope` `proposed`, `quote_ref` empty → not ready | — |
| 5 | Production quotes and builds the package | production | Production tool knowledge (dated) | `permission` | package with `payload_ref`, `inputs` = approved direction and reference versions | — |
| 6 | Preflight of the package | reviewer | Review criteria | `independent_review` | review B: predicted readiness | — |
| 7 | User approves scope v1 with its spend limit | — | — | — | `execution_scope` approval | User |
| 8 | Production generates within the scope | production | — | — | attempts, assets with tool, rights, `package_ref` | Inside scope v1 only |
| 9 | Review of the clips | reviewer | — | `independent_review` | review C: observed acceptance; linked to the package | — |

## Variant B · campaign where the words decide the result

Same flow, but at step 2 the Director delegates the script to a script writer with trigger `quality` and the reason recorded ("the claims and the hook carry the campaign"). The request carries the approved facts, the brand voice version and the direction; the handoff returns the script with `explicit_unknowns` and `permissions_carried: NONE`. The Director keeps ownership of the direction and integrates the script. For a series, the trigger would be `authority_owner` instead: Story owns the script as canon, and the Director directs from the approved version.

## Mapping the Director's contract

| Video Director field | Core record |
|---|---|
| `direction_package` | Deliverable; lifecycle from `project-context.md` |
| `dimension_policy`, `preserve` / `vary` / `open` | Execution scope fields of the same names |
| `proposed_execution_scope.status`, `approval_ref` | Lifecycle state and approval record |
| `references[]` (source, tool, rights, version) | Assets and entities with rights; `stable_entities` in handoffs |
| `authorities` (brand, products, claims, budget) | Project `authorities`, `facts` and budgets |
| "Changes after approval" table | Rule A1 (exact version; changes the approved fields allow) |
| "v0.1 cannot record approvals" | Rule A2 (evidence or nothing) |

## Gaps found

| Gap | Class | Note |
|---|---|---|
| The Director's scope has no `schedule`, `stop_condition`, `executor_roles` | Accepted limitation | Optional or defaulted in the core scope; the Director's design stays as it is |
| Production's package format per route | Domain extension | Production's own schema under `extension` |
| Who reviews at boundary B before a reviewer role exists | Open question | Part of the host and evaluation decisions |

No blocking gap.
