# R2R v0.1.0 — release candidate notes (NOT PUBLISHED)

**Status:** this is a historical release-preflight checklist. The owner has now approved MIT and the `v0.1.0` release. Confirm [the actual Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) and associated CI evidence; do not treat the approval itself as proof.

## What the product includes

- **Portable Agent Skill** in `skills/r2r/`: Start, Continue, Harden and developer steering, no R2R background runtime.
- **One-project-state template:** `skills/r2r/assets/R2R.md`, with complete product plan + actual state and next run.
- **Self-contained instructions:** `skills/r2r/references/operating-guide.md`, portable with the Skill.
- **Documentation:** [user guide](../../quickstart/use.md), [installer guide](../../quickstart/install.md), [README](../../README.md).
- **Candidate packaging:** `scripts/skill_release.py --pack dist/r2r-skill.zip` creates a deterministic Skill-only ZIP and SHA-256 text. [GitHub Actions candidate workflow](../../.github/workflows/skill-candidate.yml) runs source tests and saves an artifact **without publishing**.

## What is explicitly not included

No R2R native CLI, IDE, multi-Agent backend, scheduler, hosted API, unattended cross-session agent, or proven throughput benchmark. GitHub CLI's `gh skill` installer/publisher are **external tools**, not R2R-developed software.

## Proposed distribution

1. After owner-approved rights, license, tag, and target branch decisions, merge/rebase the approved candidate.
2. Run `gh skill publish --dry-run` with a compatible GitHub CLI.
3. Create `v0.1.0` GitHub Release using `gh skill publish --tag v0.1.0` **only when authorized**.
4. Optionally attach the Skill-only ZIP and SHA-256 produced by the approved commit's package job.
5. Try an actual host installation and report PASS or NOT_RUN. The release itself should clearly disclose any untested hosts.

## Lightweight first-release acceptance

- [x] `skills/r2r/` includes Skill + internal template and reference (observed in Git source).
- [x] Installation and end-user Start/Continue/Harden docs exist (observed in Git).
- [x] Python source checks, five unit tests and candidate ZIP + SHA-256: [Actions run #39734487738](https://github.com/kingwangking/r2r/actions/runs/39734487738), SUCCESS on `7fecbed11aa037d594d755e457f225664653c192`.
- [x] Official GitHub CLI `gh skill publish --dry-run`: [Actions run #39734623413](https://github.com/kingwangking/r2r/actions/runs/39734623413), SUCCESS on `972cbd536b3fd5cd3659f11ab2882e43badcfeb6`.
- [x] Owner authorized MIT and v0.1.0 publication. Full independent legal/name clearance is not asserted.
- [x] PR #1 merged into main at `1f7bdd09e2f304d4dd03f6575114ebc73a5e413a`; Git tag `v0.1.0` points to the same SHA.
- [x] **GitHub CLI local installer** completed in isolated CI directory and preserved Skill/template/reference: [run #39735594895](https://github.com/kingwangking/r2r/actions/runs/39735594895) — SUCCESS on `7746c07a686dae74a2fd73ab52ca9f16837c2538`.
- [x] **Remote pinned-SHA Skill install** from GitHub repository completed in isolated CI directory and preserved all Skill assets: [run #39735750731](https://github.com/kingwangking/r2r/actions/runs/39735750731) — SUCCESS on `8a4946e74c1b2f48ed56cc0f9c18d8dad6d209c2`.
- [ ] **Actual agent-host activation/behavior** in Codex, Claude Code or other coding agent — NOT_RUN. Installing via CLI to a temporary CI directory does not establish prompt-trigger reliability.
- [x] [GitHub Release v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) published with `r2r-skill-v0.1.0.zip` and `r2r-skill-v0.1.0.zip.sha256`.

**Post-release finding:** publication succeeded, but [release CI run 39737475626](https://github.com/kingwangking/r2r/actions/runs/39737475626) marked the final installer step FAIL because it incorrectly expected the installed `SKILL.md` to match source bytes. GitHub CLI successfully installed the tagged Skill, while adding installation metadata. [Post-release smoke #39737882456](https://github.com/kingwangking/r2r/actions/runs/39737882456) **PASS** verifies immutable tag, asset checksum and `r2r@v0.1.0` installation. This is *not* proof of real Codex/Claude activation. Controlled efficiency experiments can follow an early, honestly labeled release; unsafe external changes or unsupported claims cannot.
