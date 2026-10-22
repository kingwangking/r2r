# R2R + Spec-driven development + parallel agents

**R2R is the rapid-iteration and product-convergence layer.** It does not replace requirements/specification systems or a multi-agent implementation system.

| Practice | Optimizes | Typical existing artifacts | How it combines |
| --- | --- | --- | --- |
| **Spec / SDD** | Correct intent, constraints, architecture and acceptance | `spec.md`, `plan.md`, `tasks.md`, ADR/contract docs | Keep those documents authoritative; R2R uses them as its PLAN inputs |
| **Parallel multi-agent execution** | **Horizontal** throughput: multiple independent components in the same iteration | Component ownership, interfaces, worktrees/branches, integration contracts | Use when layers/modules have clear boundaries and integration ownership; primary executor integrates results |
| **R2R** | **Longitudinal** throughput: next slice after next slice, steering, focused Review and repeated HARDEN | Lightweight program/checkpoint (`R2R.md`), existing issue/CI evidence, batched P2/P3 queue | Controls RUN / triage / fix / resume across serial or parallel implementation |

## Combined example (not a required stack)

```text
Developer + Spec / Spec Kit: objectives → architecture → tasks/contracts
                                   ↓
         Primary Codex chooses iteration scope and slice sequence
                    ↓                          ↙
             Agent A: UI layer          Agent B: API/domain
                    ↓                          ↓
             independent work within clear interface ownership
                              ↓
                    primary executor integrates
                              ↓
                   short synchronous Review
                   ├─ real security/data/functional issue → fix by severity
                   ├─ ordinary P2/P3 → grouped fix queue
                   ├─ text-only Finding → fix; no Review carousel
                   └─ developer STEER → revise order/Spec as needed
                              ↓
                       next iteration
                              ↓
                  repeated product HARDEN → READY
```

This is **conceptual composition**, not proof a specific agent runtime or an automatically orchestrated parallel pipeline exists. A solo-agent workflow uses the same loop without Agents A/B. You may use independent reviewers if tools allow, but R2R's baseline is short synchronous self-review because it should work without additional orchestration.

### For Spec Kit users

Spec Kit's documented process includes **Specify → Plan → Tasks → Implement → Converge**. Do not claim that it lacks convergence, review or iterative capability. R2R contributes a **deliberate policy for execution horizon, prioritizing developer feedback, selective rechecks and nonblocking repair queue**, and a final end-product HARDEN program. It can be layered around or inside existing `/speckit.implement` / `/speckit.converge` work.

If an existing Spec already contains a complete long-term roadmap, **link it** from the project's root `R2R.md`; do not create a competing requirements authority.

### When parallel work is useful

Parallelize only when there are sufficiently separable layers, module contracts, owned files/data, tests and integration authority. Avoid concurrent edits to the same canonical persisted state, uncoordinated interface changes or pretending parallelism is free. The primary executor collects outcomes and steers the next iteration after integration.

### Frequent developer involvement is intentional

The developer continuously chooses product priorities, constraints, exceptions, batch length, risk tolerance **within protected invariants**, and when to restructure. STEER is not a late approval ceremony; it is the control loop between implementation batches.

**Summary:** Spec makes the target clear; parallel agents shorten the *width* of work; R2R shortens the *serial iteration and re-review path* while protecting final accepted quality.

See [one-page method](../method/r2r.md), [Review economics](../method/review-economics.md), and [Spec Kit](https://github.github.com/spec-kit/).
