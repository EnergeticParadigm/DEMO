#!/usr/bin/env python3
"""Replay recorded results publicly, or execute the original evaluator with an authorized local installation."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent

def actual_run(runtime):
    path = runtime.resolve() / "assessment" / "rubric_eval.py"
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location("erplp_rubric", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    rubric = mod.load_rubric()
    paper = "Synthetic research exercise: a hypothetical claim that method A improves outcome B. No real empirical results are supplied."

    def base():
        x = mod.make_template(rubric)
        x.update(paper_sha256=hashlib.sha256(paper.encode()).hexdigest(),
                 paper_class="synthetic teaching exercise",
                 research_scope="Demonstrate qualification control, not scientific assessment")
        return x

    def rated():
        x = base()
        for k in x["scores"]:
            x["scores"][k] = {"score": 4,
                "rationale": "Artificial maximum score for control test only",
                "evidence": ["synthetic placeholder; not scientific evidence"]}
        return x

    x = base()
    cases = [("unassessed", x)]
    x = rated()
    x["hard_objections"] = [{"id": "S4-demo", "state": "OPEN"}]
    cases.append(("high_score_open_objection", x))
    x = rated()
    x["gate_statuses"] = {g: "PASS" for g in mod.GATES}
    x["actor"] = "independent_reviewer"
    x["reviewer_independence_verified"] = True
    cases.append(("perfect_score_claimed_pass", x))
    x = rated()
    x["scores"][next(iter(x["scores"]))]["evidence"] = []
    cases.append(("missing_evidence_anchor", x))
    out = []
    for name, x in cases:
        r = mod.evaluate(x, rubric)
        out.append(dict(case=name, criterion_count=r["criterion_count"],
            domain_count=r["domain_count"], unassessed_count=len(r["missing_criteria"]),
            structural_error_count=len(r["structural_errors"]),
            blocked_gate_count=len(r["blocked_gates"]),
            open_objection_count=len(r["unresolved_hard_objections"]),
            advisory_score=r["total_advisory_score"], process_status=r["process_status"],
            scientific_qualification=r["scientific_qualification"],
            release_authorization=r["release_authorization"]))
    return out

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runtime", type=Path, help="Authorized ERPL-P directory containing assessment/rubric_eval.py")
    parser.add_argument("--case", choices=["unassessed", "high_score_open_objection", "perfect_score_claimed_pass", "missing_evidence_anchor"])
    args = parser.parse_args()
    recorded = json.loads((HERE / "recorded_results.json").read_text())["cases"]
    if args.runtime:
        result = actual_run(args.runtime)
        print("MODE=LIVE_LOCAL_PRIVATE_ENGINE")
        print("RECORDED_RESULT_MATCH=" + ("YES" if result == recorded else "NO"))
    else:
        result = recorded
        print("MODE=RECORDED_EVIDENCE_REPLAY_NOT_LIVE_ENGINE")
    for row in result:
        if not args.case or args.case == row["case"]:
            print(json.dumps(row, indent=2))
    if args.runtime and result != recorded:
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
