# Common execution instructions — DQB-03

You are the executor of **one** isolated run. All your material is in the working directory assigned to you
(`$RUN`). Work only there.

## What you receive in `$RUN`

- `brief.md`: the fixed brief for a real brand. Follow it fully. It is the only product truth you may use.
- `rubric.md`: the criteria the result will be judged by.
- `assets/` and `fonts/`: shared materials.
- `ai-creative-skill/`: the AI Creative Skill methodology you must apply. Start with `ai-creative-skill/SKILL.md`
  and load the references the method itself points to for a website request (`WEB_PREVIEW`). Apply the method as
  written; do not add rules from other sources.

## Request

"Create the website described in `brief.md`, with a professional visual finish, using the materials provided.
Deliver a local navigable version."

## Isolation and parity rules

- Read nothing outside `$RUN`: no other runs, branches, reports, Git history, other repository directories or other
  places on the machine. Do not use `git`.
- No internet (no WebSearch, WebFetch, curl or CDN). No visual references other than what `$RUN` contains.
- Do not load host skills or external design guides. The only methodology is `ai-creative-skill/`.
- Do not generate images, do not edit photo pixels, and do not introduce other images that depict the product,
  people or places. Simple icons or ornaments you draw yourself in SVG are allowed. Do not redraw brand logos.
- No publication, deploy, paid service or external submission.

## Tools (identical for every run)

- Files and shell in `$RUN`.
- Python 3 with Playwright and Chromium installed, to open the site in a browser and take screenshots if your method
  asks for browser verification. Minimal example: `python3 -c "from playwright.sync_api import sync_playwright as p; ..."`
  with `page.goto('file://' + absolute_path)`. You can look at screenshots by opening the image files.
- `jsonschema` and `beautifulsoup4` for the method's optional scripts.

## R0 delivery

- Site in `$RUN/r0/` with `index.html` and every local resource (copy `assets/` and, if used, `fonts/` into `r0/`).
  HTML/CSS/JS without framework, dependencies or build. Hash routes or static pages.
- `$RUN/execution.md` (outside the site) with: start and end in UTC; method files you actually read (with excerpts if
  you read partially); direction decisions; checks performed and their results; known limitations.
- Optional: the method's delivery record (for example `web-delivery-r0.json`) and QA evidence in `$RUN/evidence-r0/`.
- Limit: **30 minutes** of active work for R0, including reading the method, building and the internal checks your
  method asks for. There is no prize for speed.
- When finished, **do not modify `r0/` again**. Reply with the path, approximate time and limitations. Wait: there
  may be one later review round.
