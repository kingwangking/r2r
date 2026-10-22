# R2R — Run to Ready

### AI can write the code. Why is your product still not ready?

**An AI-native software delivery method & installable Agent Skill.**

**The bottleneck moved.** Coding agents can create more software, more quickly, than ever. But a pile of generated features, parallel branches and green unit tests is not necessarily a product anyone can actually use.

> **The problem is no longer just generating code. It is getting the *right product* all the way to READY.**

**中文：** AI 编码已经很快了，为什么复杂产品还是迟迟交付不了？R2R（Run to Ready）聚焦 AI 时代的新交付瓶颈：**目标正确、横向并发、纵向持续迭代，最终整合到真实可用的产品。**

[**Try R2R ↓**](#try-it-in-your-existing-coding-agent) · [中文使用指南](quickstart/use.md) · [How the three capabilities fit together](docs/product/compatibility.md) · [Stable v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) · [MIT](LICENSE)

---

## Does this sound familiar?

*An illustrative situation, not a measured benchmark:*

| It looks productive… | …until you try to ship |
| --- | --- |
| AI completes slice after slice | The overall user journey is still broken |
| Several agents work in parallel | Interfaces conflict; their outputs do not integrate |
| Every PR receives another comprehensive Review | Fix → Review → fix → Review becomes the slowest part |
| The test suite looks green | GUI, persistence, upgrade or real negative paths still fail |
| The backlog is almost empty | Nobody can confidently say **READY** |

**All the activity is real. The delivery is still stuck.**

Adding more agents is not enough if the target is wrong. A detailed Spec is not enough if execution repeatedly stalls. Shipping more code is not enough if the integrated product remains incomplete.

This is why R2R starts with the **delivery problem**, not a new framework or a promise of magical speedups.

## What's actually missing?

Three closely connected capabilities need to work **as one system**:

| | Established building block | Contribution to READY |
| --- | --- | --- |
| **01 · Get the goal right** | **Spec / Spec-driven development** ([Spec Kit](https://github.github.com/spec-kit/), existing requirements, architecture and acceptance) | Build the *correct* product, with credible module boundaries and real completion criteria |
| **02 · Expand execution width** | **Multi-agent parallel coding** (only where real agents, interfaces and independent ownership exist) | Build separated layers concurrently without pretending integration is free |
| **03 · Keep iterations compounding** | **R2R's longitudinal loop**: developer STEER, meaningful RUN batches, focused Review, triage and grouped repairs | Prevent work from dying in repeated review ceremonies; integrate, learn and continue the next safe slice |

**Then HARDEN until READY.** Real product journeys, state integrity, recovery, contracts, rights/security, regressions and the maintainer's acceptance—not simply “tasks completed”.

```text
                       R2R = RUN TO READY
               THE RIGHT, USABLE, ACCEPTED PRODUCT
                                ▲
                 REAL INTEGRATION + HARDEN
                                ▲
      ┌─────────────────────────┼──────────────────────────┐
      │                         │                          │
  CORRECT DIRECTION       HORIZONTAL WIDTH         VERTICAL MOMENTUM
  Spec + architecture     Parallel multi-agent     RUN → focused Review
  user journeys           isolated modules         important fixes now
  READY criteria          integration ownership    ordinary P2/P3 batched
      └─────────────────────────┼──────────────────────────┘
                       FREQUENT DEVELOPER STEER
```

**Why the combination is plausible:** mature tools already handle specifications, coding agents and parallel work. R2R does **not** claim to invent them, or to replace [Spec Kit's implementation and convergence](https://github.github.com/spec-kit/). R2R proposes a practical **whole-delivery operating policy** joining these capabilities and making the *serial iteration/re-review bottleneck* an explicit problem to solve.

[Read the architectural fit →](docs/product/compatibility.md) · [Read the Finding/review policy →](docs/method/review-economics.md)

## The difference is what happens after the first implementation

**Common stall (illustrative)**

```text
Plan → build Slice 1 → Review → fix → Review → fix → Review
                  ↓
             next Slice waits
                  ↓
           integration postponed
                  ↓
         product is still NOT READY
```

**R2R operating loop**

```text
Real Spec → safe independent work in parallel where useful
              ↓
       integrate a meaningful RUN batch
              ↓
       short, risk-focused Review
          ├─ serious functionality/security/data issue → fix promptly
          │                                               ↳ focused recheck
          ├─ ordinary P2/P3 → visible queue → grouped repair batch
          └─ wording only → correct directly, no review carousel*
              ↓
     DEVELOPER STEER → NEXT SAFE SLICE → NEXT RUN
              ↓
       real end-to-end HARDEN → READY
```

*Exception: wording that affects acceptance, authorization, security or traceability deserves the necessary scrutiny. Safety/data integrity never gets deferred just to keep a loop moving.*

The developer participates **throughout**: correcting product understanding, switching priorities, changing architecture, deciding run horizons and demanding deeper checks when risk warrants them. **R2R is not “tell the agents to run unattended forever.”**

## See the problem — then the solution

**[▶ Open the animated, interactive demo in your browser →](https://htmlpreview.github.io/?https://github.com/kingwangking/r2r/blob/hardening/post-v0.1.0-usability/docs/product/landing.html)**

[View the standalone HTML source](docs/product/landing.html) or download that one file and open it locally; it needs no external scripts or stylesheets. The instant preview uses a third-party public-GitHub HTML viewer and points to the **development PR branch** (not a permanent GitHub Pages address). After merging, switch this link to a stable hosted page.

The page animates a **hypothetical failure pattern** and a **proposed R2R workflow**, not fabricated measured performance data.

## Try it in your existing coding agent

**Released Skill:** [R2R v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) · MIT · [Installation guide](quickstart/install.md)

In a GitHub CLI version supporting `gh skill`:

```bash
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent codex --scope user
```

**No installer needed:** give your current coding agent this prompt:

```text
Use R2R (Run to Ready) on this project.
Start from our existing Specs, architecture, users and acceptance criteria;
do not create a competing requirements authority. Build a complete but
revisable path to a genuinely READY product. If actual parallel agents and
well-owned layers are available, use them on independent work and integrate.
RUN meaningful implementation batches. I will steer frequently.
After each batch, do a short synchronous self-review; fix significant
functionality, security and data-integrity issues by severity, use targeted
rechecks when needed, and batch ordinary P2/P3 repairs instead of repeatedly
stopping the next safe Slice. Do not re-review wording-only edits endlessly.
HARDEN whole user journeys, permissions, persistence, recovery and regressions
until the agreed product readiness criteria have actual evidence.
Maintain a short R2R.md checkpoint reconciled with live Git state.
Only claim tools/tests/actions really run; do not bypass release approvals.
Start the first safe authorized batch now.
```

The **current development branch** refines the three-capability definition and Finding policy; the published `v0.1.0` Skill is immutable and does not magically inherit unmerged changes.

**Three everyday actions:** `Start R2R` → `Continue R2R` → `Harden with R2R`, and **STEER at any time**. These are natural-language intents, not a proprietary scheduler or native slash commands.

## What R2R is — and isn't

- **Is:** a practical, developer-led operating approach and portable Skill for moving from the right Spec to a product that passes real acceptance.
- **Is:** compatible with existing Spec-driven workflows, coding agents, CI, Git and optional parallel subagents.
- **Isn't:** a replacement for those tools, a multi-agent runner, an unsupervised background daemon, a waiver for risky changes or a guarantee of product quality.
- **Actual evidence:** [v0.1.0 Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0), MIT license, source/package checks and [CLI installer smoke](https://github.com/kingwangking/r2r/actions/runs/39737882456). **Real host behavioral studies and measured productivity advantage are not yet demonstrated.**

[中文上手](quickstart/use.md) · [One-page method](docs/method/r2r.md) · [FAQ](docs/product/faq.md) · [Contributing](CONTRIBUTING.md) · [Project's own R2R.md](R2R.md)

**Plan big. Run long. Harden deep. Steer anytime.**
