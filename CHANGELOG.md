# Changelog

R2R publishes versioned Agent Skills using GitHub Releases. Consult [the actual Releases page](https://github.com/kingwangking/r2r/releases) to determine which versions have been published.

## Unreleased — post-v0.1.0 HARDEN (in Draft PR #2)

- Clarify R2R as rapid iteration **complementing Spec and parallel agents**; refresh searchable README, product positioning and recommended GitHub Topics.
- Add Finding triage: severity-based functional/security/data repair, grouped P2/P3, and no reflexive repeat independent Review of wording-only fixes; primary executor resumes the next Slice.
- Correct published-version installation/Chinese onboarding and contributor/Skill status after the first Release.
- Add root `R2R.md` so R2R itself follows its Start / Continue / Harden practice without duplicating existing plans.
- Add documentation-state and internal Markdown-link regression checks with isolated positive/negative unit tests.
- Require MIT LICENSE in the distributable Skill source/package; guard missing-license regressions in tests.
- Existing `v0.1.0` Tag and published ZIP remain unchanged. Do not advertise this unreleased work as installed v0.1.0 functionality.

## v0.1.0 — initial Skill release

### Added
- Portable `r2r` Agent Skill with self-contained template and operating guide.
- Start / Continue / Harden user commands and developer STEER guidance.
- Long-program `R2R.md` target-project template.
- Documentation for GitHub CLI `gh skill` release/install and prompt-only use.
- Stdlib-only source validation, deterministic Skill-only ZIP and SHA-256 generation.
- Read-only GitHub Actions candidate build (no automatic Release creation), with official GitHub CLI publish dry-run.
- Isolated GitHub CLI local and pinned-remote Skill installation smoke tests, verifying state template and guide files.

### Method
- Long-horizon PLAN and RUN; synchronous risk-scoped lightweight self-Review after meaningful batches; repeated structural HARDEN and evidence-based READY.
- No mandatory local multi-Agent implementation.

### Unverified
- Real host installation, empirically proven speedup and release-grade product-quality field results are **NOT_RUN**. License: MIT. The packaged and CLI installer checks are automated; real coding-agent end-to-end behavior and measured throughput remain outside the scope of these release tests.

See [candidate notes](docs/product/release-candidate-v0.1.0.md).
