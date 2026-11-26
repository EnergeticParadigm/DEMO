# 05 — ERPL: research workflow demonstration

**Executable now.** This entry runs the existing [ERPL Public v1](https://github.com/EnergeticParadigm/ERPL) implementation, not a mock of a private engine.

## Run

Requires Python 3.10+, Git, and internet access for the initial checkout. No model, API key, or paid service is required.

```sh
git clone https://github.com/EnergeticParadigm/DEMO.git
cd DEMO/05-erpl
python3 run.py
```

Use a different case (edit the JSON with your question, initial claim and supplied evidence):

```sh
python3 run.py --case example_case.json --output custom-run
python3 run.py --verify-only custom-run
```

Inspect the output directory: question, claim, evidence, evaluation, review, revision, closure, state, provenance and SHA-256 manifest. The wrapper checks manifest coverage and lifecycle order in addition to running the upstream verification.

## What this establishes

The actual public engine materializes the supplied research case into eight stages and produces a verifiable closure record. The user may change the supplied inputs and inspect the generated record. It does **not** discover facts, generate new hypotheses from a question alone, assess scientific truth, compare intelligence against an LLM, or reproduce the private research engine.

## Related research-production capabilities

The public demo does not execute these separate research or engineering engines:

- [ERPL-P — research qualification](https://github.com/EnergeticParadigm/energetic-paradigm-research/blob/main/engineering-status/2026-11-24/erpl-p.md)
- [ERPL-R — scientific review](https://github.com/EnergeticParadigm/energetic-paradigm-research/blob/main/engineering-status/2026-11-24/erpl-r.md)
- [ERPL-Med — medical research lifecycle](https://github.com/EnergeticParadigm/energetic-paradigm-research/blob/main/engineering-status/2026-11-24/erpl-med.md)

Only the public implementation is retrieved. No private code, prompts, models or internal research data are distributed.
