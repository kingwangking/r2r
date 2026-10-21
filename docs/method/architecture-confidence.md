# Architecture confidence: why a developer can authorize a longer run

A long agent run shifts judgment upstream. The developer is no longer expected to read every line of AI-generated code, but must understand the product and where an incorrect architectural assumption could amplify rework.

**Confidence is flexible and qualitative, not a mandatory readiness-score worksheet.**

## Before a large run, know enough of these

- **Product:** What is the real user journey and final deliverable?
- **Responsibility:** Which module owns each decision and persistent state?
- **Reuse:** Which mature components should be adopted rather than rebuilt?
- **Interfaces:** Which seams must remain stable so Agent A cannot silently break Agent B?
- **Reversibility:** Can we replace provisional implementations without destroying durable data?
- **Evidence:** Which cheap actual observation would disprove our biggest architectural assumption?
- **Human control:** Which action needs approval, and when will the developer inspect progress?

Do not demand a complete answer to every detail before any implementation. Concentrate research on uncertainties with the **highest downstream consequences**.

## Minimal confidence note (optional)

```text
We believe: One document store should own durable text state.
Because: Every editor and history action must preserve a consistent revision.
Unverified: Whether the old search index accepts revision-aware updates.
Next cheap probe: Change a document and inspect the index revision.
If false: Stop dependent index work; change the boundary before next long run.
```

An agent's fluent answer is not evidence. When a response matters for architectural steering, request exact source references, a contract test or a real integrated demonstration.

## Developer control is active, not ceremonial

After any agent batch, a developer may ask **one** high-information question instead of ordering a blanket whole-diff review:
- “Are we still using the original business authority?”
- “Can a user complete the path without debug fixtures?”
- “Do our current modules match the planned direction, and where don't they?”
- “How expensive is a mistake at this dependency?”

On good evidence, extend the next execution horizon. On new uncertainty, narrow it. This keeps ultra-long execution possible without treating unattended optimism as governance.

See [developer steering](steering.md), [decision guide](../../quickstart/decision-guide.md) and [convergence](convergence.md).
