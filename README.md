# OPC Agent Legion Runtime

This repository root is the integrated test runtime for an expanding agent legion.

The directory is intentionally split into two runtime-facing parts:

```text
no1 agent/    # standalone package users can copy directly into a project
root runtime  # integrated legion runtime used for local testing
```

Codex recognizes the root runtime because `AGENTS.md`, `.agents/`, and `.codex/` are directly under this repository root.

## Current Integrated Subsystem

`no1` is the Founder Stage-Gate system:

- 9 namespaced skills under `.agents/skills/no1-*`
- 6 namespaced agents under `.codex/agents/no1-*.toml`
- shared references, templates, and scripts under `.agents/shared/no1/`
- examples under `examples/no1/`
- docs under `docs/no1/`

The root also contains:

- `.codex/agents/commander.toml`: top-level routing agent
- `AGENTS.md`: root-level governance and routing rules
- `docs/legion-architecture.md`: integration architecture

## Why This Structure Exists

Standalone packages such as `no1 agent/` are easy for users to install: they copy that folder's contents into their project root.

The root runtime is different. It is the combined legion workspace. Multiple standalone systems cannot simply be pasted together because their agents, skills, shared templates, scripts, docs, and examples can collide. The root runtime therefore uses namespaces such as `no1-`, `no2-`, and `no3-`.

## Add The Next Subsystem

When creating `no2`:

1. Build it independently in `no2 agent/`.
2. Keep `no2 agent/` directly installable for users.
3. Integrate a namespaced copy into the root runtime:
   - `.agents/skills/no2-*`
   - `.agents/shared/no2/`
   - `.codex/agents/no2-*.toml`
   - `docs/no2/`
   - `examples/no2/`
   - `assets/no2/`
4. Update root `AGENTS.md`, `.codex/agents/commander.toml`, and `docs/legion-architecture.md`.

## Verify Current Runtime

```bash
python .agents/shared/no1/scripts/stage_gate_check.py examples/no1/sample-evidence.json
python .agents/shared/no1/scripts/pmf_signal_score.py examples/no1/sample-pmf-metrics.json
```

Expected result: both commands print structured output.

## Copy For Testing

When testing the integrated legion in another project, copy the root runtime files while excluding development and sales folders:

```text
include:
  AGENTS.md
  .agents/
  .codex/
  docs/
  examples/
  assets/
  README.md
  MANIFEST.md

exclude:
  .git/
  no1 agent/
  no2 agent/
  no3 agent/
```
