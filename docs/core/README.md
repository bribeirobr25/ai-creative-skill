# Shared Core v0.1 (candidate specification)

**Status:** candidate, provisional and unproven (ADR-0006 D9). It authorizes nothing: no build, runtime, model run, spend, connection, publication or contact. `docs/core/` is its provisional home until the shared-core work decides where system code lives.

The Shared Core is the set of contracts every agent and every area uses, whatever it makes: a logo, a landing page, an ad, a photoshoot, a book or a series. It defines how work is assigned, how agents and people talk, how context, assets and approvals are kept, how quality is checked and how a project continues after new events or results. Specialist knowledge stays in each specialist's packs; the core holds only what is shared.

## Files

| File | Responsibility |
|---|---|
| [roles.md](roles.md) | What a role is, what it may decide and use, and the three forms it can take |
| [knowledge-packs.md](knowledge-packs.md) | How knowledge is packaged, tagged, dated, loaded and proposed for change |
| [collaboration.md](collaboration.md) | **The central contract:** ownership, delegation, messages, modes of operation, events and resumption, conflicts |
| [project-context.md](project-context.md) | Shared project records: access, entities and assets, lifecycle, dependencies, external references, research findings, execution packages, the status view |
| [authority-and-permissions.md](authority-and-permissions.md) | Who approves, approval records, permission levels, execution scopes, budgets, continuous and scheduled work |
| [review.md](review.md) | Evaluation boundaries, independent review, the closing check, repair limits, calibration |
| [playbooks.md](playbooks.md) | Proven sequences for a type of goal, including flows that continue after results |
| [scenarios/](scenarios/) | Four conceptual compatibility checks, with their gaps classified |

## Principles

1. **Records are the source of truth; conversation is the interface.** Agents and people talk in human-readable messages, but every message, decision, approval and event that matters is a durable record (ADR-0006 D3).
2. **Domain-neutral core, controlled extensions.** The core knows owners, identities, versions, authority, references, dependencies, approvals and handoffs. It does not know what a character, a city or a landing page is. An area may extend a core record (see "Extensions").
3. **Reuse before invention.** Each spec points to its sources and copies as little as possible. What is new is marked *new here* with the reason.
4. **Agents hold no authority.** Only the user, or an approver the user designates, grants permissions; none is passed on by delegation (ADR-0006 D3, D6; ADR-0004 I3).
5. **Autonomy inside the scope, approval at the edges.** Agents collaborate, delegate and iterate without asking each time; anything that needs new permissions, spend, restricted data, publication, contact or a material scope change goes to the authority.
6. **Useful work, not activity.** Continuous work needs a goal, a budget and a stop condition.
7. **Policy is not enforcement.** These contracts state what is allowed. Whether a host enforces it mechanically is a host property, checked when the host is chosen (ADR-0005 D6). Text instructions alone do not guarantee behaviour (V2.5 SMS §11).

## Glossary

One term per concept, used the same way in every file.

| Term | Meaning |
|---|---|
| **Project** | A goal pursued over time for one user or one end client, with its own context |
| **Task** | A bounded unit of work with one owner role and one deliverable; a project has many |
| **Deliverable** | What a task hands over: a document, a plan, an asset, a decision request |
| **Role** | A bounded responsibility; it may run as a pack, an agent or a shared capability ([roles.md](roles.md)) |
| **Owner** | The role responsible for a deliverable and its coherence. Never an approver |
| **Authority** | A human holder of approvals (the user or a designated approver), or a recorded decision they made |
| **Entity** | Anything whose identity must stay stable: a product, a character, a place, a brand, an offer |
| **Asset** | A file or artifact produced or supplied, with provenance |
| **Version** | An immutable revision of an entity, asset, scope or document |
| **Execution scope** | The user-approved envelope for an operation: what, how many, which tool class, spend limit |
| **Execution package** | What is actually sent to a tool: a prompt, parameters, code or another payload |
| **Message** | A human-readable record between agents and people ([collaboration.md](collaboration.md)) |
| **Event** | A recorded occurrence that may resume work: a reply, an approval, a due date, a result |
| **Status view** | A summary derived from records on read, never stored as truth |

## Vocabulary ownership

The project has several state and evidence vocabularies. They are kept apart by owner and never merged (V2.5 SMS §13.1; QA Evidence & Rights §6.1).

| Vocabulary | Values | Owner |
|---|---|---|
| Record kind | `OBSERVED`, `CHANGE_REQUESTED`, `DECISION_RECORDED` | [Brain record contract](../../brain/CONTRACT.md) (ADR-0005 D5) |
| Task status (*new here*) | `active`, `waiting`, `stopped`, `closed` | [collaboration.md](collaboration.md) |
| Task outcome | `COMPLETE`, `PARTIAL`, `BLOCKED` | ADR-0002 (exit) |
| Stop code | `STOP_*` | V2.5 EC §26 |
| Lifecycle of entities, assets, scopes | `proposed`, `in_review`, `approved`, `superseded`, `invalidated` | [project-context.md](project-context.md) |
| Review verdict | `ACCEPTED`, `REPAIR`, `BLOCKED`, `UNVERIFIED` | V2.5 EC §12, used by [review.md](review.md) |
| Reviewer independence | `INDEPENDENT`, `MIXED`, `SELF_REVIEW`, `UNKNOWN` | V2.5 SMS §11 |
| Requirement class | `REQUIRED`, `CONDITIONAL`, `OPTIONAL`, `CREATIVE_OPEN`, `WAIVED` | V2.5 Completeness Catalog §1 |
| Completeness check | per element `PASS`, `MISSING`, `INSUFFICIENT`, `UNKNOWN`, `NOT_APPLICABLE`; overall `PASS`, `PARTIAL`, `BLOCKED`, `UNVERIFIED` | V2.5 Completeness Catalog §3 |
| Evidence class | `OBSERVED`, `USER_PROVIDED`, `VERIFIED`, `INFERRED`, `UNKNOWN` | V2.5 EC `HANDOFF_PACKET` |
| Research freshness verdict | `CURRENT`, `STALE`, `CONTRADICTED`, `UNSUPPORTED`, `UNVERIFIED` | V2.5 Research Evidence Synthesis §11 |
| Knowledge tag and strength | `rule` … `hypothesis`; `binding` … `option` | [knowledge-packs.md](knowledge-packs.md) |
| Action disposition | `AUTO_ALLOWED`, `ASK_BEFORE`, `FORBIDDEN_OR_OUTSIDE_AUTHORITY` | V2.5 EC `AUTONOMY_ENVELOPE` |
| Job states, route freshness | `PREPARED` … `UNKNOWN`; `FRESH` … `INVALIDATED` | V2.5 EC §5.4, §6: Production's, not the core's |

## Extensions

An area may add its own structure to a core record (an entity, an asset, a deliverable, a task) under `extension`:

```yaml
extension:
  owner: story            # the area or role that owns the extension schema
  schema: story.character.v0   # versioned name, owned by that area
  data: {}                # ignored by the core
```

Rules: an extension never redefines a core field or vocabulary; the core never reads `data`; the owning area documents the schema with its packs; two areas that need the same structure promote it to the core through a reviewed change, not by copying.

## Sources and short names

- ADRs: [ADR-0002](../decisions/ADR-0002-capability-bounded-invocation.md), [ADR-0004](../decisions/ADR-0004-PROPOSED-agent-workspace-durable-memory.md) (kept parts only, per ADR-0005 D2), [ADR-0005](../decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md), [ADR-0006](../decisions/ADR-0006-system-direction-agent-teams.md); the [vision](../vision/README.md); current decisions in `python3 -m brain status`.
- The [Video Director v0.1](../agents/video-director-v0.1/README.md) design, used unchanged as the reference specialist.
- Frozen V2.5 references in `src/ai-creative-skill/references/`, cited by short name: **EC** (Execution Contracts), **SMS** (Specialist Method System), **ARCH** (Architecture Spec), **CAL** (Calibration and Experience Memory), **RA** (Runtime Activation and Packaging), **RES** (Method Research Evidence Synthesis), **Completeness Catalog** (Deliverable Completeness Catalog), **QA Realism** (Method QA Realism Performance). They are raw material: cited for meaning, not adopted as authority by citation.

## Settled tensions

- **Scheduled work.** The default is read-level research and reminders (ADR-0002 as carried by ADR-0006). Other scheduled effects are allowed only inside an execution scope the user approved for them (ADR-0006 D6). This is a default, not a prohibition.
- **Proposing next steps.** Agents propose alternatives and next steps (ADR-0006 D2). A proposal is never an authorization and never runs by itself (ADR-0002 NEXT; Completeness Catalog `PROJECT_NEXT_ACTION`). V2.5's ban on unsolicited offers is replaced by this rule.
- **Evidence vocabularies.** Kept apart by owner (table above).

## Open questions (not decided here)

1. The agent host, and how much of these policies it can enforce mechanically (ADR-0005 D6; vision step 3).
2. The evaluation design, including whether execution-package preflight can be calibrated against observed assets ([review.md](review.md); ADR-0006 D9).
3. JSON Schemas and an offline validator for these records: deferred until a host exists.
4. The canonical location of system code and of private project instances (the private-half layout).
5. Who may act as a designated approver for an agency's end client, and how that delegation is evidenced.
