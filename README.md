# R2R — Run to Ready

**Fast AI coding iteration. Fewer review bottlenecks. Real product readiness.**

*Plan big · Run long · Harden deep · Steer anytime.*

**中文：** R2R 是 AI 编码快速迭代 Skill：在 Spec 规划和可选的多 Agent 并行开发基础上，通过开发者高频参与、分级处理 Finding、批量修复普通问题与最终 HARDEN，持续推进真实软件产品交付。

[Quick start](#quick-start) · [中文使用指南](quickstart/use.md) · [Spec + multi-agent compatibility](docs/product/compatibility.md) · [v0.1.0 Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) · [MIT](LICENSE)

## The problem: AI writes faster than projects finish

AI coding agents can produce code rapidly. But complex products often slow down because:

- Every tiny change enters **full Review → fix → full Review again**, creating a serial bottleneck.
- Ordinary P2/P3 findings and wording-only changes keep interrupting the main coding agent.
- Developers have critical product and architecture insight, yet conventional loops underuse **frequent developer steering**.
- Many completed slices or parallel agent outputs don't automatically become **one reliable, integrated product**.

**R2R's answer:** keep the full product destination visible, RUN meaningful batches, do short risk-focused Review, promptly repair impactful functionality/security/data problems, **queue ordinary P2/P3 for grouped fixes**, and resume the next Slice. Then repeatedly HARDEN actual user journeys. Never defer dangerous real-data, permissions, rights or safety boundaries merely for speed.

## R2R fits with Spec-driven development and parallel agents

| Layer | What it solves | How R2R combines |
| --- | --- | --- |
| **[Spec-driven development / Spec Kit](https://github.github.com/spec-kit/)** | Requirements, architecture, tasks, contracts and acceptance criteria (including its own implementation/convergence) | **Preserve existing Spec as authority**; R2R does not duplicate or replace it |
| **Parallel multi-agent coding** | **Horizontal throughput** across independent UI / API / domain components with clear ownership | Multiple agents may implement in parallel when the host and architecture permit; the main executor integrates |
| **R2R** | **Longitudinal iteration throughput** across many batches, findings, human decisions and integration | RUN → quick synchronous Review → fix important / batch ordinary findings → next Slice → repeated HARDEN |

**Spec sets the target; parallel agents speed up independent work; R2R keeps successive iterations moving toward a mature product.** R2R works with one agent too. It does **not** ship a new orchestrator or prohibit multi-agent development.

```text
Developer + existing Spec / architecture
                  ↓
Main Codex → RUN useful slice(s) ← optional parallel UI / API agents
                  ↓
Integrate → short synchronous Review
            ├── important code / security / data issue → scoped fix & quick recheck
            ├── ordinary P2/P3 → batch repair queue
            └── wording only → correct, usually no independent re-review
                  ↓
Developer STEER → next Slice → next Slice → product HARDEN → READY
```

[Detailed compatibility and practical example](docs/product/compatibility.md) · [Finding routing](docs/method/review-economics.md)

## Quick start

**Stable published Skill:** [v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) (MIT). The post-release [CLI install / ZIP checksum smoke](https://github.com/kingwangking/r2r/actions/runs/39737882456) passed.

For Codex, use GitHub CLI with `gh skill` support:

```bash
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent codex --scope user
```

For Claude Code, see [installation and ZIP/manual alternatives](quickstart/install.md).

**Without installing a Skill:** copy this prompt into an AI coding agent with access to your project:

```text
Use R2R for fast iteration on this project. Read the real repository and
existing Specs/architecture; keep the Specs authoritative. Set a revisable
whole-product plan and a short R2R.md checkpoint, then start the first
authorized useful RUN. After meaningful batches, perform a short synchronous
self-review. Fix impactful code, safety and data-integrity issues by severity,
with a focused recheck if needed; group ordinary P2/P3 repairs; don't restart
full Review for wording-only fixes unless acceptance, security authorization
or traceability depends on them. I will steer frequently. Continue the next
safe Slice. Use parallel workers only for well-owned independent modules if
the actual host supports them. HARDEN real integrated user journeys before
claiming READY. Preserve permissions and honest PASS/FAIL/NOT_RUN evidence.
```

The refined Finding-routing text on the current HARDEN branch is **unreleased**; it does not retroactively alter the immutable v0.1.0 ZIP.

## Use three natural-language actions — steer at any time

| Say | Expected agent behavior |
| --- | --- |
| **Start R2R** / 采用 R2R 开发 | Read real source/Spec; create or update `R2R.md` and a long product plan; begin authorized code work |
| **Continue R2R** / 继续 R2R | Verify actual Git state; collect findings, batch nonblocking repairs and continue the next safe Slice |
| **Harden with R2R** / 进入 R2R HARDEN | Connect real product paths, repair structural failures, test recovery/negative cases and converge on acceptance |

**STEER frequently:** “Check the persistence authority”, “Parallelize the independent UI and API tasks”, “Repair P2/P3 in one batch”, “Don't review this wording change again”, or “Pause this dangerous migration”.

R2R does not create unattended background execution. Same-agent quick review is **self-review**, not an independent reviewer. Real tool access and developer authorization still govern execution.

## Who is it for?

Developers using **Codex, Claude Code or other AI coding agents**, especially with existing Spec-driven processes, CI, Git worktrees and optional parallel agents on clearly layered software. R2R is the **iteration, feedback-routing and final-convergence layer**, not a replacement for Spec, tests, CI or high-risk reviews.

[Full Chinese guide](quickstart/use.md) · [One-page method](docs/method/r2r.md) · [Compatibility](docs/product/compatibility.md) · [Contributing](CONTRIBUTING.md) · [Project's own R2R.md](R2R.md)

**Evidence boundary:** official Skill publishing checks and CLI installation have passed. Real Codex/Claude Code workflow adherence and measured development-speed improvements remain unverified; no numeric performance claim is made.
