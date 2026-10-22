# R2R distribution — GitHub Release as the versioned product

**Decision:** Use GitHub-native Skill publishing/installing instead of developing a custom installer or requiring users to browse a GitHub directory. Source repository is the development/workspace; a **tagged GitHub Release** is the supported versioned distribution artifact.

**First release:** the owner approved MIT licensing, merging and `v0.1.0` publication. [GitHub Release v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) is live, with tag pinned to `1f7bdd09e2f304d4dd03f6575114ebc73a5e413a` and Skill-only ZIP/SHA-256 assets. The publish job succeeded through release/asset creation; its last exact-byte installer assertion failed because the installer adds metadata. [Post-release smoke run #39737882456](https://github.com/kingwangking/r2r/actions/runs/39737882456) **PASS** accounts for installer metadata. The immutable tag has not moved.

## Three distinct concepts

| Layer | Where | What users get |
| --- | --- | --- |
| **Source and development** | `skills/r2r/SKILL.md` + sibling assets/references inside Git | Reviewable/editable Skill, not a public release |
| **Release / version** | Existing Git tag + GitHub Release `v0.1.0` | Frozen version, release notes, GitHub-generated source archives and Skill-only ZIP |
| **Installation / discovery** | `gh skill install`, `npx skills add`, eventually plugins/marketplaces | Convenience, source tracking, update paths, potentially broader discovery |

**Important:** An Agent Skill is *intrinsically a directory*; a Release is its **versioned publication**, not a replacement for `SKILL.md`. Many Skill catalogs directly serve GitHub directory references without Releases. For R2R, publish a tagged version so users needn't track an unstable development HEAD.

## Distribution contract

- Repo layout: `skills/r2r/SKILL.md`, `skills/r2r/assets/R2R.md`, `skills/r2r/references/operating-guide.md`.
- Published brand/version: R2R / Run to Ready **v0.1.0**, approved by the owner and tagged; future versions require their own explicit decision.
- User install after public release:
  ```bash
  gh skill install kingwangking/r2r r2r --agent codex --scope user
  gh skill install kingwangking/r2r r2r@v0.1.0 --agent codex --scope user
  npx skills add kingwangking/r2r --skill r2r
  ```
- Manual fallback: download Skill-only release asset *if provided*, or release source archive then copy entire `skills/r2r` folder.
- Running the installed Skill uses the coding agent's **existing tools and permissions**, not a new R2R runtime.
- Target-project root `R2R.md` is created **during usage**, not a file the installer must force into every repository.

## What happened for v0.1.0; repeatable steps for later versions

1. The owner approved **MIT** and the first **v0.1.0** release. License copies live at the repository root and inside the portable Skill. The repository is already Public; do not change its visibility. Do not publish private project details without permission.
2. Commit final `skills/r2r` assets and human-facing install/usage docs on an authorized release ref. Resolve PR merge by owner instruction.
3. The project's read-only [candidate workflow](../../.github/workflows/skill-candidate.yml) has already run both package tests and the official `gh skill publish --dry-run` at [run #39734623413](https://github.com/kingwangking/r2r/actions/runs/39734623413): SUCCESS. Repeat on the **final approved release commit** if its sources changed. A successful dry-run is not a Release.
4. After authorization, use `gh skill publish --tag vX.Y.Z` to validate and create a tagged GitHub Release. The public release version must point to the intended source, not a Draft PR-only branch.
5. GitHub includes source zip/tar archives for a Release. Optionally attach a dedicated `r2r-skill-vX.Y.Z.zip` containing only the standalone folder for manual users, with checksum if useful. **This extra ZIP does not replace the Git source used by installers.**
6. CI has already confirmed **local** `gh skill install --from-local` ([run 39735594895](https://github.com/kingwangking/r2r/actions/runs/39735594895)) and **pinned remote GitHub source** `gh skill install --pin <SHA>` ([run 39735750731](https://github.com/kingwangking/r2r/actions/runs/39735750731)) without creating a Release. The v0.1.0 post-release [GitHub CLI installation smoke](https://github.com/kingwangking/r2r/actions/runs/39737882456) passed. **Actual prompt activation in a Codex/Claude Code host**, user/project scope behavior and future updates still require observation; label those NOT_RUN rather than claiming comprehensive validation.
7. Subsequent versions use SemVer tags, clear release notes and updated installation instructions. Avoid republishing a mutable tag.

## Optional later discovery, not the MVP

- GitHub CLI already has skill search/preview/install/update; `agent-skills` repo topic improves discovery when appropriate.
- Vercel's `skills` CLI/skills.sh can consume GitHub-hosted skills directly; **no separate custom R2R registry needed**.
- OpenAI's **skills-only Plugin** directory and Claude Code Plugin Marketplace are separate, higher-level distribution options. They need their own manifest/submission/review rules; do not confuse those with a GitHub Release. Consider them *after* core release and onboarding work, not as a reason to build a local multi-agent system.

## Release readiness vs scientific validation

A complete instruction package may be released as an **early candidate** with truthful limitations before costly controlled studies establish an efficiency claim. Do not advertise unproven measured speedups or assert install tests ran when they did not. Core safety boundaries and rights/publication permissions remain required.

## Official documentation

- [GitHub CLI — gh skill publish](https://cli.github.com/manual/gh_skill_publish)
- [GitHub CLI — gh skill install](https://cli.github.com/manual/gh_skill_install)
- [GitHub CLI — gh skill update](https://cli.github.com/manual/gh_skill_update)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [Vercel skills CLI](https://github.com/vercel-labs/skills)
- [OpenAI Plugin packaging](https://developers.openai.com/plugins/build/plugins)
