"""Create the 8 isolated DQB-03 run directories (coordinator tooling).
usage: python3 setup_runs.py <dqb3_root> <runs_root>
Neutral run ids; the condition map is written only to <dqb3_root>/private/condition-map.json."""
import json, random, shutil, subprocess, sys, pathlib, hashlib

ROOT, RUNS = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
SH = ROOT / "shared"
BRIEFS = {"D1": ("brief-della.md", "assets-della"), "D2": ("brief-diboas.md", "assets-diboas")}
rng = random.Random(20261021)
plan = []
used = set()
for brief in ["D1", "D2"]:
    conds = ["A", "A", "B", "B"]
    for i, cond in enumerate(conds):
        while True:
            rid = ("d" if brief == "D1" else "f") + str(rng.randint(10, 99))
            if rid not in used: used.add(rid); break
        plan.append({"run": rid, "brief": brief, "condition": cond, "repetition": 1 + (i % 2)})
for r in plan:
    run = RUNS / r["run"]
    if run.exists(): raise SystemExit(f"{run} exists")
    run.mkdir(parents=True)
    bf, assets = BRIEFS[r["brief"]]
    shutil.copy(SH / bf, run / "brief.md")
    shutil.copy(SH / "executor-common.md", run / "INSTRUCTIONS.md")
    shutil.copy(SH / "rubric.md", run / "rubric.md")
    shutil.copytree(SH / assets, run / "assets")
    subprocess.run([sys.executable, str(ROOT / "tools/font_pack.py"), str(SH / "fonts"), str(run / "fonts"), r["run"]], check=True, capture_output=True)
    shutil.copytree(ROOT / f"skill-{r['condition']}/src/ai-creative-skill", run / "ai-creative-skill")
    r["fonts_order"] = [l[2:].split(" (")[0] for l in (run / "fonts/FONTS.md").read_text().splitlines() if l.startswith("- ")]
    r["skill_profile_sha256"] = hashlib.sha256((run / "ai-creative-skill/references/AI_Creative_Skill_Work_Profile_Web_Experience_v0.2.md").read_bytes()).hexdigest()
(ROOT / "private").mkdir(exist_ok=True)
(ROOT / "private/condition-map.json").write_text(json.dumps(plan, indent=1))
for r in plan: print(r["run"], r["brief"], r["condition"], r["repetition"], r["fonts_order"][:3])
