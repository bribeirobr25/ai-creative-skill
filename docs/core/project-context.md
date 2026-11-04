# Project context

**Sources:** ADR-0005 D5 (one record contract, separate instances) and the [Brain record contract](../../brain/CONTRACT.md); ADR-0004 I1, I5, I8 and the privacy and erasure rules (kept by ADR-0005 D2); ADR-0006 D7, D8; decision `rights-and-trust`; V2.5 EC `PROJECT_CONTINUITY_STATE`, §2.3, §10 (asset sidecar), §10.1 (authority dependency snapshot), §12; CAL §6.1 (canon promotion); RES §7, §11, §13; ARCH §2 (authority order), §10 (evidence state).

Each project has one shared context that every authorized agent reads, so work survives sessions and handoffs. It follows the ADR-0005 D5 record contract: emitter is not persister, superseded records are never current, contradictions fail closed, nothing is promoted automatically.

## Where it lives

The specification is public. **Every real project instance is private** and lives outside this repository, in the private half (ADR-0004 I8). Each user's and each end client's data stays separate: an agency's context is one tenant per end client, and nothing crosses between them (ADR-0006 D8).

## Contents

The project record extends EC `PROJECT_CONTINUITY_STATE`:

```yaml
project:
  project_id:        # required
  tenant:            # required: the user, or the agency's end client
  objective:         # required: goal, audience, success signal
  constraints: []    # deadlines, budgets refs, must-preserve, must-avoid
  facts: []          # approved facts and claims, each with source; unknowns stay UNKNOWN
  authorities: []    # entity refs whose approved versions bind others (brand kit, canon, product truth)
  entities: []       # refs
  assets: []         # refs
  approvals: []      # refs (authority-and-permissions.md)
  scopes: []         # execution scope refs
  tasks: []          # task refs (collaboration.md)
  messages: []       # message refs
  events: []         # event refs
  findings: []       # research finding refs
  packages: []       # execution package refs
  open_questions: []
  next_actions: []   # proposals only; a suggested step is not an authorization
  revision:          # required; stale writes are rejected (EC §2.3)
```

## Access

Shared context does not mean everyone reads everything. Every record and asset declares who may read it:

```yaml
access: shared        # shared | area:<area> | restricted:[<role_id>, ...]
privacy_class:        # public | private | personal (the Brain contract's field, widened for the private half)
```

- `shared`: every role on the project (facts, approved authorities, the plan).
- `area:<area>`: one area's working context (draft scripts, prompts, technical research).
- `restricted`: named roles only (budgets of other campaigns, client commercial data, consent records). Credentials are never in the context at all, only a secret locator ([authority-and-permissions.md](authority-and-permissions.md#credentials)).

Rules: **P1** a request carries only references its recipient may read; **P2** a role's `reads` list bounds what it may open; **P3** these are policies, and whether a host enforces them is checked when the host is chosen.

## Entities and assets

**Entity:** anything whose identity must stay stable across work.

```yaml
entity:
  entity_id:         # required, stable across every handoff
  kind:              # required, free label owned by an area: product, character, location, logo, offer...
  canonical_label:   # required
  owner_role:        # required: who keeps it coherent
  versions: []       # each version: version, lifecycle state, approval_ref, refs to defining assets
  relations: []      # { type, entity_ref }: appears_in, wears, located_in, variant_of...
  access:
  extension: {}      # domain structure, e.g. a character sheet (README "Extensions")
```

**Asset:** reuses the EC §10 asset sidecar (asset id, version, provider and route, request ref, reference ids, parent assets, authority dependency refs and revision snapshot, hash, review verdict, approval status), plus:

```yaml
  tool:              # required for generated assets: tool and date (ADR-0006 D8)
  rights:            # required: source, licence, consent refs
  access:
  package_ref:       # the execution package that produced it, if any
```

Rules: **E1** downstream roles use `entity_id`, never a name inferred from appearance (EC "Stable entity handoff"); **E2** a nickname is presentation only; **E3** an asset without a rights record is not usable for publication.

## Lifecycle

Entities' versions, assets, execution scopes and other controlled artifacts share one lifecycle. It is a **projection**: the current state is derived from the records below, never edited directly.

| State | Meaning | Backed by |
|---|---|---|
| `proposed` | Created by a role; no authority yet | A `CHANGE_REQUESTED` record, or the artifact's creation |
| `in_review` | Being checked against criteria and constraints | A review in progress ([review.md](review.md)) |
| `approved` | An authority approved this exact version for a stated scope | A `DECISION_RECORDED` approval with its `authority_ref` |
| `superseded` | A later approved version replaced it | The later approval's `supersedes` |
| `invalidated` | An authority it depended on changed; it must be re-reviewed and re-approved before reuse | A recorded dependency on the changed authority (EC §10.1 `ACCEPTANCE_INVALIDATED`, same meaning) |

Mapping notes:
- The Brain's record kinds are **events**, not states: they back the transitions above (ADR-0005 D5).
- A review verdict `ACCEPTED` means the artifact passed review; it does not approve it. Approval is a separate authority act.
- The Video Director's scope `status: proposed | approved | superseded` is this lifecycle without `in_review` and `invalidated`.
- Historical records never change; only the projection does (EC §10.1).

**Canon.** An entity version is canon when it is `approved` and listed in `authorities`. A choice that keeps appearing in generations is not canon; promotion needs an authority and records what was promoted, from which latitude, for which scope and from when (CAL §6.1 `canon_promotion_ref`).

## Dependencies and selective invalidation

When an asset or deliverable is accepted, record which authority versions it depends on (EC §10.1). When an authority changes:

```text
authority version changes
→ compare recorded dependencies
→ mark only actual dependents `invalidated`
→ leave unrelated accepted work untouched
→ re-review and re-approve the affected work
```

Dependencies are never inferred from being made in the same session. If a required authority revision cannot be recovered, work stops for the authority (`STOP_REQUIRED_AUTHORITY_MISSING`).

## External references

Tools and systems the user already has stay the source of truth for their own records (a ticket in a tracker, a file in a drive). The context keeps a reference, not a copy (ADR-0004 I1: one authority per subject).

```yaml
external_ref:
  ref_id:            # required
  system:            # required: the system's kind, not a credential
  locator:           # required: stable locator
  as_of:             # required: version or timestamp observed
  retrieved_at:      # required
  provenance:        # who fetched it and how
  snapshot_ref:      # optional: a stored extract, where the source's terms and privacy allow it
  rights:
  access:
```

When a decision depends on external content, keep a snapshot or extract where permitted, so a link that disappears does not take the justification with it.

## Research findings

```yaml
finding:
  finding_id:        # required
  claim:             # required, one sentence
  evidence: []       # RES §7 evidence records: source, outcome, relevance, strength, independence key
  evidence_class:    # README vocabulary
  checked_at:        # required
  review_by:         # required: when it must be re-checked (e.g. 2 weeks for trends)
  verdict:           # CURRENT | STALE | CONTRADICTED | UNSUPPORTED | UNVERIFIED (RES §11)
  counterevidence: []
  access:
```

Rules: **F1** a finding past `review_by` raises a `research_due` event ([collaboration.md](collaboration.md#events-and-resumption)); **F2** a finding is re-checked at the moment a decision depends on it (RES §11, act-time verification); **F3** a previous report is context, not timeless truth (RES §13); **F4** an empty result is a valid result, never filled by the model's intuition.

## Execution packages

What is actually sent to a tool is a versioned record, so it can be reviewed before execution and compared with what came back.

```yaml
package:
  package_id:        # required
  version:           # required
  scope_ref:         # required: the approved execution scope it runs under
  built_by:          # role, usually production
  target:            # tool class and route (never only a vendor name)
  payload_ref:       # required: prompt, parameters, code, structured instruction or other payload
  inputs: []         # direction, references and authority versions it was built from
  preflight_ref:     # review at boundary B (predicted readiness)
  result_assets: []  # assets it produced
  acceptance_ref:    # review at boundary C (observed acceptance)
```

Not every deliverable is a prompt: a website or a code-based animation has code as its payload. Linking `payload_ref`, `preflight_ref`, `result_assets` and `acceptance_ref` lets every real project produce, at no extra cost, the evidence needed to calibrate preflight against observed quality ([review.md](review.md#calibration)).

## Status view

What the user sees is derived from the records on read, like `python3 -m brain status`, and never stored as truth (ADR-0006 D7). No dashboard is built (M5 dashboards stay withdrawn).

| Section | Derived from |
|---|---|
| Progress per deliverable | Tasks: status, outcome, lifecycle of their deliverables |
| Waiting and blocked | Tasks `waiting` or `stopped`, with what they wait on and their stop codes |
| Pending approvals | Approval requests without a recorded answer, with the exact version to approve |
| Cost and usage | Budgets: authorized, reserved, spent; operating usage of agents |
| Recent decisions | Approvals and supersessions since the last view |
| Learnings | Learning candidates proposed, adopted, expired |
| Due | Findings and knowledge past their review dates; scopes about to expire |
| Next actions | Proposals, labelled as not authorized |

The host decides how and how often the view reaches people (a daily summary message, a host view, a reply on request). The view is one more reading of the records, so it cannot go stale.
