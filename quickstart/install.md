# Install R2R — Release → skill installer → Start / Continue / Harden

R2R is a **versioned Agent Skill**, not a separate process or executable server. The standard distribution target is **GitHub Releases with a semver tag** and direct installation from the GitHub repository. The portable source lives at [`skills/r2r/`](../skills/r2r/SKILL.md).

**Versioning:** install from [a published Release](https://github.com/kingwangking/r2r/releases) for stable, reproducible behavior. `v0.1.0` is the authorized first-version target; check that the tag exists before using it. The project uses the [MIT license](../LICENSE).

## Recommended: one-command install (after release)

GitHub CLI's [native Skill installer](https://cli.github.com/manual/gh_skill_install) discovers `skills/r2r/SKILL.md`; when no version is specified it prefers the latest tagged release and otherwise uses the default branch HEAD.

```bash
# Install R2R for Codex, available to the current user
gh skill install kingwangking/r2r r2r --agent codex --scope user

# Install R2R into the current project's Claude Code scope
gh skill install kingwangking/r2r r2r --agent claude-code --scope project

# Pin to one published release/tag for reproducibility
gh skill install kingwangking/r2r r2r@v0.1.0 --agent codex --scope user

# Preview without installing
gh skill preview kingwangking/r2r r2r
```

The example `v0.1.0` is **a proposed future version, not an existing R2R tag**. Use an actually published version when available. The `gh skill` commands are currently a [GitHub CLI preview](https://cli.github.com/manual/gh_skill), so users need a CLI build that supports them.

**Alternative:** the open [skills installer](https://github.com/vercel-labs/skills) can install directly from GitHub:

```bash
npx skills add kingwangking/r2r --skill r2r
```

This installer may use the repo source rather than a specific GitHub Release; check its behavior if you need a pinned version. Install/upgrade mechanisms are separate from the underlying `SKILL.md` standard.

**Updates:** for GitHub CLI installs, see `gh skill update`; pinned installs will not update automatically unless explicitly unpinned. The release is a stable ref while ongoing `main` development can continue.

## Download a GitHub Release (manual fallback)

After release, open [R2R Releases](https://github.com/kingwangking/r2r/releases), select a version and download either:
- A dedicated `r2r-skill-vX.Y.Z.zip` asset containing only `r2r/SKILL.md`, `r2r/assets/`, `r2r/references/` **if the maintainers attached such an asset**.
- Or GitHub's automatic source archive; locate `skills/r2r/` inside it.

Copy the whole `r2r` folder into the host's skills directory, preserving paths. The package's reference files live alongside `SKILL.md`, so copying only that file loses useful content.

| Agent | Project-local installation | User-global location |
| --- | --- | --- |
| Codex | `<project>/.agents/skills/r2r/` | Managed by host installer; may use `~/.codex/skills` or `~/.agents/skills` depending on CLI/host version |
| Claude Code | `<project>/.claude/skills/r2r/` | `~/.claude/skills/r2r/` |
| Other Skill hosts | See the host's Agent Skills documentation | See host support |

## No installation: use as a prompt

Copy the **Start R2R** prompt from [README](../README.md) into an authorized chat. It can build/update a project-root `R2R.md` and implement only when that assistant has actual repository tools. It cannot start an invisible background coding process.

## Actual operation after installation

1. **Start R2R on this project** — read the real code/spec, establish a complete long-horizon program in root `R2R.md`, and start a safe meaningful RUN.
2. **Continue R2R** — compare `R2R.md` with live Git, continue safe work with synchronous lightweight self-review.
3. **Harden with R2R** — repeatedly integrate, restructure and verify whole-product readiness.
4. **STEER anytime** — change scope, run length and review depth.

These are natural-language triggers, not native CLI commands implemented by the Skill. [中文使用说明](use.md).

## Publisher's release workflow

See [distribution plan](../docs/product/distribution.md). GitHub CLI provides `gh skill publish --dry-run` to validate and `gh skill publish --tag vX.Y.Z` to create a release **after authorization**. The official `gh skill publish --dry-run` and candidate ZIP/sha256 packaging **passed in GitHub Actions** at [run #39734623413](https://github.com/kingwangking/r2r/actions/runs/39734623413), along with Python source/unit checks. Further successful CI checks:
- [Run #39735594895](https://github.com/kingwangking/r2r/actions/runs/39735594895) installed `r2r` from its **local repository** using `gh skill install --from-local` into a runner temp directory and confirmed asset integrity.
- [Run #39735750731](https://github.com/kingwangking/r2r/actions/runs/39735750731) installed `r2r` from **GitHub at the exact PR head SHA** using `gh skill install --pin`, and confirmed the copied template/reference content.

Neither run published a Release or started a real Codex/Claude Code agent. **Host activation remains NOT_RUN**; license choice, release authorization and version tag remain pending.
