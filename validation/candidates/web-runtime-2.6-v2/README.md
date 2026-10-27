# Web runtime 2.6 v2 — review candidate, not a release

**Status:** active source candidate (2.6.0-dev). Parent: [web-runtime-2.6-v1](../web-runtime-2.6-v1/README.md), whose records
stay byte-identical to the commit that reviewed them (`0f7089a`). Release approval: **false**.

v2 adds items 2–8 of the October 2026 learnings audit (a repository research record that lands through the research
PRs). The evidence comes from the DQB-03 benchmark, a product-photoshoot prompt study and an 18-style site test. v2 adds
no files to the skill, generates no media, calls no paid provider and promotes no release.

## Scope added over v1 (cumulative)

| File | Change | Evidence |
|---|---|---|
| `web/runtime/qa.py` | **Collapsed images** fail `images_rendered` at 1440 and 390: a drawn side under 2 px, a side under 16 px with the aspect distorted more than 2×, or a sized image clipped by a collapsed overflow container. Hidden images (display, visibility, opacity), clipped sr-only images and small icons drawn at their own aspect are not flagged. **file:// audit:** without `--url` the browser opens the built `index.html`; pages that use ES modules, `fetch`/XHR or dynamic `import()`, or that raise file-incompatibility errors, keep the browser checks `NOT_TESTED` with "needs an HTTP preview (--url)". A page with no visible text or images fails `browser_render`. Captures are clipped at 16 000 px and each viewport fails independently, so one slow viewport no longer discards the others. Evidence never carries local paths: over HTTP the image actually requested is named (relative to the page), under `file://` the authored `src` or first `srcset` URL; `redact` converts `file:` URIs (percent-encoded, Windows drives) and replaces known roots only as whole absolute-path prefixes. Canvas, SVG and video count as visible content. `srcset` parsing keeps `data:` URLs whole and drops them from the asset list. `draft_record()` writes a delivery-record draft from one QA run, refuses a QA matrix from another build, lists `src`, `srcset` and root-relative images, and gives HTTP open instructions when the page needs them. `browser=False` keeps an audit static even with a URL. | Style test: a site passed its own 62 checks with six product images collapsed to 0 px; 17 of 18 executors skipped the record and all 18 skipped the preview server. Review probes: path leaks under `file://`, blank module/fetch pages reported as PASS, icon false positives, flaky long-page capture. |
| `web/runtime/validate.py` | `UNFILLED_FIELD` for any value that starts with the `TODO:` marker (case-insensitive, ignoring zero-width characters), reported together with schema errors. Words such as "Todos" or a `todo-app` folder are not flagged. | Same. |
| `web/runtime/cli.py` | `record <site_dir> --qa <qa_matrix.json> --output <record.json> [--project-root] [--project]`; `audit --static-only` (honoured with `--url`). | — |
| `web/runtime/migrate.py` | The legacy migration scaffold stays static with the reason "Legacy migration: browser checks not re-run". | Keeps the v0.2 migration semantics. |
| `references/…Work_Profile_Web_Experience_v0.2.md` | Step 6: `file://` is a valid local preview only without modules, `fetch`/XHR or dynamic `import()`. Step 7: the audit command, collapsed-image rule, per-viewport captures, never changing the site to please a capture tool. Step 8: mandatory record with the full `python scripts/creative_web.py` commands. QA note: keep `crossorigin` on font preloads; the `file://` console error is harmless. | Style test. |
| `references/…Method_Route_Compilation…md` §7.2 | Derived one-product crops are required when the route receives only whole images (e.g. GPT Image through a custom GPT in ChatGPT); capability mismatch only when nothing can be isolated; resampling only for provider input limits, recorded. | Blind review of two prompt packs for the same product photos (October 2026): reference selection 4/5 with crops vs 2/5 without. |
| `references/…Method_Image_Direction…md` §5.1, §9.1, §10 | Declared fact contradicted by the photos is a conflict, not a fact. Applied labels drawn small (inferred starting threshold ≈120 px in a 1024–1536 px output) get a real-label composite; large generated labels pass only after a 3× zoom check. §10 points to the crop rule. | One photoshoot: 11/11 multi-product labels and 3/25 small single-shot labels garbled, large ones correct; two input errors reached executors. |
| `references/…Method_Localized_Repair…md` §6.2 | Label text on a product: the real-label composite is the default repair; regenerating is a fallback. | 14/14 garbled labels fixed without new generations. |

Known limits, by design:
- Panels the page declares closed are not checked for collapse: `hidden`, `inert`, `aria-hidden="true"`,
  `role="tabpanel"`, or the target of `aria-controls` on an element with `aria-expanded="false"`. A collapsed box with
  no such state (a 0-height wrapper, or a `grid-template-rows: 0fr` track without ARIA) still fails, since the style-test
  defect carried none.
- Only sr-only style zero-area clipping (`clip: rect(…)` with no area, `clip-path: inset(50%)`/`circle(0)`) exempts an
  image; decorative `clip-path` shapes do not.
- An image fully clipped by a container that is not collapsed (scrolled out of a carousel or scroll area) is not reported.
- `needs_http` reads executable scripts with comments removed (an approximate stripper); runtime file-incompatibility
  errors under `file://` remain the main signal.
- `UNFILLED_FIELD` matches the `TODO:` marker case-insensitively, so a real value starting with "Todo:" (e.g.
  "Todo: comprar pão") is also reported; rephrase it.

Governance: `CANDIDATE_SCOPES['web-runtime-2.6-v2']` is pinned in code and includes v1's scope. v1 is superseded at
`0f7089a`. Because `main` takes squash merges only, that commit is not on `main`, so v1's two records (README and
source manifest) are pinned by sha256 in `SUPERSEDED`; adding, removing or changing a v1 record fails
`preserved_history`. boundary-hardening-v1 is still compared to the bytes of its reviewing commit `b83b331`, which is on
`main`. Pointing `ACTIVE.json` back to v1 fails as not the newest in its lineage.

## Gates

```sh
python -m validation.release_integrity      # V2.5.0 exported from 39a0bfa, unchanged
python -m validation.candidate_integrity    # tree == this manifest; scope pinned in CANDIDATE_SCOPES
python -m validation.candidate_tests
python -m validation.harness --profile candidate --host --check --output build/validation/candidate.json
python security/publication_guard.py --range "origin/main...HEAD" --history-range "origin/main..HEAD"
```

Local results at authoring time (Playwright and Chromium installed, so browser tests ran) are recorded in the PR.
In CI the browser tests skip, as before.
