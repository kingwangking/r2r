# Dynamic developer steering

**Run length is decided by what the developer knows, fears, needs and can verify.** Long runs are central to AI-era throughput, but neither a 100-slice run nor a review every five slices is mandatory.

| Situation | Appropriate options |
| --- | --- |
| Clear architecture and reversible implementation | Very long continuous campaign |
| Significant shared dependency uncertainty | Medium run and targeted integration probe |
| Unknown data authority or viability assumption | Short run, architecture question, source inspection or spike |
| Reviewer needs deep investigation but next work is independent | Defer review, continue unaffected work |
| Rights, secrets, auth or destructive real-data effects | Explicit hard protection; deeper verification or approval before the affected operation |
| Structural design appears wrong | Redirect now, reshape plan, resume after correction |

Questions can be a cheaper form of review:
- “Which complete user journey works *in reality*? Show the source or observed evidence.”
- “Did we duplicate a data authority that already exists?”
- “Which architecture assumption did implementation invalidate?”
- “What would break if we continued this dependency?”
- “What is the lowest-cost test that could prove this claim wrong?”

**Question ≠ proof.** For material uncertainty, ask for exact files, logic, running evidence or a focused experiment.

A **checkpoint** records reality and next action. A **gate** blocks a particular risky action. A **review** reduces uncertainty. Do not make every checkpoint a gate or every review a multi-hour ritual.

The owner may intervene at any time. Without intervention, the agent proceeds within the **actual** authorized session, tooling and resource limits. Stop if required permission, key risky invariant or environment is unavailable. Never promise hidden perpetual execution.
