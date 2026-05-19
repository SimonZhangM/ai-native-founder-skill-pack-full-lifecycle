# AGENTS.md - OPC Agent Legion Runtime

This repository root is the active integration runtime for an OPC agent legion. Codex should treat the root as a runnable test workspace for the combined agent/skill system.

## Repository Layers

- `product/`: finished marketplace or sales packages. Do not use it as runtime.
- `no1 agent/`: standalone no1 package. Users can copy its contents into a project root and use it directly.
- Root runtime: the integrated legion test area. Codex reads root `AGENTS.md`, `.agents/`, and `.codex/` from here.

Do not mechanically copy standalone packages into the root without integration. The root runtime needs namespacing, shared routing, and a commander agent.

## Root Runtime Structure

```text
AGENTS.md
.agents/
  skills/
    no1-*/
  shared/
    no1/
.codex/
  agents/
    commander.toml
    no1-*.toml
docs/
  legion-architecture.md
  no1/
examples/
  no1/
assets/
  no1/
```

## Command Model

Use the current Codex thread as the main coordinator. Use `commander` when the request may cross multiple systems or when routing is unclear.

Current subsystems:

- `no1`: Founder Stage-Gate system for startup validation, MVP scope, PMF, launch readiness, founder bottlenecks, scale, and moat.

Future subsystems should use the same namespace pattern:

- Skills: `.agents/skills/no2-*`
- Shared support: `.agents/shared/no2/`
- Agents: `.codex/agents/no2-*.toml`
- Docs/examples/assets: `docs/no2/`, `examples/no2/`, `assets/no2/`

## Routing Rules

- Startup validation, founder workflow, PMF, launch, or scale questions route to `no1-founder-orchestrator` or a `no1-*` specialist.
- Mixed or unclear questions start with `commander`.
- Do not use another subsystem unless the user asks for it or the commander explicitly routes there.
- When subsystems conflict, root `AGENTS.md` wins over subsystem docs.

## Naming Rules

- Every integrated skill must have a namespace prefix such as `no1-`.
- Every integrated custom agent file must have a namespace prefix such as `no1-`.
- Shared files must live under `.agents/shared/<namespace>/`.
- Standalone package directories may use simpler names internally, but the root integrated runtime must stay namespaced.

## Safety Boundaries

Ask for explicit approval before:

- Modifying files outside the requested pack or runtime edits.
- Installing dependencies.
- Editing deployment, CI/CD, database, migration, secret, or `.env` files.
- Running destructive commands.
- Calling production APIs.
- Sending customer communications or creating paid resources.

## Default Response Shape

```markdown
## Route
Subsystem:
Agent / Skill:

## Evidence
...

## Decision
PASS / HOLD / REVIEW

## Risks
...

## Next Smallest Action
...
```

## Verification

For the current no1 subsystem:

```bash
python .agents/shared/no1/scripts/stage_gate_check.py examples/no1/sample-evidence.json
python .agents/shared/no1/scripts/pmf_signal_score.py examples/no1/sample-pmf-metrics.json
```

Also check:

- `.agents/skills/no1-*/SKILL.md` has `name` and `description` frontmatter.
- `.codex/agents/commander.toml` exists.
- `.codex/agents/no1-*.toml` files have `name`, `description`, and `developer_instructions`.
