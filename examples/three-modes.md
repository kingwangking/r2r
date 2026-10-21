# Three R2R operating modes — the same principle, different decisions

**These are illustrative scenarios, not proven product benchmark outcomes.**

| Case | RUN horizon | Why | Feedback now | HARDEN |
| --- | --- | --- | --- | --- |
| A. Tiny documentation UX | Short batch | Outcome small, low-risk and reversible | Link checks and a question about reader comprehension | Read quickstart from a newcomer perspective |
| B. Multi-module application | Long campaign, possibly tens of changes | Overall architecture and permissions understood, reversible internal work | Cheap smoke, selective seam review, occasional real path probe | Integrate API/UI/state, restructure, real user flow, negative tests |
| C. Permission/data migration | Very short until boundary proven | A single assumption could corrupt real state and invalidate much downstream work | Exact authority check, migration fixture, independent high-risk review | Repeat data integrity and recovery verification before live deployment |

## A: Small useful change
A developer asks ChatGPT web to clarify a user-facing quickstart. A self-review checks links and claims; there is no need to open an architecture committee. The final text still needs actual reader feedback before claiming ease-of-use.

## B: Large complex application
A developer has a believable domain map and wants 40 feature slices. They authorize a long RUN and periodic feedback. When the agent says “a role selector is equivalent to real auth,” the developer asks for the authority/source map and shortens RUN to correct that seam. Other isolated UI work continues. Later HARDEN runs real login, persistence and failure paths. The agent isn't required to maintain final GUI polish every slice.

## C: High-risk dependency
A purportedly tiny schema update might permanently alter customer data. This is NOT a good candidate for “long run now, verify eventually.” The developer halts that affected operation, uses a migration copy/backup and real rollback evidence, then resumes broader work after resolving the risk.

## What all three have in common

- Overall product goal and READY criteria.
- Developer direction and immediate ability to steer.
- No confusion between a planned check, a check that ran, and release readiness.
- Protected high-consequence boundaries, even when intermediate quality is flexible.

Related: [10-minute trial](../quickstart/10-minute-trial.md), [worked long campaign](long-campaign.md).
