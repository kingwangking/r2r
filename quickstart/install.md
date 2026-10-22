# 安装 R2R — 已发布的 Agent Skill

**正式稳定版本：[v0.1.0](https://github.com/kingwangking/r2r/releases/tag/v0.1.0)**。源代码采用 [MIT 许可证](../LICENSE)。安装它不需要 R2R 专属服务器、数据库、守护进程或多 Agent 运行架构。

## 推荐：GitHub CLI 直接安装

需要一版**支持 `gh skill` 子命令**的 GitHub CLI（该功能当前属于预览功能）。下面的 `v0.1.0` 是真正存在的版本：

```bash
# Codex：当前用户范围，固定发布版本
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent codex --scope user

# Claude Code：当前项目范围
gh skill install kingwangking/r2r r2r --pin v0.1.0 --agent claude-code --scope project

# 安装前预览
gh skill preview kingwangking/r2r r2r@v0.1.0
```

固定版本便于复现；省略 `--pin` 时可能安装最新版本。具体安装路径由 GitHub CLI 与宿主管理，项目级与用户级安装并不相同。若 `gh skill` 不存在，先升级到支持该功能的 GitHub CLI，或使用下面的手动方式。

## 不使用 GitHub CLI

可以下载 [Release ZIP](https://github.com/kingwangking/r2r/releases/download/v0.1.0/r2r-skill-v0.1.0.zip)（对应 [SHA-256](https://github.com/kingwangking/r2r/releases/download/v0.1.0/r2r-skill-v0.1.0.zip.sha256)），解压后将**整个 `r2r/` 目录**放进宿主的技能目录：

| 宿主 | 项目范围 | 用户范围 |
| --- | --- | --- |
| Codex | `<project>/.agents/skills/r2r/` | 按 Codex 所使用的用户级 Skill 目录 |
| Claude Code | `<project>/.claude/skills/r2r/` | `~/.claude/skills/r2r/` |

安装目录需要有 `SKILL.md`、`LICENSE`、`assets/R2R.md` 和 `references/operating-guide.md`。不要只复制单独的 `SKILL.md`。安装后按宿主的正常规则刷新或重新打开项目，并明确要求 Agent 使用 R2R。

也可以尝试第三方 [skills installer](https://github.com/vercel-labs/skills)：`npx skills add kingwangking/r2r --skill r2r`。它的版本选择/安装行为可能与 GitHub CLI 不同；需要严格固定版本时优先使用 Tag 安装。

## 完全不安装

直接复制 [README 中的提示词](../README.md) 给有权限访问代码仓库的 AI 编码助手。R2R 的方法不依赖 Skill 安装机制；没有代码或 Git 工具的普通聊天无法凭此执行软件更改。

## 安装后怎么使用？

在你的软件**项目目录**打开 Codex/Claude Code 等 Agent，然后说：

```text
Start R2R on this project. Read actual source, create or update R2R.md,
plan the whole product and begin the first authorized safe RUN.
```

后来只需说 **Continue R2R**，需要进行全面整合时说 **Harden with R2R**。你可以随时 STEER。

[中文完整操作指南](use.md) · [目标项目 R2R.md 模板](../skills/r2r/assets/R2R.md)

## 哪些部分确实检查过？

- GitHub 的 [v0.1.0 发布后 Smoke](https://github.com/kingwangking/r2r/actions/runs/39737882456) 检查了 Tag、Release ZIP、SHA-256，以及通过 GitHub CLI 安装指定版本后的 Skill 文件完整性。
- **尚未实测：** Codex/Claude Code 在真实项目中遵循 Start、Continue、Harden 指令的完整行为。这与安装成功是两种不同的证据。

源码版本和 Release 使用不同的引用。`main` 的后续修改不会自动变成 `v0.1.0`，也不会修改已发布 ZIP。
