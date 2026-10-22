# R2R glossary — 用统一语言讨论速度、复杂度和最终稳定性

**Status:** working definitions. R2R is a proposed method, not an established software engineering standard.

| Term | Meaning / 中文解释 | Do not confuse with |
| --- | --- | --- |
| **Accepted-product throughput / 有效交付吞吐** | Actual end-user journeys **accepted at the specified quality bar** per time/resource budget. | Lines of code, PR count, number of agent turns. |
| **Complexity / 系统复杂度** | Functional breadth, cross-module coupling, state/authority boundaries, environmental and organizational constraints. | Just file count or task count. |
| **Final stability / 最终稳定性** | Repeatable correct behavior, resilience and safety **at the agreed release scope**, supported by evidence. | A single green smoke test. |
| **Intermediate quality / 中间质量** | The level of working behavior and proof intentionally required **right now**. Adjustable with dependency/risk. | Automatic release approval. |
| **PLAN / 全局定向** | Whole-product target, architecture hypothesis, authority boundaries, roadmap and readiness test. | Frozen exhaustive implementation design. |
| **RUN / 持续建设** | Delivering meaningful product capabilities within a chosen execution horizon. | An indefinite background process or unbounded churn. |
| **HARDEN / 系统收敛** | Repeated integration, structural correction, real-use validation and defect repair until acceptance. | Only fixing small bugs at the end. |
| **STEER / 开发者动态裁决** | Developer controls direction, run length, verification depth and interruption. | Obligatory manual approval after each task. |
| **Review / 降低不确定性** | Targeted question, code review, contract probe, architecture audit or real-product observation. | Every review is a serial gate or independent approval. |
| **Checkpoint / 可恢复记录** | Truthful progress and next-step state at an actual artifact/ref. | Acceptance or a request to halt. |
| **Gate / 受影响边界的阻断** | Specific operation or dependency cannot proceed until a critical condition is met. | Stop all unrelated implementation. |
| **Verification debt / 验证债务** | A known claim whose required proof is deferred, with scope, risk and due stage. | Automatically acceptable outstanding defects. |
| **Convergence capability / 可收敛性** | The demonstrated prospect of reaching final acceptance without unbounded rework under current architecture and feedback. | Belief that “AI can always fix it later.” |
| **Evidence / 工程证据** | Exact code/test artifact, reproducible probe or real user-observed behavior with scope. | Agent explanation, test plan, or generic confidence. |
| **READY / 最终就绪** | Agreed, evidence-supported product acceptance and authorized release decision. | “All backlog items implemented.” |

## Essential distinctions

- **Long roadmap vs long run:** a complete product roadmap can be hundreds of items; any actual run may stop when time, permission, risk or developer judgment requires.
- **Quality deferral vs protection:** an incomplete UI can wait; real-data loss, secret leakage, rights violations and unbounded authority errors cannot.
- **Progress vs readiness:** useful intermediate progress need not be shippable, but must be traceable and should move real product outcomes toward acceptance.
- **Confidence vs proof:** developer confidence is a rational control input, updated by evidence; it never turns NOT_RUN into PASS.

Useful adjacent reading: [R2R method](r2r.md), [convergence](convergence.md), [developer steering](steering.md).
