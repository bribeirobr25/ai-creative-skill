#!/usr/bin/env python3
"""Offline deterministic Agent Skill and OpenAI portable plugin builder.

The checked-in source tree is never mutated. Only Python standard library required.
This does not certify host activation, rights, or creative fidelity.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src" / "ai-creative-skill"
PLUGIN = ROOT / "packaging" / "plugin.json"
ATTESTATION = ROOT / "docs" / "migration" / "v2.5.0-source-attestation.json"
FIXED_TIME = (2026, 10, 18, 0, 0, 0)
AGENT_NAME = "AI_Creative_Skill_V2.5_Agent_Skill.zip"
PLUGIN_NAME = "AI_Creative_Skill_V2.5_OpenAI_Portable_Plugin.zip"

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def payloads() -> tuple[dict[str, bytes], bytes]:
    if not SOURCE.is_dir() or not PLUGIN.is_file():
        raise FileNotFoundError("V2.5 source tree or plugin.json missing")
    items = {}
    for file in sorted(SOURCE.rglob("*")):
        if not file.is_file():
            continue
        if file.is_symlink():
            raise ValueError(f"Symlink not supported in release: {file}")
        relative = file.relative_to(SOURCE).as_posix()
        if "__pycache__" in file.parts or relative.endswith((".pyc", ".pyo")):
            continue
        items[relative] = file.read_bytes()
    manifest = json.loads(items["MANIFEST_SHA256.json"])
    if set(manifest["sha256"]) != set(items) - {"MANIFEST_SHA256.json"}:
        raise ValueError("V2.5 manifest contains missing or extra files")
    if manifest.get("files") != len(items) - 1:
        raise ValueError("Manifest count mismatch")
    if any(sha256(items[name]) != digest for name, digest in manifest["sha256"].items()):
        raise ValueError("Baseline source changed")
    attestation = json.loads(ATTESTATION.read_text())
    if {name: sha256(data) for name, data in items.items()} != attestation["files_sha256"]:
        raise ValueError("Imported source differs from original V2.5 attestation")
    return items, PLUGIN.read_bytes()

def entries(kind: str) -> dict[str, bytes]:
    items, descriptor = payloads()
    if kind == "agent":
        return {f"ai-creative-skill/{name}": data for name, data in items.items()}
    if kind == "plugin":
        return {"plugin.json": descriptor, **{f"skills/ai-creative-skill/{name}": data for name, data in items.items()}}
    raise ValueError(f"Unknown format: {kind}")

def write_zip(path: Path, files: dict[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, content in sorted(files.items()):
            if name.startswith("/") or ".." in name.split("/"):
                raise ValueError(f"Unsafe path: {name}")
            info = zipfile.ZipInfo(name, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, content, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

def verify_zip(path: Path, expected: dict[str, bytes]) -> None:
    with zipfile.ZipFile(path) as z:
        if len(z.namelist()) != len(set(z.namelist())) or set(z.namelist()) != set(expected):
            raise ValueError(f"Duplicate or unexpected paths in {path}")
        if z.testzip() is not None:
            raise ValueError(f"CRC failure: {path}")
        for name, content in expected.items():
            if z.read(name) != content:
                raise ValueError(f"Output content differs: {name}")

def build(output_dir: Path) -> dict:
    artifact = {}
    for kind, filename in [("agent", AGENT_NAME), ("plugin", PLUGIN_NAME)]:
        path = output_dir / filename
        files = entries(kind)
        write_zip(path, files)
        verify_zip(path, files)
        artifact[kind] = {"filename": filename, "files": len(files), "bytes": path.stat().st_size, "sha256": sha256(path.read_bytes())}
    report = {"version": "2.5.0", "plugin_version": "0.3.0", "status": "REBUILT_CONTENT_VERIFIED_NOT_HOST_CERTIFIED", "artifacts": artifact}
    (output_dir / "build_manifest.json").write_text(json.dumps(report, indent=2) + "\n")
    return report

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.output_dir), indent=2))
    except Exception as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

if __name__ == "__main__":
    main()
