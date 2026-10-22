# How one developer uses R2R from idea to READY

**Fictional teaching conversation — not a tested application or transcript of real tool execution.**

Example project: an existing local desktop note tool with unfinished editing, navigation, storage and export. The agent has authorized access to its repository.

## 1. Developer: start

> Start R2R on this project. Build a mature note tool with create, edit, search, save/restart, export and safe recovery.

**Expected agent action:** inspect actual code and specs, write/update root `R2R.md`, link the original specs and identify one authoritative note-store owner; plan the entire product and final acceptance, then begin the first safe feature campaign rather than stopping at planning.

**Expected output:** `R2R.md` describes the product route; actual code changes and commits (if implemented); a truthful quick-review note and next campaign. No claim that the example actually ran.

## 2. Developer: continue long

> Continue R2R; develop as much of the safe product roadmap as this authorized run permits.

**Expected agent action:** read actual HEAD and `R2R.md` first; implement several meaningful reversible batches; synchronous quick self-review between batches; update the state with evidence and risks. Do not require an approval after every trivial edit. Do not claim work persisted outside the actual session.

**Possible project state:** editing/navigation/search exist but export is incomplete, UI rough, and a restart smoke has not yet run. `R2R.md` explicitly records these gaps without pretending the project is READY.

## 3. Developer: steer at the consequential question

> Who owns the authoritative note content? Did the new search index become a second source of truth? Give source evidence.

**Expected agent action:** inspect the code and trace writes. If a conflict is found, stop dependent persistence modifications, repair the architecture and adjust the long plan. Independent, reversible UI work may continue if truly isolated.

This is **targeted steering**, not a universal deep review of every commit.

## 4. Developer: continue from a fresh session

> Continue R2R. Read Git and R2R.md; don't restart planning.

**Expected agent action:** re-read actual source/PR state, reconcile the previous checkpoint, and continue the next safe meaningful campaign. If no repository tools are available, say so rather than invent edits.

## 5. Developer: harden

> Harden this product using R2R. First make whole user journeys reliable, then do repeatable recovery and negative tests.

**Expected agent action:** exercise actual create → edit → save → restart → search → export, then repair structural contracts, negative permission cases and recovery. Re-run regressions after any architectural redesign.

| Promised outcome | Example status before genuine runs |
| --- | --- |
| Create/edit/save in packaged application | NOT_RUN |
| Restart retains content | NOT_RUN |
| Search uses the canonical stored revision | NOT_RUN |
| Export/re-import loses no authorized content | NOT_RUN |
| Negative permission and data-recovery checks | NOT_RUN |

Only actual observations replace `NOT_RUN`. Releasing is the developer's explicit decision after agreed evidence.

## What makes this different?

The project never needs a separate R2R server. Its existing coding agent implements, Git holds durable facts, `R2R.md` holds the long product route and current state, **short synchronous review prevents obvious drift**, and deep acceptance evidence is concentrated where it matters.

The exact scenario is hypothetical; it demonstrates the **finished user experience**, not an empirically measured speedup. See [install](../quickstart/install.md) and [copyable project-state template](../skills/r2r/assets/R2R.md).
