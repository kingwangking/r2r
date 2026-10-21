# The 10-minute R2R trial — one real repository, no installer

This is a **manual exercise**, not a claim that a ten-minute session can finish a complex product or prove efficiency. Bring a repo you may inspect. You do not need to change its code.

## Step A — 2 minutes: plan the whole product
Give a coding assistant the current README/spec and say:

```text
Use R2R. What are the 3–5 real end-to-end user journeys this product promises?
Which component owns each important persistent state? Which existing mature
components should be reused? Give me an ordered complete roadmap and the
eventual READY tests. Mark actual repo facts vs guesses.
```

**Expected artifact:** a concise product map and a roadmap. These are candidate interpretations until checked against real source; do not silently turn guesses into authoritative specifications.

## Step B — 2 minutes: choose a run horizon
Pick one reversible, bounded improvement and say:

```text
RUN within this exact branch and allowed scope. Continue implementation while
the session is active, with cheap relevant checks, until the selected campaign
is done or a specific high-risk dependency blocks it. Preserve a precise
checkpoint with outcomes, tests actually run and the next action.
```

For a **read-only trial**, ask for the same plan without writing. If no coding tool is available, practice on documents or a fictional bounded example instead; do not pretend code executed.

## Step C — 2 minutes: steer via a question
Ask one question that would change the decision:

```text
Which architectural assumption would invalidate the most upcoming work?
Show the source path or cheapest observable test that supports your answer.
```

Decide to **extend RUN**, **narrow RUN**, **probe a dependency**, or **restructure**. There is no requirement to ask the agent to re-review everything.

## Step D — 2 minutes: classify verification
Inspect one real or proposed review/test and ask:
- Does it guard a sensitive dependency **now**?
- Can it be deferred safely until integrated/product-level validation?
- What exact evidence would prove the claim?
- Which claims are still NOT_RUN?

Don't call a speculative answer a test pass.

## Step E — 2 minutes: define READY
Pick one real user journey and list the minimum product observation, negative case and recovery behavior necessary before release.

## How to know the trial was understood
A newcomer should be able to explain:
- Why long runs are enabled but their length can change.
- Why a non-green intermediate build may be acceptable while real-data/security boundaries remain protected.
- Why a quick review isn't a release sign-off.
- Why final product quality includes end-to-end evidence and possible early structural redesign.

**Not measured:** time savings, defect rates and third-party usability. A later independent exercise should record these results rather than assume success.

Related: [one-card worksheet](../templates/one-card.md), [run/review decision guide](decision-guide.md), [worked run](../examples/long-campaign.md).
