# Start here (any agent, any tool)

1. Run `python3 -m brain status` and read the current decisions before proposing anything that touches them. See [brain/README.md](brain/README.md).
2. Once per clone, run `python3 security/install_hooks.py`, which adds the pre-push publication check. The repository is public. Never commit client media, personal data, credentials, account or environment details. Private material lives outside the repository.
3. Work on a branch and open a pull request. Merges, releases, `src/` changes, paid APIs, private data and external operations each need the owner's explicit authorization; one approval does not carry over to the next step.
4. `src/ai-creative-skill/` is frozen (ADR-0005 D1). Changes there go only through a reviewed candidate in `validation/candidate_integrity.py`.
5. When work settles a question, add a decision record (brain/CONTRACT.md) with `authority_ref` set to the PR; the owner's merge is the decision.
