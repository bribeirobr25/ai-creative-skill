# ADR-0002 · Capability invocation and bounded completion

**Status:** owner-directed architectural requirement; proposed integration after V2.5 import validation.  
**Date:** 2026-10-18  
**Scope:** all existing and future capabilities, and independently useful sub-operations.

## Decision

**Every capacity participates in the shared AI Creative Skill architecture, and every meaningful operation may be invoked and completed independently.** The creative workflow is a set of possible stages, not a mandatory linear sequence.

Shared authority, canonical context, Work Profile, method selection, capability discovery, route compilation (only when necessary), approvals, costs, provenance, QA, delivery and learning remain one architecture. No parallel orchestration system per feature.

The smallest sufficient user-requested operation must have:

1. **ENTRY:** direct user intent, available context and minimum inputs, including entry from an intermediate stage.
2. **EXECUTION:** only necessary prerequisites and relevant methods, without forcing the entire creative flow.
3. **VERIFICATION:** proportional technical and creative QA, separately recording unknowns, human acceptance and blocking conditions.
4. **EXIT:** requested bounded deliverable, explicit complete/partial/blocked status and stop.
5. **NEXT:** one useful optional continuation if appropriate, never an implicit approval or automatic tool invocation.

## Three supported invocation modes

| Mode | Example | Correct boundary |
| --- | --- | --- |
| End-to-end | Create a full campaign | Orchestrate only required stages and finish upon requested deliverable |
| Standalone capability | Reframe a source video 16:9 to 9:16 | Reframe, QA and deliver, without forced upstream research or generation |
| Standalone sub-operation | Research image outpainting providers | Deliver comparative research and stop, without rendering |

A bounded repair/review is equally valid; a user may explicitly start in the middle or stop before the end. Operation completion is not equivalent to project completion.

## Invariants

- Existing TASK PATH, MINIMUM SUFFICIENT TASK PATH, Specialist Method Stack, HANDOFF_PACKET, execution contracts and approval gates are reused, not duplicated.
- A capability need not become a separate Work Profile to support direct invocation.
- Paid calls, identity changes, publication, rights, irreversible changes and external sending remain gated regardless of invocation mode.
- Handoff between capabilities preserves lineage, canon, rights and approval.
- Next-step suggestions do not authorize execution.

## Future capability acceptance tests

T1. Cold standalone request and correct result.
T2. Entry at a valid intermediate stage with existing assets.
T3. Partial operation explicitly forbidding other stages.
T4. Embedded operation within approved multi-step work.
T5. Block/partial status when a prerequisite or approval is missing.
T6. Return result and optionally recommend a next step without executing it.
T7. Cross-capability handoff preserves provenance, identity and rights.

V2.5 already contains much of this behavior. Its gap is the explicit transversal capability-level entry and exit contract. This ADR does not change the attested V2.5 source. Promote in a versioned candidate only after tests and owner approval.
