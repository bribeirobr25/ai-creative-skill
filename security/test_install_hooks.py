import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import install_hooks

HERE = Path(__file__).resolve().parent
ZERO = '0' * 40


def git(repo, *args):
    return subprocess.run(['git', '-c', 'user.name=t', '-c', 'user.email=t@example.com', *args], cwd=repo,
                          capture_output=True, text=True, check=True).stdout.strip()


class PrePushHook(unittest.TestCase):
    """Finding S0-3: the publication check can run locally before every push."""

    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo)
        git(self.repo, 'init', '-q', '-b', 'main')
        (self.repo / 'security').mkdir()
        for name in ('publication_guard.py', 'history_audit.py'):
            shutil.copy(HERE / name, self.repo / 'security' / name)
        (self.repo / 'README.md').write_text('hello\n')
        git(self.repo, 'add', '-A')
        git(self.repo, 'commit', '-q', '-m', 'base')

    def push(self, text):
        (self.repo / 'notes.md').write_text(text)
        git(self.repo, 'add', '-A')
        git(self.repo, 'commit', '-q', '-m', 'change')
        sha = git(self.repo, 'rev-parse', 'HEAD')
        hook = install_hooks.hook_path(self.repo)
        return subprocess.run([str(hook), 'origin', 'url'], cwd=self.repo, input='refs/heads/x %s refs/heads/x %s\n' % (sha, ZERO),
                              capture_output=True, text=True)

    def test_install_check_and_block(self):
        install_hooks.install(self.repo)
        self.assertTrue(install_hooks.installed(self.repo))
        self.assertEqual(self.push('just text\n').returncode, 0)
        blocked = self.push('token=' + 'ghp_' + 'X' * 32 + '\n')
        self.assertEqual(blocked.returncode, 1)
        self.assertIn('BLOCK: GITHUB_TOKEN', blocked.stdout)

    def test_foreign_hook_is_not_overwritten(self):
        path = install_hooks.hook_path(self.repo)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('#!/bin/sh\necho mine\n')
        with self.assertRaises(SystemExit):
            install_hooks.install(self.repo)
        self.assertIn('mine', path.read_text())


if __name__ == '__main__':
    unittest.main()
