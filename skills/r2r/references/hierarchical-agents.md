# Hierarchical Agent execution — adapt models and reasoning effort per task

R2R works on existing coding agents; it does **not** provide its own orchestrator or guarantee that the current host can spawn nested agents. For **substantial software programs with independently deliverable Campaigns and real subagent support**, prefer the following execution topology instead of a single serial executor or multiple parent agents without local workers.

## Two tiers of useful delegation

```text
                        Actual Spec + READY / Program
                                    │
                          Program Lead / Integrator
                    (Wave, contracts, dependency frontier,
                     high-impact findings, cross-Campaign joins)
                ┌───────────────────┼────────────────────┐
                ▼                   ▼                    ▼
         Campaign Lead A      Campaign Lead B       Campaign Lead C
         (outcome A)          (outcome B)           (outcome C)
           ├── A1 implementation ├── B1 implementation  ├── C1 evidence
           ├── A2 test/negative   └── B2 review/repair    ├── C2 interface
           └── A3 review                                     └── C3 test
                │                   │                    │
           Campaign-local integrate/verify (one owner per campaign)
                                    │
               Cross-Campaign Integrator: shared seams ONE writer
                                    │
            integrated acceptance → next READY Campaigns → HARDEN
```

**Default for a large, separable, capable execution surface:**
1. The Program Lead launches **multiple Campaign Lead Agents concurrently** when their real dependencies permit.
2. **Each Campaign Lead genuinely delegates** one or more scoped Workstream subagents; prefer several when useful (implementation, test, reference study, independent lightweight review). Each Lead remains accountable for integrated behavior and repairs; do not treat child PASS as campaign PASS.
3. Establish frozen shared contracts, input commit SHA, read-only references, disjoint owned paths/worktrees, risk holds and one owner of common state/schema/entrypoints before fan-out.
4. Campaign Leads integrate their own children; the Program Integrator integrates shared interfaces, releases newly eligible dependent work as soon as real prerequisites exist, and reports actual end-to-end evidence.
5. Review subagents may work alongside the parent implementation but findings feed **a repair/recheck loop**, not a recurring global Review hold. Use genuine independent review when consequential; label quick same-agent checks as self-review.
6. Keep parallel breadth and recursion bounded by verified resources, actual task independence, local memory, latency/API quotas and cost. Nested delegation does not mean infinite child trees: **Program Lead → Campaign Leads → Workstream subagents** is normally enough.

This is a *preferred topology for a substantial, separable program*, not a demand to spawn layers for a trivial correction. If subagent tools or true concurrency are unavailable, preserve boundaries and work sequentially, recording that actual concurrency was unavailable; **never fabricate spawned agents or execution results**.

## Dynamic model and reasoning-strength routing

Select each Agent's model and supported reasoning effort at execution time from **available tool-capable, authorized** options, not one fixed provider or a compulsory high-effort preset. The Program Lead and Campaign Leads may select differently from their children.

| Work | Typical capability priority | Effort guidance (only if supported by the client) |
| --- | --- | --- |
| Product/architecture, owner of risky shared contracts | Strong cross-file reasoning and consistency | high / extra-high when warranted |
| Campaign lead implementation/integration | Solid coding, repo tooling and repair reliability | medium/high; escalate for hard faults |
| Child implementation, focused tests or docs | Speed/cost-efficient model that meets task's tools and accuracy | low/medium where sufficient |
| Security, persistence, data authority, sensitive migration review | High-reliability reasoning with separate evidence/context | high/extra-high where needed |
| Deterministic builds, linters, checksum checks | Run tools/scripts directly | model not required |

Before assigning a model: check the current host/CLI exposes it, whether its agent/child/tool feature works, whether use is authorized, and what token/latency/compute/billing cost is acceptable. Reassign or escalate when real test failures or risk show that the current model is insufficient. There is **no model-family or effort whitelist** in R2R.

Changing the model for a child does not automatically imply changing the user's primary local coding execution channel. This is agent configuration guidance, **not** entitlement, API-key or model availability evidence.

## Minimal delegated work packet / honest evidence

```yaml
parent: program-lead | campaign-lead
child_role: campaign-lead | workstream-implementer | verifier | reviewer
campaign: complete end-to-end behavior
scope_and_done: observable acceptance for this child
input_sha: exact verified upstream commit
owned_paths: only the explicitly isolated files
shared_seams: integrator-only
stop_conditions: permissions | data authority | destructive migration
model_selection: choose at runtime by capability/risk/cost
effort: choose at runtime by task complexity and consequence
handoff: diff/commit, tests genuinely run, failures, findings, next-safe-task
```

Actual Workstream children can use disjoint worktrees or branches. Record only meaningful agent provenance, model and effort where possible, no secrets. A reviewer cannot truthfully be called independent unless it really ran in a separate review context.

## Links to the main R2R operating loop

The Spec and project's actual authority remain unchanged. The **Wave** chooses what is dependency-ready; the **Campaign Lead** produces a complete behavior with children; the **Program Integrator** connects true shared seams; **R2R** keeps running with targeted fixes, grouped low-impact cleanup, developer STEER and real integrated HARDEN.

**Do not equate hierarchical concurrency with READY.** More spawned agents or green unit tests are not a substitute for integrated user flows, rights, recovery and Owner acceptance. An unavailable nested-agent runtime is a capability constraint, not permission to invent it.
