# R2R 中文使用指南

**安装一次，之后让已有编码 Agent 持续完成产品开发。** R2R 不是单独的软件运行器，而是**Spec + 可选多 Agent 并行之上的快速迭代方法**：Spec 负责需求/架构/验收，模块职责分明时并行 Agent 负责横向执行，R2R 负责纵向持续迭代、开发者实时 STEER、Finding 分级处理、批次修复和最后 HARDEN。

[正式 v0.1.0 Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) · [安装方法](install.md) · [完整教学示例](../examples/complete-usage.md)

## 1. 安装或直接复制

Codex 用户在支持 Skill 的 GitHub CLI 中：

```bash
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent codex --scope user
```

也可下载 [Skill ZIP](https://github.com/kingwangking/r2r/releases/download/v0.1.0/r2r-skill-v0.1.0.zip)，完整解压到项目的 Skill 目录。不支持 Skill 的网页端 AI 助手可以复制 [README 提示词](../README.md)，但软件修改需要其拥有实际仓库工具。

## 2. 第一次：开始 R2R

在**你要开发的软件仓库**中对 Agent 说：

```text
采用 R2R 开发这个项目。读取真实代码、原有规格、架构和已有进度。
建立覆盖完整产品的长期路线、关键模块职责与最终 READY 验收目标，
写入项目根目录 R2R.md，并立即开始第一批已授权的安全功能开发。
每个有意义的批次后同步快速自检，记录确实修改和测试的内容，
然后继续。会话结束前写回实际进度和下一步。
```

理想交付：`R2R.md` 中可以看到完整规划与实际下一批工作，并且（宿主具备执行权限时）至少开始了真实的代码/功能建设。**单纯生成计划并不意味着已完成 RUN。**

## 3. 日常：继续 R2R

```text
继续 R2R。先读取 Git 的真实 HEAD、工作区和 R2R.md，
修正过期记录，按长期路线继续下一批有价值的功能开发。
同步轻量 Review；代码功能、安全与数据完整性问题按严重程度及时修复，必要时做受影响路径的快审；一般 P2/P3 记入集中修复队列；纯文档措辞除影响验收、安全授权或追溯外不反复独立 Review。修复后直接继续下一个安全 Slice，不重新开启完整 Review 循环。
```

R2R 不强制“每五个任务正式 Review 一次”；每个有意义的批次做一次短自检。涉及权限、凭据、真实数据和不可逆副作用时，必须在影响发生前做必要的深入检查。

**停止时**将结果写回 `R2R.md`；新会话通过 Git 和该文件恢复。并没有脱离 Agent 会话自动运行的隐藏任务。

## 4. 随时 STEER

例如：“这一轮执行更长，不要为普通小问题反复停下”“先确认哪些模块有持久化权威”“修改总体规划，优先做完整 GUI 流程”“对数据迁移进行深入审查”。

Agent 应以真实源码或测试回答重要判断，而不是用解释代替证据。

## 5. 功能成形：HARDEN

```text
进入 R2R HARDEN。用真实集成产物走完整用户业务链，
先解决架构、状态权威与模块接线问题，再进行实际交互、
崩溃/重启/恢复、权限负例、回归和必要的性能检查。
对每个最终验收项记录 PASS/FAIL/NOT_RUN 及准确的版本证据；
发现结构问题就调整设计并重测，直到达到约定 READY 要求。
```

HARDEN 可能要重构整个模块，而不是只修小 Bug。最终是否发布由有权限的项目维护者批准。

## R2R 留下哪些资产？

最少只有**一个项目根目录 `R2R.md`**，包含产品目标、架构风险、长程计划、当前真实成果和下一步；可直接链接已有 Spec/Issue/ADR，不新造一套治理体系。[模板](../skills/r2r/assets/R2R.md)。

**限制说明：** Skill 安装与完整性已有 [GitHub Actions](https://github.com/kingwangking/r2r/actions/runs/39737882456) 证据，真实 Codex/Claude Code 使用场景尚未经过外部完整验证；不声称 R2R 已被证明能提高开发速度。
