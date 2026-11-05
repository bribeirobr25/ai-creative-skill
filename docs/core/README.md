# Shared Core v0.1 (candidate specification)

**Status:** candidate, provisional and unproven (ADR-0006 D9). It authorizes nothing: no build, runtime, model run, spend, connection, publication or contact. Where it differs from a current decision (`python3 -m brain status`), the decision prevails. Items marked *new here*, including numeric defaults, are proposals that need their own owner decision before they bind. It is the specification part of the vision's step 3; the agent host and the location of system code stay open (questions 1 and 4 below), and `docs/core/` is a provisional home until the owner decides them.

The Shared Core is the set of contracts every agent and every area uses, whatever it makes: a logo, a landing page, an ad, a photoshoot, a book or a series. It defines how work is assigned, how agents and people talk, how context, assets and approvals are kept, how quality is checked and how a project continues after new events or results. Specialist knowledge stays in each specialist's packs; the core holds only what is shared.

## Files

| File | Responsibility |
|---|---|
| [roles.md](roles.md) | What a role is, what it may decide and use, and the three forms it can take |
| [knowledge-packs.md](knowledge-packs.md) | How knowledge is packaged, tagged, dated, loaded and proposed for change |
| [collaboration.md](collaboration.md) | **The central contract:** ownership, delegation, tasks, messages, modes, events and resumption, conflicts |
| [project-context.md](project-context.md) | Records and who writes them, access, entities and assets, lifecycle, dependencies, external references, findings, execution packages, the status view |
| [authority-and-permissions.md](authority-and-permissions.md) | Who approves, approval records, permission levels, execution scopes, budgets, scheduled and event-driven work, protective actions |
| [review.md](review.md) | Evaluation boundaries, independent review, the closing check, repair limits, calibration |
| [playbooks.md](playbooks.md) | Proven sequences for a type of goal, including flows that continue after results |
| [scenarios/](scenarios/) | Four conceptual compatibility checks, with their gaps classified as blocking, domain extension, accepted limitation or open question |

## Principles

1. **Records are the source of truth; conversation is the interface.** Every message, decision, approval and event that matters is a durable record (ADR-0006 D3).
2. **Domain-neutral core, controlled extensions.** The core knows owners, identities, versions, authority, references, dependencies, approvals and handoffs, not what a character, a city or a landing page is.
3. **Reuse before invention.** Each spec cites its sources and gives each rule one home; other files link to it. What is new is marked *new here* with the reason.
4. **Agents hold no authority.** Only the user grants permissions; the user may name an approver for stated approval kinds (*new here*, see [authority-and-permissions.md](authority-and-permissions.md#who-holds-authority)). No permission is passed on by delegation (ADR-0006 D3, D6; ADR-0004 I3).
5. **Autonomy inside the scope, approval at the edges.** Agents collaborate, delegate and iterate without asking each time; what needs new permissions, spend, restricted data, publication, contact or a material scope change goes to the authority.
6. **Useful work, not activity.** Continuous work needs a goal, a budget and a stop condition ([authority-and-permissions.md](authority-and-permissions.md#scheduled-and-event-driven-work)).
7. **Policy is not enforcement.** These contracts state what is allowed. Whether a host enforces it (read-only review, access classes, attested authorship, append-only history) is a host property, checked when the host is chosen (ADR-0005 D6). Text instructions alone do not guarantee read-only behaviour (V2.5 SMS §11); this spec applies the same caution to every policy.

## Glossary

One term per concept, used the same way in every file.

| Term | Meaning |
|---|---|
| **Project** | A goal pursued over time for one user or one end client (the *tenant*), with its own context |
| **Task** | A bounded unit of work with one owner role and one deliverable |
| **Deliverable** | What a task hands over. Its versions are recorded as assets of kind `document` or as the produced assets |
| **Role** | A bounded responsibility; it may run as a pack, an agent or a shared capability ([roles.md](roles.md)) |
| **Owner** | The role responsible for a deliverable and its coherence. Never an approver |
| **System owner** | The person who owns this repository and the system; sets the system operating budget and approves core rule changes |
| **Authority** | A person who holds approvals (the user or a named approver), or a recorded decision they made |
| **Entity** | Anything whose identity must stay stable: a product, a character, a place, a brand, an offer |
| **Asset** | A file or artifact produced or supplied, with provenance |
| **Version** | A revision of an entity, asset, scope or document; immutable once an approval or review is requested for it |
| **Execution scope** | The user-approved envelope for spending: what, how many, which tool class, spend limit |
| **Execution package** | What is actually sent to a tool: a prompt, parameters, code or another payload |
| **Acceptance** | An independent review verdict `ACCEPTED` on a final deliverable. Not an approval |
| **Approval** | A person's recorded decision on an exact version. Not an acceptance |
| **Message** | A human-readable record between agents and people ([collaboration.md](collaboration.md#messages)) |
| **Event** | A recorded occurrence that may resume work: a reply, an approval, a due date, a result. Not the ADR-0004 event envelope; the Brain's record kinds are kinds of record, not events |
| **Status view** | A summary derived from records on read, never stored as truth |

## Vocabulary ownership

Vocabularies are kept apart by owner and never merged (V2.5 SMS §13.1; QA Evidence & Rights §6.1). Rule ids (`CO1`, `AU1`…) are local to their file.

| Vocabulary | Values | Owner |
|---|---|---|
| Record kind | `OBSERVED`, `CHANGE_REQUESTED`, `DECISION_RECORDED` | [Brain record contract](../../brain/CONTRACT.md) (ADR-0005 D5) |
| Record origin (*new here*) | `agent`, `person_attested`, `external_party`, `system` | [project-context.md](project-context.md#records) |
| Access class (*new here*) | `shared`, `area:<id>`, `restricted:[roles]` | [project-context.md](project-context.md#access) |
| Lifecycle | `proposed`, `in_review`, `approved`, `rejected`, `superseded`, `invalidated` | [project-context.md](project-context.md#lifecycle) |
| Task status (*new here*) | `active`, `waiting`, `stopped`, `closed` | [collaboration.md](collaboration.md#task-record) |
| Task outcome | `COMPLETE`, `PARTIAL`, `BLOCKED` | ADR-0002 (exit) |
| Stop code | `STOP_*` | V2.5 EC §26 |
| Message type, event kind (*new here*) | see [collaboration.md](collaboration.md#messages) | collaboration.md |
| Approval kind and decision (*new here*) | see [authority-and-permissions.md](authority-and-permissions.md#approval-record) | authority-and-permissions.md |
| Review verdict (boundaries A, C) | `ACCEPTED`, `REPAIR`, `BLOCKED`, `UNVERIFIED` | V2.5 EC §12 |
| Readiness (boundary B, *new here*) | `READY`, `NOT_READY`, `UNVERIFIED` | [review.md](review.md) |
| Reviewer type; independence | `HUMAN`, `MODEL`, `TECHNICAL`, `MIXED`; `INDEPENDENT`, `MIXED`, `SELF_REVIEW`, `UNKNOWN` | V2.5 EC §12; SMS §11 |
| Finding severity | `BLOCKER`, `REPAIR_REQUIRED`, `NOTE` | V2.5 QA Realism §9 |
| Requirement class; waiver | `REQUIRED`, `CONDITIONAL`, `OPTIONAL`, `CREATIVE_OPEN`; `WAIVED` is a separate status that needs an authority reference | V2.5 Completeness Catalog §1 |
| Completeness check | per element `PASS`, `MISSING`, `INSUFFICIENT`, `UNKNOWN`, `NOT_APPLICABLE`; overall `PASS`, `PARTIAL`, `BLOCKED`, `UNVERIFIED` | V2.5 Completeness Catalog §3 |
| Handoff evidence class | `OBSERVED`, `USER_PROVIDED`, `VERIFIED`, `INFERRED`, `UNKNOWN` | V2.5 EC `HANDOFF_PACKET` |
| Evidence state; claim status | ARCH §10 (`VERIFIED_EXTERNAL`, `PROJECT_EMPIRICAL`…); QA Evidence & Rights claim registry | V2.5 ARCH §10; QA Evidence & Rights. Not merged with the handoff class |
| Research freshness verdict | `CURRENT`, `STALE`, `CONTRADICTED`, `UNSUPPORTED`, `UNVERIFIED` | V2.5 RES §11 |
| Knowledge layer, tag and strength; learning origin | `core`, `current`, `experience`; `rule` … `hypothesis`; `binding` … `option`; CAL §1.2 classes | [knowledge-packs.md](knowledge-packs.md) |
| Action disposition | `AUTO_ALLOWED`, `ASK_BEFORE`, `FORBIDDEN_OR_OUTSIDE_AUTHORITY` | V2.5 EC `AUTONOMY_ENVELOPE` |

## Extensions

An area may add its own structure to a core record (an entity, an asset, a deliverable, a task) under `extension`:

```yaml
extension:
  owner: story                  # the area or role that owns the extension schema
  schema: story.character.v0    # versioned name, owned by that area
  data: {}                      # ignored by the core
```

An extension never redefines a core field or vocabulary; the core never reads `data`; the owning area documents the schema with its packs; two areas that need the same structure promote it to the core through a reviewed change, not by copying.

## Sources and short names

- ADRs: [ADR-0002](../decisions/ADR-0002-capability-bounded-invocation.md); [ADR-0004](../decisions/ADR-0004-PROPOSED-agent-workspace-durable-memory.md), whose invariants I1–I5, I8, I9, privacy and erasure rules, two-level idempotency and T01–T08 are kept by ADR-0005 D2, and whose task, message and role contracts were not kept and are used here only as raw material; [ADR-0005](../decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md); [ADR-0006](../decisions/ADR-0006-system-direction-agent-teams.md); the [vision](../vision/README.md); the current decisions.
- The [Video Director v0.1](../agents/video-director-v0.1/README.md) design, used unchanged as the reference specialist.
- Frozen V2.5 references in `src/ai-creative-skill/references/`, cited by short name: **EC** (Execution Contracts), **SMS** (Specialist Method System), **ARCH** (Architecture Spec), **CAL** (Calibration and Experience Memory), **RA** (Runtime Activation and Packaging), **RES** (Method Research Evidence Synthesis), **Localized Repair**, **QA Realism**, **QA Evidence & Rights**, **Completeness Catalog** (Deliverable Completeness Catalog), the **frozen ledger** (External Skill Analysis Ledger). They are raw material: cited for meaning, not adopted as authority by citation.

## Settled tensions

- **Scheduled work.** The ADR's default holds; its D6 extension is defined once, in [authority-and-permissions.md](authority-and-permissions.md#scheduled-and-event-driven-work).
- **Proposing next steps.** Agents propose alternatives and next steps (ADR-0006 D2). A proposal never authorizes and never runs by itself ([collaboration.md](collaboration.md#messages), CO4). This replaces V2.5's ban on unsolicited next-step offers (ARCH §7.1; EC §27 CT-14).
- **Evidence vocabularies.** Kept apart by owner (table above).

## Open questions (not decided here)

1. The agent host, and how much of these policies it enforces mechanically: read-only review, access classes, append-only history (finding `FND-AUDIT2-EVIDENCE-GUARANTEE`) and telling a person's act from an agent acting under the person's identity (finding `FND-AUDIT2-AGENT-IDENTITY`).
2. The evaluation design, including whether execution-package readiness can be calibrated against observed assets ([review.md](review.md#calibration); ADR-0006 D9).
3. JSON Schemas and an offline validator for these records: deferred until a host exists.
4. The canonical location of system code and of private project instances (the private-half layout).
5. Who may be named as an approver for an agency's end client, and how that naming is evidenced.
6. The project operating budget: who pays for the agents' own work, and whether it is a new user checkpoint ([authority-and-permissions.md](authority-and-permissions.md#budgets)).
7. Recurring publication under a standing permission, which meets the "no auto-publishing" limit (decision `business-scope`).
8. Numeric defaults: delegation depth 2; caps on fan-out and on request rounds between two roles (none set).
