"""Tests for system/hooks/guard.py (PreToolUse guard). Run: python3 -m unittest tests.test_system_guard"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GUARD = os.path.join(ROOT, "system", "hooks", "guard.py")
sys.path.insert(0, os.path.join(ROOT, "system", "hooks"))
import guard  # noqa: E402

CONFIG = {
    "write_roots": ["projects/demo", "hostcheck"],
    "subagent_protected": ["*/records/approvals.jsonl"],
    "deny_paths": ["projects/demo/sources"],
    "mcp_allow": ["mcp__reader__search"],
    "bash_scripts": ["tools"],
}


class Decide(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def d(self, tool, tool_input, agent=None):
        event = {"tool_name": tool, "tool_input": tool_input}
        if agent:
            event["agent_type"] = agent
        return guard.decide(event, CONFIG, self.dir)[0]

    def test_write_inside_root_allowed(self):
        self.assertTrue(self.d("Write", {"file_path": "projects/demo/records/tasks.jsonl"}))

    def test_write_outside_root_denied(self):
        self.assertFalse(self.d("Write", {"file_path": "/tmp/elsewhere.txt"}))
        self.assertFalse(self.d("Edit", {"file_path": "README.md"}))

    def test_path_traversal_denied(self):
        self.assertFalse(self.d("Write", {"file_path": "projects/demo/../../escape.txt"}))

    def test_deny_paths(self):
        self.assertFalse(self.d("Write", {"file_path": "projects/demo/sources/a.md"}))

    def test_subagent_cannot_write_approvals(self):
        path = {"file_path": "projects/demo/records/approvals.jsonl"}
        self.assertFalse(self.d("Write", path, agent="reviewer"))
        self.assertTrue(self.d("Write", path))  # main session may

    def test_bash(self):
        self.assertFalse(self.d("Bash", {"command": "ls"}, agent="research"))
        self.assertTrue(self.d("Bash", {"command": "ls -la"}))
        for cmd in ["git push origin main", "gh pr create -t x", "gh api repos/x/y -X POST",
                    "curl -X POST https://example.org", "curl -d a=1 https://example.org", "vercel deploy",
                    "npm publish", "scp a b:c"]:
            self.assertFalse(self.d("Bash", {"command": cmd}), cmd)

    def test_bash_allowlist_allows_reads(self):
        for cmd in ["ls -la", "cat a.txt | grep x | wc -l", "shasum -a 256 f.md", "git status", "git log --oneline -3",
                    "grep -c y f 2>/dev/null", "find . -name '*.jsonl'", "head -5 a && tail -2 b", "jq .id r.jsonl",
                    "cat f 2>&1 | head", "python3 tools/check.py --x", "echo 'a > b'"]:
            self.assertTrue(self.d("Bash", {"command": cmd}), cmd)

    def test_bash_allowlist_denies_writes_and_escapes(self):
        for cmd in ["echo x >> records/approvals.jsonl", "echo x > f", "cat a >| b", "ls &> out", "tee f < a",
                    "cp a b", "mv a b", "rm -rf x", "touch f", "mkdir d", "sed -i s/a/b/ f", "sed 'w out' f",
                    "python3 -c 'open(1)'", "python3 other/x.py", "python3", "bash -c ls", "sh x.sh",
                    "ls; rm x", "ls\nrm x", "ls && touch y", "echo $(rm x)", "echo `rm x`", "cat <(ls)",
                    "X=1 ls", "/bin/rm x", "git commit -m x", "git checkout .", "git -c a=b log", "git diff --output=f",
                    "find . -delete", "find . -exec rm {} ;", "sort -o out in", "rg --pre sh x", "echo 'unclosed",
                    "uniq a b", "dd if=a of=b", "awk '{print > \"f\"}' a", "gh pr view 3"]:
            self.assertFalse(self.d("Bash", {"command": cmd}), cmd)

    def test_mcp_default_deny(self):
        self.assertFalse(self.d("mcp__mail__send_message", {}))
        self.assertTrue(self.d("mcp__reader__search", {}))

    def test_read_tools_unrestricted(self):
        self.assertTrue(self.d("Read", {"file_path": "/etc/hosts"}))


class Process(unittest.TestCase):
    def run_guard(self, event, config=CONFIG):
        d = tempfile.mkdtemp()
        os.makedirs(os.path.join(d, ".claude"))
        if config is not None:
            with open(os.path.join(d, ".claude", "guard.json"), "w") as f:
                json.dump(config, f)
        env = dict(os.environ, CLAUDE_PROJECT_DIR=d)
        env.pop("SYSTEM_GUARD_CONFIG", None)
        return subprocess.run([sys.executable, GUARD], input=json.dumps(event), text=True,
                              capture_output=True, env=env)

    def test_deny_output_shape(self):
        r = self.run_guard({"tool_name": "Write", "tool_input": {"file_path": "/tmp/x"}})
        self.assertEqual(r.returncode, 0)
        out = json.loads(r.stdout)["hookSpecificOutput"]
        self.assertEqual(out["permissionDecision"], "deny")

    def test_allow_is_silent(self):
        r = self.run_guard({"tool_name": "Read", "tool_input": {"file_path": "a"}})
        self.assertEqual((r.returncode, r.stdout), (0, ""))

    def test_fails_closed_without_config(self):
        r = self.run_guard({"tool_name": "Read", "tool_input": {}}, config=None)
        self.assertEqual(r.returncode, 2)

    def test_fails_closed_on_bad_input(self):
        d = tempfile.mkdtemp()
        r = subprocess.run([sys.executable, GUARD], input="not json", text=True, capture_output=True,
                           env=dict(os.environ, CLAUDE_PROJECT_DIR=d))
        self.assertEqual(r.returncode, 2)


if __name__ == "__main__":
    unittest.main()
