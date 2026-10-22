# R2R current state — productized usage candidate

**Updated:** 2026-10-22. **Truth source:** live GitHub branch and PR, not this checkpoint. This note references the **last observed content commit before the checkpoint commit**; re-read actual HEAD on resume.

## Project / permission facts

- Repository: `kingwangking/r2r`, last observed **Private**. Default `main` based on bootstrap `b5265fc52a71b94aed5cb9771d925054168eafd6`.
- Work branch: `feat/r2r-method-foundation-v0`, [PR #1](https://github.com/kingwangking/r2r/pull/1) open/draft/unmerged.
- Source preceding this state update: `425b6a5d824964fb841f9f1b299df0118aff863b`.
- Current authorized authorship: ChatGPT web + GitHub; synchronous lightweight **same-agent self-review** after meaningful batches. No mandatory local multi-Agent architecture.
- Owner instruction changed priority: **deliver a complete usable R2R package and explain real final user experience before investing in expensive comparative validation**.

## Delivered — end-user experience

A user can use **Start → Continue → Harden**, steering anytime:
- [Product README](../../README.md): the three user actions and copy/paste prompt, no installation.
- [Full Chinese use guide](../../quickstart/use.md): step-by-step end-user onboarding.
- [Codex / Claude Code / generic install guide](../../quickstart/install.md): copy the full skill folder, not only SKILL.md.
- [Portable complete Skill](../../skills/r2r/SKILL.md) with its **internal** [state template](../../skills/r2r/assets/R2R.md) and [reference](../../skills/r2r/references/operating-guide.md), no reference outside copied folder.
- [Fictional complete user journey](../../examples/complete-usage.md), explicitly not an executed product test.
- R2R project itself retains W0–W4 methodology, architecture, research and development record. These are optional reading for the end user, not a prerequisite to using the Skill.

**Important distinction:** The R2R user's own repository keeps **one root `R2R.md`** with whole-product plan, state and next run. It is not this method project's `docs/program/current-state.md`. Existing specs are referenced, not duplicated.

## Actual light synchronous Review

At `425b6a5d`:
- GitHub PR diff and branch tree reported **53 tracked/changed files**.
- **182/182 relative Markdown links** in added PR content resolved to GitHub tracked paths; no unpaired added-line code fences observed.
- Portable `skills/r2r/SKILL.md` has `name: r2r` and a descriptive frontmatter; the package includes the required assets and references.
- Prior narrower check of eight new/replaced user-facing files: **34/34** relative refs existed and Skill-internal relative refs did not reach outside `skills/r2r/`.

These are **author-side documentation consistency checks only**. They are not host execution, real software testing, independent review or evidence of higher throughput.

## Unfinished / intentionally deferred

- Actual Codex/Claude Code Skill installation and host execution: **NOT_RUN**.
- External beginner onboarding, rigorous empirical throughput comparison, real software GUI/end-to-end/restart/security verification: **NOT_RUN**.
- Rights/licensing/name audit for open source, publication, public visibility and official release: **NOT_AUTHORIZED / NOT_DONE**.
- No dedicated R2R CLI, daemon, background scheduler, hosted platform or installer exists, and none is required for this portable initial product.

## Next practical priorities (not a new research bureaucracy)

1. Refine end-user usability and correct any real instruction/host-path issues surfaced when the owner tries the Skill in an existing coding agent.
2. Ensure `skills/r2r/` stays portable and `R2R.md` stays minimal as the method evolves.
3. When explicitly chosen, run field studies and W5/W8 deeper verification; **do not let complex tests displace shipping a usable package now**.
4. For public open-source release, request owner's explicit decisions on license, rights, visibility and scope; do not auto-merge or publish.

**Resume:** read current branch/PR HEAD first, then this file and AGENTS.md. Start the next valuable authorized work; no work is presumed to have occurred while the web conversation was inactive.
