# R2R Agent Skill — portable product package

The distributable artifact is the **entire** [`skills/r2r/`](r2r/SKILL.md) folder:

```text
r2r/
  SKILL.md                       ← agent entry and three natural-language modes
  assets/R2R.md                  ← optional root project-state template
  references/operating-guide.md ← additional detail only when needed
```

Everything linked from the Skill stays **inside the same copied folder**, so it does not depend on the original source repository being checked out.

[Installation guide](../quickstart/install.md) uses **GitHub Releases/Tags + `gh skill install`** as the proposed official distribution, with `npx skills add` and manual folder copy as alternatives. [Release workflow](../docs/product/distribution.md). The current repository is still unreleased and Private.

## User-facing behavior

- **Start R2R** → inspect real project and specs, create/update root `R2R.md`, immediately start the first safe authorized campaign.
- **Continue R2R** → inspect Git and R2R.md, reconcile stale facts and continue.
- **Harden with R2R** → focus on real integrated product quality and explicit readiness.

Review defaults to synchronous lightweight **self-review**, not a fictional second agent. R2R does not include an execution scheduler or extra local runtime.

**Current distribution status:** candidate in a **private** repository. The file structure follows the published Agent Skills pattern, but Skill-host installation, validation and real end-user evaluation remain `NOT_RUN`; public distribution awaits license/rights and maintainer approval.
