# R2R in one page

**R2R = Run to Ready.** Plan big. Run long. Harden deep. Steer anytime.

## Core principle
**The final product must be stable; intermediate products need not be release-ready.** The developer chooses how much intermediate stability is required for progress. Safety, recoverability, permissions, intellectual property and truthful evidence never become optional.

## Relation to Spec-driven and parallel multi-agent development

**Spec defines intent** and acceptance (for example, Spec Kit's specify → plan → tasks → implement → converge). **Parallel agents increase horizontal capacity** where architecture, ownership and integration contracts are clear. **R2R increases longitudinal iteration throughput** across slices, developer intervention, feedback, repairs and HARDEN. They are compatible layers, not competing methodologies. Keep original specs authoritative and use R2R.md only for the overarching roadmap/checkpoint. Parallel implementation is welcome; synchronous quick Review remains the simple default when no separate reviewer infrastructure exists.

## PLAN
Establish a whole-product capability map, actual user journeys, architectural/data ownership, mature implementations to reuse, high-impact unknowns, long-horizon roadmap and final acceptance. Plans may be extremely long and are revisable. Prioritize overall direction, not exhaustive low-level design.

## RUN
Let an authorized agent (or coordinated independent agents) implement and continue producing useful changes. After each meaningful execution batch, perform a **synchronous, lightweight, risk-focused review** in the current workflow; triage meaningful Findings, promptly fix functionality/security/data-integrity issues by severity, queue nonblocking P2/P3 for batched repairs and continue. A repair triggers only the **necessary focused recheck**, not a new complete Review cycle. Deep reviews remain developer- or risk-triggered, not obligatory after every edit. A failing noncritical smoke test is a fact to record, not necessarily a stop-the-world event. A P0/P1 risk blocks its **affected dependency**, while unrelated work may continue safely. Preserve the actual work state for restart; do not require developer approval after every small task.

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

**Current execution mode:** one agent/active web workflow is sufficient: **implement → synchronous quick Review → continue**. Without a separate reviewer, this is an **author self-check**, not an independent audit. Async/multi-agent review is not required or assumed.

**Truth rules:** NOT_RUN is not PASS. One SHA's review does not approve later SHAs. An author self-check is not an independent reviewer. A dormant CLI/chat session is not background autonomous progress.

**Go deeper only when needed:** [principles](principles.md) · [glossary](glossary.md) · [architecture confidence](architecture-confidence.md) · [review economics](review-economics.md) · [convergence](convergence.md).
