# Long-run protocol — maintain speed across batches and sessions

R2R exists to support projects with **large whole-product plans** and sustained implementation, not a task/PR/review ceremony after every tiny edit. The method is usable with **one active agent** and a Git repository. No local daemon or asynchronous reviewer infrastructure is required.

## 0 — Inputs worth knowing before running

- **Product promise / READY:** actual user journeys and final quality conditions.
- **Architecture boundary:** responsibilities and canonical data owners; important reusable solutions.
- **Program:** a long, revisable sequence of meaningful outcomes (possibly tens or hundreds of slices).
- **Authorization:** repository, branch, actions allowed, sensitive data/rights, who controls publication.
- **Recoverable truth:** last observed Git SHA, actual results, outstanding risks and next campaign.

These can fit in an existing spec, AGENTS.md and a **single checkpoint**. Don't create new governance folders just to follow R2R.

## 1 — RUN meaningful batches, not one review per line

```text
Whole-product PLAN
  ↓
RUN one meaningful batch: user-facing slice(s), not arbitrary fixed count
  ↓
REVIEW synchronously in the same active execution:
  Is the direction still right? Did the change violate a critical authority?
  What actually changed? What evidence ran? What is NOT_RUN?
  ↓
Repair only affected critical dependency (P0/P1) / queue P2/P3
  ↓
Continue the next authorized RUN batch
  ↘ Developer STEER anytime; HARDEN as integration demands
```

A meaningful batch may include **one** risky change or **many** reversible independent changes. The developer selects length and Review depth, and may extend/shorten a campaign midstream.

A *quick* Review is a **synchronous self-review** by default. It is **not** independent audit and does not imply whole-product readiness. High-risk changes may need deeper focused verification *at once* or a genuinely separate sequential reviewer if available.

## 2 — Dependency-scoped holds; no false global stop

Given a finding, distinguish:
- **P0/P1 on data/permissions/critical contract:** stop that action and work that relies on its unsafe assumption; fix it or change the design before depending further.
- **Independent reversible work:** can proceed if its correctness truly does not depend on the unresolved issue.
- **P2/P3 or unrun noncritical tests:** log the claim, missing evidence, owner and due stage; choose when to verify.
- **Lost architectural confidence:** ask a high-information question or run a focused probe; adjust the horizon rather than blindly accumulating output.

Don't use P0/P1 labels to hide a global compromise: if an issue undermines the common foundation, dependent work may in fact include the whole program.

## 3 — Checkpoint when it saves time, not as an approval gate

Store the *smallest* durable record that a future session needs:

```text
Repo / branch / actual HEAD / PR status
Done with evidence / missing proof
Risk and exact dependent paths
Next valuable authorized campaign
Other changed assumptions / necessary permissions
```

The checkpoint may be an existing `docs/program/current-state.md`, a PR comment, or a conversation note committed to the repo. It is **not a substitute for reading Git** on resume.

Save or update the checkpoint after meaningful commits and before handing off. It is acceptable to record the previous verified content SHA inside a commit whose final SHA cannot be known until Git creates it—never claim it is the final commit.

## 4 — Actual cross-session recovery

When the developer returns and says “继续”, follow [one-message resume](../../quickstart/resume-in-one-message.md). **Read the current repo first**, reconcile differences with checkpoint, and then RUN. A disconnected web session cannot keep running.

## 5 — Conditional HARDEN

Do not wait until all tasks are coded if:
- shared state ownership has split;
- repeated patches create more integration failure;
- every new feature rewrites old ones;
- real end-user journeys cannot be exercised despite supposed progress;
- unverified claims become an unpayable acceptance debt.

Switch the affected work into structure-first integration/hardening; resume RUN when evidence supports it. For details see [convergence](convergence.md).

## Operational success criteria

Someone can stop a program after any authorized batch and resume from current Git **without reading an old conversation**; the resumer correctly distinguishes what was done, what was tested, and what remains. Large plans keep direction; *short synchronous review* is not a serial deep-review bottleneck.

**Not guaranteed by this document:** unattended cross-session execution, agent concurrency, fixed speedups, final product quality without real tests.
