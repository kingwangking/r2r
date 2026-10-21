# R2R — Run to Ready

**Plan big. Run long. Harden deep. Steer anytime.**

**[简体中文说明 / 中文快速上手](docs/zh/README.md)** · [Web + GitHub 实践指南](quickstart/web-github.md)

R2R is a lightweight, developer-steered engineering method for building **complex software with AI agents at high throughput while ensuring final product readiness**.

AI generates implementation faster than developers can fully review every intermediate change. At the same time, AI makes larger projects viable. R2R responds by organizing **when to implement, when to validate, when to restructure, and when a product is truly ready**.

> Spec describes what to build. R2R helps keep building it and reach a reliable product.

## The four moves

1. **PLAN** — Set whole-product outcomes, a capable architecture, a long-horizon plan and final acceptance.
2. **RUN** — Keep delivering valuable work. Synchronous lightweight review after meaningful batches; deepen only when risk demands it, rather than gating every small edit on an exhaustive review.
3. **HARDEN** — Integrate real user journeys, restructure where needed, fix defects, test and repeat until final quality is evidenced.
4. **STEER ANYTIME** — The developer can ask targeted questions, adjust how long agents run, increase/decrease review effort or redirect architecture.

**Long runs are a core capability, not a compulsory fixed interval.** Intermediate product builds may be incomplete or unstable. Security, rights, irreversible data protection, source authority and truthful reporting remain non-negotiable.

## One-file agent skill (optional)

**Current Review mode:** synchronous, short, risk-scoped review in the active execution sequence: implement → review immediately → record findings → continue. It does **not** require a local multi-agent system or a separate reviewer. A self-check must be labeled self-check; a genuine independent Review is optional and must be performed separately if claimed. See [Review economics](docs/method/review-economics.md).

The [R2R Agent Skill](skills/r2r/SKILL.md) packages these instructions in the portable **Agent Skills** format. Copy the core prompt below if your agent does not support skills—**no installation or local process is required**.

## Start in two minutes

Use this with your existing AI coding assistant; no R2R app, local runner or installation needed:

```text
Use R2R for this project:
PLAN the complete product, architectural boundaries, long-term roadmap and final acceptance.
RUN meaningful feature work continuously within my authorized scope; make cheap targeted checks,
review synchronously and briefly after each meaningful batch, and do not stop productive work for routine deep re-reviews or an
imperfect intermediate version. Leave a recoverable account of actual changes and next work.
I may STEER ANYTIME by questioning direction, requesting evidence, changing run length or review depth.
Once the product paths exist, HARDEN repeatedly through integration, restructuring, real-use
checks and comprehensive repair until the agreed release bar is actually demonstrated.
Never bypass security/rights/irreversible-data boundaries or claim tests ran when they did not.
```

Continue with [quickstart](quickstart/README.md), [one-page method](docs/method/r2r.md), [long program](docs/program/roadmap.md) and [templates](templates/README.md).

## Scope and honesty

Current deliverable: a **usable method, instruction kit, templates and evolving real-world study plan**. R2R is not yet a validated standard, an autonomous execution runtime or a promise of unattended execution outside an active authorized agent session. The repository is currently private; public licensing and visibility require separate approval.

See [documentation map](docs/README.md).
