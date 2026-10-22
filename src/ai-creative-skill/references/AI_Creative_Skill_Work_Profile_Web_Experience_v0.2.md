# WEB_EXPERIENCE · Work Profile v0.2

**Task ownership:** landing page/site research, concept, navigable preview, scoped edit, explicitly authorized publication. Default build path **FAST**, not endless benchmark.

## Host route

`WEB_RESEARCH_ONLY`: research is final deliverable, no code demanded. `WEB_CONCEPT_ONLY`: stop at specified concept/wireframe. `WEB_PREVIEW`: build-first, one functional preview. `WEB_EDIT`: load last accepted or reviewed build and preserve approved regions. `WEB_PUBLICATION`: never inferred from preview; separate domain/privacy/security approval.

**Activate** when final task is a website or landing page, even when the user supplies only a photo, product, service or idea. Consult Project Profile/canon and existing brand/assets; if a single essential action is unknown ask one targeted question. Other reversible choices are creatively open and should be identified as provisional. Never invent prices, product material, awards, testimonials, available features or regulatory approvals.

## Minimal FAST flow

1. Resolve intent and project canon. Create concise `WEB_BRIEF` (product/service truth vs unknown vs inference, audience, single primary action, authority/rights).
2. Use existing research + a few live niche, visual and funnel examples **only if material**. Reference acceptance is per dimension. Do not imitate trade dress.
3. Produce one purposeful `WEB_DIRECTION`: value proposition, section purposes, content and CTA, visual language and optional motion. Preserve brand authority; do not require full brand guidelines before draft.
4. Plan/reuse/create minimum assets. Asset existence is not approval, and approval is scoped by use. Never imply rights from an external inspiration site. Paid generation requires authorization.
5. **Build a working site** using host tools (HTML/CSS/JS or framework as appropriate). Responsive desktop/mobile, working navigation and honest CTAs are minimum. Motion must respect reduced motion and content legibility. A calculated-on-device form is `LOCAL_CALCULATION`, not lead capture or a mock. Avoid fake successful signups/checkout.
6. Host preview using supported environment (if permitted use `python scripts/creative_web.py preview start <site_dir>`). Without a host preview server, the built `index.html` opened in a browser (`file://`) is a valid local preview: give the reopen instruction (path relative to the delivery); hash routes work offline. Do not present a screenshot or code as an interactive preview. Verify exact URL/process and ability to reopen; ephemeral links are not persistent.
7. QA from the same build version using browser when available: `python scripts/creative_web.py audit <site_dir> --output <evidence_dir> [--project-root <root>]` opens the page itself (`--url` for a preview server, otherwise `file://`); collapsed images (laid out but drawn under 16 px) fail `images_rendered`. Register `WEB_QA` evidence by check_id, mode, requirement, result, build hash, screenshot/trace and tested viewport. `STATIC_INSPECTED` is not `BROWSER_OBSERVED`; missing browser tests remain `NOT_TESTED`. Judge per-viewport captures, not only full-page ones (fixed headers and lazy images distort full-page captures), and never change the site only to please a capture tool. Distinguish QA `PASS/PARTIAL/BLOCKED/UNVERIFIED` from user approval.
8. Write the delivery record, which is mandatory: `creative_web.py record <site_dir> --qa <evidence_dir>/qa_matrix.json --output <record.json> [--project-root <root>]`, fill every `TODO`, then `creative_web.py validate <record.json> --site-dir <site_dir> [--project-root <root>]` must report no errors. A delivery without a valid record is incomplete. Then deliver real preview + files, key decisions and requested feedback opportunity. Stop. Only proceed with revision/publication on new authority.

## Contracts, tooling and operational boundaries

- Source of truth for records: `web/schemas/web_delivery_v0.2.schema.json`; validate via `scripts/creative_web.py validate ...`. No free-text status enum; use canonical `BRIEF_RECOVERED`, `DIRECTION_PROVISIONAL`, `PREVIEW_DRAFT`, etc. Legacy v0.1 aliases require explicit migration.
- A deterministic route checker is a helper, **not** a semantic agent. Host skill must still infer user intent and select method stack. `scripts/creative_web.py route` supports explicit --intent when necessary.
- Owner-only preview lifecycle: `preview start/status/restart/stop`. Do not kill unrelated processes or expose local files/secrets.
- `WEB_EDIT`: register approved region/attributes and snapshot, modify only permissible surface, compare shared CSS/JS dependencies, invalidate affected QA, present diff. Code/hash-only evidence does not certify pixels or behavior.
- Evaluate differences at 1440 and 390px when possible, and check 320px for horizontal overflow; test 768px if useful. Scroll the full page before judging images, so lazy-loaded media is actually rendered. Keyboard dialog focus/Shift+Tab/Escape, image crop, no overflow, form truth and CTA are specific risks from Della/diBoaS pilots. Motion/reduced motion require observed testing to claim PASS. Do not put `crossorigin` on local font preloads: under `file://` it logs a console error while the font loads anyway.
- Respect provider, spending, privacy and publication gates in the inherited Execution Contracts. Tool availability never grants spend or deploy authority.

## Validated evidence / what remains open

Pilots Della and diBoaS produced real sites using these specifications **manually** with host tools and the Sites skill. Web v0.2 deterministic tests and migrated records passed, but web builder auto-activation in a fresh host, live browser QA where blocked, and a human-approved scoped edit remain unresolved. Never claim an automatic agent integration was already demonstrated.

Supporting docs: `web/docs/DELTA_AND_GATES.md`; `web/README_PTBR.md`.
