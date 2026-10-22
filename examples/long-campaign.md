# Worked example — a long-horizon AI application campaign

**FICTIONAL training scenario. No code was executed. No review/test results below are genuine.**

Product: local-first writing workbench. Four domains: project/library, manuscript editor, AI assistance (optional), persistence/history. Final promise: an author can create a project, write, revise, undo/redo, restart the app and recover work, with no unauthorized external AI request.

## PLAN — complete route, credible architecture

- **Ownership:** Manuscript storage is authoritative for text/revision; editor exposes transactions, not an independent durable DB; AI generates proposals and cannot silently commit text; UI is a view/command surface.
- **Constraints:** No real author data destroyed; AI egress off by default; sandbox test fixtures; versions and change records traceable.
- **READY:** normal packaged UI author journey, cross-process restart, undo/redo ordering, read/write authority checks, denied unsafe actions and consistent persistence.

## RUN — four campaigns, twelve proposed slices

| Campaign | Ordered slices (illustrative IDs) | Delivery shape | Feedback strategy |
| --- | --- | --- | --- |
| C1: usable author shell | L01 project create/open; L02 chapter editor; L03 save UI | App can present and edit a chapter | Targeted persistence contract; UI may be rough |
| C2: persistent editing | L04 durable save; L05 revision identity; L06 undo/redo | Text edits survive ordinary workflow | T1 cross-module probe; review dangerous data ownership |
| C3: AI as proposal | L07 selection context; L08 local offline candidate; L09 author-approved apply | User can explicitly choose AI edits | Synchronous focused contract review of revision/authority seam; distinct sequential reviewer only if available and needed |
| C4: author usability | L10 search; L11 history timeline; L12 recovery/reporting | Whole author workflow is connected | T2 actual GUI and process-restart trial |

**Current execution convention:** after each meaningful campaign/batch, the implementing agent performs a **short synchronous self-review**, records high-risk holds and moves to the next authorized batch. A deeper review may be requested for L05/L09; a second agent or parallel reviewer is **not required**. No fixed reviews per slice and no simulated async Review.

The overall route is much longer than any one agent context. The developer can authorize all four campaigns, or shorten after L02/L05/L08. No rigid “review every 3 slices” rule.

## Example of dynamic steering after L05

Developer asks: “Do the editor and history share one authoritative revision, or are they independently writing?” Suppose source inspection **reveals** two conflicting owners. That would force a change: hold dependent L06/L09, correct the persistence boundary, and allow unrelated L10 UI planning if safe. The listed finding is **hypothetical**, not an observation.

## Simulated review ledger (not actual review evidence)

| Candidate change | Proposed review | If failing | Independent next work |
| --- | --- | --- | --- |
| L02 UI edit shell | Quick UI check | Record known rough UX, proceed | L03 if not coupled to failing persistence |
| L05 revision identity | Deep contract check | Stop L06 and L09 until corrected | L10 search spec if isolated |
| L08 offline suggestion | Cheap offline negative test | Block external egress if detected | L11 read-only history view |
| L12 recovery | Real cross-process proof | Product is NOT READY | Correct recovery structure in HARDEN |

## HARDEN — not just bug fixes

Round 1: connect all state/read/write paths and restructure duplicate document authorities.  
Round 2: run actual packed GUI journeys and author-input scenarios; revise confusing interaction design.  
Round 3: negative authorization, AI-off, crash/restart, undo/redo and consistency verification.  
Round 4: full regression/performance and owner usability acceptance; repeat where structural changes invalidate evidence.

## What is NOT claimed

No implemented app, actual 12 commits, Windows build, real independent reviewer, latency savings or working save recovery were produced by this example. It is a **copyable execution-planning illustration**.

Use [one-card template](../templates/one-card.md) and [review economics](../docs/method/review-economics.md).
