# ERPL — Energetic Research Production Line

**See how ERPL organizes a research question into an evidence-driven investigation.**

ERPL is an AI-enabled research architecture developed under Energetic Paradigm. It organizes research from an initial question through research design, investigation, evidence evaluation, revision and the delivery of defensible findings.

![ERPL demonstration: from a research question to a question-specific research design, research map and investigation](https://raw.githubusercontent.com/EnergeticParadigm/DEMO/8dc61bd1d34db0621274a65cb6a2b7a3007b4297/erpl/demonstration/demonstration-flow.svg)

Your research question determines the research design and its corresponding Mermaid research map. The diagram above describes the demonstration interaction, not a predetermined research plan.

**Research outputs in the intended workflow**

- **Research design:** the proposed methods, evidence requirements and rationale specific to your question.
- **Research map:** a question-specific diagram showing dependencies and evidence-driven decisions.
- **Research progress:** findings and revisions as the investigation proceeds.
- **Research results:** documented findings, supporting evidence and unresolved questions.

## Inspect a real demonstration

The public reference run begins with this research question:

> Can an executable staged research workflow preserve explicit state and provenance from initial framing through closure?

Inspect its [research question](https://github.com/EnergeticParadigm/ERPL/blob/main/examples/reference_run/question.json), [research state](https://github.com/EnergeticParadigm/ERPL/blob/main/examples/reference_run/research_state.json), [evidence and review artifacts](https://github.com/EnergeticParadigm/ERPL/tree/main/examples/reference_run), and [closure decision](https://github.com/EnergeticParadigm/ERPL/blob/main/examples/reference_run/closure.json).

The public executable and reproduction instructions are available in [ERPL Public v1](https://github.com/EnergeticParadigm/ERPL). Human reviewers and AI agents can inspect the machine-readable artifacts directly without contacting a person.

The public version demonstrates the staged lifecycle and its verification. A new research question can be used to create a public case scaffold, but this does not execute the private ERPL research engine. This page does not currently provide a public arbitrary-question research endpoint.

