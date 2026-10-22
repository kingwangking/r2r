---
name: r2r
description: Use R2R (Run to Ready) to deliver AI-built software from correct Spec through nested multi-agent Campaign execution when available, dynamic model/effort selection, rapid iteration and evidence-backed readiness. No extra runtime.
---

# R2R — Run to Ready

**Plan big · Run long · Harden deep · Steer anytime.**

**R2R = Run to Ready: get from a trustworthy product goal to an actually usable, accepted product.** The outcome is READY, not merely generated code, a complete task list or a fast iteration counter. Its coherent operating model combines three connected capabilities:
1. **Direction / correctness — Spec:** establish true user outcomes, constraints, architecture/ownership and acceptance using the project's existing specification system.
2. **Width / parallel execution — multi-agent:** on large separable programs, prefer **multiple concurrent Campaign Lead Agents, each genuinely delegating its own scoped Workstream subagents**, with one Integrator for shared seams. Models and reasoning effort are selected per role and risk, not pinned to one preset. If agents/tools are unavailable, execute sequentially and say so.
3. **Depth / successive iteration — R2R's focus:** advance RUN after RUN, with frequent developer STEER, targeted Review, severity-routed fixes, a batched P2/P3 queue, durable recovery and repeated product HARDEN until evidence supports READY.

**These are interdependent, not three competing frameworks.** Wrong goals make parallel implementation wasteful; parallel outputs without integrated iteration drift apart; rapid iterations without agreed READY criteria can produce an incomplete product. Spec and agent runtimes supply mature building blocks, while R2R supplies the encompassing delivery policy. It is an instruction Skill for existing coding agents—not a new Spec engine, agent orchestrator or background daemon.

**One integrated workflow:** preserve existing Spec/Spec Kit `spec.md`, `plan.md`, `tasks.md` as authority; translate its tasks into bounded work for independent agents only when useful; let the primary executor integrate their results, collect meaningful Findings, apply focused synchronous Review and resume the next Slice. Developer steering is frequent and authoritative. Spec Kit itself supports implement/converge; R2R builds on, rather than claims to replace, those steps.

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

## PLAN — correct destination from real Spec

Use the product's existing Spec/SDD, accepted user journeys, architectural ownership and measurable READY criteria to ensure the work is pointed at the **right outcome**. No competing specs; if gaps exist, clarify them with the developer and update the established authority. An efficient but wrong product is not R2R success.

## PLAN — whole product, long but revisable program

Capture **actual product promise**, complete major user journeys, credible architecture/data ownership and mature reuse, protected risks, long-horizon outcomes and final READY criteria. The roadmap may contain dozens/hundreds of slices. Unknown details are hypotheses, not facts; change them when reality disproves them.

Do not stop after a beautiful plan when the user also authorized implementation; **start the first safe meaningful RUN**.

## RUN — hierarchical agent topology and model selection for substantial work

If several complete Campaigns are ready and the current execution surface genuinely supports nested agents:

1. **Program Lead / main executor:** freeze only necessary shared contracts and source pins, own Wave/frontier/triage and launch independent Campaign Lead Agents concurrently.
2. **Every Campaign Lead:** actively delegate scoped implementation, testing, reference, review or repair work to its own Workstream subagents (more than one when useful); integrate and verify the child results before claiming the Campaign delivered.
3. **One Integrator per shared seam:** cross-Campaign state, public DTOs, migrations, Host/Save and protected release operations are not editable by unrelated children.
4. **Adaptive models:** select actually available models and supported reasoning effort by task capability, consequence, latency/cost and current permissions. A single model family or fixed maximum thinking effort is **not a global requirement**; routine work may use faster/lower-effort agents, critical architecture/security may merit stronger reasoning.
5. **Proof, not theater:** report which Agents actually ran, their owned inputs/outputs, actual checks, child findings and integrated outcome. When real subagents/parallelism are unavailable or unsafe, use scoped sequential work and state the limitation. Do not fake nested dispatch or require paid services.

Read [hierarchical agents & model-routing details](references/hierarchical-agents.md) only when this topology is applicable. It is the **preferred scalable execution pattern**, not mandatory for trivial tasks, permission gates or a host with no nested-agent support.

## RUN — continuous execution in authorized scope

1. Choose a meaningful batch horizon (small for uncertain dangerous seams, large for understood reversible work). The developer can extend/shorten it at any moment.
2. Implement **real product value**, not merely create docs/task IDs. For substantial separable work with supported resources, execute the **Program Lead → parallel Campaign Leads → each Lead's Workstream subagents** topology above; the parent/Integrator combines outputs and verifies full behavior. Otherwise execute within the available scope sequentially. Never mistake an instruction to spawn agents for evidence that they actually ran.
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

Never pretend a second independent reviewer exists. Current default Review is synchronous and lightweight; **hierarchical multi-Agent execution is the preferred option for large, separable projects when actually supported**. Model/effort assignment is flexible, not fixed. No automatic async Review infrastructure is assumed. Do not claim hidden work after a session ends or that unrun tests passed. No auto-merge, public release or deployment without authorization.

More detail if needed: [references/operating-guide.md](references/operating-guide.md). No external R2R repository files are required to use this copied Skill.
