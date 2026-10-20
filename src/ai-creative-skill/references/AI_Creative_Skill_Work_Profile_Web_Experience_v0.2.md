# WEB_EXPERIENCE · Work Profile v0.2

**EXPERIMENTAL CANDIDATE — NOT RELEASED OR VALIDATED FOR SUPERIOR DESIGN.** This branch tests a minimal Web visual-direction and critique delta while preserving the V2.5 `main` attestation. Do not describe it as installed or production-approved.

**Task ownership:** landing page/site research, concept, navigable preview, scoped edit, explicitly authorized publication. Default build path **FAST**, not endless benchmark.

## Host route

`WEB_RESEARCH_ONLY`: research is final deliverable, no code demanded. `WEB_CONCEPT_ONLY`: stop at specified concept/wireframe. `WEB_PREVIEW`: build-first, one functional preview. `WEB_EDIT`: load last accepted or reviewed build and preserve approved regions. `WEB_PUBLICATION`: never inferred from preview; separate domain/privacy/security approval.

**Activate** when final task is a website or landing page, even when the user supplies only a photo, product, service or idea. Consult Project Profile/canon and existing brand/assets; if a single essential action is unknown ask one targeted question. Other reversible choices are creatively open and should be identified as provisional. Never invent prices, product material, awards, testimonials, available features or regulatory approvals.

## Minimal FAST flow

1. Resolve intent and project canon. Create concise `WEB_BRIEF` (product/service truth vs unknown vs inference, audience, single primary action, authority/rights).
2. Use existing research + a few live niche, visual and funnel examples **only if material**. Reference acceptance is per dimension. Do not imitate trade dress.
3. Produce one purposeful `WEB_DIRECTION`: value proposition, section purposes, content and CTA, visual language and optional motion. When visual distinctiveness materially matters, specify **one brief-specific composition decision** (focal element, relationship between typography/images/actions, and intended hierarchy), **one expected observable consequence** on desktop/mobile, and **one explicit tradeoff**. Accept visual references by *dimension and purpose*, recording what must not be inherited; consult only relevant references, never apply a style-family preset by industry. Reuse `visual_direction`, `approved_reference_scope`, `creative_open_zones` and existing brief/brand fields; no mandatory extra form, style research or approval pause. Preserve brand authority; do not require full brand guidelines before draft.
4. Plan/reuse/create minimum assets. Asset existence is not approval, and approval is scoped by use. Never imply rights from an external inspiration site. Paid generation requires authorization.
5. **Build a working site** using host tools (HTML/CSS/JS or framework as appropriate). Responsive desktop/mobile, working navigation and honest CTAs are minimum. Motion must respect reduced motion and content legibility. A calculated-on-device form is `LOCAL_CALCULATION`, not lead capture or a mock. Avoid fake successful signups/checkout.
6. Host preview using supported environment (if permitted use `python scripts/creative_web.py preview start <site_dir>`). Do not present a screenshot or code as an interactive preview. Verify exact URL/process and ability to reopen; ephemeral links are not persistent.
7. QA from the same build version using browser when available; register `WEB_QA` evidence by check_id, mode, requirement, result, build hash, screenshot/trace and tested viewport. **When visual presentation matters**, compare the actual homepage, relevant inner page(s) and one task-critical interaction at the requested desktop/mobile sizes with the intended focal point, hierarchy and brand constraints. Distinguish an objective visibility/function/fidelity defect, a failure of the selected visual direction, and a legitimate aesthetic preference; assess product prominence **and** CTA discoverability without a universal pixel threshold. For a material defect, record the affected screen and effect, repair the smallest permitted surface via `WEB_EDIT`, and repeat affected visual and functional checks within authorized time/cost. If no relevant defect is found, do not invent an extra revision. `STATIC_INSPECTED` is not `BROWSER_OBSERVED`; automated or agent critique is not independent human quality approval; missing browser tests remain `NOT_TESTED`. Distinguish QA `PASS/PARTIAL/BLOCKED/UNVERIFIED` from user approval.
8. Deliver real preview + files, key decisions and requested feedback opportunity. Stop. Only proceed with revision/publication on new authority.

## Contracts, tooling and operational boundaries

- Source of truth for records: `web/schemas/web_delivery_v0.2.schema.json`; validate via `scripts/creative_web.py validate ...`. No free-text status enum; use canonical `BRIEF_RECOVERED`, `DIRECTION_PROVISIONAL`, `PREVIEW_DRAFT`, etc. Legacy v0.1 aliases require explicit migration.
- A deterministic route checker is a helper, **not** a semantic agent. Host skill must still infer user intent and select method stack. `scripts/creative_web.py route` supports explicit --intent when necessary.
- Owner-only preview lifecycle: `preview start/status/restart/stop`. Do not kill unrelated processes or expose local files/secrets.
- `WEB_EDIT`: register approved region/attributes and snapshot, modify only permissible surface, compare shared CSS/JS dependencies, invalidate affected QA, present diff. Code/hash-only evidence does not certify pixels or behavior.
- Evaluate differences at 1440 and 390px when possible; test 768px if useful. Keyboard dialog focus/Shift+Tab/Escape, image crop, no overflow, form truth and CTA are specific risks from Della/diBoaS pilots. Motion/reduced motion require observed testing to claim PASS.
- Respect provider, spending, privacy and publication gates in the inherited Execution Contracts. Tool availability never grants spend or deploy authority.

## Validated evidence / what remains open

Pilots Della and diBoaS produced real sites using these specifications **manually** with host tools and the Sites skill. Web v0.2 deterministic tests and migrated records passed, but web builder auto-activation in a fresh host, live browser QA where blocked, and a human-approved scoped edit remain unresolved. Never claim an automatic agent integration was already demonstrated.

Supporting docs: `web/docs/DELTA_AND_GATES.md`; `web/README_PTBR.md`.
