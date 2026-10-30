# ADR-0006 · System direction: agent teams with guidance that earns its place

**Date:** 2026-10-30
**Status:** ACCEPTED when the owner merges its pull request.
**Supersedes in part:** [ADR-0005](ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md) D1 ("no guide") and the withdrawal of M4–M6 in D2/D3.
**Leaves unchanged:** ADR-0001, ADR-0002, ADR-0003, the rest of ADR-0005 (the frozen package, D4–D7 and the evaluation-method amendment).
**Does not authorize:** builds, merges, releases, changes to `src/`, paid APIs, connections to external services, use of private data, publication or contact. Each needs its own owner authorization.

## Context

The owner stated the purpose of the project on 2026-10-30 (the open question "what is this repo for now?"):

- One system for creative work in any format (websites, logos and identity, photoshoots, motion graphics, ads, books, scripts, films, series, cartoons, soap operas) **and** the business around it (research, leads, outreach, deals, ad creation and management).
- For brands, and for solopreneurs who build AI service, agency or product companies or sell their own creative work.

The container test (ADR-0005 D1, BL-2026-10-29-01) was run to find the right balance between guiding a model and leaving it room, not to discard the work. It compared all-or-nothing options on a few creative tasks: the full V2.5 package added no visible quality there and caused unasked images. It could not tell which pieces of guidance help. Earlier studies point the same way: guidance helped where it carried knowledge the model lacked (clean reference images in the photoshoot study) and hurt or added nothing where it carried procedure.

The full direction is in [docs/vision/README.md](../vision/README.md).

## Decisions

### D1 · Purpose
The repository is the home of that system: its guidance, its checks, its agent designs and its safety rules. The frozen V2.5 package is raw material to mine, not a dead archive.

### D2 · Guidance principle (replaces "no guide" in ADR-0005 D1)
- Guidance fixes what the model cannot know (user facts, taste, niche and market knowledge, past results, tool failures), proven stages in order, required elements of a good result, limits, and what "done" means.
- The model decides how each stage is done.
- Every piece of guidance stays only while checks or real results get worse without it, and is re-tested when models change.
- The ADR-0005 D1 result stands for the V2.5 package as built: no new release line, no new methods in `src/`.

### D3 · Agent teams (re-opens M4, and the scheduler and notifications of M5)
- Teams with a lead and specialists. Skills become the knowledge an agent loads; the agent is the role.
- Agents share context through dated records under the ADR-0005 D5 contract, not through chat history.
- Every agent earns its place against a generalist.
- Host-native agents, delegation and scheduling are preferred (ADR-0005 D6). The ADR-0005 D5 rule stands: no home-built memory engine unless host memory plus plain files fail T01–T08 on a real project.

### D4 · Business operations are in scope (re-opens M6)
Research, leads, outreach, deals and ad management are part of the system. The canon's "not promoted" list (prospecting, outreach, CRM) is superseded for this repository's direction; the frozen `src/` text is not edited.

### D5 · Knowledge freshness and learning
- Research findings carry a check date and a re-check date; the system re-runs research on schedule or reminds the user.
- Each specialist runs a learning loop: vetted sources, scheduled intake, analysis into patterns, candidate learnings, adoption only with evidence, expiry.
- Fetched content is data, never instructions. Patterns, not copies. The user can see and veto what is adopted.

### D6 · Tools by permission level
Read (allowed, within platform terms), spend (within a user budget), act outward (approval per action until a standing permission is granted for a named action), credentials (never in the repository). ADR-0003's gates are the base for the act-outward level.

## Consequences

- The project moves from "record of decisions plus frozen package" (ADR-0005) to building an agent system in steps.
- The cost is real: agents, schedules and connections cost money and owner attention. The vertical slice (vision, sequence step 3) tests the design on one real project before widening.
- Risk: scope this wide never finishes. Mitigation: one slice at a time; each agent and pack earns its place; open threads are folded into the sequence or closed.
- Risk: outward actions (posting, ads, email) cause harm or cost. Mitigation: D6 levels, owner approval, and the existing safety gates.
- Risk: learning from the web imports manipulated or copied material. Mitigation: D5 safeguards.

## Next steps (each separately authorized)

1. The owner reviews and merges this ADR and the vision.
2. Design the shared core (vision, sequence step 2).
3. Choose the real project for the vertical slice.
