# FAQ

### Is R2R just “skip code review”?
No. R2R avoids treating **every intermediate change as a release candidate**. Deep review stays necessary for important structural risks and final delivery, and relevant tests must be honestly recorded.

### Does R2R require multiple agents or asynchronous reviewers?
No. Its current default is **RUN a meaningful batch → synchronous lightweight self-review → continue**. Only material risks trigger deeper source-grounded verification. A separate independent reviewer can be used sequentially when genuinely available; a same-agent self-check must never be advertised as independent.

### Does R2R replace Spec-driven development or Spec Kit?
No. Specs and Spec Kit remain the authoritative sources for requirements, tasks, contracts and acceptance—and Spec Kit includes implementation and convergence. R2R focuses on **successive rapid iterations, developer interventions, Finding routing and final product HARDEN** alongside the existing Spec workflow. [Compatibility](compatibility.md).

### Is R2R opposed to many agents working in parallel?
No. Parallel development is a horizontal speed multiplier when architecture has clear module/layer boundaries. R2R controls the iteration/integration feedback loop and works with one executor or many available agents. It does not create or schedule those agents.

### Does each fixed issue require another independent Review?
No. Important code, security and data-integrity findings are fixed according to severity, with a **focused quick recheck if warranted**. Ordinary nonblocking P2/P3 go into a grouped repair queue. Pure documentation/evidence wording is corrected without repeated independent Review unless acceptance, security authorization or traceability is affected. The main Codex/executor collects Findings, coordinates scoped fixes and **moves to the next safe Slice**.

### Are long plans mandatory?
A complete high-level product roadmap is central, and long-horizon execution is a major supported use. The developer may shorten a run or revise the plan whenever new information arrives.

### Must an intermediate version compile or pass smoke?
Not always. Its needed quality is decided by dependencies and current goals. Temporary failure is acceptable for isolated unfinished functionality, but important integration probes should not be indefinitely postponed. Never silently damage actual data, rights, secrets or external systems.

### How can a developer control hundreds of Agent changes?
By understanding the product/architecture, asking high-information questions, checking source-grounded answers, requiring deep feedback on dangerous seams and retaining a durable state of what is done and unverified.

### How do we prevent a disastrous final cleanup?
Protect invariants, inspect reality periodically, record verification debt, integrate meaningful user paths, and shorten the execution horizon when repeated rework exposes a structural mistake. R2R is not a guarantee that delayed validation is always cheaper.

### Is a new application required?
No. Start with one method page and prompts. Automation may be considered later but does not define R2R.

### Is R2R already shown to improve speed?
Not yet. See [evaluation protocol](../research/evaluation-protocol.md); comparative data is a future deliverable.
