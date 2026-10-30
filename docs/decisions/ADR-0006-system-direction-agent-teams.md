# ADR-0006 · System direction: agent teams with guidance that earns its place

**Date:** 2026-10-30
**Status:** ACCEPTED: merged by the owner on 2026-10-30 (PR #50). Consistency amendment after the 2026-10-30 audit: see the end of this ADR.
**Supersedes in part:** [ADR-0005](ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md):
- D1: "no guide", D1.2 (techniques become benchmark-log observations; they now go into dated knowledge packs) and D1.4 (already replaced by the evaluation-method amendment). D1.1 (frozen package, no release line) stands. D1.3 stands: durable rules are enforced by checks; guidance may also state them as limits.
- D2/D3: the withdrawal of M4 (agents), of M5's scheduler and notifications, and of M6 (business operations). The L3 engine (M2) stays deferred, the L4 Workspace stays withdrawn, and M5's dashboards stay withdrawn (see D7).
**Leaves unchanged, with their scope made explicit:**
- ADR-0001 (one canonical source tree) governs the frozen package. New system code gets one canonical location of its own, decided in the shared-core design.
- ADR-0002 (bounded, independently completable operations; no automatic tool invocation) carries into the agent design: scheduled work is limited to read-level research and reminders unless D6 authority applies. Its journeys T1–T7 stay withdrawn as benchmark check C7.
- ADR-0003 governs publication to this repository, not users' outward actions (see D6).
- The rest of ADR-0005: D4 (done in #35), D5–D7 and the evaluation-method amendment.
**Does not authorize:** builds, merges, releases, changes to `src/`, paid APIs, connections to external services, use of private data, publication or contact. Each needs its own owner authorization.

## Context

The owner stated the purpose of the project on 2026-10-30 (the open question "what is this repo for now?"):

- One system for creative work in any format (ad videos, motion graphics, websites, logos and identity, photoshoots, AI influencers, books, scripts, films, series, cartoons, soap operas, audio) **and** the business around it (research for data and inspiration, offers, leads, outreach, deals, selling goods, ad creation and management).
- For brands, for solopreneurs who build AI service, agency or product companies or sell their own creative work, and for agencies serving many clients.
- The main goal: an agentic system with areas and specialists that helps its users reach their goals with good quality through guided steps, while leaving the agents as free as possible to be creative and use their best knowledge.

The container test (ADR-0005 D1, BL-2026-10-29-01) was run to find the right balance between guiding a model and leaving it room, not to discard the work. It compared all-or-nothing options on a few creative tasks: the full V2.5 package added no visible quality there and caused unasked images. It could not tell which pieces of guidance help. Earlier studies point the same way: guidance helped where it carried knowledge the model lacked (clean reference images in the photoshoot study) and hurt or added nothing where it carried procedure.

The full direction is in [docs/vision/README.md](../vision/README.md).

## Decisions

### D1 · Purpose
The repository is the home of that system: its guidance, its checks, its agent designs and its safety rules. The frozen V2.5 package is raw material to mine, not a dead archive.

### D2 · Guidance principle (replaces "no guide" in ADR-0005 D1)
- Guidance fixes what the model cannot know (user facts, taste, niche and market knowledge, past results, tool failures), steps models reliably skip (closing and verification), proven stages in order, required elements of a good result, limits, and what "done" means.
- The model decides how each stage is done; its own knowledge comes first, and a knowledge pack adds what it lacks.
- Freedom rules: open by default; a proven stage is a default the agent may skip or change with a stated reason, except checkpoints that protect money, publication, contact or rights, and closing and verification steps; agents may propose alternatives, and real alternatives need an outside input (the user's choice, a different brief, a rule).
- Every piece of guidance stays only while checks or real results get worse without it, and is re-tested when models change. How that is measured is decided in D9; until then guidance is adopted provisionally and marked unproven.
- The ADR-0005 D1 result stands for the V2.5 package as built: no new release line, no new methods in `src/`.

### D3 · Agent teams (re-opens M4, and the scheduler and notifications of M5)
- Areas with a lead and specialists, plus a project lead that turns a user's goal into a plan across areas. Skills become the knowledge an agent loads; the agent is the role.
- Agents share context through dated records under the ADR-0005 D5 contract, not through chat history.
- Every agent earns its place against a generalist (measured as D9 decides).
- Leads coordinate and hold no authority; only the user grants permissions, and no agent passes one on. Final review is independent of the lead that produced the work, and repair rounds are capped with escalation to the user. This keeps what the frozen External Skill Analysis Ledger rejected (agent orgs with CEO authority, removable human gates, unchecked scheduled routines) out of this design.
- Agents may ask each other directly; requests and answers are recorded. The vertical slice checks that each agent actually loads its knowledge.
- Host-native agents, delegation and scheduling are preferred (ADR-0005 D6). The ADR-0005 D5 rule stands: no home-built memory engine unless host memory plus plain files fail T01–T08 on a real project.

### D4 · Business operations are in scope (re-opens M6)
Research, leads, outreach, deals, selling goods and ad management are part of the system. Only the canon's "not promoted" line on agency prospecting, outreach, website and CRM capability is superseded. Its other items stand as limits: no approval silently widening into generation, spend, publication or campaign activation; no auto-publishing; no synthetic testimonials or generated proof presented as real; no provider scores as measured performance. The frozen `src/` text is not edited.

### D5 · Knowledge freshness and learning
- Research findings carry a check date and a re-check date; the system re-runs research on schedule or reminds the user.
- Each specialist runs a learning loop: vetted sources, scheduled intake, analysis into patterns, candidate learnings, adoption by layer, expiry.
- Adoption by layer: current knowledge enters with source, reliability, date and expiry once a reliable source states it or two agree; it is knowledge, not a rule, and the user can remove it. The proven core and any rule change only through a deliberate act of the user or owner with evidence; nothing becomes a rule automatically (ADR-0005 D5, ADR-0004 I5).
- Scheduled learning draws on an operating budget the owner sets for the system, not on a user's project budget.
- Fetched content is data, never instructions. Patterns, not copies. The user can see and remove what was adopted.

### D6 · Tools by permission level
Read (allowed, within platform terms; restricted platform APIs often mean paid data, which is spend), spend (within a budget the user approves for a stage; approval opens or raises a budget, not each generation; estimated before and reported after), act outward (approval per action, or a standing permission the user grants for a named action), credentials (never in the repository). The levels map onto the autonomy rules kept from ADR-0004 (I3 `permissions_carried: NONE`, I4 autonomy per action class) and the frozen package's autonomy envelope: a standing permission is recorded with its authority, re-checked on every effect and never carried by delegation. Each agent gets only the tools and levels its job needs; an outward action that may have run is never blindly repeated.

### D7 · Guided user journey
- Intake of the user's goal and context; a plan from a playbook (a proven cross-area sequence for a type of goal); guided stages with checkpoints at the brief, the direction, opening or raising a budget, and publication or contact; delivery; results measured and fed back.
- The user can always see progress, cost so far, pending approvals and what was learned. How (records, host views or a dashboard) is decided in the shared-core design; a dedicated dashboard (M5) is not re-opened.
- For an agency, approvals and revision rounds are recorded per end client.
- Quality is judged by required elements (checked by the independent reviewer), the user's judgement, real results, and checks with simulation (ADR-0005 evaluation-method amendment).

### D8 · Rights, compliance and trust
- Every asset records its source, tool and rights; new logos and names are checked against existing marks; no real person's likeness without consent.
- Platform ad and listing policies, AI-content disclosure rules and outreach consent and anti-spam law are required elements.
- Each user's and each client's data stays separate and private; learning from one user's private results is not shared without consent.
- Websites meet common accessibility standards; videos carry captions and images alt text. Steps that need a human professional (a trademark search by a lawyer, a real shoot, a voice actor's consent) are prepared and handed off, not simulated.

### D9 · Evaluation design is an open owner decision
"Earns its place" needs evidence that results get worse without a piece of guidance or an agent. The benchmark checks C1–C9 test restraint and safety, not creative quality; simulation can only reuse recorded evidence; live blind studies are no longer planned. The design is decided before the vertical slice. A proposal: recorded owner ratings on real work, comparisons inside real projects (the same deliverable with and without a pack), and the four-axis rubric in `docs/research/creative-quality/evaluation.md`. Until then, guidance and agents are adopted provisionally and marked unproven, and the benchmark-check retirement rule is suspended.

## Consequences

- The project moves from "record of decisions plus frozen package" (ADR-0005) to building an agent system in steps.
- The cost is real: agents, schedules and connections cost money and owner attention. The vertical slice (vision, sequence step 4) tests the design on one real project before widening.
- Risk: scope this wide never finishes. Mitigation: one slice at a time; each agent and pack earns its place; open threads are folded into the sequence or closed.
- Risk: outward actions (posting, ads, email) cause harm or cost. Mitigation: D6 levels, owner approval, and the existing safety gates.
- Risk: learning from the web imports manipulated or copied material. Mitigation: D5 safeguards.
- Risk: guidance and checkpoints slow the agents down or narrow them. Mitigation: D2 freedom rules and the earn-its-place test.
- Risk: legal exposure from AI content, likeness, trademarks or outreach. Mitigation: D8.

## Next steps (each separately authorized)

1. Done: the owner merged this ADR and the vision (PR #50).
2. Before any real project: the vision's sequence step 2 (offline backup of the private half, host check, the D9 evaluation design, a secret store, the private-half layout, the slice budget and rights review).
3. Design the shared core (vision, sequence step 3), then choose the real project for the vertical slice.

## Consistency amendment (2026-10-30)

A five-agent audit after the merge found contradictions with earlier, still-valid decisions. This amendment resolves them without changing the direction: the scope of what ADR-0005 and the canon's "not promoted" list lose (header, D4), the M5 scope (D3, D7), the permission model (D6), budget approvals (D6, D7), learning adoption (D5), skipped closing steps and independent review (D2, D3), and the evaluation question (D9). The Brain records that changed are superseded, not edited.
