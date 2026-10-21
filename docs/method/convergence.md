# Convergence capability — when can imperfect intermediate software become a reliable product?

**Status:** proposed design principle and warning signs; not an empirically established law.

R2R intentionally removes the requirement that *every* intermediate change be release-ready. The difficult part is **preserving a realistic route to final acceptance**.

## Working definition

A program has useful **convergence capability** if, given known architecture boundaries, dependencies, verification debt, feedback access and finite resources, the team can plausibly improve the integrated product toward its agreed end-to-end acceptance without endlessly undoing earlier work.

This is a **judgment based on evidence**, not a numeric score or an assurance that late testing always works.

## Convergence loop (may begin during RUN)

1. **Observe reality:** try a promised user journey on the actual integrated system, not just a mocked code path.
2. **Diagnose level:** is the failure missing implementation, broken contract, duplicated authority, wrong product interaction, or merely a local bug?
3. **Choose the highest-leverage correction:** restructure a seam or user flow before repeatedly patching its symptoms.
4. **Reintegrate:** maintain one authoritative state ownership, trace real write/read paths, and check critical dependencies.
5. **Verify outcomes:** collect real behavior and negative/failure-path evidence appropriate to risk.
6. **Reassess:** continue expansion, harden more deeply or alter PLAN when evidence changes.

A first hardening round may **rearchitect or redesign**, not just “fix bugs.” Structural change is expected, but needs a product/recovery justification.

## Signals to keep running long

- Planned features share an understood domain/data authority map.
- Recent changes are reasonably isolated or reversible.
- Periodic real-path checks expose problems that are finite and explainable.
- Review backlog/deferred tests have owners and will not invalidate upcoming work.
- A newcomer can identify which product capabilities really exist.

## Signals to shorten RUN / intervene early

- Two components both act as canonical owners of the same persistent state.
- Similar defects recur after several repairs because modules disagree on a contract.
- Each new feature requires rewriting numerous unrelated modules.
- Core end-to-end flows cannot be attempted due to missing integration seams.
- P0/P1 dependencies, unverified migration assumptions or unrecoverable state are accumulating.
- Review/test debt is growing without a believable date or method of repayment.

When these appear, **pause only the affected risky/dependent work** where feasible, ask a high-value architecture question, run a focused probe and correct the underlying model. R2R is not permission to knowingly extend a broken architectural branch.

## What can be unstable without being unsafe?

| Allowed, with truthful evidence | Needs immediate risk-specific protection |
| --- | --- |
| Partial feature navigation or rough UI | Real user-data destruction / silent migration corruption |
| Missing optional feature behavior | Unauthorized access or credential disclosure |
| Failing noncritical intermediate smoke | Irreversible unsafe external effects |
| Unoptimized performance on an unfinished flow | Violations of rights, privacy or licensed asset constraints |
| Provisional internal module layout | Contradictory data ownership used for high-impact writes |

Some applications (medical, financial, industrial, critical infrastructure) need **much stricter intermediate gates** for affected live/safety domains; developer discretion does not replace legal or safety obligations.

## No artificial maturity labels

Use evidence-backed statuses:

```text
PLANNED → IMPLEMENTED → INTEGRATED → OBSERVED → VERIFIED_FOR_SCOPE
```

These are descriptions of proof, **not obligatory synchronous state gates**. Work can continue in parallel along safe independent paths. A feature may also regress; report the actual current evidence instead of retaining an old VERIFIED label forever.

## Ready is relative to a promised product scope

Final acceptance is **explicit**, **repeatable** and **version-pinned**. It includes necessary real product paths, negative/failure behavior, rights/security and owner decision. Shipping fewer features by re-scoping with owner agreement may be valid; quietly redefining acceptance to match whatever happens to work is not.

See [quality](quality.md) and [adaptive steering](steering.md).
