# AI Creative Skill

**Status:** V2.5.0 integrated installable baseline, **not** production-quality or clean-host certified. Plugin metadata version \`0.3.0\`.

This is the public, provider-neutral source of the AI Creative Skill. The only canonical implementation tree is \`src/ai-creative-skill/\`. The Agent Skill and OpenAI Portable Plugin ZIPs are **generated artifacts**, not source trees that should be edited independently.

## Build & check

\`\`\`bash
python packaging/build.py --output-dir dist
python -m unittest discover -s tests -p 'test_*.py' -v
python -m unittest discover -s src/ai-creative-skill/web/tests -p 'test_*.py' -v
python src/ai-creative-skill/scripts/smoke_install.py
\`\`\`

Runtime tests require optional local packages described in the source installation guide. No paid providers or GPU inference are called by repository CI.

## Governance

- \`main\`: baseline source V2.5 import under validation.
- \`v2.5.0-import\`: source import milestone, **not** product approval.
- \`feature/media-reframe-research\`: comparative research; no implementation or promotion before evaluation.
- Every capability belongs to the shared creative architecture **and** may run and finish independently at the user-requested boundary.
- Changes to canon, paid inference, publication and releases require separate authority.
- **PUBLIC repository:** only publish code, generic documentation and permitted examples. Never commit client media, user data, API keys or third-party weights.
- Distributed skill works without access to this GitHub repository or the owner's Google Drive.

## Repository

- \`src/ai-creative-skill/\`: byte-preserved V2.5 source content.
- \`packaging/\`: original plugin descriptor and deterministic two-format build.
- \`docs/migration/\`: hashes and provenance.
- \`docs/decisions/\`: architecture decisions (new proposals do not silently mutate V2.5).
- \`assets/manifests/\`: storage-neutral asset schema, no actual media.
- \`.github/workflows/\`: offline CI only.

Original ZIP releases and old snapshots remain preserved in Google Drive.

## Reusable validation

The [validation harness](validation/README.md) adds synthetic canonical-helper probes,
controlled fault/mutation tests, fictional journey definitions and illustrative cost
simulations. Read the [initial findings](validation/reports/2026-10-20-findings.md):
known defects remain explicit FAILs, and a green regression check is not production approval.
No paid provider calls, private assets or installed-skill changes are involved.
