# R2R in one page

**R2R = Run to Ready.** Plan big. Run long. Harden deep. Steer anytime.

## Core principle
**The final product must be stable; intermediate products need not be release-ready.** The developer chooses how much intermediate stability is required for progress. Safety, recoverability, permissions, intellectual property and truthful evidence never become optional.

## PLAN
Establish a whole-product capability map, actual user journeys, architectural/data ownership, mature implementations to reuse, high-impact unknowns, long-horizon roadmap and final acceptance. Plans may be extremely long and are revisable. Prioritize overall direction, not exhaustive low-level design.

## RUN
Let an authorized agent implement and continue producing useful changes. Make cheap relevant checks, independent fast reviews or delayed deep reviews when justified. A failing noncritical smoke test is a fact to record, not necessarily a stop-the-world event. A P0/P1 risk blocks its **affected dependency**, while unrelated work may continue safely. Preserve the actual work state for restart; do not require developer approval after every small task.

## STEER ANYTIME
The developer sets the current horizon and may ask product/architecture questions, inspect evidence, shorten/extend execution, change review intensity, stop for a key uncertainty or trigger re-design. Agent explanations are not proof; demand source-grounded evidence for important claims.

## HARDEN
As real product paths emerge, integrate them; the first improvements may be *major restructuring*, not trivial bug fixes. Repeat actual product use, resilience/security checks, regression and defect correction until final acceptance can be demonstrated.

```text
Whole-product PLAN
      ↓
Long / short RUN ↔ developer STEER at any moment
      ↓
Real integration and architecture correction (as needed)
      ↓
Repeated HARDEN ↔ real product observation
      ↓
Evidence-backed READY
```

Stages are **dominant objectives, not rigid gates**. RUN may require early restructuring or deep checks; HARDEN may reveal missing capabilities and send work back to RUN.

**Truth rules:** NOT_RUN is not PASS. One SHA's review does not approve later SHAs. An author self-check is not an independent reviewer. A dormant CLI/chat session is not background autonomous progress.
