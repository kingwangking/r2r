# R2R — Run to Ready

**Plan big. Run long. Harden deep. Steer anytime.**

[中文快速上手](quickstart/use.md) · [安装与更新](quickstart/install.md) · [v0.1.0 Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0) · [方法介绍](docs/method/r2r.md)

R2R 是现有 AI 编码 Agent 可采用的轻量工程方法：**先完成整体产品规划 → 长周期持续建设 → 每个有意义的批次同步快速自检 → 反复整合与修复，直到真实产品满足交付要求**。开发者可以随时调整方向、执行长度和审查深度。

R2R 是一个可安装的 **Agent Skill**，不是新的 IDE、模型、任务调度服务或后台永动 Agent。它使用当前 Agent 已经拥有的 Git、代码执行和测试权限，不会凭空获得额外能力。

## 安装已发布版本

**R2R v0.1.0 已正式发布，MIT 开源。** 推荐使用支持 `gh skill` 的 GitHub CLI：

```bash
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent codex --scope user
```

Claude Code 项目范围安装：

```bash
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent claude-code --scope project
```

[完整安装说明](quickstart/install.md) · [下载 Skill ZIP 与 SHA-256](https://github.com/kingwangking/r2r/releases/tag/v0.1.0)。GitHub Actions 已验证版本安装和文件完整性；具体 Codex/Claude Code **对指令的实际遵循效果尚未实测**。

**不安装也能使用。** 在有项目访问权限的 AI 助手中复制：

```text
使用 R2R 开发当前项目。先读取真实仓库与已有规格，形成覆盖完整产品的
可修订长期计划、架构边界和最终 READY 标准，保存在项目根目录 R2R.md。
在我已授权的范围内立即实现第一批有价值的功能；每个有意义的批次后
同步轻量自检，阻止受重大风险影响的操作，记录真实证据并继续。
我可以随时调整方向和执行长度。退出前记录实际 Git 状态与下一步。
不虚构后台执行、独立 Review 或未运行的测试。
```

## 使用者只需要三个操作

| 说什么 | Agent 应当做什么 |
| --- | --- |
| **Start R2R / 采用 R2R 开发这个项目** | 读取现有项目和规格，建立整体路线与 `R2R.md`，立即开始第一批安全工作 |
| **Continue R2R / 继续 R2R** | 用实际 Git 状态核对进度文件，不从零重复规划；持续建设、同步轻量 Review |
| **Harden with R2R / 进入 R2R HARDEN** | 走通真实用户路径，修复结构、集成、恢复和回归问题；只在证据充分时宣布 READY |

**随时 STEER：**“检查持久化架构后再继续”“这一轮执行更长”“先处理真实 GUI 流程”“深入审查这个高风险接口”。

这些是自然语言指令，不是 R2R 新开发的 CLI 子命令。AI 助手如果无法访问项目或运行工具，就只能规划，不能声称已修改或测试软件。

## 它会在你的仓库留下什么？

对于需要长期迭代的项目，一份**项目根目录 `R2R.md`** 就能记载完整产品目标、路线、真实进度、待验证风险和下一批工作；已有 Spec/ADR/Issue 直接引用，不必再造一个文档系统。

你可以选用 [R2R.md 模板](skills/r2r/assets/R2R.md)；[Agent Skill](skills/r2r/SKILL.md) 完全自包含，可独立安装，其详细操作参考位于包内。

## 当前产品状态

- **已交付：** 正式的 [v0.1.0 Release](https://github.com/kingwangking/r2r/releases/tag/v0.1.0)，MIT、Skill 包及校验文件，实际 GitHub CLI 安装检查。
- **持续打磨：** `main` 后续改进不改变已发布的 `v0.1.0` Tag；发行以 Tag 为准。
- **仍待验证：** 在真实 Codex/Claude Code 宿主中触发与遵循 Skill、复杂软件中长期效果的独立实测。

[中文逐步使用指南](quickstart/use.md) · [完整教学示例（非真实执行）](examples/complete-usage.md) · [项目自举进度](R2R.md) · [深度文档目录](docs/README.md)
