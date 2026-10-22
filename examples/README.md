# Example (illustrative, NOT an actual measured experiment)

Product: a complex note editor with UI, persistent document model, search and export.

**PLAN:** define create/edit/search/export/restart user journeys and **one** authoritative storage owner. Make a long capability map.

**RUN:** build the screens and document features rapidly; accept temporarily broken layout or missing search behavior. A developer can ask “Does the editor write through the correct authority?” and require code or runtime evidence. A broken intermediate smoke test need not stop unrelated export work.

**STEER:** if multiple modules start owning document state, stop dependent work, correct the architecture and resume; no need to wait for the final release cycle to fix this.

**HARDEN:** integrate real input, undo, save/restore in separate processes and export; restructure document transactions before polishing low-impact bugs. Repeat realistic product tests until acceptance passes.

**Counterexample:** blindly defer storage-authority checks through dozens of slices and accumulate severe coupling; later redesign costs more than early feedback would have. R2R does not guarantee long runs always win.

See [quickstart](../quickstart/README.md).
