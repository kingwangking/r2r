# Resume R2R in one message

Use this prompt in a **new conversation** after a prior session ended. It is designed for ChatGPT Web + GitHub, but can work with a coding agent that has repository read permissions.

```text
Continue the R2R program in <OWNER/REPO>. Do not restart planning from scratch.
First inspect the actual default branch, current development branch/PR, exact HEAD,
AGENTS.md, docs/program/current-state.md and docs/program/roadmap.md.
Treat the repository as source of truth; correct any stale checkpoint using Git.
Summarize (1) what was truly delivered, (2) what is unverified,
(3) which high-risk dependencies are blocked, and (4) the next useful work.
Then immediately carry out the next authorized, safe campaign in coherent batches:
RUN → synchronous lightweight self-REVIEW → repair critical affected paths → RUN.
Keep the long-horizon plan and developer STEER, but do not require a new
approval after each ordinary item. Commit actual work and update a compact
resume checkpoint. Do not merge, publish, modify rights or claim background work.
```

## Minimal source check

1. Locate real repository and authority; do **not** start from an old chat summary alone.
2. Read **current branch and PR HEAD**; compare with `docs/program/current-state.md`. An old exact SHA in a checkpoint is *historical*, not a forced checkout instruction.
3. Inspect AGENTS, plan, most recent actual changes and any open P0/P1 holds.
4. If the branch has moved unexpectedly, inspect its actual new diff before writing; use a new branch or seek clarification if concurrent edits would collide.
5. Confirm scope and authorization carried in the live instruction; don't infer permission to merge/release.
6. Continue the next **meaningful** campaign; complete a short synchronous self-review after it. A self-check is not independent Review.
7. Record new actual commit/PR/evidence, unresolved issues and next action.

**Stop condition:** a missing access right, changed owner intent, unknown destructive effect, unsafe dependency, or inability to establish a reliable current source. Ordinary lack of full intermediate smoke quality is not itself a universal stop.

## What a resume response should look like

```text
Observed: owner/repo; branch; HEAD; PR open/draft/merged state
Last delivered: source-backed user-visible outcomes
Review evidence: PASS/FAIL/NOT_RUN, exact scope; self vs independent
Risk/holds: specific affected dependency
This campaign: delivered refs + synchronous quick review finding
Next: next valuable safe step or actual blocker
```

Do not say work ran between conversations. This is **state recovery and continued work after a new instruction**, not perpetual execution.

For the real project record, see [R2R web recovery practice](../examples/r2r-recovery-actual.md) and [long-run protocol](../docs/method/long-run-protocol.md).
