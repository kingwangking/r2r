# R2R current state — first Release published

**Snapshot:** 2026-10-22. **Source of truth:** live GitHub repository, main branch, Release page and CI run records.

## Published product

- Repository `kingwangking/r2r` is **Public** and licensed under **MIT** in both root `LICENSE` and portable `skills/r2r/LICENSE`.
- [PR #1](https://github.com/kingwangking/r2r/pull/1) was approved and merged.
- [**GitHub Release v0.1.0**](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) is published, not a Draft/preview-only announcement; tag pins merge commit `1f7bdd09e2f304d4dd03f6575114ebc73a5e413a`.
- Release includes `r2r-skill-v0.1.0.zip` plus its `sha256` checksum as actual GitHub assets.
- End-user Skill behavior: **Start → Continue → Harden** with dynamic STEER; root `R2R.md` in the target project; synchronous lightweight self-review, not compulsory local multi-agent orchestration.

## Actual release pipeline and issue

- [Release workflow run #39737475626](https://github.com/kingwangking/r2r/actions/runs/39737475626) created the tag, Release and downloadable files successfully.
- **One final CI assertion FAIL:** `gh skill install ... --pin v0.1.0` itself reported successful installation, but test compared installed `SKILL.md` bytes to source. Installer adds provenance/install metadata, so byte equality was a mistaken requirement.
- Follow-up code corrects comparison to check installed Skill semantics/name and byte equality of unmodified assets/LICENSE. A separate post-release workflow verifies actual pinned-version installation and asset checksum; its result must be checked before claiming post-release smoke PASS.
- Candidate pipeline had earlier run successful source/unit/dry-run/local/remote SHA-pinned checks.

## Scope / remaining verification

- **Real GitHub publication complete:** source, tag, MIT and assets are present.
- **NOT_RUN:** an actual Codex/Claude host invocation that demonstrably follows R2R; empirical efficiency comparison or production project HARDEN results.
- Do not rewrite or move `v0.1.0` because of a CI test bug; use a post-release follow-up test and future patch release only if the published content has an actual defect.

## Next

1. Obtain post-release smoke CI outcome, and correct any legitimate installation mismatch.
2. Improve installation onboarding if a real host reveals friction.
3. Evaluate R2R in a practical project when useful; do not use exhaustive comparative trials as a prerequisite to the already published Skill.

This document is a snapshot, and does not imply hidden execution when no authorized agent session is running.
