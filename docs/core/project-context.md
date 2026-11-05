# Project context

**Sources:** ADR-0005 D5 (one record contract, separate instances), D6, and the [Brain record contract](../../brain/CONTRACT.md); decision `memory-architecture`; ADR-0004 I1, I5, I8 and the privacy and erasure rules (kept by ADR-0005 D2); ADR-0006 D5, D7, D8; decision `rights-and-trust`; V2.5 EC `PROJECT_CONTINUITY_STATE`, §2.3, §3, §10 (asset sidecar), §10.1 (authority dependency snapshot); CAL §6.1 (canon promotion); RES §7, §8, §10, §11, §13; ARCH §10.

Each project has one shared context that every authorized agent reads, so work survives sessions and handoffs. It applies the ADR-0005 D5 rules: the emitter is not the persister, superseded records are never current, contradictions fail closed, nothing is promoted automatically.

## Where it lives

The specification is public. **Every real project instance is private** and lives outside this repository, in the private half (ADR-0004 I8). Instances use host memory or plain files, and are checked against the memory scenarios T01–T08 before they hold real data (decision `memory-architecture`; ADR-0005 D6). Each user's and each end client's data stays separate: an agency's context is one tenant per end client, and nothing crosses between them (ADR-0006 D8).

## Records

Every core record (project, task, message, event, approval, review, entity, asset, scope, package, finding, budget, learning candidate, external reference, autonomy envelope) carries one envelope:

```yaml
id:              # required
project_id:      # required: a project id, or `system` for work outside any project
tenant:          # required: the user, the agency's end client, or `system`
written_by:      # required: the role, host component or person that persisted it
origin:          # required: agent | person_attested | external_party | system  (new here)
channel_evidence:  # required when origin is person_attested: the host's proof of who sent it, through which channel
access:          # required, default shared (see Access)
privacy_class:   # required: public | private | personal
created_at:      # required
revision:        # required for records that change; stale writes are rejected (EC §2.3)
```

`person_attested` means the host attests that a person made the record. Whether a host can tell a person from an agent acting under the person's identity is a host property (finding `FND-AUDIT2-AGENT-IDENTITY`; README open question 1). `privacy_class` takes the Brain contract's field, which allows only `public` in this repository, and adds the values private instances need (*new here*).

**Who writes what:**

| Record | Created by | Changed by |
|---|---|---|
| Project | The project lead, from the user's request | `status` only by the user; other fields by the project lead, with revision |
| Task | The requester | Only `depends_on`, `inputs` and the status fields, through recorded transitions ([collaboration.md](collaboration.md#task-record)) |
| Message, event | The sender; the host stamps `origin` and `channel_evidence` | Never; a correction is a new record |
| Approval | The host, only from a `person_attested` act | Never; a new approval supersedes, rejects or revokes |
| Review | The reviewer | Never |
| Entity or asset version, scope version | The owner role; others send change requests to the owner | Never once an approval or review is requested; then a change is a new version |
| Package | The executor | Never; later records link to it |
| Finding | The research role | Never; a re-check is a new finding that supersedes |
| Budget | The host, from a budget approval | Ledger entries by executors (EC §4) |
| Learning candidate, external reference | The proposing or fetching role | Never |
| Autonomy envelope | The host, from approvals | Only by new approvals |

## Contents

The project record extends EC `PROJECT_CONTINUITY_STATE`:

```yaml
project:
  objective:         # required: goal, audience, success signal
  status:            # required: open | closed (closed only by the user)
  constraints: []    # deadlines, budget refs, must-preserve, must-avoid
  facts: []          # approved facts and claims, each with source; unknowns stay UNKNOWN
  authorities: []    # entity refs whose approved versions bind others (brand kit, canon, product truth)
  max_delegation_depth:  # optional; default 2 (collaboration.md CO6)
  # indexes: entities, assets, approvals, scopes, tasks, messages, events, findings, packages, budgets
  open_questions: []
  next_actions: []   # proposals only (collaboration.md CO4)
```

## Access

Shared context does not mean everyone reads everything (*new here*):

- `shared`: every role on the project (facts, approved authorities, the plan).
- `area:<id>`: one area's working context (draft scripts, prompts, technical research).
- `restricted:[roles]`: named roles only (budgets of other campaigns, client commercial data, consent records). Credentials are never in the context, only a secret locator ([authority-and-permissions.md](authority-and-permissions.md#credentials)).

1. **CX1** A request carries only references its recipient may read.
2. **CX2** A role's `reads` list bounds what it may open.
3. **CX3** Content derived from records (a summary, a handoff's text, a status line) takes the most restrictive access of its sources.
4. **CX4** These are policies; whether a host enforces them is checked when the host is chosen.

## Entities and assets

```yaml
entity:
  entity_id:         # required, stable across every handoff
  kind:              # required, free label owned by an area: product, character, location, logo, offer, consent...
  canonical_label:   # required
  owner_role:        # required: who keeps it coherent
  versions: []       # each: version, defining asset refs, dependency refs; lifecycle state derived on read
  relations: []      # { type, entity_ref }: appears_in, wears, located_in, variant_of...
  extension: {}      # domain structure, e.g. a character sheet (README "Extensions")
```

An **asset** reuses the EC §10 asset sidecar (asset id, version, provider and route, request ref, reference ids, parent assets, authority dependency refs and revision snapshot, hash), with its review verdict and approval status derived on read from review and approval records, plus `kind` (required: a free label such as `document`, `image`, `video`, `code`), `tool` (required for generated assets: tool and date, ADR-0006 D8), `rights` (required: source, licence, consent refs) and `package_ref`. A deliverable's versions are assets of kind `document` or the produced assets.

1. **CX5** Downstream roles use `entity_id`, never a name inferred from appearance (EC "Stable entity handoff"); a nickname is presentation only.
2. **CX6** An asset without a rights record is not usable for publication.
3. **CX7** A consent (a likeness, a voice, a contact's opt-in) is an entity of kind `consent`, so revoking it invalidates what depends on it. Each consent version must point to a `person_attested` or `external_party` evidence record, such as a signed release or a recorded opt-in; an agent never creates that evidence.

## Lifecycle

Entity versions, assets, deliverables, execution scopes and candidates for core pack items share one lifecycle. It is a **projection**: the current state is derived from records on read, never stored or edited.

| State | Meaning | Derived from |
|---|---|---|
| `proposed` | Created by a role; no authority yet | The version's record, or a `CHANGE_REQUESTED` record |
| `in_review` | Being checked | An open review task whose deliverable is this version |
| `approved` | An authority approved this exact version for what the approval covers | An approval with decision `approve` |
| `rejected` | An authority declined this version | An approval with decision `reject` |
| `superseded` | A later approved version replaced it | The later approval's `supersedes` |
| `invalidated` | Something it depended on changed or was revoked; it must be re-reviewed and re-approved before reuse | A recorded dependency on the changed authority, or a `revoke` |

Mapping notes:
- The Brain's record kinds back these states; they are not states themselves (ADR-0005 D5).
- For an asset or deliverable, `invalidated` corresponds to EC §10.1 `ACCEPTANCE_INVALIDATED`. For an execution scope or approval it corresponds to EC §3 `APPROVAL_STALE`.
- A review verdict `ACCEPTED` means the artifact passed review; it does not approve it.
- The Video Director's stored scope `status` and `approval_ref` are this projection; the core derives them instead of storing them.
- Historical records never change; only the projection does (EC §10.1).

1. **CX8 · One current version.** At most one approved, current version per entity and per approval coverage. Two make a `STOP_UNRESOLVED_AUTHORITY_CONFLICT`.
2. **CX9 · Canon.** An entity version is canon when it is `approved` and listed in `authorities`. A choice that keeps appearing in generations is not canon; promotion is an `authority_change` approval that records what was promoted, from which latitude, for which scope and from when (CAL §6.1 `canon_promotion_ref`).

## Dependencies and selective invalidation

Every version, asset, package and deliverable records, **when it is created**, which authority versions and consents it depends on. When one changes or is revoked:

```text
authority version changes or is revoked
→ follow the recorded dependencies, transitively
→ mark only actual dependents `invalidated`, including work in progress
→ leave unrelated accepted work untouched
→ re-review and re-approve the affected work in new tasks
```

Dependencies are never inferred from being made in the same session (EC §10.1). If a required authority revision cannot be recovered, work stops (`STOP_REQUIRED_AUTHORITY_MISSING`).

## External references

Tools and systems the user already has stay the source of truth for their own records (a ticket, a file in a drive). The context keeps a reference, not a copy (ADR-0004 I1).

```yaml
external_ref:
  system:            # required: the system's kind, never a credential
  locator:           # required
  as_of:             # required: version or timestamp observed
  retrieved_at:      # required
  provenance:        # required: who fetched it and how
  snapshot_ref:      # optional: a stored extract, where the source's terms and privacy allow it
  retention_ref:     # required with a snapshot: how long it is kept and how it is erased
  rights:
```

When a decision depends on external content, keep a snapshot or extract where permitted, so a link that disappears does not take the justification with it.

## Research findings

```yaml
finding:
  claim:             # required, one sentence
  evidence: []       # required: RES §7 evidence records, each with its independence key (RES §8)
  checked_at:        # required
  review_by:         # required: when it must be re-checked (e.g. 2 weeks for trends)
  verdict:           # required: CURRENT | STALE | CONTRADICTED | UNSUPPORTED | UNVERIFIED (RES §11)
  counterevidence: []
```

1. **CX10** A finding past `review_by` raises a `research_due` event (ADR-0006 D5; decision `knowledge-freshness`).
2. **CX11** A finding is re-checked when a decision depends on it (RES §11, act-time verification).
3. **CX12** A previous report is context, not timeless truth (RES §13); an empty result is a valid result, never filled by the model's intuition (RES §10).

## Execution packages

What is actually sent to a tool is a versioned record, reviewable before execution and comparable with what came back.

```yaml
package:
  version:           # required
  built_for:         # required: the deliverable, and the execution scope version when running it spends
  built_by:          # required: the executor role, usually production
  target:            # required: tool class and route, never only a vendor name
  payload_ref:       # required: prompt, parameters, code, structured instruction or other payload
  inputs: []         # required: direction, references and authority versions it was built from
```

The scope must be approved before the package runs whenever running it spends; a package that only renders locally needs no scope. The readiness review, the produced assets and their acceptance point back to the package (`subject_ref`, `package_ref`), so every real project gathers, at no extra cost, the evidence to calibrate readiness against observed quality ([review.md](review.md#calibration)). Not every payload is a prompt: a website or a code-based animation has code as its payload.

## Status view

What a person sees is derived from the records on read, like `python3 -m brain status`, and never stored as truth (ADR-0006 D7). No dashboard is built (M5 dashboards stay withdrawn). It is derived **per viewer**, showing only what that viewer may read: an end client's approver does not see the agency's operating costs.

| Section | Derived from |
|---|---|
| Progress per deliverable | Tasks and the lifecycle of their deliverables |
| Waiting and blocked | Tasks `waiting` or `stopped`, with what they wait on and their stop codes |
| Pending approvals | Approval requests without a recorded decision, with the exact version |
| Cost and usage | Budgets: authorized, reserved, spent |
| Recent decisions | Approvals, rejections, revocations and supersessions since the last view |
| Learnings | Candidates proposed; current knowledge adopted; items expired |
| Due | Findings and knowledge past their dates; scopes about to expire |
| Next actions | Proposals, labelled as not authorized |

The host decides how and how often the view reaches people (a daily summary message, a host view, a reply on request).
