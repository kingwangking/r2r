# R2R — Run to Ready

**From AI-generated code to a real, ready-to-use product.**

**One goal. Three connected capabilities. Continuous developer steering.**

R2R is an **AI-native software delivery method and portable Agent Skill**. It brings together proven **Spec-driven direction**, **multi-agent parallel implementation** when the architecture supports it, and **fast successive iteration**, then keeps integrating, repairing and hardening until the real product meets its acceptance criteria.

**中文：** R2R（Run to Ready）面向 AI 时代的核心交付挑战：**不只是更快生成代码，而是更快、更可靠地把正确的产品真正做出来。** 以 Spec 保证目标和架构方向，用多 Agent 在分层清晰时横向并发，通过持续纵向迭代与开发者高频纠偏推进，最终整合、修复、HARDEN 到 READY。

[Install R2R](#try-r2r) · [中文使用指南](quickstart/use.md) · [Three-capability model](docs/product/compatibility.md) · [v0.1.0 GitHub Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) · [MIT](LICENSE)

## The problem R2R addresses

AI coding drastically expands implementation capacity. A complex product still fails to reach a usable finish if the **goal is wrong**, **parallel changes cannot integrate**, or **serial review/fix/re-review and fragmented tasks stall progress**. Finally, numerous completed tasks are not the same as a reliable product.

**R2R's answer is an integrated path to READY**, not a competing Spec tool, new multi-agent runtime or permission to skip quality:

| Connected capability | What it accomplishes | Practical foundation |
| --- | --- | --- |
| **1 · Correct direction — Spec** | Define *the right product*: actual user journeys, constraints, architectural ownership, contracts and READY criteria | Existing Spec / SDD / [GitHub Spec Kit](https://github.github.com/spec-kit/) |
| **2 · Horizontal throughput — Multi-Agent** | Implement truly independent layers/modules in parallel when the host, ownership and integration contracts allow | Existing coding-agent subagents, branches/worktrees and CI |
| **3 · Longitudinal throughput — Iteration** | Advance Slice after Slice through frequent human STEER, focused synchronous Review, severity-ranked fixes and batched P2/P3 repairs | R2R's distinctive operating policy on top of the existing agent |

**The outcome is not pillar #3. The outcome is READY.** These capabilities feed each other: Spec sets safe implementation boundaries; parallel development increases useful work but creates integration needs; fast iterations feed observed evidence back to the developer and Spec. **Repeated product HARDEN** closes the gap between code produced and the product actually usable.

```text
                   R2R = RUN TO READY
          One target: an accepted software product
                              ▲
              real integration + repeated HARDEN
                              ▲
     ┌────────────────────────┼───────────────────────┐
  CORRECT DIRECTION      HORIZONTAL SPEED       VERTICAL SPEED
  Spec / architecture    optional Multi-Agent   fast RUN / next Slice
  user journeys          owned modules          frequent developer STEER
  contracts / READY      safe parallel work     focused Review / fix queues
     └────────────────────────┼───────────────────────┘
                       observed Git + tests
```

**Mature foundations, unified purpose.** R2R reuses methods and tooling that already exist; it does **not** claim to have invented specification, parallel agents, or convergence. Spec Kit itself supports implementation and convergence. R2R's proposed contribution is a **practical delivery policy integrating these capabilities and allocating human/review effort over time**, especially around rapid vertical iteration.

[How to combine Spec, parallel agents and R2R](docs/product/compatibility.md) · [Finding/review rules](docs/method/review-economics.md)

## How R2R drives progress

After planning against the product's existing Spec:

- **RUN real work.** Allow meaningful batches, with independent agents in parallel where genuinely useful.
- **STEER frequently.** The developer revises product/architecture decisions, priorities, execution length and review depth throughout—not only at phase boundaries.
- **Review briefly and by risk.** Fix material code, security, safety and data-integrity issues promptly, with targeted rechecks when warranted. Queue ordinary, nonblocking P2/P3 for batch repair. Do not re-review harmless wording changes endlessly.
- **Continue the next safe Slice.** The primary Codex/executor collects important Findings and coordinates fixes; one repair does not trigger a mandatory full Review loop.
- **HARDEN to READY.** Integrate real user paths, correct structural faults, exercise recovery and negative scenarios, and verify acceptance of the actual artifact. Do not confuse intermediate progress with finished quality.

Neither long RUN nor parallel implementation overrides credentials, permissions, real-data integrity, intellectual-property rights or irreversible-operation safeguards.

## Try R2R

**Published stable Skill:** [v0.1.0 Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0), MIT, standalone ZIP + SHA-256. [Post-release GitHub CLI install check](https://github.com/kingwangking/r2r/actions/runs/39737882456) passed.

In a GitHub CLI version with `gh skill` support, install to Codex:

```bash
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent codex --scope user
```

[Other agent install options](quickstart/install.md) · [Download release ZIP](https://github.com/kingwangking/r2r/releases/tag/v0.1.0)

**Or without an installation**, prompt a coding agent with actual repository access:

```text
Use R2R (Run to Ready) to deliver this product.
1. Start from our existing Spec, architecture and user acceptance; correct
   missing intent rather than duplicating or replacing the Spec.
2. If the architecture permits and real subagents are available, parallelize
   independently owned layers/modules with explicit integration contracts.
3. Execute meaningful batches and keep successive iterations moving.
   I will steer priorities and architecture frequently. After each batch,
   quickly self-review; fix important functionality/security/data findings
   by severity, batch ordinary nonblocking P2/P3, and avoid full re-review
   cycles for wording-only edits.
4. Integrate, restructure and HARDEN actual product journeys until there
   is evidence for our agreed READY criteria.
Maintain a concise R2R.md progress checkpoint, read real Git state on resume,
protect permissions/data/rights, and report PASS/FAIL/NOT_RUN truthfully.
Begin the first authorized useful batch.
```

The improved three-capability definition and Finding policy in the active development PR are **not** retroactively part of immutable `v0.1.0`; the prompt above reflects the **current source direction**.

## Three actions, developer steering all the way

| Say to the existing agent | Expected action |
| --- | --- |
| **Start R2R** / 采用 R2R 开发 | Ground work in existing Spec, plan safe parallel boundaries and long path to READY; begin authorized work |
| **Continue R2R** / 继续 R2R | Read actual Git and `R2R.md`, integrate results, triage findings and move through more slices |
| **Harden with R2R** / 进入 R2R HARDEN | Repeatedly restructure, integrate, exercise real product/negative/recovery paths and close acceptance gaps |

**STEER ANYTIME:** “We got the architecture wrong”, “Have UI and API agents work in parallel”, “Batch these P2/P3”, “Stop unsafe migration”, “Show the true persisted user path”.

You can start with one agent, without Spec Kit or a multi-agent runtime. R2R **composes available capabilities** rather than installing them. It cannot execute secretly after its authorized session ends, and a same-agent check is not an independent review.

## Trust and scope

**What is real:** published [v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0), MIT license, tested Skill source/package and GitHub CLI install path. **What is not yet proved:** measured speedups over other methods, end-to-end behavior in a real Codex/Claude Code project, or that every developer/project will reach READY.

**R2R offers a complete *operating approach* to an AI-era delivery problem**, not a verified one-click solution, automatic parallel-agent orchestration, or a guarantee of successful delivery. Its value claim can be tested on real projects.

[中文使用](quickstart/use.md) · [One-page method](docs/method/r2r.md) · [Compatibility](docs/product/compatibility.md) · [FAQ](docs/product/faq.md) · [Contributing](CONTRIBUTING.md) · [This project's R2R.md](R2R.md)
