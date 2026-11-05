# System (public, domain-neutral parts)

The parts of the agent system that hold no project data: role definitions, knowledge packs, playbooks, record templates, hooks and evaluation cases (decision `system-location`). Project instances (records, research snapshots, exports, deliverables) live in the private half, never here. `src/` stays frozen.

| Path | What |
|---|---|
| [hooks/guard.py](hooks/guard.py) | `PreToolUse` guard: write roots, no subagent writes to approval records, no Bash in subagents, outward commands blocked, MCP tools denied unless allowed. Fails closed. Tests: `python3 -m unittest tests.test_system_guard` |
| [hostcheck/](hostcheck/) | The host check (ADR-0005 D6): procedure and test-only subagents |

Built for the [slice 01 plan](../docs/slices/01-research-offer-landing.md). Everything here is `unproven` until it earns its place (decision `evaluation-method`).
