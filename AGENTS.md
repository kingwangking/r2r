# R2R Agent Charter

Read [README](README.md), [method](docs/method/r2r.md), [roadmap](docs/program/roadmap.md) and [current state](docs/program/current-state.md) before work.

**Product:** a simple, reusable high-throughput AI engineering **method** and optional portable instruction assets. R2R does not require a local runtime. ChatGPT Web + GitHub is the primary development channel for this repository.

**PLAN:** Know end-product promise, broad architecture, complete roadmap and important risks.
**RUN:** Ship useful artifacts in coherent batches; synchronous lightweight review after each meaningful batch, then continue; no separate local reviewer/async infrastructure required, and no perpetual documentation or formal review.
**STEER:** Owner can interrupt, ask source-grounded questions, shorten/lengthen runs, direct deeper review or reshape architecture any time.
**HARDEN:** Repeatedly integrate, restructure, test real outcomes and address verification debt until final criteria are actually met.

Rules:
- State what is planned, implemented, tested, independently reviewed or unverified accurately.
- Long planning is allowed; no fiction about tools running after a web session has ended.
- Keep high-consequence effects safe: real data, permissions, secrets, intellectual property and public distribution.
- Preserve current Git state. Do not auto-merge, force push, change repository visibility or choose a license on the owner's behalf.
- Reuse specs and existing tools; do not introduce a server/database/orchestrator without evidence it solves a real adoption problem.
- Current default is **synchronous Review in the same work sequence**: implement a meaningful batch → quick focused self-review → repair P0/P1 affected paths → record P2/P3 → keep executing. The agent must not label its own self-review independent.
- A developer may request a deeper sequential review or a separate independent reviewer if one is actually available. No asynchronous reviewer queue or extra local multi-agent framework is assumed; avoid deep mandatory gates for every tiny draft.
- Keep [docs/program/current-state.md](docs/program/current-state.md) and [docs/README.md](docs/README.md) aligned with actual repo facts.
