# Web Experience — executed A/B/C experiment

## Design and provenance

A = private archived Della preview; D = archived diBoaS preview; B = A + `direction-b.css`; C = B + `repair-c.css`. The original archives and extracted baseline remain unchanged. B/C are isolated local copies. All content, links, JavaScript and 16 image files are byte-identical to A; only the copied stylesheet changes. `prepare.py` independently reproduced both variants byte-for-byte.

Archive hashes:
- WEB-ARCHIVE-A: `2f4b3a6733875d0139b6b87464ea3100d413d54c38aff2f9659b0500412df6a1`
- WEB-ARCHIVE-D: `3ce3b141a5ebb0e3dccd2559d861662d4127dd08d8f6a28c01bb15ee30674a9f`

**Hypothesis:** a more explicit image-led hierarchy plus one visual repair pass can improve the perceived composition without generating assets or changing brand/content. This is an iterative implementation experiment, not randomized generation A/B. C receives the planned review pass, so its extra work is part of the intervention, not hidden equal-effort evidence. The original sites' production effort and vendor attempts are UNKNOWN.

## Observed comparison

| Artifact | Desktop observation | Mobile observation / limitation |
|---|---|---|
| A | Warm editorial identity, serif hierarchy and clear CTA; conventional split hero; photographs from different original environments in catalog | Product begins at y=429; large image but narrow crop; CTA at y=348; no overflow |
| D | Coherent teal/Instrument Sans system, visible calculator goal, real local calculation; familiar split layout | Intro dominates first screen; image begins near y=595; long page (~6004px), no overflow |
| M044 | Oversized brand letterforms, overlapping fashion subject, high contrast, coordinated catalogue images, visible modal/cart transitions | No mobile source or interactive build available. Screen recording only; not tested as a website |
| B | Full-width photograph, enlarged headline and more consistent catalog proportions; gradient washes part of product field | Image collapsed to 6.59px due to inherited absolute positioning/max-height. Reject this candidate |
| C | Hero image repositioned to the right, gradient away from main product field, headline/subject separated | Restored full-width image in normal flow at y=82; 219px high; CTA at y=588; no overflow |

Automated reviewer's aesthetic judgment: A=3/5 coherent draft, D=3/5 coherent explanatory draft, B desktop=3/5 but **mobile=1/5**, C=4/5 in observed composition. M044=4/5 for the visible desktop presentation only. These are **one reviewer's ordinal judgments**, not independent acceptance or proof of equality. C's earlier product visibility trades off against a later CTA; no conversion superiority is claimed. The softer Della style and diBoaS purpose should not be replaced by streetwear aesthetics.

### Why the presentation feels different

| Criterion | A / D and the controlled C treatment | M044 observation and comparison limit |
|---|---|---|
| Hierarchy and typography | A's editorial serif and D's tight sans heading are already intentional. Their opening uses a familiar two-column hierarchy. C increases the photograph's share of the desktop field and keeps a distinct text region | At 0.50s, the enormous HIGGS lettering becomes the spatial composition itself, behind the model. This is a stronger visual signature, not merely a different font |
| Spacing and rhythm | Both pilots repeat generous section spacing. D has explanatory blocks, calculator, a darker Practice section and FAQ; C retains those content decisions for Della and tightens the catalog image proportions | At 7.96s and 10.45s the recording alternates a dark editorial frame with a dense, pale product grid. That contrast creates rhythm; it cannot prove better reading or conversion |
| Images and composition | Della's generated hero is coherent, but the six catalog photos have varied lighting/backgrounds. CSS can align frames, not make those photographs a coordinated campaign. C's mobile image shows the full scene earlier and at smaller detail scale | M044's cutout hero, coordinated black/lime clothing and consistent product backgrounds support the layout before any UI code. Asset preparation is a plausible contributor, not a controlled causal finding |
| Brand, colors and contrast | Cream, cocoa and warm imagery remain Della's language; teal and restrained illustration remain diBoaS's. C preserves those colors and brand bytes. Contrast ratios were not comprehensively measured | Black/lime/off-white creates strong visible separation. Importing it into the two pilot brands would not constitute quality improvement by itself |
| Navigation, CTA and components | Gallery controls, filters, menus and calculator were actually exercised. C keeps the same actions; its CTA moves down on mobile. Images, captions, borders and button alignment were visually inspected | Recording shows catalog at 15.43s, product detail at 20.41s, cart at 22.90s and order form at 25.39s. This demonstrates a presented flow, not verified checkout or usable keyboard navigation |
| Microinteractions and movement | Pilot reveal effects and hover styling exist; runtime reduced-motion behavior passed the bounded check. The final collector scrolls instantly between observation positions so smooth scrolling cannot conceal unreached sections | Lime letter highlights are visible around 2.99s and modal transitions later. Timing, keyboard parity and reduced-motion behavior were not independently tested |
| Responsive finish and accessibility | Real 390px captures found and repaired B's collapse; no horizontal overflow in final cases. Focus/Escape checks are narrower than full accessibility conformance. Physical devices and screen readers were not tested | No mobile rendering, semantic DOM or accessibility evidence is available |
| Performance and efficiency | Same local image bytes in A/B/C; C adds 3,839 CSS bytes. Resource totals below are observed, not speed scores. One B→C correction pass; original and vendor production time unknown | A recording cannot establish asset weight, runtime cost, speed or number of creative retries |

## Concrete metric changes

| Metric | A | B | C |
|---|---:|---:|---:|
| Desktop hero image box | 746.92×530px | 1440×766px | 1036.80×796px |
| Mobile hero top / height | 429.02 / 340px | 82 / 6.59px | 82 / 219.13px |
| Mobile CTA top | 348.02px | 390.77px | 588.17px |
| Desktop full page height | 4413px | 4860px | 4860px |
| Mobile full page height | 4568px | 4349px | 4536px |
| Desktop resources transferred during controlled scroll | 1,425,920 bytes | 1,428,860 bytes | 1,429,759 bytes |
| New image/model calls | 0 | 0 | 0 |

Transfer sizes are one local run, include resource response overhead and observed lazy loads, not a network-speed benchmark or Core Web Vitals result. The CSS payload adds 3,839 bytes from A to C; image bytes are unchanged. D's observed transfer total was 340,155 bytes. Different content volumes prevent a direct efficiency ranking. No total labor-cost estimate is invented.

## Failure and correction record

B inherited `.hero-visual > img { position:absolute; max-height:calc(100% - 30px) }` while its mobile figure used automatic height. The image remained decoded but contributed no height to the parent; resulting height was 6.59375px. The initial functional suite missed it. C sets `position:relative`, clears inset/max-height, retains natural aspect ratio, and adjusts only local spacing. Desktop C reduces overlap by moving the image field and narrowing the gradient.

The early collector also falsely called a CSS-hidden image and pending lazy footer images “broken.” That was an **instrumentation defect**, not a site defect. The collector was corrected to await visible-image decoding and list hidden images separately. Initial raw captures are retained privately; final same-version runs supersede them. This correction was applied equally to A, B, C and D.

Full-page review then exposed a second capture issue: repeated `scrollTo` calls inherited smooth scrolling and did not reach every reveal section before the screenshot. The collector now uses explicit instant positioning with a short observation wait. All eight cases were recaptured with this version; final screenshots show the actual revealed content. No site CSS or JavaScript was changed to manufacture a screenshot. The original intermediate captures remain private and are not the canonical review packet.

## Browser QA and acceptance

Final run: **100 assertions: 99 PASS, 1 FAIL**. The failure remains B-mobile hero collapse. A:26/26; B:25/26; C:26/26; D:22/22. Scope: loaded visible images, no horizontal overflow, product filtering, gallery navigation, dialog open/focus/Escape, mobile menu/Escape, calculator valid/invalid cases, tabs keyboard, runtime reduced-motion, script/resource errors and external network attempts. External network was blocked; none was requested. Instagram destination was inspected, not contacted; payments/publication were not tested or executed.

Screenshots: hero, full page, and gallery interaction for A/B/C at both widths; hero/full page for D. All fingerprints recorded in public results; image bytes are private. Browser emulation is not a screen-reader/contrast certification. No automated claim of professional quality. Source preservation is necessary but CSS crops and overlays also require visual review.

The existing integrated `web/runtime/revision.py` helper was also run on A→C across hero,
collection, product editorial, details and contact. It reports protected source regions
unchanged and **PARTIAL**, because shared CSS changed and browser retesting is required.
That result is preserved in [source-preservation.json](../../../validation/creative_quality/results/source-preservation.json);
the separate actual browser evidence supplies the requested retest without rewriting the
helper's status or treating it as aesthetic approval.

## Reproducibility

See [adapter instructions](../../../validation/creative_quality/README.md). Scripts use the existing validation harness's `outcome` helper from PR #7's pinned checkout, without changing it or rerunning its unrelated audit. The experiment is based on integrated main; harness infrastructure remains an external development dependency until its own PR integrates. Source tree `src/` remains unchanged.
