# Playbooks

**Sources:** ADR-0006 D2, D7; ADR-0002 (bounded completion, entry at any stage); decision `user-journey`; V2.5 Completeness Catalog §1, §2 (requirement classes, `STORYBOARD_PLAN` as a default stage, `PROJECT_NEXT_ACTION`); ARCH §19 (progressive fidelity); EC §13.3 (task canary).

A playbook is a proven sequence for a type of goal, across areas. The project lead uses it to turn the user's goal into a plan; it is a default, not a cage.

## Format

```yaml
playbook:
  playbook_id:          # required
  goal_type:            # required: e.g. launch a service offer, product photoshoot, series pilot
  version:              # required
  status: provisional   # provisional until it earns its place (ADR-0006 D9)
  intake: []            # required: what to gather (goal, audience, brand or story, budget, deadline, what exists, taste)
  stages:
    - stage_id:         # required
      deliverable:      # required: type
      owner_role:       # required
      inputs: []        # stages or records it needs
      required_elements:  # required: each with class REQUIRED | CONDITIONAL | OPTIONAL | CREATIVE_OPEN
      done:             # required: what "done" means
      checkpoints: []   # approvals at or after this stage (approval kinds)
      may_skip_when:    # optional: when the stage may be skipped, and the reason recorded
      estimate:         # optional: typical cost and effort
  continuation:         # optional: for goals that continue after delivery
    on_events: []       # event kinds that start the next iteration (e.g. external_result, research_due)
    next_iteration:     # the stage the next iteration starts from
    ends_when:          # required if continuation is set
```

## Rules

1. **PB1 · A stage is a default.** An owner may skip or change a stage when it has a better way, and says why (ADR-0006 D2). The storyboard is the model case: a default stage that can be skipped for a clear one-shot, with the reason recorded (Completeness Catalog `STORYBOARD_PLAN`).
2. **PB2 · Never skipped:** checkpoints protecting money, publication, contact or rights; the closing check; independent review before acceptance. A standing permission is how the user answers a checkpoint in advance, not a skip.
3. **PB3 · Enter and stop anywhere.** A user may start mid-sequence with existing material or ask for one stage only; the plan covers only what was asked (ADR-0002). Completing a task is not completing the project.
4. **PB4 · Cheap checkpoints before expensive stages.** Test the riskiest unknown at the lowest valid cost before scaling (ARCH §19; EC §13.3): a storyboard before generation, a few frames before a batch, a local render before publication.
5. **PB5 · Required elements are substance.** `REQUIRED` means real domain content, not a heading; every item of a batch is checked; unknown facts stay `UNKNOWN` (Completeness Catalog §1).
6. **PB6 · Next steps are proposals.** The plan and each delivery may suggest one useful next step, labelled as not authorized (Completeness Catalog `PROJECT_NEXT_ACTION`).
7. **PB7 · Flows may continue.** A playbook may declare `continuation`: results, due research or new material start a new iteration from a named stage, through events ([collaboration.md](collaboration.md#events-and-resumption)), within the authority in force. Every continuation has an end condition.

## From playbook to plan

The project lead instantiates a playbook as tasks ([collaboration.md](collaboration.md#task-record)): one per stage that applies, with owners, dependencies, checkpoints and estimates, plus the approval requests the user will see. The plan states each step's deliverable, cost estimate and where the user approves (ADR-0006 D7). The user may change any part of it.

The reference playbook for v0.1 is in [scenarios/01-research-offer-landing.md](scenarios/01-research-offer-landing.md). Other goals (a brand identity, a photoshoot, a book, a series) get their own playbooks when a real project needs them; each earns its place.
