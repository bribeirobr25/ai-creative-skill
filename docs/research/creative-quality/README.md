# Creative Quality Gap Assessment — Issue #8

Research candidate, 20 October 2026. **No release, production approval or canon change.**

The user's assessment is the starting signal: Higgsfield looks better in product photos, hyper-motion and websites; the 30-second commercial looks roughly comparable. This investigation preserves that feedback without treating it as a controlled causal verdict.

## Executive decision

**The clearest demonstrated improvement is the review loop, not a new model or longer prompt.** An isolated art-direction change made the desktop hero more immersive but collapsed its mobile image to **6.59 px**. Navigation, gallery, image loading and overflow probes still passed. Screenshot inspection identified the defect; a localized CSS repair restored the image to **219.13 px**, with unchanged HTML, JavaScript and all 16 image files. The final variant passed 26 bounded browser assertions across desktop/mobile. Human preference and commercial approval remain open.

Do not claim that our methods already match Higgsfield because similar rules exist in documentation. Equally, do not conclude that a new provider is necessary: the website experiment changed presentation materially with the **same assets, text, browser and tools**, without generation.

The research branch starts at `main` **39a0bfa39270ea4b685b0f862e7dbf647cf81d77**, skill 2.5.0 / plugin 0.3.0. PRs #2, #5, #6 and #7 were inspected and left untouched. The earlier handoff prioritizes Reframe; the current user instruction supersedes that sequencing and assigns Issue #8. Technical records live here; private website copies and screenshots remain outside public Git.

## Evidence and deliverables

| Deliverable | Record |
|---|---|
| Assessment / executive decisions | This file |
| Comparison methodology, acceptance and rubric | [Evaluation framework](evaluation.md) |
| Executed website experiment / metrics | [Web experiment](web-experiment.md) |
| Image, motion and commercial observations | [Media assessment](media-assessment.md) |
| Coverage of five possible gaps | [Capability matrix](capability-matrix.md) |
| Narrow integration proposals | [Method proposals](method-proposals.md) |
| Browser collection, reproducible CSS treatments, harness adapter | [Validation adapter](../../../validation/creative_quality/README.md) |
| Public bounded results and screenshot fingerprints | [Browser summary](../../../validation/creative_quality/results/browser-summary.json) |
| Private visual evidence | Logical bundle `CQ8-PRIVATE-20261020`; supplied to owner separately, not linked publicly |

## What explains the perceived difference?

**Observed in the selected artifacts:** M044 uses oversized custom-looking brand typography, a full-width fashion composition, a restrained black/lime palette, coordinated product imagery and compact catalog/detail/cart transitions. Both archived pilots use a familiar text-left/image-right opening followed by relatively regular sections. Their brands, purposes and input assets differ: diBoaS explains a financial-life concept and a calculator; Della presents pouches and an Instagram handoff; the exemplar is a fashion storefront. Those are material confounders, not excuses to ignore design quality.

**Demonstrated locally:** CSS hierarchy, image allocation and review can change the result without replacing assets or buying generation. The mobile regression and repair have a direct code-level cause. This establishes the value of rendered review and case-specific visual assertions. It does **not** isolate the causal contribution of a prose method, estimate conversion lift, or show that C universally beats A.

**Still inconclusive:** the vendor's model advantage, generation success rate, retries, full production cost, source code, mobile behavior, accessibility and backend operation. M044 is only a screen recording. No interactive website was invented or reconstructed as evidence of the original.

## Findings ranked

| ID | Priority | Finding and confidence | Consequence |
|---|---|---|---|
| Q01 | High | Archive delivery records explicitly say manual host execution of an experimental pre-V2.5 web specification. Confirmed. | Treat pilots as historical outputs, not a controlled execution test of installed V2.5. |
| Q02 | High | Functional probes missed B's collapsed mobile hero; screenshot review and a targeted height assertion caught it. Confirmed. | Keep functional, visual and human acceptance separate. |
| Q03 | High | A/B/C preserve source text, app behavior and asset bytes; CSS alone changes the composition. Confirmed. | Prioritize practical art direction and a bounded visual revision loop. |
| Q04 | High | Our retrieved image/video directions already specify lighting, material, camera, reference roles and variation. Confirmed documentation; effect not isolated. | Reject “just add more detailed prompts” as a sufficient diagnosis. |
| Q05 | Medium | Selected vendor fashion images vary angle, gesture, light and scene more than the three selected pouch editorials. Reviewer observation. | Test an intentional range of compositions appropriate to each product, not the vendor's exact aesthetic. |
| Q06 | High | Vendor motion is 1920×1080; our closest retrieved motion is 480×854 draft. Confirmed metadata. | Separate resolution/finishing from creative method. No matched-quality causal ranking. |
| Q07 | High | Five opportunities have reusable methods but no evidence here of complete, independent, installed journeys. Bounded repository audit. | Map concrete deliverables and adapters before adding capabilities or profiles. |

## What we already do well

The existing pilots have real navigation, responsive layouts, local assets, honest action boundaries and usable product galleries/calculation. The retrieved pouch editorials already have coherent warm light, legible main labels and consistent visual language. The narrative café commercial has coherent setting, shot/reverse-shot coverage and recurring characters in sampled frames. These are observed strengths, not proof of equality across all dimensions. The user's commercial-parity judgment remains a human observation, not a newly certified result.

## Implement first

1. Add a small **visual review checkpoint** to the existing Web Experience method: inspect the primary image, text/CTA hierarchy and one critical interaction at target viewports; compare actual rendering with direction; repair locally; recheck affected regions.
2. Make `WEB_DIRECTION` concrete enough to state one intended visual distinction and one observable success condition. Do not add a new contract or force a moodboard into every request.
3. Reuse Image Direction's protected/open dimensions and category-aware lighting. Test variation and outcome review rather than duplicating “Product Read” as another authority.
4. Keep generated end cards, logos and publication specifications independently checked. Aesthetic approval does not erase a mismatch against the delivery contract.

Do not import third-party skill text, mandate eight-panel storyboards, force casting, treat 50 emails/day as consent, or create a universal “Higgsfield look.” Do not enlarge the router or add Work Profiles for these recipes.

## Next highest-value validation

Obtain **two independent human paired reviews** of A and C at equal scale, randomized labels, separately rating composition, fidelity and usefulness. Reviewers must also see a short functional walkthrough. No such reviews occurred in this run. If preference supports C without fidelity regressions, repeat on a fictional unrelated category, holding assets, brief, tool and one revision allowance fixed. This tests transfer before changing the installed method. A second paid media generation is lower priority than this free human validation.

## Sources and limits

- [Issue #8](https://github.com/bribeirobr25/ai-creative-skill/issues/8), full body read; no prior comments at start.
- [Higgsfield article](https://higgsfield.ai/@adilinthewildtempo/blogs/5-ai-side-hustles), previous complete study and current source media reinspection; selected marketing exemplars, no reuse license established.
- Private owner-provided website archives, historical project prompts and approved media; logical IDs and hashes, no private links/source code/assets in Git.
- [Web profile](../../../src/ai-creative-skill/references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md), [release gates](../../../src/ai-creative-skill/references/AI_Creative_Skill_Release_Gates_v2.5.md), and methods linked in the proposals.

Single agent/operator review, not blind and not independent. Browser coverage is Chromium emulation, not physical-device or screen-reader certification. Media sampling is explicitly bounded; continuous temporal/audio perception remains unverified. No model generation, paid operation, publication, email, canon edit, installed-skill replacement or merge occurred. A price-only quote used no media uploads or job submission.
