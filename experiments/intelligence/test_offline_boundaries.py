"""Static guards against S3 becoming an accidental network or execution path."""
import ast
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent
CANDIDATE_MODULES = ("policy_gate.py", "provider_templates.py", "s2_projection.py", "contract_canary.py", "engine.py", "research_bridge.py")
PROHIBITED_ROOTS = frozenset({
    "requests", "httpx", "urllib.request", "socket", "subprocess", "http", "ftplib",
    "aiohttp", "boto3", "sqlite3", "psycopg2", "sqlalchemy"
})
PROHIBITED_NAME_CALLS = frozenset({"eval", "exec", "__import__", "open"})  # pure lab
DYNAMIC_MODULE_FUNCTIONS = frozenset({"import_module"})
PROHIBITED_ATTRIBUTE_CALLS = frozenset({"connect", "urlopen", "Popen", "run", "system",
                                        "write_text", "write_bytes", "unlink", "mkdir", "open"})


def _imports_experiments(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import) and any(
            a.name == "experiments" or a.name.startswith("experiments.")
            for a in node.names
        ):
            return True
        if isinstance(node, ast.ImportFrom) and (
            (node.module or "") == "experiments"
            or (node.module or "").startswith("experiments.")
        ):
            return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in DYNAMIC_MODULE_FUNCTIONS and node.args:
                arg = node.args[0]
                if isinstance(arg, ast.Constant) and type(arg.value) is str and (
                    arg.value == "experiments" or arg.value.startswith("experiments.")
                ):
                    return True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == "__import__" and node.args:
                arg = node.args[0]
                if isinstance(arg, ast.Constant) and type(arg.value) is str and (
                    arg.value == "experiments" or arg.value.startswith("experiments.")
                ):
                    return True
    return False


class S3IsolationTests(unittest.TestCase):
    def test_candidate_modules_do_not_import_network_or_storage_libraries(self):
        for filename in CANDIDATE_MODULES:
            tree = ast.parse((ROOT / filename).read_text(encoding="utf-8"))
            for item in ast.walk(tree):
                imported = []
                if isinstance(item, ast.Import):
                    imported = [alias.name for alias in item.names]
                if isinstance(item, ast.ImportFrom) and item.module:
                    imported = [item.module]
                for name in imported:
                    with self.subTest(filename=filename, module=name):
                        self.assertFalse(
                            any(name == p or name.startswith(p + ".")
                                for p in PROHIBITED_ROOTS),
                            "unsafe module in synthetic-only lab: " + name,
                        )

    def test_candidate_modules_do_not_call_dynamic_code_evaluation(self):
        for filename in CANDIDATE_MODULES:
            tree = ast.parse((ROOT / filename).read_text(encoding="utf-8"))
            calls = [
                node.func.id for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id in PROHIBITED_NAME_CALLS
            ]
            self.assertEqual([], calls, filename)
            attributed = [
                node.func.attr for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr in PROHIBITED_ATTRIBUTE_CALLS
            ]
            self.assertEqual([], attributed, filename)

    def test_production_src_never_imports_experimental_package(self):
        production = ROOT.parents[1] / "src"
        for py in production.rglob("*.py"):
            with self.subTest(path=str(py.relative_to(production))):
                tree = ast.parse(py.read_text(encoding="utf-8"))
                self.assertFalse(_imports_experiments(tree))

    def test_detects_dynamic_import_in_synthetic_module(self):
        self.assertTrue(_imports_experiments(
            ast.parse('import importlib\nimportlib.import_module("experiments.intelligence.engine")')))
        self.assertTrue(_imports_experiments(
            ast.parse('import experiments.intelligence.engine')))
        self.assertFalse(_imports_experiments(ast.parse('import json')))

    def test_no_provider_credentials_or_payload_files_in_candidate_folder(self):
        permitted = {".py", ".md"}
        for path in ROOT.iterdir():
            if path.is_file():
                self.assertIn(path.suffix.lower(), permitted)
            if path.is_dir():
                self.assertEqual("__pycache__", path.name)


if __name__ == "__main__":
    unittest.main()
