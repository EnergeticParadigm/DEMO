# ERPL — Research capability demonstration
**Actual ERPL V1 private-runtime execution | 27 November 2026**

## Research question

Can a research system use measured experimental evidence to reject a false hypothesis, initiate a revised experiment, and reach a different evidence-based judgment without an operator manually rewriting the conclusion between rounds?

A second question is whether the same research engine can discriminate competing hypotheses and transfer its execution process to a different dataset.

## 1. Contradiction and research revision: Iris

The operator supplied an initial directional hypothesis: a petal-threshold classifier would be at least five percentage points worse than a constant-class baseline. The experiment used the public Iris dataset, with frozen primary and held-out case registries.

| Dataset partition | Cases | Candidate accuracy | Baseline accuracy | Difference |
|---|---:|---:|---:|---:|
| Primary | 100 | 94% | 34% | +60 percentage points |
| Held-out | 50 | 96% | 32% | +64 percentage points |

**Round 1:** The original engine executed four model/partition runs and returned **CONTRADICTED**.

**Research response:** The existing discovery policy generated the next action, materialized a successor hypothesis and experiment, and executed four additional runs. The successor reversed the original directional claim and required a minimum five-percentage-point improvement.

**Round 2:** The engine returned **SUPPORTED** for the revised claim, with the same observed accuracy values. The recursive transition reached COMPLETED and the project's evidence relationships were verified by the original runtime.

This demonstrates evidence-driven revision and execution within a predefined scientific domain. The second round uses the same frozen benchmark and is not independent replication or discovery of a novel scientific mechanism.

## 2. Competing hypotheses: Iris

Two opposing directional hypotheses and two candidate experiment specifications were supplied. The engine selected the experiment with larger **supplied** expected endpoint separation (0.8), executed both hypotheses' four-run evaluations, and returned:

| Hypothesis | Decision |
|---|---|
| Candidate performs at least five percentage points worse | CONTRADICTED |
| Candidate performs at least five percentage points better | SUPPORTED |

The competition reached RESOLVED. The original runtime verified the competition and materialized a next experiment; that next experiment was not executed in this demonstration. The model and predictions were supplied, not invented by ERPL.

## 3. Transfer to a different real dataset: Wine

The operator supplied an externally packaged Wine classification adapter and a signed snapshot of the public Wine dataset, with 178 records. ERPL executed a centroid classifier and a constant-class baseline on the two frozen partitions.

| Dataset partition | Cases | Candidate accuracy | Baseline accuracy | Difference |
|---|---:|---:|---:|---:|
| Primary | 120 | 96.67% | 33.33% | +63.33 percentage points |
| Held-out | 58 | 98.28% | 32.76% | +65.52 percentage points |

The hypothesis requiring a minimum five-percentage-point improvement was **SUPPORTED**. ERPL materialized a next experiment, which was not executed in this demonstration. The submission qualification gate did not pass; these are acceptance-mode research exercises.

## 4. What is actually demonstrated?

- Execution of quantitative experiments on two real, established datasets.
- Evidence-based rejection and support of pre-specified claims, with the same quantitative standard applied to both.
- Automated materialization and execution of a revised hypothesis after contradiction, using the existing discovery policy.
- Selection between competing hypotheses using supplied discrimination predictions and measured outcomes.
- Operation of the research process with a separately packaged benchmark and model adapter.

Twenty experiment runs completed (8 recursive, 8 competition, 4 Wine) and five hypothesis judgments were recorded. These counts include repeated executions on the same data; they are not twenty independent studies.

ERPL orchestrates the research process; the classifiers produce the predictions. The reported accuracy is **not** an ERPL intelligence benchmark, an advantage over an LLM, or a comparison with a strong scientific baseline. A constant classifier is intentionally weak. No new scientific knowledge, autonomous open-ended hypothesis invention, publication-ready paper, independent third-party reproduction, or scientific superiority is established.

## 5. Execution and disclosure

The canonical private ERPL V1 runtime (erpl-discovery-loop 1.0.5) and its existing discovery-example drivers were executed fresh on macOS in isolated temporary directories. These are re-executed existing research examples, not invented outputs or newly designed experiments. Aggregate observations above were read from the newly generated judgment/evidence records, not from a prerecorded report. The original runtime verified all three projects. The initial Wine run failed due to inconsistent macOS temporary-path resolution; setting TMPDIR to /private/tmp allowed the existing Wine driver to complete without changing the runtime. No private source, raw run records, adapters, keys, databases or proprietary rules are published.

This public report is an inspectable record of a live internal execution, not a downloadable copy of the private research engine. [Machine-readable aggregate results](research_results.json) are provided for inspection. The separate [public workflow demo](README.md#optional-public-workflow-sandbox) runs locally but does not reproduce the experiments above.

**Next scientific evidence milestone:** an unseen research question, stronger comparators, and expert evaluation of the actual research contribution. No claim of completion is made for this milestone.
