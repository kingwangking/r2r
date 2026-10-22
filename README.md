# R2R — Run to Ready

**Plan big. Run long. Harden deep. Steer anytime.**

**[中文：R2R 如何真正使用](quickstart/use.md)** · [Installation](quickstart/install.md) · [One-page method](docs/method/r2r.md) · [Research](docs/README.md)

R2R is a **portable, developer-steered workflow for AI coding agents**. It helps build complex software through a whole-product plan, sustained implementation, synchronous lightweight review, recoverable progress and repeated product-level hardening.

It is **not** a new coding model, daemon, task scheduler, orchestration server or requirement to keep every intermediate revision release-ready.

## Use R2R in an existing project

There are two ways:

**Without installing anything:** paste this into an AI assistant that has access to your repository:

```text
Use R2R for this project. Read the actual repository and existing specs.
Create or update R2R.md as one durable program + execution checkpoint:
whole-product goals, architecture boundaries, long-horizon roadmap, final READY,
current evidence, risks and the next meaningful campaign.
Then, within my authorized scope, start implementing the first safe campaign.
After each meaningful batch, synchronously do a short self-review and continue.
I may steer at any time. Never claim unrun tests passed, bypass security/rights
boundaries or publish/merge without permission. Save actual state before stopping.
```

**Install the released Skill (after public publication):** GitHub CLI can install directly from a tagged R2R repository release, and tracks updates:

```bash
gh skill install kingwangking/r2r r2r --agent codex --scope user
# Alternative cross-agent installer:
npx skills add kingwangking/r2r --skill r2r
```

**Installation:** select an actually published tag from [GitHub Releases](https://github.com/kingwangking/r2r/releases), or copy the self-contained [`skills/r2r/`](skills/r2r/SKILL.md) folder or use a [prompt-only route](quickstart/install.md). The distributable release is a **versioned GitHub Release/Tag** over this source; a dedicated ZIP containing only the Skill folder is optional. See [distribution and release process](docs/product/distribution.md), [v0.1.0 candidate notes](docs/product/release-candidate-v0.1.0.md) and [changelog](CHANGELOG.md).

## Then use three natural-language actions

| Say | What the agent should do |
| --- | --- |
| **“Start R2R on this project”** | Read actual code/specs; create or update the single project-level `R2R.md` program; start the first authorized RUN. |
| **“Continue R2R”** | Compare `R2R.md` to live Git, resume the next safe campaign, synchronous quick review after each meaningful batch, update state. |
| **“Harden this product with R2R”** | Integrate and actually exercise end-to-end paths; restructure, fix, rerun meaningful quality checks and report what remains before READY. |

**Steer anytime:** “Pause and inspect the persistence architecture”, “Run longer”, “What is working end to end?”, “Change the roadmap”, or “Review this security boundary deeply.”

These are **natural-language triggers**, not claimed native slash commands or self-running background jobs.

## What is persisted?

The agent uses **one `R2R.md` in the user's project** as a small durable control file; it links to existing specifications rather than duplicating them:

```text
my-product/
  existing code and docs...
  R2R.md                     ← goal, long program, current truth, next RUN
  .agents/skills/r2r/        ← optional Codex project-local Skill (copy folder)
```

[Copyable starter template](skills/r2r/assets/R2R.md). It is optional for a trivial one-off task, but highly recommended for long-horizon and multi-session work.

## Core policy

- **PLAN:** whole-product direction, important architecture and readiness criteria; long roadmap but revisable detail.
- **RUN:** sustained meaningful work in authorized sessions. Intermediate builds may remain incomplete or imperfect.
- **REVIEW synchronously:** quick self-review after meaningful batches, not full deep review after each small edit; deep checks when important risk demands it.
- **HARDEN:** repeated integration, structural improvement, real-path and negative testing until the agreed product is genuinely READY.
- **STEER ANYTIME:** developer controls run length, scope and review intensity.
- **Always protect:** rights, credentials, permissions, real or irreversible data, and truthful PASS/FAIL/NOT_RUN reporting.

## Choose the shortest reading path

1. [Use it from start to finish (Chinese)](quickstart/use.md)
2. [Install or copy the Skill](quickstart/install.md)
3. [Illustrative first-to-final conversation](examples/complete-usage.md)
4. [Portable Skill](skills/r2r/SKILL.md) and [single project-state template](skills/r2r/assets/R2R.md)

Deep methodology, research, comparisons, examples and the [internal R2R development program](docs/program/roadmap.md) are optional reading, not installation requirements.

**Versioned distribution:** [GitHub Releases](https://github.com/kingwangking/r2r/releases). The first version is `v0.1.0`; inspect the actual Releases page to confirm it has been published before using a pinned installation command.

**License:** [MIT](LICENSE), including the distributable Skill directory. This is an instruction-based product: package verification can pass without proving that a particular AI host follows every R2R instruction.
