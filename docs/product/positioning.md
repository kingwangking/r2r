# R2R product positioning — Run to Ready

**Definition:** **R2R / Run to Ready is an AI-native end-to-end product delivery operating method**, aiming to convert expanded AI coding capacity into a **correct, integrated, evidence-backed accepted software product**. Fast vertical iteration is R2R's distinctive practical policy, **not the entire definition**.

## The AI-era bottleneck

AI generates software artifacts quickly, but production success needs **correct product intent**, **scalable yet integratable implementation**, and **continuous feedback/repair until genuinely usable**. Optimizing just one dimension fails: fast wrong requirements produce the wrong product; lots of independent agent output can lack integration; repeated broad review consumes iteration throughput; finishing tasks does not establish READY.

## Three connected capabilities, one goal

| Capability | Adopted foundation | R2R's purpose |
| --- | --- | --- |
| **Correct goal / Spec** | Existing SDD/Spec Kit and project architecture/contracts/acceptance | Ensure the work targets the real desired product |
| **Horizontal execution / parallel agents** | Existing available multi-agent tools plus stable module boundaries | Multiply independently owned work without uncontrolled conflict |
| **Vertical execution / iterative RUN** | R2R's long useful batches, frequent developer STEER, risk-focused Review, grouped findings/fixes | Preserve high iteration velocity across time, maintain context, integrate and correct course |

**Outcome:** repeated integration / structural HARDEN / actual negative and product checks → evidence-backed READY.

### Differentiation and prior art

R2R does **not** invent specification, parallel coding, iterative feedback, review, or convergence. Spec Kit itself performs `implement` and `converge`; available agent runtimes can spawn workers. R2R provides **a complete practical composition and developer-led execution policy** across those mature capabilities. Its notably emphasized problem is **longitudinal iteration economics**; the project name describes the *overall destination*, not only that one solution.

### Delivery form

A portable Skill + prompts + optional project-root `R2R.md` referencing existing Specs; no required SDD replacement or multi-agent orchestrator. Parallel execution is conditional on actual agents and safe ownership; a single coding agent can implement the full operating loop more slowly.

**Evidence limits:** [v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) is publicly released under [MIT](../../LICENSE) with successful package/CLI installation checks. No controlled performance advantage or complete real-agent outcome is claimed. Improvements on the current HARDEN PR are not automatically included in the tagged release.

[Three-practice integration](compatibility.md) · [Current method](../method/r2r.md) · [Spec Kit official documentation](https://github.github.com/spec-kit/) · [OpenAI parallel agent guidance](https://developers.openai.com/api/docs/guides/agents-api/multi-agent)
