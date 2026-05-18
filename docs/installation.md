# Installation

This pack supports two shapes:

1. **Source repository shape**: `skills/`, `agents/`, `shared/`, `templates/`, `docs/`, `examples/`, `assets/`.
2. **Runtime shape**: `.agents/skills/`, `.agents/shared/`, `.codex/agents/`, `.codex/config.toml`, and root `AGENTS.md`.

The zip already contains both shapes, so it can be inspected as source and opened directly as a runnable Codex project.

## Why root `AGENTS.md` is included

Root `AGENTS.md` is the pack's active project instruction file. It is not a custom agent. It tells Codex the working rules for this repository: keep stage gates, avoid unsafe edits, and preserve the source/runtime mirror relationship.

`templates/AGENTS.md` remains available because users need a project-ready file to copy into their own repositories.

## Full lifecycle default: 9 Skills + 6 Agents

The default runtime profile keeps all four playbook stages first-class:

```text
Idea    -> founder-stage-diagnosis, idea-validation, customer-discovery
MVP     -> mvp-scope, ai-coding-context, pmf-feedback-loop
Launch  -> launch-readiness, founder-bottleneck-audit, pmf-feedback-loop
Scale   -> scale-moat-system, founder-bottleneck-audit, launch-readiness
Review  -> reviewer agent across all stages
```

Runtime inventory:

```text
.agents/skills/
  founder-stage-diagnosis/
  idea-validation/
  customer-discovery/
  mvp-scope/
  ai-coding-context/
  pmf-feedback-loop/
  founder-bottleneck-audit/
  launch-readiness/
  scale-moat-system/

.codex/agents/
  founder-orchestrator.toml
  idea-validator.toml
  mvp-architect.toml
  launch-operator.toml
  scale-operator.toml
  reviewer.toml
```

## Direct mode: use this pack as-is

The package already contains runtime mirrors:

```text
.agents/skills/
.agents/shared/
.codex/agents/
.codex/config.toml
AGENTS.md
```

Open Codex from the package root and ask:

```text
List the available AI Native Founder skills and custom agents you can see. Then summarize the AGENTS.md rules you loaded.
```

## Install into another project

```bash
mkdir -p .agents .codex
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/skills .agents/skills
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/shared .agents/shared
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/agents .codex/agents
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/templates/AGENTS.md AGENTS.md
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/templates/config.example.toml .codex/config.toml
```

Why copy `shared/`? The skills reference common material through paths like `../../shared/references/lifecycle-stage-gates.md`. If only `skills/` is copied, the skills still work from embedded instructions but lose access to templates, references, and scripts.

## Slim starter profile, optional

Only use this if you deliberately want a smaller starter runtime:

```bash
rm -rf .agents/skills/launch-readiness
rm -rf .agents/skills/scale-moat-system
rm -f .codex/agents/scale-operator.toml
```

This is no longer the default because Launch and Scale are core stages in the playbook.

## Global mode

```bash
mkdir -p ~/.agents ~/.codex
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/skills ~/.agents/skills
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/shared ~/.agents/shared
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/agents ~/.codex/agents
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/templates/AGENTS.md ~/.codex/AGENTS.md
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/templates/config.example.toml ~/.codex/config.toml
```

## Verify

Ask Codex:

```text
List the available AI Native Founder skills and agents you can see. Then summarize the AGENTS.md rules you loaded.
```

Run scripts:

```bash
python .agents/shared/scripts/stage_gate_check.py examples/sample-evidence.json
python .agents/shared/scripts/pmf_signal_score.py examples/sample-pmf-metrics.json
```

## When to restart Codex

Restart or open a new session if newly copied skills, agents, config, or AGENTS.md rules are not visible.
