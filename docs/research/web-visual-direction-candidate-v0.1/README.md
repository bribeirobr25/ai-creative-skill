# WEB Visual Direction Candidate v0.1 — experiment only

**Status:** TEST CANDIDATE · NOT APPROVED · NOT RELEASED · NOT A PROFESSIONAL-QUALITY CLAIM.

> **Desfecho (21/10/2026):** candidata testada no DQB-02 e **não incorporada** (PR #12 fechado sem merge).
> Decisão formal `INCONCLUSIVE`; leitura exploratória `REVISE CANDIDATE`. A alteração proposta no Work Profile
> permanece no PR #12. Veja [DQB-02](../dqb02/README.md) e o [relatório de decisão](../dqb02/relatorio-decisao.md).

## Reason for this experiment

DQB-01 (draft PR #11) produced complete navigable websites using a general host baseline and manual AI Creative Skill guidance, but did **not** demonstrate superior aesthetic quality, a winning design, clean-host automatic skill activation, or a native Higgsfield workflow. Previous PRs #9/#10 demonstrated that rendered review can detect failures missed by functional tests; their repair evidence does not prove mature first-pass visual design. This candidate targets that narrower gap.

Sources of proposed ideas: three user-supplied v0.1 research drafts (visual reference library, visual decision sheet, design critique). They remain research proposals. Never reproduce third-party website layouts, logos, text, images or downloaded skill text as output assets.

## Smallest proposed implementation

Only `src/ai-creative-skill/references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` is intentionally changed in this branch.

| Existing owner | Experimental behavior | Fields reused |
| --- | --- | --- |
| FAST 2 / reference acceptance | Consult relevant visual references only when needed; accept principles by dimension, record excluded inheritance | `approved_reference_scope` and existing brand/rights authorities |
| FAST 3 / direction | State **one project-specific compositional choice**, one visible desktop/mobile outcome, one tradeoff; keep proportional to task | `WEB_DIRECTION.visual_direction`, `primary_cta_intent`, `sections_and_purpose`, `creative_open_zones` |
| FAST 7 / rendered QA | Inspect homepage/inner page and critical interaction; distinguish objective failure, direction mismatch and preference; repair only affected surface and retest | `WEB_QA.checks`, viewport/evidence/build hash; `WEB_EDIT` / `WEB_REVISION` |

No schema changes, new validation engine, Work Profile, status enum, mandatory form, external generation call, moodboard requirement or universal visual style.

## Reference vocabulary — experimental, not six mandatory presets

| Language family | Initial public reference / observation scope | Transfer only when useful |
| --- | --- | --- |
| Contained / systematic | https://www.swissted.com/ — storefront/poster artwork, desktop opening | Alignment, typographic hierarchy, controlled contrast |
| Editorial / brand-led | https://agnestoth.com/ — desktop opening | Purposeful interplay of story, imagery and content |
| Graphic / expressive | https://gumroad.com/ — desktop opening | Coherent motifs while keeping controls recognizable |
| Warm / organic | https://www.headspace.com/ — desktop opening | Friendly forms with clear information hierarchy |
| Retro / playful | https://poolsuite.net/ — desktop opening | Historic visual vocabulary with contemporary usability |
| Spatial / exploratory | https://www.duda.works/ — desktop opening | Exploration with equivalent direct navigation |

**Evidence limitation:** one example per family, desktop openings only; these are observed exemplars, not universal styles, complete usability audits, IP licenses or empirical conversion evidence. Separate language from composition (bento/asymmetry), surface (glass/texture), theme (dark), interaction (scroll/3D), and component system. The user-provided full library remains the reference draft; do not copy reference brands' distinctive implementation.

## Execution protocol: DQB-02

### Preflight and allocation
1. Freeze a **new** fiction-only brief, original/licensed assets, copy, page set and tasks; avoid recycling NOMA, Della or Oficina Aurora as the test itself.
2. Fix the same model/host/tool availability, capabilities, fonts, assets, iteration cap and active production-time budget for both conditions. Log exact model/config if exposed, otherwise UNKNOWN. Preserve the prompt transcript and exact method version.
3. Two independent clean execution contexts, ideally isolated workspaces. Use identical common Sites instructions in both. Different conditions only:
   - **A:** exact V2.5 `main` Web work profile.
   - **B:** the candidate Web work profile in this branch.
4. Give both **the same reference availability**, not additional inspiration to B. B differs only in the method for selecting/applying references and critiquing rendered output. Reserve the same browser review and **at most one** repair pass for both. If A chooses not to use it, log that.
5. Snapshot and blind-evaluate **R0 before any human corrective feedback**, then allow a controlled matched R1; label no-op where no repair is justified. All failures, extra work and asset constraints remain recorded.
6. Repeat on a second materially different fictional brief to test transfer, not just a branded variation. Cross-brand diversity matters: detect if both turn into the same template.

### Evidence/assessment
- Deliver locally navigable homepage + relevant inner pages/states; real desktop 1440×900 and mobile 390×844 QA, plus useful 768px check.
- Technical acceptance and fidelity are gating, **not** aesthetic scores. Aesthetic rubric: art direction / identity, typography, composition, imagery integration, components, interactions and perceived finish; usability: task completion, CTA discovery and information order. Report viewport-specific tradeoffs.
- Obtain at least two genuine independent counterbalanced human reviews, ideally one design-experienced. Never simulate reviewers with AI personas. Without them, status stays `AWAITING_HUMAN_REVIEW`.
- Record first-pass preferences independently of after-repair preferences; use visible evidence and descriptions rather than ungrounded adjectives.
- Explicitly note retrieval of references, tokens/timing, model/tool parity, material interventions and missing provenance. No conversion lift, ROI or blanket professional-quality claims.
- Maintain optional ablation follow-up if B appears better: test reference selection, concise intention and rendered critique separately before mandating all three.

### Decision gates
- **PASS FOR FURTHER REVIEW:** B has an independently justified advantage in at least two preselected aesthetic dimensions without critical fidelity/usability regressions, with repeatable evidence in a second category.
- **INCONCLUSIVE:** human evidence missing, a tie, tools/assets differ materially, or an intervention cannot be attributed.
- **REJECT OR REWORK:** added effort/noise without discernible improvement; duplicated fields; identity or CTA regressions; convergent generic layouts.
- **NO AUTOMATIC MERGE:** the research candidate must not be released until approved versioning/packaging and the existing V2.5 attestations are handled as a future version. The unchanged historical V2.5 builder will refuse modified `src/` by design. Do not rewrite historical hashes to make a test green.

## Execution and data policy

No paid generations, client-media uploads to new providers, publishing, changing live websites, copying external skill source, merge, or release promotion. Store sensitive images, candidate page binaries, screenshots and raw reviewer responses in the authorized private area, not public Git; public Git may retain scripts, sanitized metrics, nonidentifying fixture specs and provenance.

**Next step:** Work should run the bounded DQB-02 against this actual candidate and return first-pass screenshots, blind review packet, outcome/performance log and a proposed integration decision, without asking for more generic web-design research first.
