# Install R2R (or just copy one prompt)

R2R's actual product is **instructions plus a small, optional project-state template**. There is no executable package, dedicated CLI, service, subscription or required model.

## Path A — No installation (any conversational agent)

1. Open [README](../README.md) or [the Chinese guide](use.md).
2. Copy the **Start R2R** prompt into a chat with authorized access to your project.
3. The agent should create/update your project's `R2R.md`, then implement the first authorized batch.
4. Later use **Continue R2R** or **Harden this product with R2R**.

This path works only to the extent your assistant can actually read/write code or Git. A chat without repository tools can help plan and maintain text, **not** claim that it built/tested software.

## Path B — Install the portable Agent Skill

Copy the **entire** [`skills/r2r`](../skills/r2r/SKILL.md) directory, preserving `SKILL.md`, `assets/` and `references/`, to the destination for the specific agent.

| Agent | Project-local destination | Personal destination |
| --- | --- | --- |
| OpenAI Codex | `<your-project>/.agents/skills/r2r/` | `~/.codex/skills/r2r/` |
| Claude Code | `<your-project>/.claude/skills/r2r/` | `~/.claude/skills/r2r/` |
| Other Agent Skills hosts | Host-specific skill folder | Host-specific skill folder |

**Expected file at destination:** e.g. `<your-project>/.agents/skills/r2r/SKILL.md`, with `assets/R2R.md` and `references/operating-guide.md` beside it. **Do not copy only `SKILL.md`** if you want its referenced template.

If your existing agent does not discover the skill immediately, follow that host's documented refresh/reload process and explicitly ask it to use the r2r skill. Agent capabilities and permission prompts are host-specific.

**Current source repository is private.** A different user cannot install it via a public GitHub link until the maintainer authorizes public release. Until then, only someone granted access can clone or download the source.

## Path C — Project instructions without native skills

Copy the [three-mode instructions](../skills/r2r/SKILL.md) or the [small start prompt](../README.md) into the project's existing agent instructions, preserving unrelated project governance. R2R is designed to **complement** specs and project AGENTS.md, not overwrite them.

## Next actions

- Start: `Start R2R on this project. Read the real repository, create R2R.md and begin the first safe campaign.`
- Continue: `Continue R2R from the actual repo HEAD and R2R.md. Don't replan from scratch.`
- Harden: `Harden this product with R2R until the agreed readiness tests are evidenced; report missing checks honestly.`

See [the complete usage guide](use.md).

## Sources for host layout (verify in your host before copying)

- [OpenAI Codex examples and project-local skills](https://developers.openai.com/blog/skills-agents-sdk)
- [OpenAI Codex skills](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md)
- [Claude Code Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Agent Skills specification](https://agentskills.io/specification)

**Packaging status:** source format/path documentation has been checked against published documentation. **No actual installation, host execution or external Skill validator has been run**; do not promote this to installation PASS.
