# Example: 40-slice plan, flexible batch length

**Training scenario only. No implementation, Review, UI test or package was executed.** This illustrates why R2R supports a complete plan larger than any one agent session.

## Product

A local-first personal knowledge workbench: notes, tagging, cross-document search, revisions, file attachment management, export, sync (opt-in only), diagnostics and recovery.

**Whole-product constraints:** a single canonical note store, explicit write transactions, offline-first, user consent for external data transmission, import/export rollback, no destructive migration without recoverable copy.

**READY:** packaged product can create/edit/search/tag/recover/export with real data fixtures and process restart; negative permission and corruption scenarios have observable results; release owner approves scope and rights.

## Forty planned slices: eight outcome groups

| Group | Five slices in order | What should exist after the group | Review / integration emphasis |
| --- | --- | --- | --- |
| G1 — Project shell | S01 workspace; S02 create; S03 open; S04 navigation; S05 settings | A navigable real workspace | Cheap synchronous source/UX check |
| G2 — Document editing | S06 editor; S07 save; S08 revisions; S09 undo; S10 redo | Text editing and reversible author actions | Storage authority and transaction seam |
| G3 — Organize | S11 tags; S12 collections; S13 move; S14 reorder; S15 delete-to-trash | Organized content, recoverable deletes | Negative state/recovery probe |
| G4 — Search | S16 index; S17 full text; S18 filters; S19 relevance; S20 index rebuild | Discoverable persistent notes | Index staleness and canonical authority |
| G5 — Attachments | S21 import; S22 preview; S23 dedup; S24 locate; S25 cleanup | Files safely linked to notes | Sandbox paths, real-data protection |
| G6 — Export/import | S26 markdown export; S27 bundles; S28 validate import; S29 rollback; S30 version mapping | Portable content without loss | Must check irreversible effects before dependent writes |
| G7 — Resilience | S31 autosave; S32 crash recovery; S33 damaged index; S34 interrupted import; S35 audit log | Failure recovery and diagnostics | Real process-restart test |
| G8 — Polish/acceptance | S36 keyboard flows; S37 accessibility; S38 offline guarantees; S39 performance; S40 release report | End-to-end product candidate | HARDEN, deep release checks and owner acceptance |

## The developer may choose different horizons

- **Long RUN:** authorize G1–G4 together if state ownership and relevant contracts are understood; perform a **short synchronous quick Review after each meaningful group/batch**, then continue. No independent reviewer required.
- **Short RUN:** if S07 save design raises an unverified data ownership risk, ask a targeted question and require a real read/write probe *before* S08/S09 rely on it.
- **Restructure now:** if G4 reveals duplicate stores, redirect the affected dependency immediately. Don't knowingly compound the problem until release.
- **HARDEN early:** for corruptible import/export and restart, run real fixture checks before any live destructive operations; other reversible UI work can continue when safe.
- **Final HARDEN:** whole-app assembly and repeated integration/recovery tests after features form. A green isolated G3 test is not READY.

## End-of-batch micro-checkpoint

```text
Observed source: <real repo/ref/SHA>
Delivered journey(s): <actual evidence>
Synchronous self-review: <scope + PASS_FAST / findings>
Dependent P0/P1 hold: <scope>; deferred validation: <owner + due>
Next slice/group: <one high-value outcome>
```

This 40-slice map **permits** long execution and changing run length; it does not require exactly 40 turns, 8 reviews or a particular model. Its example results are NOT_RUN.
