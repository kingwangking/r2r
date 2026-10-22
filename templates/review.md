# R2R REVIEW — <question or change>

- **Review goal:** <which uncertainty matters?>
- **Exact target:** <SHA/diff or real user journey; no assumed later-head approval>
- **Timing / reviewer:** <synchronous after meaningful RUN batch; executing agent self-check by default; distinct reviewer only when actually used>
- **Review level:** <developer question / fast diff / focused test / deep audit>
- **Evidence:** <files, observed behavior, tests actually run>
- **Actionable findings:** <up to 3 for a fast review; depth may grow for high risk>
- **Affected-path P0/P1 holds:** <specific unsafe dependency>
- **P2/P3 or missing tests:** <owner and due-by>
- **Decision:** <continue, repair, inspect deeper, restructure>
- **Honesty:** <PASS_FAST / REVIEW_NOT_RUN / tested scope only>

**Default next step:** complete this short synchronous check, repair critical affected-path findings, record ordinary findings and continue RUN within authorization. Do not launch an async review queue or force full deep review after every tiny task.

A self-review is not independent. A green fast review is not a public release sign-off.
