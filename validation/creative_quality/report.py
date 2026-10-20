"""Use the existing PR #6/#7 harness outcome helper; do not duplicate its runtime.

Read captured browser assertions, verify screenshot hashes, and emit only an
allowlisted public summary. Keep URLs, DOM copy and media in private storage.
This cannot assess aesthetics or confer human acceptance.
"""
import argparse
import collections
import hashlib
import importlib
import json
import subprocess
import sys
from pathlib import Path

BASELINE = "39a0bfa39270ea4b685b0f862e7dbf647cf81d77"

def public_observation(check):
    """Remove image filenames and error/network content from the public record."""
    if check["id"] in {"images-loaded", "script-errors", "resource-errors", "external-network"}:
        return 0, len(check["actual"])
    if check["id"] == "gallery-next":
        return "different photo", "different photo" if check["outcome"] == "PASS" else "unchanged photo"
    return check["expected"], check["actual"]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--harness-root", required=True, type=Path)
    p.add_argument("--evidence", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    sys.path.insert(0, str(a.harness_root.resolve()))
    harness = importlib.import_module("validation.harness")
    source = json.loads(a.evidence.read_text())
    rows, assets = [], []
    for case in source["rows"]:
        for screenshot in case["screenshots"]:
            f = (a.evidence.parent / screenshot["file"]).resolve()
            if a.evidence.parent.resolve() not in f.parents:
                raise ValueError("Screenshot must remain in evidence directory")
            actual = hashlib.sha256(f.read_bytes()).hexdigest()
            if actual != screenshot["sha256"]:
                raise ValueError("Screenshot hash mismatch")
            assets.append({"id": screenshot["file"], "sha256": actual})
        for c in case["checks"]:
            # Numeric metrics and test observations only, not private page text/URLs.
            expected, actual = public_observation(c)
            rows.append(harness.outcome(
                f"CQ-{case['id']}-{case['width']}-{c['id']}",
                expected, actual, c["outcome"] == "PASS",
                mode="browser_observed", viewport_width=case["width"],
                build_sha256=case["build_sha256"]))
    report = {
        "schema": "creative-quality-research/1",
        "baseline_commit": BASELINE,
        "harness_commit": subprocess.check_output(["git","-C",str(a.harness_root),"rev-parse","HEAD"], text=True).strip(),
        "browser": source["browser"], "playwright": source["playwright"],
        "captured_at": source["time"], "results": rows, "evidence": assets,
        "counts": dict(collections.Counter(r["outcome"] for r in rows)),
        "expected_research_failure": "CQ-web-b-390-hero-not-collapsed",
        "provider_generation_calls": 0, "human_quality_approval": "UNVERIFIED",
        "limitation": "One automated reviewer; Chromium emulation; no randomized generation experiment or professional certification."
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["counts"]))
    observed = {r["id"] for r in rows if r["outcome"] == "FAIL"}
    if observed != {report["expected_research_failure"]}:
        raise SystemExit("Unexpected failure set; investigate without rewriting baseline")

if __name__ == "__main__":
    main()
