# R2R — <PROJECT>

> One file in the **target project's root**, not a new management system. Link existing authoritative specs and issues; never silently overwrite user work. Keep this useful, not exhaustive.

## PLAN — the whole product

**Goal and real users:** <the final user-visible product promise>

**Existing sources:** <links to spec / README / ADR / backlog; avoid copies>

**Architecture and reuse:** <major component responsibilities; canonical state owner; proven reuse; unknowns>

**Protected boundaries:** <permissions, rights, secrets, irreversible data, authorized release operations>

**READY definition:** <end-to-end user journeys, correctness, recovery, security and real evidence required before delivery>

### Long-horizon program

| Order | Outcome / user journey | Key dependency or uncertainty | State |
| --- | --- | --- | --- |
| 1 | <coherent capability> | <seam/owner> | PLANNED |
| 2 | <coherent capability> | <seam/owner> | PLANNED |
| … | Extend to the whole product; use a linked existing backlog if large | | |

This is a **complete but revisable product route**, not a fixed number of tasks. Intermediate builds need not be release-ready.

## RUN — current actual state

- **Observed repo / branch / HEAD:** <verify live; do not invent>
- **Last delivered user outcomes:** <only actually implemented, with evidence>
- **Active next campaign:** <meaningful batch of safe work>
- **Review policy:** synchronous quick self-review after meaningful batches; deeper when risk demands
- **Evidence:** <what actually passed / failed / was NOT_RUN; exact scope>
- **P0/P1 holds and affected dependencies:** <none verified / specific; not generic>
- **Deferred proof / P2/P3:** <claim, owner, due milestone; use 'none known' only if checked>
- **Latest STEER / architecture change:** <developer direction and why>
- **Resume instruction:** inspect actual Git/ref, reconcile this file, continue next authorized batch

## HARDEN — maturity and delivery

- **Integrated journeys observed:** <actual build/path/result or NOT_RUN>
- **Structural convergence work:** <actual changes / known problems>
- **Recovery, security and regression evidence:** <PASS/FAIL/NOT_RUN with artifact>
- **Open acceptance blockers:** <actual>
- **Owner release decision:** NOT_READY unless explicitly accepted with evidence

**Guardrail:** Git and source/artifacts outrank stale prose. This checkpoint is not an automatic execution permission or release approval.
