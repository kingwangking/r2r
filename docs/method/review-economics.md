# Review economics — choosing the cheapest *sufficient* feedback

R2R's key question is **not “How can we avoid review?”** It is “Which verification now would change what we safely do next, and which verification provides better value at integration or release time?”

## Why the choice matters
When AI can produce many changes quickly, **review can be a serial dependency**. But deferring it carelessly can cause more rework and risk than it saves. Both costs must be considered. No precise savings ratio is claimed.

## Three kinds of feedback

| Feedback | Example | Useful when | Evidence limit |
| --- | --- | --- | --- |
| **Targeted developer question** | “Does this feature use the existing state authority?” | Testing an architectural assumption cheaply | An agent answer is a lead, not an independent audit |
| **Fast source/contract check** | Examine frozen diff and affected callers; focused test | Common regressions or local seam risk | Does not prove whole-product usability |
| **Integrated/deep review** | Real GUI/API path, data restart, negative authorization, cross-module audit | Shared state, unsafe effects, major architectural uncertainty, READY claim | Scope and actual source/build must still be pinned |

**No blanket rule:** a low-risk presentation change may go without separate deep review; a one-line authorization change may demand a focused independent audit.

## Async review without false safety

```text
Builder commits S → independent reviewer inspects S
                        ↓
Builder may proceed on a truly nondependent task
                        ↓
Review returns finding and affected path
                        ↓
Risky/dependent paths repaired and rechecked before further reliance
```

This pattern requires real agent/workspace isolation if implemented automatically. A prompt saying “read-only” is not a security boundary. **Web-only authoring** may use a later separate ChatGPT review or code inspection instead; it must not claim a reviewer was launched if none was.

## Severity isn't enough: include *dependencies*

- P0/P1 → identify **which** future work becomes unsafe or invalid; hold it and fix with evidence.
- P2/P3 → owner assigns deferred proof/fix and a due stage; safe independent progress may continue.
- Failure without known impact → ask the smallest question/experiment that distinguishes local inconvenience from systemic risk.

## Review cost signals

Track, when possible: review waiting time, repeated re-review cycles, false-positive fixes, defect severity discovered later, integration rework, human attention and time-to-accepted-product. Cheap checks are only a win if final quality and total rework remain credible.

See [decision guide](../../quickstart/decision-guide.md), [quality](quality.md), [evaluation protocol](../research/evaluation-protocol.md).
