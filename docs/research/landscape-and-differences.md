# R2R and adjacent engineering approaches

**Status:** scoped conceptual comparison, not a claim of novelty, superiority or an exhaustive systematic review.

## What is already established?

| Existing approach | Relevant existing strengths | R2R contribution / unresolved question |
| --- | --- | --- |
| **GitHub Spec Kit / SDD** | Clear intent → plans/tasks/implementation **and convergence**, customizable processes, extensions and automation. | Focuses specifically on the **economics and temporal placement of verification** while AI implementation volume and product complexity grow; does not claim Spec Kit cannot do convergence or long runs. |
| **Continuous Integration (CI)** | Frequent integration, rapid feedback, avoiding long divergent branches; techniques like branch-by-abstraction and feature flags facilitate incremental change. | Permits selectively non-release-ready intermediate product behavior while keeping integration observability and safety; not an argument to disable CI or defer all integration. |
| **Iterative/incremental and evolutionary architecture** | Evolving design with feedback, lightweight risk handling and incremental learning. | Re-examines execution and verification cadence when AI agents dramatically lower implementation effort, and allows structural hardening rounds. Not a claim that iteration was invented by R2R. |
| **Coding-agent loops & review bots** | Automatic implementation cycles, code comments, parallel agents, Git integration and test execution. | Defines developer steering, whole-product acceptance and risk-directed review timing independent of a particular runtime. Existing tools can implement R2R without new infrastructure. |

## Important correction to simplistic marketing

It would be inaccurate to claim **“Spec Kit only writes specifications and never handles convergence.”** Its current official materials include convergence and flexible workflow design. R2R can be run *inside* an existing Spec Kit or another SDD workflow. The difference is a proposed **engineering policy** for throughput, intermediate quality requirements and final verified delivery, not an exclusive feature list.

Likewise, it would be wrong to claim **“CI demands every unfinished feature already works.”** Teams can use incremental integration, feature flags and branch-by-abstraction to keep a healthy baseline while incomplete work exists.

## Source links (public primary documentation)

- [GitHub Spec Kit docs](https://github.github.com/spec-kit/) — current features/process scope, viewed October 2026.
- [GitHub Spec Kit source](https://github.com/github/spec-kit) — adaptable process, extensions and convergence.
- [Martin Fowler: Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) — integration discipline, incremental techniques.
- [Martin Fowler: Evolutionary Database Design](https://martinfowler.com/articles/evodb.html) — incremental design/migration constraints.

## What must still be proven

The R2R hypothesis is **not** “deep review is always bad” or “long runs always win.” It is that an **adaptive allocation of human attention, deep verification and structural hardening** may increase throughput to an equally well-verified final product under high AI coding capacity.

Only controlled comparison of **accepted product outcomes**, defects, time and rework—not document naming—can support that claim.

See [research hypotheses](problem-and-hypotheses.md) and [evaluation protocol](evaluation-protocol.md).
