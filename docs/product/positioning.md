# R2R product positioning

**User:** a developer directing AI agents to build multi-module software beyond toy demos.

**Problem:** AI accelerates code production and makes complex ambitions possible, but full serial review of each intermediate change may cost more than implementation. Large amounts of passing micro-tests or PR activity are not the same as a mature usable product.

**Objective:** Increase *verified end-product delivery* for complex systems without sacrificing the final stability requirement.

**Approach:** strong whole-product direction; long but steerable runs; **synchronous lightweight Review after meaningful batches**, depth proportional to risk (no automatic full deep gate); acceptable imperfect intermediate shapes; repeated structural convergence and final real-product verification.

## The distinction
- **Spec-driven development:** clarifies expected behavior and tasks. R2R consumes those inputs; it governs pace, validation timing and final convergence. Compatible, not a replacement.
- **Agent loops:** automate repetition. R2R includes architectural confidence, human steering, high-risk boundaries and a product-level exit.
- **Automated PR reviewers:** review diffs. R2R decides which reviews are useful, what must block dependent work and what can safely be deferred.
- **Continuous integration:** detects breakage. R2R allows an intentionally non-release-ready intermediate product without concealing failing probes or sacrificing real-data safety.

## Current product, not speculative product
A concise method, copyable prompts, templates, an honest worked example and a research plan. **No mandatory CLI, hosted web app, model connector, database or local executor.**

Optional automation is a later research decision, only if repeated evidence shows an essential unmet need.

**Open source:** currently private; license, rights and public visibility are unresolved. Do not claim a public release.
