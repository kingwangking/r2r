# R2R product positioning — the fast iteration layer for AI coding

**Audience:** developers using Codex, Claude Code or comparable coding agents, with or without existing Spec-driven development and multiple concurrent workers.

**Problem:** AI coding accelerates implementation, yet serial Review → fix → full Review loops, ordinary P2/P3 interruptions, lost human direction and incomplete integration can consume the gains before a real product becomes usable.

**R2R's job:** make *successive development iterations* flow faster, with a complete but revisable destination, frequent **developer STEER**, short synchronous Review, severity-based Finding triage, **batched ordinary repairs**, continuous RUN and repeated real-product HARDEN.

## Three complementary dimensions

| Dimension | Focus | R2R's relationship |
| --- | --- | --- |
| **Spec / SDD / Spec Kit** | Requirements, architecture, contracts, tasks and accepted outcomes; its own implement/converge operations | Keep original specifications authoritative; R2R extends the practical iteration and decision cadence |
| **Parallel multi-agent implementation** | Horizontal execution capacity across distinctly owned layers/modules | Use available parallel workers on genuinely separable tasks; let the main Codex integrate results |
| **R2R** | Longitudinal pace of slice-to-slice progress, human steering, risk-scoped Review and final HARDEN | Continue work after meaningful findings; do not restart a comprehensive Review merely because a fix landed |

R2R is compatible with **one or many agents**. It does not run a scheduler, create subagents or replace spec tools. Clear layered architecture and agreed interface ownership are especially helpful for concurrency. An integrated outcome must still be verified when appropriate.

**A developer is highly engaged:** product/architecture decisions, changing priorities, review depth and execution length are regularly steered. R2R is not “set it and forget it”.

[Compatibility guide](compatibility.md) · [Review/Finding economics](../method/review-economics.md) · [v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0)

**Release and evidence:** MIT source and a published `v0.1.0` Skill exist. The improved positioning/routing in this branch is **unreleased**; agent-host behavior and measured iteration speedups remain unverified.
