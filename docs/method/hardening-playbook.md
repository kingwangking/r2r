# HARDEN playbook — make the integrated product truly ready

R2R values long-run implementation throughput, but **the finished product, not the backlog, is the acceptance target**. HARDEN is repeated product-level work and may start early when shared architecture becomes unstable. It is **not** a one-time final QA event or merely fixing superficial bugs.

## When to switch from RUN toward HARDEN

| Signal | Developer choice | Why |
| --- | --- | --- |
| Important user journeys connect across modules | Begin real integration and product observation | Discover the missing seams while they are still affordable |
| Repeated local repairs break adjacent modules | Shorten RUN, map systemic contracts, restructure | Fix source of recurring symptoms |
| Two modules act as durable owners of the same state | Pause affected writes, resolve ownership immediately | Prevent compounding data loss and rework |
| Tests report green yet real GUI/process restart is unusable | Prioritize real product path/packaged execution | Correct evidence mismatch |
| Many missing high-impact checks or acceptance debt | Set due stages, run high-information negative/integration probes | Preserve credible convergence |
| User wants candidate release | Full applicable final acceptance; no selective passing | Final quality remains a hard requirement |

The run/harden boundary is **dynamic**, not “after exactly 40 slices.” A partial product may go back to RUN after an architectural repair.

## Practical 5-pass convergence loop (repeat/reorder as evidence demands)

**Pass A — Architecture and authority.** Trace the actual UI/API→domain→store path. Check canonical data ownership, permissions, side effects and module boundaries. If systemic conflicts exist, redesign the boundary and its contracts *first*.

**Pass B — True product journeys.** Use the integrated artifact the user would use. Try create/edit/save/search/export and equivalent promised tasks; distinguish mocks, fixtures, API tests and genuine GUI/packaged workflows. Observe negative input and persistence across a fresh process when relevant.

**Pass C — Recovery, rights and resilience.** Negative authorization, malformed or interrupted operations, restart, migration/rollback, external egress/credentials, and rights of bundled assets. Use isolated fixtures and backups; never use the live customer's data as a crash test.

**Pass D — Regression and performance.** Retest seams changed by structural repairs, then run appropriate broader regressions; measure realistic resources and response. A previous passing test on old SHA or artifact is not approval of the new one.

**Pass E — Scope-level final judgment.** Compare evidence against the promised user journeys, important failure scenarios and explicit acceptance. List P0/P1 and any still-unrun material proof. Owner approves GO/NO-GO; the agent never invents final authorization.

## A small actual evidence record

```text
Product/Build: <repo, SHA, actual tested artifact>
Journey:       <promised user action>
Observation:   PASS / FAIL / NOT_RUN, exact path and source
Structural gap:<contract/data owner/interaction issue, if any>
Repair:        <change/commit actually made, or PLANNED>
Recheck:       <what genuinely reran on the new build>
Remaining:     <risk, test gap, owner, due stage>
Release:       NOT_READY unless full promised quality is supported
```

Keep reports short. A release evidence matrix can be embedded in existing notes; no new database or service needed.

## Failure patterns worth detecting

1. **Late all-at-once testing:** dozens of incompatible state implementations accumulate. Correct approach: early focused authority/integration probes when assumptions matter.
2. **Test theater:** mock tests green while the real packaged app cannot save or restart. Correct approach: observed user-path/restart/negative evidence at relevant milestones.
3. **Endless refactor:** architecture rewrites expand scope with no product acceptance progress. Correct approach: link each structural change to a concrete failed journey and a closing verification.
4. **Scope shrinking by accident:** mark unfinished features “not important” without owner permission. Correct approach: renegotiate scope explicitly; keep original target visible.
5. **Safety deferral:** knowingly leave auth/data-loss/rights risks for the last round. Correct approach: stop affected high-risk operations now.

## Exit criterion

HARDEN is complete **only for the approved scope and tested artifact** when real target journeys and relevant negative/regression behavior have actual passing evidence, material security/rights risks are resolved, and the owner authorizes release. A method example or document consistency pass does **not** prove a complex app is ready.

Related: [quality policy](quality.md), [convergence capability](convergence.md), [HARDEN worksheet](../../templates/harden.md), [illustrative failure scenarios](../../examples/hardening-scenarios.md).
