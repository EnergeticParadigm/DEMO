#!/usr/bin/env python3
"""Run the actual published ERPL Public v1 engine on a supplied case."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

SOURCE = "https://github.com/EnergeticParadigm/ERPL.git"
REVISION = "e906ebd1ec4aecf728c6919e1879ea153759cccd"
STAGES = ["DISCOVERY_FRAMING", "QUESTION", "CLAIM", "EVIDENCE",
          "EVALUATION", "REVIEW", "REVISION", "CLOSURE"]
REQUIRED = {"discovery.json", "question.json", "claim.json",
            "evidence/evidence.json", "evaluation/evaluation.json",
            "review/review.json", "revision/revision.json", "closure.json",
            "research_state.json", "provenance.jsonl"}

def verify(run):
    run = run.resolve()
    entries = {}
    for line in (run / "manifest.sha256").read_text().splitlines():
        digest, name = line.split("  ", 1)
        p = (run / name).resolve()
        if not p.is_relative_to(run) or name in entries:
            raise ValueError("Invalid manifest entry: " + name)
        if hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            raise ValueError("Hash mismatch: " + name)
        entries[name] = digest
    actual = {p.relative_to(run).as_posix() for p in run.rglob("*")
              if p.is_file() and p != run / "manifest.sha256"}
    if set(entries) != actual or not REQUIRED <= actual:
        raise ValueError("Manifest coverage mismatch")
    state = json.loads((run / "research_state.json").read_text())
    if [x["stage"] for x in state["history"]] != STAGES:
        raise ValueError("Lifecycle mismatch")
    if state["status"] != "CLOSED" or json.loads((run / "closure.json").read_text())["decision"] != "CLOSED":
        raise ValueError("Not closed")
    print("DEMO_VERIFY=PASS")
    print("ARTIFACTS_VERIFIED=" + str(len(entries)))
    print("LIFECYCLE=" + ">".join(STAGES))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, help="JSON case; see example_case.json")
    parser.add_argument("--output", type=Path, default=Path("erpl-demo-output"))
    parser.add_argument("--verify-only", type=Path, help="Verify an existing output directory")
    args = parser.parse_args()
    if args.verify_only:
        verify(args.verify_only)
        return
    output = args.output.resolve()
    if output.exists():
        parser.error("Output already exists; choose a new directory.")
    case = args.case.resolve() if args.case else None
    if case:
        data = json.loads(case.read_text())
        for key in ("case_id", "title", "research_question", "initial_claim"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                parser.error("Case needs a nonempty string: " + key)
        if not isinstance(data.get("public_evidence"), list):
            parser.error("Case needs public_evidence as a list.")
    with tempfile.TemporaryDirectory(prefix="erpl-demo-") as tmp:
        root = Path(tmp) / "ERPL"
        subprocess.run(["git", "clone", "--quiet", "--no-checkout", SOURCE, str(root)], check=True)
        subprocess.run(["git", "-C", str(root), "checkout", "--quiet", "--detach", REVISION], check=True)
        if case:
            shutil.copyfile(case, root / "cases/public_case_001.json")
        for script in ("run_demo.py", "verify.py"):
            subprocess.run([sys.executable, str(root / "bin" / script)], cwd=root, check=True)
        run = root / "runs" / (root / "runs/LATEST").read_text().strip()
        verify(run)
        shutil.copytree(run, output)
        print("OUTPUT=" + str(output))
        print("SOURCE_REVISION=" + REVISION)

if __name__ == "__main__":
    main()
