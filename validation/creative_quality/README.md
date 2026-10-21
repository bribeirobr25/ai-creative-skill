# Creative quality research adapter

This is a bounded research collector, not a new validation engine or installed capability.
`report.py` uses `validation.harness.outcome` from the existing PR #7 checkout, pinned for
this run at `b83b331f552baa22e14f2cf760dcd396b65a5537`. The integrated baseline is
`39a0bfa39270ea4b685b0f862e7dbf647cf81d77`. These remain separate dependencies until their
own PRs integrate. Do not merge their source into this experiment.

## Reproduce with authorized private inputs

Requirements: Python 3, Node.js, Playwright with Chromium, the archived website inputs
held by the owner, and a separate checkout of the existing validation harness.
There is no provider API, generation, hosting or publication step.

1. Verify the archive hashes in the [experiment record](../../docs/research/creative-quality/web-experiment.md).
   Extract safely outside this public checkout. Keep the original immutable.
2. Run `python prepare.py /private/original-dist /private/new-experiment`.
   This creates B/C, records all file hashes and permits only `styles.css` to differ.
   Existing destinations, nested output and source symlinks are rejected.
3. Serve the authorized experiment directory using a loopback-only static server.
   Configure the four local URLs, kinds and stylesheet SHA-256 values:

```json
{
  "widths": [1440, 390],
  "targets": [
    {"id": "web-a", "kind": "gallery", "url": "http://127.0.0.1:8878/A/", "build_sha256": "SHA256_OF_STYLES_CSS", "minHeroHeight": 160},
    {"id": "web-b", "kind": "gallery", "url": "http://127.0.0.1:8878/B/", "build_sha256": "SHA256_OF_STYLES_CSS", "minHeroHeight": 160},
    {"id": "web-c", "kind": "gallery", "url": "http://127.0.0.1:8878/C/", "build_sha256": "SHA256_OF_STYLES_CSS", "minHeroHeight": 160},
    {"id": "web-d", "kind": "calculator", "url": "http://127.0.0.1:8878/D/", "build_sha256": "SHA256_OF_STYLES_CSS", "minHeroHeight": 160}
  ]
}
```

4. Run `node browser_evidence.cjs /private/config.json /private/capture`.
   Optionally set `CHROMIUM_EXECUTABLE` to the installed browser executable.
   All external requests are blocked; screenshots, copy and detailed metrics remain private.
   Selectors intentionally target these archived pilot builds, not arbitrary websites.
5. Run `python report.py --harness-root /separate/pr7-checkout --evidence /private/capture/browser-evidence.json --output results/browser-summary.json`.
   Screenshot hashes are verified. Public error lists become counts and gallery filenames
   are removed. The single expected B-mobile failure remains visible. Any different
   failure set exits unsuccessfully; do not silently rewrite the expected baseline.

The `build_sha256` field is the configured **stylesheet fingerprint**, not an attestation
of the whole build. The private preparation manifest binds all source files. A fresh
capture must update the public record deliberately after reviewing differences.

## Checked behavior and limits

The committed result has 99 PASS and one preserved research FAIL out of 100 browser
assertions. C alone passes 26/26. These are bounded observations, not broad scenario
coverage, full accessibility certification, professional acceptance or proof of
superiority over a marketing reference.

`python -m unittest discover -s validation/creative_quality -p 'test_*.py'` checks
preservation/overwrite guards using fictional files and public-output redaction. It
does not repeat the existing harness audit.

Private bundle `CQ8-PRIVATE-20261020` contains actual captures, side-by-side comparison,
isolated website copies, full source fingerprints and a packet for future independent
review. No third-party skill text or Higgsfield media is redistributed in this branch.
