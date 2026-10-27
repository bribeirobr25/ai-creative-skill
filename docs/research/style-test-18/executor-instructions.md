# Execution instructions — Della Berlin style test

You are the executor of **one** isolated run. All your material is in the working directory assigned to you
(`$RUN`). Work only there.

## What you receive in `$RUN`

- `brief.md`: the brief for a real brand. Follow it fully. It is the only product truth you may use.
- `STYLE.md`: the **visual style assigned by the owner** for this run. It is a fixed creative input, not a suggestion:
  the result must be clearly recognisable as this style at first glance, while still meeting every requirement of the
  brief (content, fidelity, behaviour, accessibility, instrumentation). Where the style and an owner preference in the
  brief conflict, the style wins; say so in `execution.md`.
- `rubric.md`: the criteria the result will be judged by.
- `assets/` and `fonts/`: shared materials.
- `ai-creative-skill/`: the AI Creative Skill methodology you must apply. Start with `ai-creative-skill/SKILL.md`
  and load the references the method itself points to for a website request (`WEB_PREVIEW`). Apply the method as
  written; treat the assigned style as the owner's chosen direction.

## Request

"Create the website described in `brief.md` in the visual style described in `STYLE.md`, with a professional visual
finish, using the materials provided. Deliver a local navigable version."

## Isolation rules

- Read nothing outside `$RUN`: no other runs, reports, Git history or other places on the machine. Do not use `git`.
- No internet (no WebSearch, WebFetch, curl or CDN). No visual references other than what `$RUN` contains.
- Do not load host skills or external design guides. The only methodology is `ai-creative-skill/`.
- Do not generate images, do not edit photo pixels, and do not introduce other images that depict the product,
  people or places. Simple icons, ornaments and patterns you draw yourself in SVG/CSS are allowed. Do not redraw
  brand logos.
- No publication, deploy, paid service or external submission.

## Tools

- Files and shell in `$RUN`.
- Python 3 with Playwright and Chromium installed, to open the site in a browser and take screenshots if your method
  asks for browser verification (`page.goto('file://' + absolute_path)`). You can look at screenshots by opening the
  image files.
- `jsonschema` and `beautifulsoup4` for the method's optional scripts.

## Delivery

- Site in `$RUN/site/` with `index.html` and every local resource (copy only the `assets/` and `fonts/` files you
  use into `site/`). HTML/CSS/JS without framework, dependencies or build. Hash routes or static pages.
- `$RUN/execution.md` (outside the site) with: start and end in UTC; method files you actually read; how the style
  was applied (3–6 concrete decisions); checks performed and their results; known limitations.
- Optional: the method's delivery record and QA evidence in `$RUN/evidence/`.
- Limit: **30 minutes** of active work, including reading the method, building and the internal checks your method
  asks for. There is no prize for speed.
- When finished, reply with the path, approximate time and limitations.
