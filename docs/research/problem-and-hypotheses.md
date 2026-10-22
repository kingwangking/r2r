# Research: speed × complexity × final stability

**Status:** motivated by real private AI-development experience; hypotheses are *not* validated general findings.

## Observed problem
In substantial AI-assisted projects, specifications, architecture documents and repeated independent review can all exist while actual product usability advances slowly. As AI generates larger changes and enables more ambitious products, thorough serial review and re-review may consume more time than implementation itself.

## Research question
Can we make the whole *accepted product* arrive sooner by allowing steerable, high-throughput long runs and deferring some intermediate verification, **without degrading final product quality**?

## Falsifiable hypotheses
- H1: serialized deep review of low-risk changes lowers whole-product throughput.
- H2: architecture-guided long runs can outperform uniformly small gated iterations.
- H3: targeted developer questions and selective review can resolve direction uncertainty at lower cost.
- H4: repeated real-path integration and structural redesign can converge more effectively than repeatedly perfecting isolated changes.
- H5 (counter-risk): excess deferred integration and misplaced confidence cause rework that *exceeds* time saved.

## Evidence to collect
Compare matched feature goals using (A) serial deep review before each continuation, (B) R2R with risk-appropriate feedback. Fix the **same final acceptance** and record elapsed time, meaningful user journeys completed, human interventions, review wait, cost if available, P0/P1 defect escapes, redesign cost and realistic package/GUI/integration evidence.

Record null and negative outcomes. Code lines, number of commits, green unit tests or AI explanations alone are not an adequate measure. An internal anecdote is not a benchmark. Do not copy code, customer data, proprietary documents or licensed media from private projects into an eventual public case study.

## Unresolved
How to detect when verification debt has become unmanageable? How much architecture confidence enables a safe long run? Which project classes benefit? How to compare quality fairly? These questions determine future research priorities.
