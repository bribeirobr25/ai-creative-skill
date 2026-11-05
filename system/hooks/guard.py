#!/usr/bin/env python3
"""PreToolUse guard for Claude Code sessions that run the system on a project.

Reads the hook input (JSON) on stdin and denies, by default:
- writes outside the configured write roots;
- writes by a subagent to protected paths (approval records);
- Bash in subagents, and outward Bash commands (push, PR or release creation,
  deploys, HTTP writes) in the main session (best effort: pattern-based);
- every MCP tool not explicitly allowed.

Configuration: JSON at $SYSTEM_GUARD_CONFIG, else <project dir>/.claude/guard.json.
Keys (all optional): write_roots, subagent_protected (glob patterns, relative
to the project dir), deny_paths (absolute or relative path prefixes that no
tool may write), mcp_allow (exact tool names), log (path of a JSONL log of
every decision, relative to the project dir).

Fails closed: if the input or the configuration cannot be read, it denies.
Domain-neutral: no project names, paths or data belong in this file.
"""
import fnmatch
import json
import os
import re
import sys
from datetime import datetime, timezone

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
OUTWARD_BASH = re.compile(
    r"\bgit\s+push\b"
    r"|\bgh\s+(pr|issue|release|repo|gist|workflow|secret|api)\b(?!\s+(view|list|status|diff|checks)\b)"
    r"|\bcurl\b[^|;&]*(-X\s*(POST|PUT|PATCH|DELETE)|--data|-d\s|-F\s|--form|-T\s|--upload-file)"
    r"|\bwget\b[^|;&]*--post"
    r"|\b(vercel|netlify|firebase|npm\s+publish|twine\s+upload|rsync|scp|sftp|ssh)\b",
    re.IGNORECASE,
)


def decide(event, config, project_dir):
    """Return (allow: bool, reason: str) for one PreToolUse event."""
    tool = event.get("tool_name", "")
    tool_input = event.get("tool_input") or {}
    subagent = event.get("agent_type") or event.get("agent_id")

    if tool.startswith("mcp__"):
        if tool in set(config.get("mcp_allow", [])):
            return True, "mcp tool allowed by configuration"
        return False, f"MCP tool {tool} is not allowed in this project (guard: mcp_allow)"

    if tool == "Bash":
        command = str(tool_input.get("command", ""))
        if subagent:
            return False, "Bash is not available to subagents (guard)"
        if OUTWARD_BASH.search(command):
            return False, "outward or remote command blocked (guard: push, PR, deploy, upload, HTTP write)"
        return True, "bash allowed"

    if tool in WRITE_TOOLS:
        raw = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
        if not raw:
            return False, "write without a path (guard)"
        path = os.path.realpath(raw if os.path.isabs(raw) else os.path.join(project_dir, raw))
        for prefix in config.get("deny_paths", []):
            p = os.path.realpath(prefix if os.path.isabs(prefix) else os.path.join(project_dir, prefix))
            if path == p or path.startswith(p + os.sep):
                return False, f"path is read-only for this project (guard: deny_paths): {raw}"
        roots = [os.path.realpath(os.path.join(project_dir, r)) for r in config.get("write_roots", ["."])]
        if not any(path == r or path.startswith(r + os.sep) for r in roots):
            return False, f"write outside the project's write roots (guard): {raw}"
        if subagent:
            rel = os.path.relpath(path, os.path.realpath(project_dir))
            for pattern in config.get("subagent_protected", []):
                if fnmatch.fnmatch(rel, pattern):
                    return False, f"subagents may not write {rel}; only the main session records approvals (guard)"
        return True, "write inside write roots"

    return True, "tool not restricted by guard"


def _log(config, project_dir, event, allow, reason):
    target = config.get("log")
    if not target:
        return
    entry = {
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "session_id": event.get("session_id"),
        "tool": event.get("tool_name"),
        "path": (event.get("tool_input") or {}).get("file_path"),
        "agent_type": event.get("agent_type"),
        "agent_id": event.get("agent_id"),
        "allow": allow,
        "reason": reason,
    }
    try:
        with open(os.path.join(project_dir, target), "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except OSError:
        pass


def _deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}))
    return 0


def main():
    try:
        event = json.load(sys.stdin)
        project_dir = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or os.getcwd()
        path = os.environ.get("SYSTEM_GUARD_CONFIG") or os.path.join(project_dir, ".claude", "guard.json")
        with open(path, encoding="utf-8") as f:
            config = json.load(f)
    except Exception as exc:  # fail closed
        print(f"guard: cannot read input or configuration: {exc}", file=sys.stderr)
        return 2
    allow, reason = decide(event, config, project_dir)
    _log(config, project_dir, event, allow, reason)
    return 0 if allow else _deny(reason)


if __name__ == "__main__":
    sys.exit(main())
