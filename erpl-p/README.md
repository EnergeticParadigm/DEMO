# ERPL-P: Scientific publication qualification

## What ERPL-P is for

ERPL-P is the publication-qualification layer of the Energetic Research Production Line. Its purpose is to improve the scientific foundations of a research paper **before** manuscript production and submission: examine prior work and originality, challenge unsupported claims, identify missing decisive evidence and resolve serious scientific objections through revision.

A high overall rating must not compensate for a fatal scientific defect. A manuscript may look polished and still be unqualified.

## Demonstration: four actual engine executions

On 27 November 2026 the original ERPL-P v1.3 source-candidate rubric evaluator was executed on macOS with four controlled, synthetic assessments. Its 16-domain, 160-criterion evaluator was used directly. The upstream rubric unit suite also passed 9/9. These are structural tests, not expert assessments of real papers.

| Input scenario | Advisory score | Observed outcome |
|---|---:|---|
| All criteria unassessed | None | Structural block; 160 unassessed criteria |
| Artificial perfect score; open serious objection | 100 | No scientific qualification; one unresolved objection |
| Artificial perfect score; all gates claimed passed | 100 | No scientific qualification or release authorization |
| Artificial perfect scores but a missing evidence anchor | None | Structural block; one structural error |

The evaluator's review-readiness label denotes only structural completeness; it is not a judgment that scientific objections have been resolved. All four cases returned NOT_GRANTED for scientific qualification and release authorization.

## Try the public evidence demo

```sh
git clone https://github.com/EnergeticParadigm/DEMO.git
cd DEMO/erpl-p
python3 run.py
python3 run.py --case high_score_open_objection
```

This **replays the recorded outputs of actual runs**, not live scientific inference. It requires Python 3.10+, no API key or third-party packages.

For authorized holders of the ERPL-P v1.3 candidate, run the same cases against the original local evaluator:

```sh
python3 run.py --runtime /path/to/authorized/ERPL-P
```

The adapter invokes the actual evaluator and compares its sanitized outputs with the published record; it does not implement a substitute evaluator. Use only a trusted authorized runtime.

## Current limits

- The supplied ratings and evidence placeholders are synthetic; the evaluator does not generate them by reading a manuscript.
- Public users cannot yet upload arbitrary papers for live scientific assessment.
- The private rubric, scientific rules, prompts and runtime are not distributed.
- The v1.3 source candidate still requires independent qualification. Neither this demo nor its scores authorize publication or establish scientific superiority.

[Recorded machine-readable results](recorded_results.json) · [Engineering status](https://github.com/EnergeticParadigm/energetic-paradigm-research/blob/main/engineering-status/2026-11-24/erpl-p.md) · [ERPL workflow](../erpl/README.md)
