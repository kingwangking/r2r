# R2R Agent Skill — portable package

[**R2R v0.1.0**](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) is published under the [MIT license](../LICENSE). The **entire** `skills/r2r/` directory is the installable package:

```text
r2r/
  SKILL.md                       — agent entry, Start / Continue / Harden
  LICENSE                        — MIT license inside the package
  assets/R2R.md                  — target project's optional root-state template
  references/operating-guide.md — optional operational detail
```

All Skill-internal references stay inside this folder; copying it does **not** require the R2R source repository or any local R2R daemon.

**Install:** [GitHub CLI or manual ZIP instructions](../quickstart/install.md). The default workflow is to install by pinned Release tag, open the target project's existing coding agent and say “Start R2R”, later “Continue R2R”, then “Harden with R2R”.

**Actual evidence:** [Release post-install smoke](https://github.com/kingwangking/r2r/actions/runs/39737882456) passed CLI installation, package file checks and ZIP checksum. This does not prove the actual Codex/Claude Agent follows every instruction; its full host behavior remains **NOT_RUN**.

The source can evolve on `main` without changing published `v0.1.0`. New substantive changes require a new version, not an overwritten tag.
