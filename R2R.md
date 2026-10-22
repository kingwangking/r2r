# R2R — 本仓库的 R2R 执行入口

这份文件是 **R2R 项目使用 R2R 自己开发的实践记录入口**，不是给每个使用者安装的额外文档。使用者只需在他们自己的软件项目里建立一份根目录 `R2R.md`。

## PLAN：项目终点

**交付物：** 易安装、易理解、可恢复、在现有 AI 编码 Agent 中可直接使用的 R2R **快速迭代** Skill；可叠加既有 Spec/SDD 与多 Agent 并行，而不是替代它们。开发者只需要 Start → Continue → Harden，随时 STEER。可移植 Skill 和发行源保持单一事实来源。

**现有权威资料：** [README](README.md)、[方法定义](docs/method/r2r.md)、[项目整体路线](docs/program/roadmap.md)、[最新发布版本](https://github.com/kingwangking/r2r/releases/latest)、[源码状态](docs/program/current-state.md)。不要在本文件里复写完整路线图。

**架构和权威：** `skills/r2r/` 是可分发的 Skill 源；`scripts/skill_release.py` 对其做检查/打包；GitHub Release Tag 是已发布版本的不可变来源，`main` 可继续演进。权限、敏感数据、无证据声称和未经批准的发布属于保护边界。

**READY：** 可分发版具有真实安装证据、准确的入门指南、来源/版权清晰、可恢复开发工作流；如要声称在具体 Agent 宿主或复杂软件场景中有效，需要对应实际证据。

## RUN：目前到哪里

- **正式已发布：** `v0.1.0`，Tag 固定在 `1f7bdd09e2f304d4dd03f6575114ebc73a5e413a`。MIT。
- **真实检查：** [发布后安装/校验 PASS](https://github.com/kingwangking/r2r/actions/runs/39737882456)；真实 Codex / Claude Code 交互执行 **NOT_RUN**。
- **当前阶段：** 发布后 HARDEN。第一轮已修复 README、中文使用指南、安装页及 Skill/贡献/定位等旧状态；新建 [Draft PR #2](https://github.com/kingwangking/r2r/pull/2)，维持已发布的 v0.1.0 不变。
- **当前工作分支：** `hardening/post-v0.1.0-usability`（历史名称；恢复时请重新读取 Git）。
- **Review：** 每个有意义的批次同步轻量自检；重大风险需深入验证；不把自检称为独立 Review。
- **真实验证：** [CI Run #39739514168](https://github.com/kingwangking/r2r/actions/runs/39739514168) **SUCCESS**：12 个源码/负例测试、文档一致性检查、官方 Skill 发布前检查、本地/远程指定 SHA 安装、ZIP/校验文件构建。仅证明这批检查范围。
- **Owner STEER：** 功能/安全/数据完整性 Finding 按风险及时修复并按需针对性快审；普通 P2/P3 批次集中修复；纯措辞不反复独立 Review（除验收/授权/追溯风险）。主 Codex 收集重要 Finding、安排修复并持续下一 Slice。R2R 聚焦纵向迭代，兼容 Spec 与多 Agent 分层并行。
- **下一批：** 验证核心 Skill/README 一致性及 CI，申请设置 GitHub About/Topics；以后再在真实 Codex 或 Claude 做 Start → Continue → Harden 试用（NOT_RUN）。

## HARDEN：本阶段验收

- 用户从 README 出发能确认已发布版本、安装命令和开始使用的方法。
- 中文入口、英文/通用安装说明、Release Tag 和工程状态不再互相矛盾。
- 自动 CI 能捕捉主要入口中“未发布/还在 Draft”的错误陈述。
- Skill 包继续自包含，既有源码/打包与 CLI 安装检查不能回退。
- [HARDEN 方法](docs/method/hardening-playbook.md)用于本仓库实际修复，不将文档检查当作真实 Agent 宿主行为的证明。

**继续时：** 先读 Git HEAD、当前 PR/分支，再核对本文件，执行下一个确实授权且安全的批次。未经确认不重新发布或移动 `v0.1.0` Tag。
