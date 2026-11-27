# ERPL — Research Process Demonstration

**From a research question to a defensible research result**

```mermaid
flowchart TD
    Q["RESEARCHER<br/>Research question or assignment"]
    subgraph R["ERPL · AI-Enabled Research Production"]
        direction TB
        A["01 · Understand<br/>Research object, scope and constraints"]
        B["02 · Investigate<br/>Existing knowledge and research gap"]
        C["03 · Formulate<br/>Hypotheses or research propositions"]
        D["04 · Design<br/>Method, experiments and evidence"]
        E["05 · Execute<br/>Analysis, derivation or experimentation"]
        F["06 · Evaluate<br/>Findings against the research question"]
        G{"Defensible<br/>conclusion?"}
        H["07 · Revise<br/>Identify the cause of insufficient evidence"]
    end
    O["08 · RESEARCH RESULT<br/>Findings, contribution and limitations"]
    S["Document unresolved issues<br/>and resources required"]
    Q --> A --> B --> C --> D --> E --> F --> G
    G -->|Supported| O
    G -->|Insufficient or contradictory| H
    H -->|Revise hypothesis| C
    H -->|Revise method or gather evidence| D
    H -->|Resource constraint| S
    classDef entry fill:#183A52,stroke:#183A52,color:#FFFFFF,stroke-width:2px
    classDef research fill:#EEF4F8,stroke:#64839A,color:#183A52
    classDef decision fill:#FFF2D8,stroke:#B38637,color:#59431C
    classDef revision fill:#F9E9E5,stroke:#AD6857,color:#703B2E
    classDef output fill:#176B60,stroke:#176B60,color:#FFFFFF,stroke-width:2px
    class Q entry
    class A,B,C,D,E,F research
    class G decision
    class H,S revision
    class O output
    style R fill:#F9FBFC,stroke:#B8C9D5,stroke-width:1px
```

The stages describe the research process, not a fixed sequence of API calls. The researcher sets the assignment and may redirect the work; EP-enabled AI performs research with available information and tools. Evidence changes the research direction. Unsupported claims are revised or left unresolved rather than being forced into a conclusion.

**Research demonstration for prospective collaborators and investors — not a public research service.**
