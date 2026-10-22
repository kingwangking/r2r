# Risk-directed verification and final convergence

## Quality over time
R2R deliberately permits incomplete functionality, rough UI, temporary integration failure and architecture reshaping during development. It does **not** promise arbitrary defect accumulation can be repaired cheaply at the end.

**Protected now:** rights, credentials, authorization, irreversible external effects, real persistent data, reproducible state and noncontradictory core data ownership.

## Four validation modes

| Mode | Question | Trigger |
| --- | --- | --- |
| T0 targeted | Is this small change obviously broken? | Cheap as useful, often each slice |
| T1 integrated | Do boundaries and combined modules behave coherently? | Periodically, shared seams, or developer demand |
| T2 product | Can users actually finish the end-to-end journey? | Milestones, uncertainty, early real-use feedback |
| T3 release | Does the full agreed quality bar hold? | Candidate delivery, repeated final hardening |

Skipping T1/T2 during a particular development slice is acceptable when risk allows; **mark NOT_RUN** and keep the gap visible. Do not claim that isolated unit tests prove real UI, persisted restart or release quality.

## Review routing
- **P0:** rights/security/irreversible data corruption or dangerous authority violation — stop affected action and resolve.
- **P1:** severe user/core path or systemic issue — hold affected dependent path, fix and retest; unrelated work may continue.
- **P2:** important but genuinely nonblocking — add to a batched repair queue with affected scope, owner and target stage; do not defer a safety/data-integrity defect merely because someone labeled it P2.
- **P3:** minor — batch or explicitly accept with owner authorization where needed.

**Synchronous by default:** immediately after a meaningful RUN batch, the executing agent performs a short risk-scoped self-review, records its actual scope and continues when safe. **Functionality, security and data integrity findings** are repaired promptly by severity, with limited focused rechecks. **Pure documentation/evidence wording** does not warrant repeated independent Review unless it changes acceptance, security authorization or traceability. The primary Codex/executor collects material Findings, queues ordinary P2/P3 for grouped repair and resumes RUN; every fix is not another universal Review gate. This is NOT independent review. A separate reviewer can later be requested and run sequentially when genuinely available. A quick review is never final release sign-off.

## Verification debt
A deferred claim needs at least: **claim, affected dependency, evidence available, evidence missing, risk, due-by stage, owner**. Example: in-process save works, separate-process restart NOT_RUN, must be checked before playable candidate. No silent promotion of NOT_RUN to PASS.

## Convergence mechanism
1. Run actual promised user journeys and observe failures.
2. Identify **systemic mismatch**: missing connections, duplicate state authority, incoherent UX, unstable architecture.
3. Restructure/rewire when needed before polishing symptoms.
4. Repair and rerun appropriate tests, including permissions, recovery and negative paths.
5. Repeat until *real* final acceptance and rights/security obligations have evidence.

If deferred checks and systemic rewrites grow faster than functionality, shorten the RUN horizon and harden earlier. Intermediate freedom cannot mean abandoning ability to converge.

**Release =** demonstrated real journeys + agreed negative/regression verification + no unresolved unacceptable risks + explicit owner release authority. All coded tasks being checked off is not release evidence.
