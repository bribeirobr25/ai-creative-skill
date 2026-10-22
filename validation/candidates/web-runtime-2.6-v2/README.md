# Web runtime 2.6 v2 — review candidate, not a release

**Status:** active source candidate (2.6.0-dev). Parent: [web-runtime-2.6-v1](../web-runtime-2.6-v1/README.md), whose records
stay byte-identical to the commit that reviewed them (`0f7089a`). Release approval: **false**.

v2 adds the items of the 21–22/10/2026 learnings audit (`docs/research/auditoria-aprendizados-2026-10-22.md`, items 2–8)
that came from direct evidence: the DQB-03 benchmark, the product-photoshoot study and the 18-style site test. It does not
add new files to the skill, generate media, call paid providers or promote a release.

## Scope added over v1 (cumulative)

| File | Change | Evidence |
|---|---|---|
| `web/runtime/qa.py` | `images_rendered` also fails on **collapsed images**: laid out (not `display:none`), visible, decoded at ≥ 64 px, yet drawn under 16 px, checked at 1440 and 390. Without `--url` the browser opens the built `index.html` via `file://`, so browser checks run without a preview server; `opened_via` records how. The file URI never enters evidence. `draft_record()` writes a delivery-record draft from one QA run: derivable fields filled, judgement fields as `TODO:`; refuses a QA matrix from another build. | Style test: a site passed its own 62 checks with six product images collapsed to 0 px on the home page; 17 of 18 executors skipped the record and all 18 skipped the preview server. |
| `web/runtime/validate.py` | New error `UNFILLED_FIELD` for any value still starting with `TODO`, reported together with schema errors, so a draft cannot validate. | Same. |
| `web/runtime/cli.py` | `record <site_dir> --qa <qa_matrix.json> --output <record.json> [--project-root] [--project]`; `audit --static-only`. | — |
| `web/runtime/migrate.py` | The legacy migration scaffold keeps browser checks `NOT_TESTED` (`open_file=False`): an archived build needs a deliberate fresh browser QA. | Keeps the v0.2 migration semantics. |
| `references/…Work_Profile_Web_Experience_v0.2.md` | Step 6: `file://` is a valid local preview. Step 7: the audit command; per-viewport captures; never change the site to please a capture tool; collapsed images. Step 8: mandatory record, fill every TODO, validate with no errors. QA note on `crossorigin` font preloads under `file://`. | Style test. |
| `references/…Method_Route_Compilation…md` §7.2 | Derived one-product crops are **mandatory** when the route cannot bind a reference to a region or role. | Blind review: reference selection 4/5 with crops vs 2/5 without. |
| `references/…Method_Image_Direction…md` §5.1, §9.1, §10 | Declared fact contradicted by the photos is a conflict, not a fact. Marks applied on the product (labels) that render small (≈120 px, inference) get a deterministic composite from a real label photo. §10 points to the crop rule. | 11/11 collection labels and 3/25 single-shot labels garbled, all small; two input errors reached executors. |
| `references/…Method_Localized_Repair…md` §6.2 | Label text on a product: default repair is the real-label composite; regenerating is a fallback. | 14/14 labels fixed without new generations. |

Governance: `CANDIDATE_SCOPES['web-runtime-2.6-v2']` is pinned in code and includes v1's scope. v1 is superseded at
`0f7089a`; `preserved_history` now byte-checks exactly the record files each superseded candidate had at its reviewing
commit (v1: `README.md`, `source-manifest.json`; boundary-hardening-v1: all four), and pointing `ACTIVE.json` back to v1
fails as not the newest in its lineage.

## Gates

```sh
python -m validation.release_integrity      # V2.5.0 exported from 39a0bfa, unchanged
python -m validation.candidate_integrity    # tree == this manifest; scope pinned in CANDIDATE_SCOPES
python -m validation.candidate_tests
python -m validation.harness --profile candidate --host --check --output build/validation/candidate.json
```

Local results at authoring time (Playwright and Chromium installed, so browser tests ran): release gate PASS; candidate
integrity PASS; 83 candidate tests OK (22 in `tests/test_web_runtime_2_6.py`); harness 308 PASS, 0 FAIL, 0 BLOCKED,
7 NOT_RUN, 2 UNVERIFIED (unchanged). In CI the browser tests skip, as before.
