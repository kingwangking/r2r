# The optional R2R Agent Skill

[**r2r/SKILL.md**](r2r/SKILL.md) is one standalone instruction file with YAML frontmatter matching the basic **Agent Skills** format. It contains no code, scripts, binaries, network actions, model keys or mandatory local runtime.

## How to use

- **Agent with Skill support:** make the `skills/r2r` directory available through the agent's documented Skill-loading mechanism, then ask it to “Use R2R” on the actual project. The exact installation/loading steps depend on the host product; **this repository does not auto-install or run anything**.
- **ChatGPT web / other chat agents:** open the file and copy its instructions into an authorized project discussion, or use the shorter [one-card prompt](../quickstart/one-card.md). An external Skill mechanism is not required.
- **Existing Spec workflow:** keep your current spec and planning tooling. R2R guides the execution horizon, validation allocation, steering and quality convergence around that workflow.

## Packaging honesty

The file structure and required metadata are based on the [Agent Skills specification](https://agentskills.io/specification). We checked the text format and basic metadata, **but have not executed an external skills validator or installed it in a host**. That compatibility work remains `NOT_RUN`.

**Current workflow:** after each meaningful execution batch, perform a **synchronous lightweight self-review** in the same agent context. No local multi-agent runtime or async reviewer dispatch is needed. A separate reviewer can be sought sequentially for consequential questions if actually available.

Do not imply the skill creates parallel agents, schedules work or performs independent reviews itself. Those are capabilities of whichever authorized host and tools are actually available.
