# Structural convergence scenarios — teaching fixtures, NOT real tests

Each scenario is **hypothetical**. No GUI, storage, data migration or application test was executed for this document. Use them as reasoning exercises or adapt only in an isolated/authorized test environment.

## 1 — Two sources of truth

**Claim:** “The new editor has save, undo, redo and history features.”
**Observation to seek:** after save → author input → undo → redo → process restart, stored revisions disagree with UI history.
**Structural diagnosis:** both editor state and history service persist independently without a single authoritative transaction.
**R2R response:** hold dependent irreversible writes; redesign one authoritative revision transaction with adapter interfaces. Then rerun actual save/undo/restart through the real UI and inspect persisted records.
**What may continue:** reversible documentation, unrelated menu layout, or other work proved independent of revision correctness.
**READY:** NOT_RUN until a real packaged process / fixture confirms the flow.

## 2 — Green code, unusable product

**Claim:** “40 functional slices are implemented and the unit suite passes.”
**Observation to seek:** app boots but UI cannot navigate from project creation to a usable editor; packaged build may lack required assets.
**Diagnosis:** locally implemented pieces never joined into real user journeys.
**R2R response:** enter integration HARDEN, wire the flow and verify the exact shipped artifact. Structural reorganization may be more valuable than another isolated unit fix.
**READY:** NOT_RUN; no user path tested in this scenario.

## 3 — The late verification debt trap

**Claim:** “Tests can wait until all features are coded.”
**Risk:** unverified assumptions spread across many dependent modules; later rewrite exceeds all time saved.
**R2R response:** stop extending the disputed shared contract, run the smallest integration/authority probe that could falsify it, then fix the root design. Do not demand deep review of unrelated reversible UI tasks.
**Verdict:** if R2R failed to prompt this correction, the method's promised throughput benefit may be false; measure total rework.

## 4 — Unsafe shortcut disguised as a quick review

**Claim:** “The migration is one line; it can be fast-reviewed later.”
**Risk:** customer data could be irreversibly rewritten.
**R2R response:** require authorized isolated copies, backup/recovery proof, precise permission and an appropriate deep review *before* affected live mutation.
**Verdict:** intermediate quality flexibility NEVER authorizes real-data loss, rights/security violations or unsafe irreversible operations.

## 5 — Structural repair becomes an endless project

**Claim:** “We should rewrite all modules because the architecture might be cleaner.”
**Risk:** endless work without measurable improvements to the actual user promise.
**R2R response:** tie redesign to an observed failed journey, name the minimal interface change, verify the corrected flow and stop extending refactor scope without new evidence.
**Verdict:** an implementation can be imperfect yet sufficient for accepted scope; R2R does not reward elegance in place of delivered product.

## Worksheet for each scenario

```text
Observation with exact artifact:     PASS / FAIL / NOT_RUN
Systemic or local failure:          hypothesis until checked
Dependent paths to hold:            only what is truly affected
Cheapest falsifying experiment:     specific
Repair + recheck:                   actual / planned
Owner acceptance:                   pending / recorded
```

See [HARDEN playbook](../docs/method/hardening-playbook.md) and [field evaluation protocol](../docs/research/evaluation-protocol.md).
