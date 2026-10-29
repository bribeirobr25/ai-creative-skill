# Third-party notices

The repository's own content is "all rights reserved" (see `LICENSE`). The items below are third-party material, which stays under its own license.

**Status:** inventory as of 2026-10-28. The rights review of sources with no declared license (§5) is **not finished**.

## 1. Code included in the skill package

| Component | Where | License |
|---|---|---|
| Real-ESRGAN, SRVGG network architecture | `src/ai-creative-skill/media/runtime/srvgg_arch.py` | BSD-3-Clause, Copyright (c) 2021 Xintao Wang. Full text in `src/ai-creative-skill/media/runtime/LICENSE_RealESRGAN`. |

The model weights are **not** shipped (`src/ai-creative-skill/media/models/README.md`).

## 2. Fonts used by validation fixtures

`validation/dqb02/shared/fonts/` holds fonts under the SIL Open Font License 1.1. Each license text is in `validation/dqb02/shared/fonts/licenses/`.

| Font | Copyright |
|---|---|
| Bricolage Grotesque | 2022 The Bricolage Grotesque Project Authors |
| Fraunces | 2020 The Fraunces Project Authors |
| IBM Plex Mono | 2017 IBM Corp. |
| Instrument Sans | 2022 The Instrument Sans Project Authors |
| Inter | 2016 The Inter Project Authors |
| Newsreader | 2020 The Newsreader Project Authors |

## 3. Photos in validation material

The benchmark material in `validation/dqb01/` and `validation/dqb02/` uses or shows photos under the Pexels License. That includes screenshots of benchmark pages in `validation/dqb02/results/comparisons/`. Authors and sources are listed in the `credits.json` files next to the assets, for example `validation/dqb01/shared/assets/credits.json`.

## 4. Method material adapted from licensed packages

Parts of the method references in `src/ai-creative-skill/references/` adapt ideas from the packages below. `AI_Creative_Skill_Method_Provenance_Map_Pre-v0.30.md` records the full lineage and what was adapted. The notices are reproduced here as a precaution.

**MIT License:**

| Package | Copyright |
|---|---|
| blader/humanizer v3.1.0 | Copyright (c) 2025 Siqi Chen |
| petergyang/no-ai-slop v1.0.6 | Copyright (c) 2026 Peter Yang |
| mvanhorn/last30days-skill v3.26.0 | Copyright (c) 2026 Matt Van Horn |
| bradautomates/claude-video v0.3.2 | Copyright (c) 2026 Bradley Bonanno |
| Motion OS | Copyright (c) 2026 Jason Lee |
| A video-to-guide package (README declares MIT; no standalone license file) | Author not recorded |

The MIT permission notice that applies to each of them:

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**Apache License 2.0:**

- heygen-com/hyperframes v0.8.135. It was used as a finishing-method reference; no runtime from it is installed. License text: <https://www.apache.org/licenses/LICENSE-2.0>.

**Custom license:**

- Remotion, probable revision 4.0.533. It was used as a narrow tooling reference; no runtime from it is installed. Whether its license allows this use is **unresolved**.

## 5. Sources with no declared license (rights review open)

The Provenance Map (§4) says material from these sources must be rewritten, or its rights confirmed, before the package is distributed:

- create-ads-with-agents v2.1.2;
- the RoboNuggets "Build Your Own /generate Skill" guide;
- an agent-organization package;
- ai-short-form-video;
- The Vibe Marketer "3 Free Skills (v2)", including content-atomizer;
- a team skill-distribution guide (PDF);
- two companion packages of the Motion OS group.

That review is **open**.

## 6. Known gaps

- This file sits at the repository root. The shipped skill package (`src/ai-creative-skill/`) doesn't include it yet. Adding a file there needs a new source candidate, because the candidate-integrity check rejects added files.
- Some older validation records describe the repository as MIT-licensed, for example "Not repository MIT assets" in the DQB-01 `credits.json` files. Those are dated records. They are superseded by `LICENSE`, and they are left unchanged because they record the state at the time.
