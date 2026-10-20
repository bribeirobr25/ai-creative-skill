# Phase 2 research tools

Continuation of PR #9, not an installed module. Reuse the parent `browser_evidence.cjs`
and `report.py`, the existing canonical Web schema/validator, and the separately pinned
PR #7 harness checkout at `b83b331f552baa22e14f2cf760dcd396b65a5537`.
No provider API, public host, enrollment or outreach is used.

## Transfer reproduction

Use Python 3 with the repository's optional `jsonschema` dependency, Node/Playwright and
an installed Chromium. Set `CHROMIUM_EXECUTABLE` only if the bundled default differs.
Run from the repository root; store outputs outside the checkout.

```sh
python validation/creative_quality/phase2/prepare_transfer.py /private/new-transfer
python validation/creative_quality/phase2/repair_mutation.py /private/new-transfer
python -m http.server 8880 --bind 127.0.0.1 --directory /private/new-transfer
```

The second command creates **R, an exact restoration control**, not creative candidate C.
The original run first captured A/B/S, then repaired S in R and retested; reproducing all
four already prepared variants together is also valid if capture sessions are recorded.
Both commands refuse to overwrite destinations. A/B/S/R retain identical HTML/JS/SVG.

Make a private JSON config with four targets (`transfer-a`, `transfer-b`, `transfer-s`,
`transfer-r`), `kind: "workshop"`, corresponding loopback URLs and `build_sha256` set to
the SHA-256 of that variant's `styles.css`. Default viewports are 1440×900 and 390×844.
This field remains a stylesheet fingerprint; complete source fingerprints are separate.

```sh
node validation/creative_quality/browser_evidence.cjs /private/config.json /private/capture
python validation/creative_quality/report.py \
  --harness-root /separate/pr7-checkout \
  --evidence /private/capture/browser-evidence.json \
  --output /private/summary.json \
  --baseline-commit e35b6f5015aa072cd76ceb91fca7d8e1f25d630d \
  --expected-failure CQ-transfer-s-1440-learning-path-visible \
  --expected-failure CQ-transfer-s-390-learning-path-visible
```

The collector adds a workshop-specific probe module; it does not create another outcome
engine. Expected failures are supplied explicitly. The original report adapter defaults
still reproduce PR #9's 99 PASS / 1 expected FAIL. Screenshot fingerprints are verified.

The recorded two-session source is called `combined.json` in the private package. For
canonical record validation, provide that file and all B PNGs in the evidence directory:

```sh
python validation/creative_quality/phase2/bind_web_record.py \
  /private/new-transfer/B /private/evidence \
  validation/creative_quality/phase2/results/web-delivery.json
```

This binds real local evidence and canonical hashes/check IDs to the existing schema.
It updates the research record; review its diff. `PARTIAL`/`PREVIEW_REVIEWED` intentionally
remain because human acceptance is absent. It does not alter canonical code or certify
that browser observations are true merely because the JSON validates.

## Private A/C human review preparation

`record_walkthroughs.cjs private-config.json private-video-dir` accepts the authorized
A/C local URLs as `{ "targets": [{"id":"a","url":"http://127.0.0.1:PORT/A/"},
{"id":"c","url":"http://127.0.0.1:PORT/C/"}] }`. It records the same silent scripted
interaction protocol, blocks other origins and confirms key actions. These selectors
are for the archived pilot, not a universal site recorder.

`prepare_review.py --captures private-phase1-final-captures --videos private-video-dir
--brief private-brief.txt --output new-private-review-dir` makes R1/R2 ZIPs with reversed
X/Y assignment, unchanged equal-resolution images/videos, a standalone local form and
a **separate coordinator-only key**. Never commit these packets or send the key to
reviewers. The brief is private input; the generic HTML template contains no customer data.

`review_gate.py private-response-dir` reads `resposta-*.json` and reports completeness.
It never asserts genuine human review or owner approval. The coordinator must verify
those externally and preserve dissent. No response is submitted by the software.

`check_review_ui.cjs /private/ui-result.json` expects a loopback server on port 8882
serving the prepared review directory. It checks both packets at two widths and tests
one export with unmistakably synthetic values, then deletes that download. This is UI
validation only, not a review or simulated human panel.

## Focused checks

```sh
python -m unittest discover -s validation/creative_quality/phase2 -p 'test_*.py'
python -m unittest discover -s validation/creative_quality -p 'test_*.py'
```

Four gate tests plus the three existing adapter boundary tests pass. Browser outcomes
are recorded separately from GitHub's packaging/source CI. The fictional source and two
annotated comparison JPGs are safe public evidence; all customer artifacts stay private.
