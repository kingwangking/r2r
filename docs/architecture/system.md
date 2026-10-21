# Architecture of the R2R method

```text
Product intent / existing spec
        ↓
PLAN: full scope + architecture + acceptance
        ↓
RUN: coding/authoring agent ↔ STEER: developer direction & questions
        ↓
Evidence / risk-directed review / resumable checkpoint
        ↓
Early integration & restructuring when necessary
        ↓
HARDEN: repeated real-product convergence
        ↓
READY only after verified product acceptance
```

The architecture is **conceptual**, not a promise of a hosted service. Existing Git and the user's existing agents are sufficient for the initial method. ChatGPT Web + GitHub can author the R2R project itself.

The first release should include:
- the core concept and contrasts with spec/CI/agent loops;
- short copyable prompts and a practical work pattern;
- templates and a minimal evidence/status contract;
- demonstrative cases and empirical evaluation;
- no compulsory platform or tool.

**Later option, not present:** an adapter dispatching builder/reviewer/checkpoints using existing agent tool APIs. First prove that coordination overhead warrants it. No arbitrary remote shell and no assumption that a disconnected session will resume itself.

Principles: minimize abstractions; don't duplicate source of truth; don't invent runtime or test results; retain developer authority; label hypotheses; protect secrets and rights; preserve Git history and release decisions.
