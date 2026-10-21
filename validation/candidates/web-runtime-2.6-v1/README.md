# Web runtime 2.6 v1 — review candidate, not a release

**Status:** active source candidate on `main` (2.6.0-dev). Parent: [boundary-hardening-v1](../boundary-hardening-v1/README.md),
whose records stay byte-identical to the commit that reviewed them (`b83b331`). Release approval: **false**.

This candidate fixes Web Experience runtime defects observed in DQB-02 (`docs/research/dqb02/`). It does not change
the creative method, generate websites, call paid providers or promote a release.

## Scope (cumulative over the parent)

| File | Change |
|---|---|
| `web/runtime/router.py` | Natural build requests route to `WEB_PREVIEW` when the site noun is the direct object of a build verb: article, at most one listed adjective, then the noun ("Crie o website descrito no briefing", "faça um site", "build me a landing page", "Crie uma loja virtual"). Weak verbs (faça, make, quero, preciso de, I want) count only with an indefinite article, so edits like "make my page faster" or "faça o site mais rápido" do not build. Questions ("como criar um site?"), social-network pages, other media ("crie o logo do site"), negations, multi-operation requests and bug reports never build. The negation look-behind is bounded, keeping long inputs linear. |
| `web/runtime/qa.py` | `audit(..., project_root=)`: QA evidence may live outside the site, so it never ships with it, but must stay under the project root later given to `validate.check`. Evidence refs and hashed file paths are relative to that root, never absolute. `#/route` and `#!/route` links are reported as `hash_routes`, not as broken anchors. The browser audit adds a 320 px width (`narrow_render`), scrolls the page before capture so `loading="lazy"` images load, and reports undecoded images (`images_rendered`). The scroll step is capped (60 steps, 8 s) so infinite-scroll pages terminate; hidden or pending images are reported as not verified. JS syntax errors keep only the error line, and browser or JS messages pass through `redact`, so evidence files carry no local directory names. |
| `web/runtime/validate.py` | `narrow_render` and `images_rendered` require `BROWSER_OBSERVED` evidence to PASS. They are not added to the mandatory FAST set, so existing records stay valid. |
| `web/runtime/cli.py` | `audit --project-root` and `validate --project-root`, so evidence written outside the site validates against the same root. |
| `references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md` | FAST QA line: check 320 px for horizontal overflow and scroll before judging images. |

Defaults are backward compatible: without `project_root`, the site root is the project root, file lists and hashes
are unchanged, and evidence must stay under the site as before.

## Gates

```sh
python -m validation.release_integrity      # V2.5.0 exported from 39a0bfa, unchanged
python -m validation.candidate_integrity    # tree == this manifest; scope pinned in CANDIDATE_SCOPES
python -m validation.candidate_tests
python -m validation.harness --profile candidate --host --check --output build/validation/candidate.json
```

The active candidate is named in `validation/candidates/ACTIVE.json`. Its allowed scope is pinned in code
(`CANDIDATE_SCOPES` in `validation/candidate_integrity.py`) and must include its parent's scope, so editing a manifest
alone cannot widen what the gate accepts. The active candidate must be the newest in its lineage and superseded
records are byte-checked whichever candidate is active, so pointing `ACTIVE.json` back cannot reopen them. Regressions: `tests/test_web_runtime_2_6.py` (router, static and browser
QA, governance). The browser tests skip when Playwright and Chromium are absent, as in CI; they were run locally.

Local results at authoring time: release gate PASS; 79 candidate tests OK; harness 308 PASS, 0 FAIL, 0 BLOCKED,
7 NOT_RUN, 2 UNVERIFIED (unchanged from the parent).

## Independent review

An independent review of the first version found routing false positives (edits, other media, social pages,
questions), an unbounded scroll on infinite-scroll pages, absolute paths in browser and JS error evidence, a CLI
root mismatch and a pointer-rollback gap. All were fixed and turned into regressions in `tests/test_web_runtime_2_6.py`.

## Not covered

- Content truth stays `NOT_TESTED`: it needs authoritative project evidence, not source inspection.
- The router is still a bounded deterministic pre-router, not language understanding. Joined verbs such as "crie e
  publique o site" still route to `WEB_PUBLICATION` (unchanged from the parent); the publication authority gate applies.
- The active manifest's file hashes are updated with the source, so source review of each PR remains required.
- Creative-method changes from DQB-02 (divergent directions before choosing, operative references, typography
  confounder control) need a new benchmark with an owner-supplied brief and are not part of this candidate.
