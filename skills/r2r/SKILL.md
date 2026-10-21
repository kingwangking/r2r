---
name: r2r
description: Apply Run to Ready (R2R) to AI-assisted software development when building a complex product through long, steerable implementation campaigns and risk-directed review, then repeated integration, restructuring and final product acceptance. Works with existing specs and Git; no special execution runtime required.
---

# R2R — Run to Ready

**Plan big. Run long. Harden deep. Steer anytime.**

Use this method when the developer explicitly asks for R2R or a long-horizon, high-throughput AI engineering workflow. Respect the repository's actual instructions, the developer's scope, available tools and safety boundaries.

## PLAN — understand the whole product before scaling implementation

1. Inspect **actual** repository facts, current branch/commit, existing specs, docs and known incomplete work.
2. Capture the real end-to-end user promises, a whole-product capability map, and final READY criteria.
3. Identify architectural ownership (especially persistent state and authority), reuse candidates, material unknowns and irreversible/high-risk boundaries.
4. Establish an ordered but **revisable long-horizon program**; do not require exhaustive microtask design or a perfect architecture prediction.
5. Distinguish verified facts, assumptions, planned features and work actually implemented.

## RUN — keep making meaningful progress

1. With the **developer's authorization**, choose a short, medium or very long execution horizon based on current confidence and risk.
2. Implement valuable product slices and do cheap **relevant** checks. Aim for user-observable outcomes, not just PRs, lines or document count.
3. When helpful and actually possible, use a **distinct independent reviewer** on a pinned change. It may run in parallel with work not depending on the reviewed risk. Never call self-review independent; never claim a reviewer ran if it did not.
4. Keep ordinary intermediate imperfections visible. A non-release-ready intermediate build is not automatically a campaign-wide stop.
5. Identify critical affected dependencies: rights, secrets, real/irreversible data and unauthorized operations cannot be deferred for speed; P0/P1 stops affected paths. Continue safe independent work where possible.
6. On any interruption, leave a concise source-grounded checkpoint of delivered outcomes, evidence, unverified claims and the next action. Do not claim hidden autonomous work after the actual session ends.

## STEER ANYTIME — developer retains the control plane

The developer may at any moment ask:
- “Which real user journey now works end to end? Show actual evidence.”
- “Did this change duplicate an existing source of truth?”
- “What architecture assumption most threatens future work?”
- “What small experiment would falsify this success claim?”
- “Should the next run be longer, shorter, or start structural hardening?”

Answer material questions with exact source, tests or observations when possible. **An agent explanation is not proof.** Change course immediately when direction is wrong, rather than relying on blind confidence in later cleanup.

## HARDEN — repeated convergence, not cosmetic bug fixing

As real product journeys exist (or systemic failures recur):
1. Integrate and observe **actual** user paths. Don't substitute a passing synthetic test for real interaction/persistence.
2. Repair architectural mismatches, duplicate authorities and broken integration contracts; first rounds may be significant restructuring.
3. Fix reproducible defects; exercise negative boundaries, recovery, restart, regression and performance as appropriate.
4. Track missing validations as `NOT_RUN` with affected scope, risk, owner and due stage. Do not silently convert deferred testing into PASS.
5. Repeat until final acceptance criteria, evidence and permitted release decision actually hold.

## Review decision — no automatic fixed cadence

- **High confidence, reversible work:** continue long RUN with focused checks.
- **A consequential unverified dependency:** investigate before building more dependent work.
- **Costly review, safe independent work exists:** defer scoped deep review, continue unaffected work.
- **Risk of real-data loss, permission/rights breach or irreversible effect:** stop the unsafe operation and get the necessary protection/approval.
- **Structural rework repeats:** shorten RUN and redesign the shared seam now.

Do not require a multi-document governance stack for small improvements. Use a concise conversation, one card or existing repo docs.

## Output after a meaningful batch (short)

```text
Delivered: <actual features/artifacts, source SHA/ref>
Proof: <specific PASS / FAIL / NOT_RUN, and what it covers>
Risk/holds: <affected dependency only>
Steering needed: <only if a real decision or permission is required>
Next: <highest-value continuation and resume point>
```

**Never:** auto-merge/release/publish without authorization, overwrite unknown local work, expose secrets, or claim an independent review, an unattended background run or product readiness without real evidence.

**Optional reading:** [R2R core method](../../docs/method/r2r.md), [review economics](../../docs/method/review-economics.md), [quality](../../docs/method/quality.md), [one-card](../../quickstart/one-card.md).
