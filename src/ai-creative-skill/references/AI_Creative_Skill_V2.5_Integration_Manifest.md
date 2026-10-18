# AI Creative Skill · V2.5 Integrated Release Manifest

Version: **2.5.0**, packaged plugin version **0.3.0**. Built 2026-10-18.

## Authority and version resolution

1. This document is the release overlay authority for *two newly installed capability routes*: `WEB_EXPERIENCE` and `MEDIA_UPSCALE`.
2. All inherited V2.4 subjects, profiles, methods and hard gates remain governed by the unchanged `AI_Creative_Skill_Current_Design_Manifest_Pre-v0.40-V2.4-CANDIDATE.md` and its exact filenames. V2.5 does NOT retroactively convert pilot experiments into project canon.
3. `SKILL.md` is the new routing entrypoint. References below are load-on-demand and are not global prerequisites for unrelated tasks.

## New references and execution

- `AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md`: WEB_RESEARCH_ONLY / WEB_CONCEPT_ONLY / WEB_PREVIEW / WEB_EDIT / WEB_PUBLICATION.
- `AI_Creative_Skill_Method_Media_Upscale_v0.3.md`: IMAGE_UPSCALE / VIDEO_UPSCALE.
- `AI_Creative_Skill_Release_Gates_v2.5.md`: status and validation limits.
- `web/runtime/`, `web/schemas/`, `scripts/creative_web.py`: deterministic helper, contract validation, preview/QA and local-preservation tools. A host with file editing/browser tools still builds and inspects the real website.
- `media/runtime/`, `media/registry/`, `scripts/creative_media.py`: local Pillow/FFmpeg and optional Real-ESRGAN processing; models are never required for other skill capabilities.

## Status gates (honest)

- *Installable build*: packaged and structurally tested. **Not** proof of clean-host automatic web building.
- *Web runtime*: route, schema, preview lifecycle and static QA are executable locally. Browser-dependent validation requires an eligible host.
- *Media conventional*: executable where Pillow/FFmpeg exist.
- *Neural routes*: **experimental**, require user-supplied verified official checkpoints and suitable resources; technical QA does not confer fidelity approval.
- *Paid integrations*: no commercial route is installed here; provider entries tagged MOCK must never submit paid calls.
- *Publication*: separate explicit authorization; preview is not live website.

Previous V2.4 packages and `00_ACTIVE` are not overwritten by the creation of this release package.
