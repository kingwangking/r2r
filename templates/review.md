# R2R REVIEW — <question or change>

- **Review goal:** <which uncertainty matters?>
- **Exact target:** <SHA/diff or real user journey; no assumed later-head approval>
- **Timing / reviewer:** <synchronous after meaningful RUN batch; executing agent self-check by default; distinct reviewer only when actually used>
- **Review level:** <developer question / fast diff / focused test / deep audit>
- **Evidence:** <files, observed behavior, tests actually run>
- **Material findings:** <focus on code behavior, security/data integrity, architecture; include all critical findings>
- **Affected-path P0/P1 holds:** <specific unsafe dependency>
- **Ordinary P2/P3 repair queue:** <owner / module / batch due; do not interrupt next safe Slice>
- **Docs/evidence wording only:** <fix directly; no repeat independent Review unless acceptance, authorization, safety or traceability affected>
- **Focused recheck after repair:** <relevant test/contract check if needed, not full Review reset>
- **Decision:** <continue, repair, inspect deeper, restructure>
- **Honesty:** <PASS_FAST / REVIEW_NOT_RUN / tested scope only>

**Main Codex / executor:** triage material Findings, assign/perform scoped fixes, recheck affected behavior when warranted, record ordinary queue and **resume the next Slice**. No full Review loop simply because the fix was submitted. Do not launch an async review queue or force full deep review after every tiny task.

A self-review is not independent. A green fast review is not a public release sign-off.
