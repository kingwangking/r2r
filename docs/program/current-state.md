# R2R release candidate — current truth

**Snapshot:** 2026-10-22. GitHub is authoritative; this document records known source commits and must not be treated as the future final HEAD.

## Repository and owner controls

- Repo: `kingwangking/r2r`, **Public**. No open-source LICENSE in the tracked branch; public source visibility is not a grant of reuse rights.
- Base: `main` bootstrap. [PR #1](https://github.com/kingwangking/r2r/pull/1) on `feat/r2r-method-foundation-v0` remains **Draft / Open / Unmerged** at the last inspection.
- Current development direction: **full usable, versioned R2R Skill product**, not more abstract process research or a new local multi-agent platform.
- Review mode: synchronous lightweight same-agent self-review after meaningful implementation batches; high-risk paths get deeper checks when appropriate.

## Actual product deliverables

- Self-contained `skills/r2r/`: `SKILL.md`, `assets/R2R.md`, `references/operating-guide.md`.
- START / CONTINUE / HARDEN with STEER ANYTIME; long-range plan, single target-project state file, risk-directed reviews, repeated final product convergence.
- GitHub Release-first distribution plan, install/usage documentation, proposed `v0.1.0` notes; **no GitHub Release or version tag created**.
- Stdlib-only Skill source checker and deterministic ZIP/SHA-256 packager; isolated positive/negative tests.
- Read-only CI candidate job with official `gh skill publish --dry-run`, local and pinned remote GitHub CLI installer smoke checks, Artifact upload.

## Executed evidence

| Source / run | Actual scope | Observation |
| --- | --- | --- |
| [39734487738](https://github.com/kingwangking/r2r/actions/runs/39734487738) @ `7fecbed1` | Unit/source checks, deterministic ZIP+checksum upload | PASS |
| [39734623413](https://github.com/kingwangking/r2r/actions/runs/39734623413) @ `972cbd53` | Official GitHub CLI `gh skill publish --dry-run` | PASS |
| [39735594895](https://github.com/kingwangking/r2r/actions/runs/39735594895) @ `7746c07a` | `gh skill install --from-local` to temp directory, asset contents match source | PASS |
| [39735750731](https://github.com/kingwangking/r2r/actions/runs/39735750731) @ `8a4946e7` | `gh skill install` from GitHub pinned PR source SHA, copied Skill assets match | PASS |

These are real CI processes in isolated runners. They **do not** mean any Codex/Claude Code assistant followed the Skill, that its full user experience works, or that R2R improves complex-project throughput.

## Remaining decisions / incomplete evidence

- **OWNER decision:** choose and approve open-source license, verify publication rights/name.
- **OWNER decision:** approve merge/source ref and initial Release tag/version (e.g. proposed `v0.1.0`). No merge, tag or Release has been performed.
- **NOT_RUN:** real host command activation, correct usage behavior and end-product studies; explicitly deferred beyond basic package candidacy.
- **NOT DONE:** publish or attach a permanent GitHub Release artifact; CI artifacts have finite retention.

## Next after owner release authorization

1. Approve rights/license, review the proposed version and source/PR merge.
2. Re-run `gh skill publish --dry-run` on the approved final source if materially changed.
3. Publish a tagged GitHub Release using the supported `gh skill publish --tag` path, optionally attach a standalone Skill ZIP + checksum.
4. Confirm real post-release installation/host behavior and correct any practical problems.

**Never silently promote PR/CI PASS to host behavior PASS or release READY.**
