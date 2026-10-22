# R2R evaluation protocol — credible adoption evidence

**Purpose:** Test, not advertise, whether R2R reduces time/cost to an actually accepted complex software outcome.

## Required comparison
- Define an identical high-level real user goal, representative subfeatures and complete **final acceptance suite** for each arm.
- Workflow **A:** deeply review/gate each small increment before continuing.
- Workflow **B:** PLAN/RUN/HARDEN with **synchronous, brief, risk-directed self-review after meaningful batches** (rather than per-slice deep gates), developer STEER and no universal intermediate release-quality requirement. Keep review time in B fully counted, not hidden.
- Preserve equivalent code/model budgets, developer experience and environment as far as practical. Record actual departures.
- Evaluate at least two different project/technology types. An existing proprietary project can contribute aggregated, rights-cleared metrics without exposing private code.

## Measure
| Metric | Why |
| --- | --- |
| Wall-clock time to accepted outcome | Primary throughput, not generated lines |
| Accepted real user journeys / scope | Counteract fake progress |
| Human interventions and time | Hidden review/coordination cost |
| Review wait, re-review cycles and false positives | Cost of verification |
| Model and infrastructure usage | Resource efficiency |
| P0/P1 remaining, escapes and regressions | Whether quality stayed credible |
| Total architectural restructuring and rework | Cost of allowing intermediate instability |
| Failure/restart recovery and scope drift | Whether long-run work is sustainable |

**Report limitations**: small sample, project comparability, learning effects, different reviewers, immature quality harnesses or inability to reproduce.

## Publication checklist
- Raw data or reproducible anonymized aggregates; exact tool versions where relevant.
- Actual tested artifact/commit and visible product acceptance, not just successful imports.
- Any missing evaluation labeled NOT_RUN.
- Do not publish restricted customer, model, project or user data.
- Include negative results, even if they weaken the method's preferred narrative.

A detailed experiment can be expensive; first validate the protocol on one small bounded feature to improve its design.
