# Full R2R development program — flexible long-horizon roadmap

**Goal:** a simple, adopted and evidence-tested method for AI-assisted high-throughput construction of complex *ultimately reliable* products.

**Productization direction (Owner, 2026-10-22):** prioritize a **complete usable end-user form** before spending cycles on complex experiments. The product is a portable no-server Skill + copy/paste Prompt + optional one-file R2R.md project state; users say Start / Continue / Harden, with STEER anytime. W5 empirical validation remains important but is **not** a prerequisite to delivering a coherent candidate package or documenting usage.

The roadmap is deliberately complete and long; execution horizons remain dynamic and developer-controlled. Completing an item means delivering evidence or an artifact, not just writing a plan.

## W0 — foundation (candidate delivered)
- W0.1 clarify problem, product, audience and non-goals.
- W0.2 publish one-page method and simple quickstart.
- W0.3 offer PLAN/RUN/Review/HARDEN/Resume templates and clear current-state.
- W0.4 fast consistency check; draft PR; no claim of empirical validation.
**Exit:** a stranger can understand and try the method without installing a runtime.

## W1 — conceptual rigor (working artifacts; branding visual/peer usability remains)
- W1.1 define throughput vs code output, complexity and final stability.
- W1.2 compare spec-driven, CI, incremental delivery, automated review and agent loops.
- W1.3 clarify interim quality vs protected invariants and verification debt.
- W1.4 define convergence capability and critical architecture uncertainty.
- W1.5 Chinese/English glossary, naming and short visual.
**Exit:** a coherent set of principles rather than an obligatory bureaucratic process.

## W2 — adoptable field kit (templates and scenarios delivered; outsider trials remain)
- W2.1 quickstart prompts for web-first and coding-agent projects.
- W2.2 sample whole-product capability map and long but revisable program.
- W2.3 developer question bank and risk-selective review notes.
- W2.4 repeated hardening / product acceptance playbook.
- W2.5 novice onboarding trials with short and long run examples.
**Exit:** end-to-end “PLAN → RUN → HARDEN” with “STEER ANYTIME” reproducible.

## W3 — long-run operations and recovery (core instructions and first real retrieval demonstrated; risk-injection work remains)
- W3.1 worked tens-of-slices program with clear task lineage.
- W3.2 exact-Git and session recovery practices (without inventing auto-resume).
- W3.3 **synchronous lightweight Review** after meaningful batches: short same-agent check, optional genuinely separate sequential independent Review, dependency-scoped holds; no local multi-agent requirement.
- W3.4 verification debt log and risk-scoped stop rules.
- W3.5 failure injection / interrupted work examples.
**Exit:** a practical long horizon without mandatory micro-approval.

## W4 — convergence and high-stability delivery (method/illustrations in progress; real software evidence remains outstanding)
- W4.1 architecture and product interaction restructuring playbook.
- W4.2 actual GUI/API/end-to-end and cross-process evidence.
- W4.3 security, permissions, real-data, rights and replay safeguards.
- W4.4 recovery from excessive technical/verification debt.
- W4.5 detailed final candidate/acceptance matrix.
**Exit:** real product readiness, not test-count theater.

## W5 — empirical case studies
- W5.1 choose at least two substantively different permitted project examples.
- W5.2 design comparable serial vs R2R evaluation and quality bar.
- W5.3 gather outcomes, human time, review lag, rework, discovered/escaped defects.
- W5.4 publish limitations and failures; do not exaggerate causal claims.
- W5.5 independent critique of evidence where available.
**Exit:** useful reproducible evidence, or explicit finding that claims remain unproven.

## Usable product package — near-term priority before complex validation
- U1 One README entry leading to the **three natural-language actions**.
- U2 Fully self-contained `skills/r2r/` folder with an internal `assets/R2R.md` and internal reference; no links outside the copied Skill.
- U3 **Release-first distribution**: use GitHub CLI's existing `gh skill publish --dry-run` / `gh skill publish --tag` pipeline and `gh skill install`, with `npx skills add` / manual copy as fallbacks. No bespoke install CLI.
- U4 First-use, resume, developer steering and HARDEN example, with real-vs-hypothetical labels.
- U5 One durable target-project `R2R.md` rather than many mandatory governance documents.
- U6 Candidate usability/source check; deeper controlled verification remains future W5, public release requires W6 owner decisions.
**Exit:** a permitted user can understand what to copy, where it goes, what to say, what state is saved and what the AI should do next, without needing a new runtime.

## W6 — open-source community preparation
- W6.1 English/Chinese concise docs and FAQ.
- W6.2 check name conflicts / repo/package availability.
- W6.3 choose license and audit all third-party/owner-source rights.
- W6.4 contributions, issue templates, governance, versioning.
- W6.5 maintainer-authorized **tagged GitHub Release** (and optional Skill-only zip), confirm one-command install/update then seek community feedback.
**Exit:** no public visibility/license change without explicit owner instruction.

## W7 — optional automation (only if justified)
- W7.1 measure repeated manual friction.
- W7.2 try smallest adapter using existing agent/Git APIs.
- W7.3 evaluate optional separate **sequential** reviewer and trustworthy resume; async/parallel infrastructure is out of the baseline and needs independent justification.
- W7.4 compare tool/no-tool outcomes.
- W7.5 accept or decline automation as core dependency.
**Exit:** R2R remains usable even if W7 is never built.

## W8 — deep hardening and ongoing improvement
- W8.1 remove contradictions, excess jargon and fake guarantees.
- W8.2 outsider usability review and examples.
- W8.3 reproduce studies and address critical counterexamples.
- W8.4 fix links and ownership/quality gaps.
- W8.5 iterate until agreed method release standards are met.

**Execution:** prefer delivering artifacts in coherent batches, light review and continuing immediately, while all authorizations and remote sessions are real. Developer may steer whenever necessary. Do not self-merge or pretend a draft PR is final publication.
