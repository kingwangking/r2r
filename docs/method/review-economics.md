# Review economics — findings should accelerate the next Slice

**R2R default:** a useful RUN batch → **synchronous quick Review** → severity-based repair/queue → **continue RUN**. Frequent developer steering is expected. The primary coding agent (such as Codex) should collect impactful Findings and keep delivery moving—not get trapped in serial full Review after every repair.

## Triage and routing

| Finding | What to do now | Repeat Review? |
| --- | --- | --- |
| **Code functionality, safety, security, data integrity** | Prioritize by severity and actual dependent harm; fix important affected paths promptly, block unsafe writes/permissions until safe; unrelated safe work can proceed | Short **focused** recheck when the changed contract/risk warrants; full deep check only when materially justified |
| **Ordinary P2/P3** | Record owner, affected module, evidence and target fix batch; **repair together later** | Not by default; targeted regression when batch lands |
| **Pure docs / evidence phrasing** | Fix cheaply and maintain true traceable state | **No repeated independent Review** unless it would corrupt acceptance, safety/authorization or audit traceability |
| **Systemic contract/architecture failure** | Stop dependent work, revisit design/Spec and interface owners; restructure early | Risk-driven deeper architecture/integration check, then return to RUN |

**Severity overrides label.** A concrete data-loss or auth issue is not safely deferrable just because someone called it P2. Never trade away rights, secrets, real-data protections or final release gates.

## The quick synchronous loop

```text
Spec / existing architecture  →  RUN a meaningful Slice or batch
                                   ↓
                       short synchronous source/evidence Review
                                   ↓
                     main Codex / executor triages Findings
                      ├─ high-impact affected path → scoped repair
                      │                             → focused recheck as needed
                      ├─ ordinary P2/P3 → queue for grouped repair
                      ├─ wording-only → correct; no review carousel
                      └─ safe independent work → continue now
                                   ↓
                       next RUN / next Slice ← developer STEER
                                   ↓
                          periodic integrated HARDEN
```

A single reviewer is enough to carry out the baseline loop and must label its own work **self-review**. A genuinely separate reviewer (sequential or in parallel) can be used when available and useful; **R2R does not prohibit parallel implementation agents**. When multiple agents own clearly isolated layers, the primary executor integrates outcomes and triages integration findings.

## What the main executor must keep visible

- Current program/Spec sources, recent changed source/ref and actual proof.
- High-impact Findings with exact affected dependencies; ensure critical repairs have a relevant recheck.
- **One small P2/P3 repair queue** grouped by module, owner or batch; avoid requiring a new governance system.
- Developer STEER changes, current Slice and the next safe iteration.
- Outstanding deep checks that final HARDEN must pay down; no NOT_RUN → PASS promotion.

## When to review deeper

Authentication, migrations, rights, destructive changes, shared persisted state, repeated contract failures or release readiness are worthy of deeper evidence; do them where the risk matters. Avoid requiring every new doc commit or small repair to repeat release-level source/GUI/independent approval.

For detailed severity safeguards see [quality](quality.md), [one-page method](r2r.md), [review template](../../templates/review.md) and [integration with other methods](../product/compatibility.md).

**Outcome to optimize:** accepted software functionality per unit of total developer + agent time, while maintaining the agreed final quality—not number of Review rounds.
