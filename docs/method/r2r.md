# R2R in one page

**R2R = Run to Ready.** Its **goal is the correct, stable and usable end product**, not merely faster code generation or faster iteration. **Plan big. Run long. Harden deep. Steer anytime.**

## The complete AI-era delivery problem

Three necessary capabilities form **one coupled product-development system**:

| R2R capability | Established practice used | Why it matters |
| --- | --- | --- |
| **Correct direction (what / why / contract)** | Existing Spec-driven development, architecture, acceptance / Spec Kit when adopted | Prevents high-speed delivery of the wrong product |
| **Horizontal throughput (how much independent work now)** | Available multi-agent parallel execution, clear layers and integration contracts | Scales implementation capacity where responsibility can be separated |
| **Longitudinal throughput (how quickly progress compounds)** | R2R's adaptive slice-to-slice RUN, frequent developer STEER, short synchronous Review, severity-based Finding triage and batched repairs | Prevents serial review/rework and stalled integration from consuming AI's coding capacity |

**READY is the governing destination**, achieved through repeated actual integration, structural HARDEN and evidence-based acceptance. The three capabilities constrain one another: wrong Specs multiply mistakes, unsafe parallel work magnifies conflicts, and fast RUN without integration/acceptance never arrives at READY.

This is a **complete practical operating model**, not a claim that R2R invented SDD, concurrency or convergence, and not proof of a measured productivity advantage. Existing Spec Kit includes implement/converge; R2R explicitly reuses those capabilities.

## Core principle
**The final product must be stable; intermediate products need not be release-ready.** The developer chooses how much intermediate stability is required for progress. Safety, recoverability, permissions, intellectual property and truthful evidence never become optional.

## Relation to Spec-driven and parallel multi-agent development

**R2R names the full Run-to-Ready goal**, not just the third technique. Spec (including existing Spec Kit workflows) grounds the target, optional parallel agents scale independently owned work, and **R2R's most distinctive operating contribution** is longitudinal execution/review/repair economics—coordinated by the developer and primary executor. Keep existing Specs authoritative; use `R2R.md` as a lightweight program/checkpoint. A solo agent is sufficient to adopt the method, even though parallelism can add capacity.

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
