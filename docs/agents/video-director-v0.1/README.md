# Video Director v0.1 (proposal)

**Status:** draft for the owner's review. Not adopted, not tested, no Brain decision yet. It authorizes nothing: no simulation, generation, external service, spend or change to the frozen `src/`.

The first specialist under the [system vision](../../vision/README.md) and [ADR-0006](../../decisions/ADR-0006-system-direction-agent-teams.md): an audiovisual creative director that turns an idea, goal or brief into a clear creative direction and an executable production plan. It is also the first concrete use of the shared parts later agents will reuse: a role definition, an input/output contract, knowledge packs with evidence tags, and an evaluation protocol fixed in advance.

| File | What it holds |
|---|---|
| [definition.md](definition.md) | Role, scope, responsibilities, boundaries, freedom, working with the user, phases, the four information categories, planning depth, repurposing, kinds of quality, relations, learning |
| [contract.md](contract.md) | Input (objective, type, medium, techniques, specifications, authorities, references, user experience, deliverable level) and output (the direction package) |
| [knowledge-packs.md](knowledge-packs.md) | Direction Core, format and medium cards, professional motion reference library, Production's tool register, and what was not adopted |
| [evaluation.md](evaluation.md) | Three simulation scenarios with planted traps; planning criteria and a decision rule fixed before testing; production-quality criteria for later |

## Design choices

- **One Director, not one agent per video type or technique.** Type, medium and technique are knowledge the Director loads; execution is Production's. Production starts as capabilities and is split by pipeline only when that proves worth it (likely candidates: code-based motion graphics, and avatars).
- **The owner's four game changers are information categories, not mandatory documents.** Their depth follows the job.
- **Freedom by default.** Each dimension of a job is preserve, bounded variation or open exploration, set by the authorities; everything else is open. Approvals, the spend limit, rights, consent and final verification are never skipped.
- **Evidence tags on every item,** so a hypothesis from a research chat cannot pass as a rule.

## Sources

- **The owner:** the description of the agent and the notes on the four information categories and brief parameters (2026-10-31).
- **The frozen V2.5 methods**, cited by section.
- **This project's research records:** the photoshoot study, the 2026-10-22 audit and the benchmark log.
- **Four AI-assistant research conversations, kept in the private half** (`research/video-2026-10`, with checksums). Only distilled points and source links are published here.

## Open questions for the owner

1. **Location:** where agent definitions live is still an open decision (vision step 2); this proposal sits under `docs/agents/` until it is decided.
2. **Evaluation run:** keep two runs per arm, or more? Is the owner the final judge on all 12 transcripts?
3. **Scenarios:** are the three fictional scenarios the right first test, or should one be replaced by a real brief from the private half?
4. **Next:** after the evaluation, build the simple motion-graphics Production route first, as proposed?
