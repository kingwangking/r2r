# Web-first R2R — ChatGPT + GitHub only

This playbook is for projects **without a mandatory local CLI, agent daemon, terminal, model SDK or build server**. The user can still use the R2R method and write long plans. A live ChatGPT web session is the actual executor for documentation/design/editing tasks; GitHub is the durable source of truth.

## 1. Read facts, not chat memory
- Inspect the actual repository and current branch/PR before claiming progress.
- Start at README/AGENTS/current-state; look up exact commit when reviewing changed source.
- Never infer that a local Codex run or a CI test happened just because it appears in a plan.

## 2. PLAN big
- Capture product positioning, end-user outcomes, conceptual architecture, important contracts and final quality bar.
- Record a full development roadmap. The plan can be longer than what can fit into one actual interaction.
- Distinguish planned deliverables from implemented source, and preserve owner changes to the roadmap.

## 3. RUN in coherent batches
- Work in a dedicated Git branch; one meaningful PR can contain several compatible iterations.
- Directly write actual reusable assets/implementation; don't spin on pre-review before any content exists.
- After a batch, verify relevant content cheaply: broken links, contradictory gates, wrong owner facts, evidence claims.
- Continue further work **within the current user-authorized interaction**, or leave a truthful next-step pointer when no further active execution is possible.
- GitHub draft PRs are workspaces, not automatic publication/merge instructions.

## 4. STEER by targeted questions
The owner can ask “Why is this architecture reasonable?”, “What is unfinished?”, “What would fail in real use?”, “What mature method did we reuse?” or demand deep review of a particular change. Answer from the repository or genuine evidence, then redirect.

## 5. HARDEN the method / product
- For R2R itself, verify that first-time users can apply the method from README and quickstart without extra ceremony.
- Audit plan/template consistency and actual Git SHA.
- For real software built using R2R, measure real journeys and release-level quality; docs-only review is not a substitute.
- Do not auto-merge, publish, alter visibility, install tooling or change license without authorization.

**Limit:** A ChatGPT web conversation does not perform hidden continuous GitHub work after the active invocation ends. Preserve the roadmap and current-state so the next session continues quickly; this is resumability, not perpetual automation.
