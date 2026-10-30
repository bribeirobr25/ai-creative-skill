# AI Creative Skill

**Status do `main`: pacote congelado ([ADR-0005](docs/decisions/ADR-0005-PROPOSED-container-decision-and-adr-0004-disposition.md)).**
A decisão de contêiner é (c): sem pacote nem guia novos; um [benchmark log](docs/benchmarks/benchmark-log.md) datado registra o que os hosts atuais fazem.
A baseline **V2.5.0** continua atestada no commit `39a0bfa39270ea4b685b0f862e7dbf647cf81d77` e verificável byte a byte. Não há linha de release nova.
Metadados do plugin: versão `0.3.0`.

A fonte em `src/ai-creative-skill/` corresponde à candidata ativa [privacy-redaction-v1](validation/candidates/privacy-redaction-v1/README.md),
que acumula o boundary hardening, o runtime Web 2.6 (v1/v2) e a redação de exposição pública (ADR-0005 D4). Release approval: false.

**Início de qualquer sessão:** `python3 -m brain status` ([Project Brain](brain/README.md)): decisões vigentes, findings, gates e trabalho aberto.

This is the public, provider-neutral source of the AI Creative Skill. The only canonical implementation tree is `src/ai-creative-skill/`. The Agent Skill and OpenAI Portable Plugin ZIPs are **generated artifacts**, not source trees that should be edited independently.

## Build & check

```bash
pip install -r validation/requirements.txt
python -m validation.release_integrity      # V2.5.0 exportada de 39a0bfa: testes, smoke e builders originais
python -m validation.candidate_integrity    # fonte atual = inventário revisado da candidata
python -m validation.candidate_tests        # testes de regressão e Web Experience da fonte atual
```

Uma nova mudança em `src/` exige uma nova candidata: escopo revisado em `CANDIDATE_SCOPES`, manifesto e
`validation/candidates/ACTIVE.json`. Candidatas anteriores e hashes históricos nunca são reescritos.
Runtime tests require optional local packages described in the source installation guide. No paid providers or GPU inference are called by repository CI.

## Governance

- `main`: pacote congelado (ADR-0005 D1), validado por dois gates (integridade imutável da V2.5 e candidata).
- V2.5.0: commit `39a0bfa`, referência de release preservada.
- Pesquisas concluídas ficam em `docs/research/`; evidência pesada (sites, fotos, capturas) fica nas branches dos PRs fechados.
- Every capability belongs to the shared creative architecture **and** may run and finish independently at the user-requested boundary.
- Changes to canon, paid inference, publication and releases require separate authority.
- **PUBLIC repository:** only publish code, generic documentation and permitted examples. Never commit client media, user data, API keys or third-party weights.
- Distributed skill works without access to this GitHub repository or the owner's Google Drive.

## Repository

- `src/ai-creative-skill/`: canonical source, frozen (V2.5 plus the reviewed candidates; active: `privacy-redaction-v1`).
- `brain/`: Project Brain: decision and finding records, gates, `python3 -m brain status`.
- `packaging/`: original plugin descriptor and deterministic two-format build.
- `docs/migration/`: hashes and provenance.
- `docs/decisions/`: architecture decisions (ADR-0001 to ADR-0005; ADR-0003 is PROPOSED, ADR-0004 partly superseded by ADR-0005).
- `docs/benchmarks/`: dated benchmark log of what current hosts and models do.
- `docs/research/`: research records (creative quality, DQB-01, DQB-02, media reframe, video upscale, preference profiles).
- `assets/manifests/`: storage-neutral asset schema, no actual media.
- `.github/workflows/`: offline CI only.

The original V2.5 ZIPs and old Drive snapshots no longer exist (deleted by the owner's request; confirmed 2026-10-30). V2.5 is rebuildable from commit `39a0bfa` and verified by `python -m validation.release_integrity`.

## Reusable validation

The [validation harness](validation/README.md) adds synthetic canonical-helper probes,
controlled fault/mutation tests, fictional journey definitions and illustrative cost
simulations. Read the [initial findings](validation/reports/2026-10-20-findings.md):
known defects remain explicit FAILs, and a green regression check is not production approval.
No paid provider calls, private assets or installed-skill changes are involved.
