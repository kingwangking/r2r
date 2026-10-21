# Choosing run length and review depth — a steering guide

R2R uses a short **synchronous quick Review after meaningful work batches** in the current agent session; no asynchronous/multi-agent review runner is required. This review is not a deep universal gate. R2R supports **very long runs by default when justified**. There is no imposed schedule such as “always review after five changes.” Developer confidence is dynamic and should be informed by reality.

## Ask these four questions

1. **Direction:** Am I confident in the product and architecture direction?
2. **Coupling:** If this assumption is wrong, how much subsequent work would become worthless?
3. **Risk:** Could this operation cause irreversible loss, a security/rights violation or harm to others?
4. **Information value:** What is the cheapest question or test likely to change my next decision?

| Condition | Try next |
| --- | --- |
| High direction confidence; changes reversible and independent | Allow a long program/campaign; concise checkpoints and cheap review |
| Important subsystem contract is unverified | Run a focused probe before implementing dependent components |
| Full deep Review would delay a reversible batch | Perform quick synchronous scoped Review, record a deferred deep check, then continue the next safe batch |
| A product journey fails mid-development | Observe and record; fix now if it blocks dependencies, otherwise prioritize by current goal |
| Many changes require rework because of the same seam | Shorten RUN, review architecture, restructure before proceeding |
| Risk touches secrets, customer data, irreversible state or rights | Protect/stop the affected operation regardless of speed goals |
| Product breadth exists but cannot be used end-to-end | Start integration and structural HARDEN now |

## Cheap high-information developer questions

- Which exact end-to-end journey is actually working, not merely represented by green unit tests?
- What is the authoritative source for each piece of persistent state?
- Is the new component duplicating an existing mature implementation?
- Which next planned work depends on a currently unverified assumption?
- If the current implementation proves the architecture wrong, what is the smallest corrective change?
- What evidence would *disprove* the agent's success claim?
- Is review now more expensive than the rework it plausibly prevents?
- Which known verification debt must be paid before declaring READY?

**Principle:** a question is a review action, not proof. Demand a cited file, exact diff or observed test when the answer could alter important decisions.
