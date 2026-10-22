# R2R — current state (pre-release)

**Snapshot:** 2026-10-22. **Authority:** actual GitHub branch, PR, Actions and Releases; this file is a checkpoint, not a replacement for live inspection.

## Confirmed source and status

- `kingwangking/r2r` is **Public**. The most recently observed `main` is the bootstrap `b5265fc52a71b94aed5cb9771d925054168eafd6`.
- [PR #1](https://github.com/kingwangking/r2r/pull/1) on `feat/r2r-method-foundation-v0`: **Draft/Open/Unmerged** at the last check.
- Current source reviewed for candidate checks:
  - `7fecbed11aa037d594d755e457f225664653c192` — added standard-library release checker, positive/negative tests, deterministic ZIP + SHA-256 and read-only candidate GitHub Actions.
  - `972cbd536b3fd5cd3659f11ab2882e43badcfeb6` — added official `gh skill publish --dry-run` in the same workflow.
- [Run #39734487738](https://github.com/kingwangking/r2r/actions/runs/39734487738): **SUCCESS**, source/unit checks, ZIP/checksum generation and uploaded `r2r-skill-candidate` artifact.
- [Run #39734623413](https://github.com/kingwangking/r2r/actions/runs/39734623413): **SUCCESS**, including official `gh skill publish --dry-run`, unit/source checks and candidate ZIP/checksum artifact.
- No GitHub Release existed at last inspection. **No open-source LICENSE was found in the repository tree**, despite Public visibility.

## Actually usable candidate product

- Source package `skills/r2r/SKILL.md`, `assets/R2R.md`, `references/operating-guide.md`.
- User flow: **Start R2R → Continue R2R → Harden with R2R**, with developer steering and synchronous lightweight self-review.
- Portable method requiring no R2R-specific server, background task or extra agent platform.
- [Release source validator and deterministic package](../../scripts/skill_release.py) and [candidate workflow](../../.github/workflows/skill-candidate.yml) exist and have executed successfully for specific SHAs.
- Detailed installation, release, and limitation docs exist; they are being aligned with current Public/unreleased state in this doc-only update.

## Still unresolved

- Owner selection/approval of LICENSE, trademark/rights implications and final version/tag.
- Owner instruction to merge PR #1 and create a tagged GitHub Release. None performed.
- Actual Skill installation and activation in an external coding agent: **NOT_RUN**.
- External usability and throughput claims: **NOT_RUN**, intentionally not gating candidate authoring.

## Next best actions

1. Keep the candidate source, packaging script, Actions workflow and documentation consistent; monitor a new workflow result if source/tooling changes.
2. Obtain owner choices for legal/license/release authorization **before** changing distribution state.
3. After authorization, merge approved source, rerun official publish dry-run on final ref and publish a named Release; attach a Skill-only ZIP/checksum if appropriate.
4. Follow with a real host installation smoke test and later W5 effectiveness studies.

Do not confuse Public repo visibility, Actions test artifacts, PR Draft, or a successful publish dry-run with an actual versioned Release.
