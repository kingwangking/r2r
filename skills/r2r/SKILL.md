---
name: r2r
description: Use R2R for fast AI software development iteration, long-running coding campaigns, human-steered implementation, batched bug fixing, focused code review and final hardening. Complements spec-driven development and parallel multi-agent coding; no extra runtime.
---

# R2R — Run to Ready

**Plan big · Run long · Harden deep · Steer anytime.**

A portable workflow for **existing** AI coding agents. It strengthens **fast successive iterations and feedback-to-fix throughput**, not the definition of specs or the parallel computing ability of multiple agents. It does not supply tool access or run a background daemon.

**Composable workflow:** keep any existing specs (including Spec Kit `spec.md`, `plan.md`, `tasks.md`) authoritative for requirements and design; when modules have clear ownership, allow distinct agents to implement independent slices **in parallel**. R2R governs the main executor's **successive** RUN → focused Review → fix/queue → next RUN → HARDEN loop across those results. Parallelism is optional, never prohibited or required. Developers steer frequently; their questions/priority changes are ordinary inputs, not exceptions. Do not duplicate or replace their Spec process.

## Recognize three user intents

1. **Start / initialize** — “Use R2R on this project”, “开始 R2R”, “用 R2R 开发它”.
2. **Continue / resume** — “Continue R2R”, “继续 R2R”, “接着执行之前的长期规划”.
3. **Harden / finish** — “Harden with R2R”, “R2R 收敛”, “把产品修到可交付”.

**Steer anytime** in any mode: ask architecture questions, change run horizon, inspect evidence, stop risky dependencies, adjust plan or Review depth. These are natural-language intents, **not** native slash commands implemented by this Skill.

## Always read the real project first

- Inspect actual repository root, branch/HEAD (and working-tree changes if available), existing specs/AGENTS/project docs and user authorization.
- In **START**, create or update one root `R2R.md` from [assets/R2R.md](assets/R2R.md) when a long-lived project needs durable state. Reuse existing specs, ADRs, issue lists and CI; link them rather than duplicate. Do not overwrite an existing R2R.md blindly.
- In **CONTINUE**, read `R2R.md` **and** current Git facts; Git reality supersedes stale status. Do not re-plan from scratch or overwrite unexpected concurrent changes.
- In **HARDEN**, read promised end-to-end journeys and READY requirements. Decide what can actually be exercised with available tools. If critical environment/test access is unavailable, say so.

## PLAN — whole product, long but revisable program

Capture **actual product promise**, complete major user journeys, credible architecture/data ownership and mature reuse, protected risks, long-horizon outcomes and final READY criteria. The roadmap may contain dozens/hundreds of slices. Unknown details are hypotheses, not facts; change them when reality disproves them.

Do not stop after a beautiful plan when the user also authorized implementation; **start the first safe meaningful RUN**.

## RUN — continuous execution in authorized scope

1. Choose a meaningful batch horizon (small for uncertain dangerous seams, large for understood reversible work). The developer can extend/shorten it at any moment.
2. Implement **real product value**, not merely create docs/task IDs, within the actual session's tools and permissions.
3. After each meaningful batch, do a **brief synchronous same-agent Review** (unless a real separate reviewer is available and actually used). Focus on impactful source, functionality, safety, data integrity, contracts and honest evidence. This is **self-review**, not independent review.
4. **Route every meaningful Finding, then keep moving:** repair code/functionality, security and data-integrity defects promptly **according to severity and dependent risk**, using a short targeted recheck when justified. Stop P0/P1-affected work, not all independent work. Queue ordinary nonblocking P2/P3 by owner/area/batch for later grouped fixes. For purely documentary or evidence-wording findings, do **not** repeatedly request independent Review unless the wording changes acceptance, security/authorization or traceability; correct the text and move on.
5. **Main executor (e.g. Codex)** owns triage, assigning fixes to itself or truly available agents, collecting material findings and resuming the next slice **after the focused fix check**. Never restart a complete Review loop just because a fix landed. Extra review is risk-triggered, not change-triggered.
6. Save the observed branch/SHA, actual delivered outcomes, meaningful findings, batched P2/P3 queue and **next safe campaign** in `R2R.md` after coherent work and on stopping. Do not require approval after each low-risk tiny change.
7. If the agent has no code/Git tools, do not pretend a modification/test happened. Save/copy the plan as text and state the actual blocker.

## HARDEN — evidence-backed readiness, repeat as needed

When important end-to-end flows exist or structural failure signals appear:
- Exercise real integrated product paths, not just green mocks.
- Correct duplicate state authority and interface/UX architecture **before** chasing repeated symptoms.
- Test real interactions, persistence/restart, permission/negative paths, recovery and appropriate regressions as the project requires.
- Distinguish `PASS`, `FAIL`, `NOT_RUN`, and `BLOCKED` with exact source/build/evidence. Rerun affected checks after material rewrites.
- Only the owner may authorize release or accept material risk. “All tasks coded” is not READY.

## Persistent state: one `R2R.md`, not a bureaucracy

Use [assets/R2R.md](assets/R2R.md) as a **starter template**. Keep it short. Maintain only the global product target and references, long roadmap and current execution truth. Don't duplicate already authoritative plans or create dozens of progress files.

At a meaningful stopping point, answer briefly:

```text
Delivered: <real outcomes and code/ref>
Quick self-review: <scope, findings, PASS/FAIL/NOT_RUN as appropriate>
Blocked: <only affected risky dependencies>
Next: <the next meaningful authorized campaign>
R2R.md: <updated / not updated, why>
```

## Safety and scope

The method never grants new access. Protect auth/rights/secrets/real irreversible data, preserve other people's work and branch history, honor human approval points. High-consequence risky changes need focused deep checks **now**, not deferred to final HARDEN.

Never pretend a second independent reviewer exists. Current default Review is synchronous and lightweight; **optional parallel implementation agents are welcome** when the host supports them and boundaries are clear. No automatic async Review infrastructure is assumed. Do not claim hidden work after a session ends or that unrun tests passed. No auto-merge, public release or deployment without authorization.

More detail if needed: [references/operating-guide.md](references/operating-guide.md). No external R2R repository files are required to use this copied Skill.
