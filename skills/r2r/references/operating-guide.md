# R2R operating guide — detailed only when needed

The parent [SKILL.md](../SKILL.md) handles the default path. Load this reference when the agent needs help with a long campaign, risky dependencies or a structured finish. Everything here ships inside the copied Skill directory.

## Start

Ask or infer from the actual project: real user promise, existing specs, architecture/data authority, biggest unknowns, long-term scope, readiness criteria and developer authorization. Read Git and preserve current work. Use [the starter asset](../assets/R2R.md) to create a root `R2R.md` **only if useful for multi-session work**. Do not make duplicate spec, roadmap, evidence and governance hierarchies.

After writing the plan, start the first safe authorized implementation campaign, unless the developer asked only for planning.

## Continue

1. Read actual working tree / branch/HEAD, PR status if available, project instructions and `R2R.md`.
2. Compare the checkpoint's previous SHA with Git; if changed, inspect diff and reconcile, don't reset or overwrite it.
3. Identify the smallest set of critical blocked dependencies; isolate ordinary missing evidence and low-risk work.
4. RUN meaningful product progress; **synchronous short self-review** after the batch; fix critical affected paths.
5. Preserve a concise checkpoint with exact changed files/commit, PASS/FAIL/NOT_RUN scope, risks and next action.
6. Resume more work while the actual session/authorization permits. A conversation ending does not create a future task.

## STEER

A good developer question has high information gain: “Does this business path truly reach persistence?”, “Who owns the canonical state?”, “Which existing mature component did we reuse?”, “What would invalidate upcoming work?”. Answer with source references or a genuine test, not model confidence.

Change execution horizon when risk/architecture understanding changes. No mandatory number of tasks per run.

## HARDEN

Use the product's actual specification/acceptance:
- A — structural architecture, authorities and interfaces;
- B — genuine user paths and integrated real behavior;
- C — errors, permissions, data/rights/recovery;
- D — full relevant regression after material repairs;
- E — explicit human READY/NO-GO judgment.

Start HARDEN early at a risky systemic seam when necessary. Repeat/reorder based on observations. A release-level test absent from the actual environment is `NOT_RUN`, never PASS.

## Review

A synchronous quick Review is a same-agent source/evidence check, often after several small implementation changes batched together. It is **not** a serial broad audit and never independent unless a distinct actual reviewer performed it. Dangerous operations may require deeper checks immediately.

Output should normally be brief: `delivered | proof | material blockers | next`.

## Portability

This guide references **only sibling files in the Skill directory**. Avoid linking to `../../docs/` because that breaks when users copy the Skill from its source repo to their own project.
