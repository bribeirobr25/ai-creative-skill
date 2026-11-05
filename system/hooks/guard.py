#!/usr/bin/env python3
"""PreToolUse guard for Claude Code sessions that run the system on a project.

Reads the hook input (JSON) on stdin and denies, by default:
- writes outside the configured write roots;
- writes by a subagent to protected paths (approval records);
- Bash in subagents; in the main session, any Bash command outside a read-only
  allowlist: every segment must start with an allowed program, with no output
  redirection, command substitution, variable assignment or unparsable quoting,
  so files are written only through Write/Edit, which the path rules see;
- every MCP tool not explicitly allowed.

Configuration: JSON at $SYSTEM_GUARD_CONFIG, else <project dir>/.claude/guard.json.
Keys (all optional): write_roots, subagent_protected (glob patterns, relative
to the project dir), deny_paths (absolute or relative path prefixes that no
tool may write), mcp_allow (exact tool names), bash_allow (program names,
replaces the default list), bash_scripts (path prefixes of scripts that
`python3 <script>` may run), log (path of a JSONL log of every decision,
relative to the project dir).

Fails closed: if the input or the configuration cannot be read, it denies.
Domain-neutral: no project names, paths or data belong in this file.
"""
import fnmatch
import json
import os
import re
import shlex
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

BASH_ALLOW_DEFAULT = {
    "ls", "cat", "head", "tail", "wc", "grep", "rg", "find", "shasum", "sha256sum", "diff", "sort",
    "cut", "jq", "echo", "pwd", "stat", "git", "python3", "true",
}
GIT_READ = {"status", "log", "diff", "show", "rev-parse", "ls-files", "blame"}
FIND_DENY = {"-exec", "-execdir", "-ok", "-okdir", "-delete", "-fprint", "-fprintf", "-fls", "-fprint0"}
SEGMENT_OPS = {";", "&&", "||", "|", "&", "\n"}
NULL_REDIRECT = {"/dev/null"}


def _check_bash(command, config, project_dir):
    """Allow a main-session command only if it is read-only by construction."""
    if OUTWARD_BASH.search(command):
        return False, "outward or remote command blocked (guard: push, PR, deploy, upload, HTTP write)"
    if "$(" in command or "`" in command or "<(" in command or ">(" in command:
        return False, "command substitution is not allowed (guard: bash allowlist)"
    try:
        lexer = shlex.shlex(command.replace("\n", " ; "), posix=True, punctuation_chars=";&|<>")
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError:
        return False, "command could not be parsed (guard: bash allowlist)"
    allow = set(config.get("bash_allow", BASH_ALLOW_DEFAULT))
    scripts = [os.path.realpath(os.path.join(project_dir, s)) for s in config.get("bash_scripts", [])]
    segments, current = [], []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok in SEGMENT_OPS or set(tok) <= set(";&|") and tok:
            if current:
                segments.append(current)
            current = []
        elif tok and set(tok) <= set("<>&|"):
            if ">" in tok:
                target = tokens[i + 1] if i + 1 < len(tokens) else ""
                if not (target in NULL_REDIRECT or (tok.endswith("&") and target in {"1", "2"})):
                    return False, "output redirection to a file is not allowed; use Write or Edit (guard: bash allowlist)"
                if current and current[-1] in {"1", "2"}:
                    current.pop()
            i += 2
            continue
        else:
            current.append(tok)
        i += 1
    if current:
        segments.append(current)
    if not segments:
        return False, "empty command (guard)"
    for seg in segments:
        prog = seg[0]
        if "=" in prog and not prog.startswith("-"):
            return False, "variable assignment is not allowed (guard: bash allowlist)"
        if os.path.basename(prog) != prog or prog not in allow:
            return False, f"command '{prog}' is not in the read-only allowlist (guard: bash_allow)"
        args = seg[1:]
        if prog == "git" and (not args or args[0] not in GIT_READ):
            return False, "only read-only git subcommands are allowed (guard: bash allowlist)"
        if prog == "find" and FIND_DENY & set(args):
            return False, "find with -exec, -delete or -fprint is not allowed (guard: bash allowlist)"
        if prog == "git" and any(a.startswith("--output") or a == "-o" for a in args):
            return False, "git --output writes files (guard: bash allowlist)"
        if prog == "sort" and any(a == "-o" or a.startswith("-o") or a.startswith("--output") for a in args):
            return False, "sort -o writes files; use Write (guard: bash allowlist)"
        if prog == "rg" and any(a.startswith("--pre") for a in args):
            return False, "rg --pre runs another program (guard: bash allowlist)"
        if prog == "python3":
            if not args or args[0].startswith("-"):
                return False, "python3 may only run an allowed script (guard: bash_scripts)"
            script = os.path.realpath(os.path.join(project_dir, args[0]))
            if not any(script == s or script.startswith(s + os.sep) for s in scripts):
                return False, f"python3 script not in bash_scripts (guard): {args[0]}"
    return True, "bash command within the read-only allowlist"


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
        return _check_bash(command, config, project_dir)

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
