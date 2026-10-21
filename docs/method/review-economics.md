# Review economics — synchronous by default, lightweight by design

**R2R current default:** **RUN → synchronous quick Review → RUN** within the same active execution process. This is an intentional engineering choice because a convenient local multi-agent execution/reviewer architecture is not presently available. It must not become the old *full deep review after every tiny change* loop.

## The distinction that matters

| | R2R default | Traditional costly bottleneck |
| --- | --- | --- |
| Frequency | After a **meaningful work batch**, which may include many small tasks | Every small increment |
| Timing | Immediately after the batch, **synchronously** | Serial gate with potentially lengthy queue/re-review |
| Depth | Fast, relevant, risk-scaled | Broad, often release-level by default |
| Reviewer | Current agent's clearly labeled **self-check**; ask another reviewer only if really available/needed | Formal independent review routinely demanded |
| Handling | Fix P0/P1 affected paths; note P2/P3 and continue approved scope | All findings repeatedly halt all work |
| Finality | Only checks this batch and what was actually observed | Risk of over-interpreting approval as product-ready |

**Synchronous does not mean deep.** A 60-second focused source/contract check and an hour-long system-wide audit are both synchronous activities but have very different costs.

## Minimum synchronous loop

```text
PLAN: whole product and current authorized campaign
     ↓
RUN: implement a meaningful batch (size chosen by developer)
     ↓
REVIEW: quick synchronous source/evidence check of that batch
     ├─ Critical risk or wrong direction → stop/fix affected work, rerun relevant check
     ├─ Ordinary issue / deferred evidence → record and continue
     └─ No material finding → continue
     ↓
RUN: next meaningful batch, while authorization/session exists
     ↓
HARDEN when integration/restructuring or final READY requires it
```

The **developer may intervene any time**; meaningful batch size and review depth are dynamically chosen. There is no “review every N commits” law, and there is no assumption that another agent is running concurrently.

## What quick Review should inspect

1. Does the change serve the agreed user/product target, or has the implementation drifted?
2. Has it broken a known architecture, data authority, permissions or irreversible-data boundary?
3. Are changed files and any PASS/FAIL/NOT_RUN statements real and source-grounded?
4. Is there a single high-information architecture/product question that must be answered before dependent work?
5. If a finding is nonblocking, what is its owner, affected path and eventual validation stage?

Keep the summary compact: **scope/commit → up to three actionable findings → decision → next work**. The limit of three is a reporting convenience **only for quick review**, never a cap on reporting real P0/P1 problems.

## When deeper synchronous review is justified

Shared persistent state, auth or credentials, data migrations, architectural pivots, recurring cross-module failures or claims that a real user journey/release is ready can merit source- or runtime-backed deeper review. Ask the developer for any consequential missing authorization. A distinct independent reviewer, if available, can perform **sequential independent review**, but do not invent its participation or label a self-check independent.

## Handling verification debt

Ordinary P2/P3 findings and tests intentionally deferred can be documented and revisited. Do not accumulate unowned missing evidence or proceed through an unsafe dependency. Periodic real integration and final HARDEN remain necessary. This is *review-effort allocation*, not deleting verification.

## Future options

Parallel/async reviewer dispatch would require real suitable agent/workspace infrastructure and a separate reason to implement it. It is **not part of this baseline workflow or an R2R requirement**.

See [quality](quality.md), [steering](steering.md), [decision guide](../../quickstart/decision-guide.md) and [evaluation protocol](../research/evaluation-protocol.md).
