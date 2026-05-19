# Installation

This repository is distributed as a ready-to-run Codex pack.

The core runtime shape is:

```text
.agents/skills/
.agents/shared/
.codex/agents/
.codex/config.toml
AGENTS.md
```

The full pack also includes user-facing documentation and verification
materials:

```text
assets/
docs/
examples/
MANIFEST.md
README.md
README_CN.md
```

Use the full pack when you want someone to install or inspect the complete
workflow package. Use runtime-only installation when adding the founder workflow
to an existing project that already has its own README, docs, and examples.

## Why root `AGENTS.md` is included

Root `AGENTS.md` is the pack's active project instruction file. It is not a custom agent. It tells Codex the working rules for this repository: keep stage gates, avoid unsafe edits, and preserve the source/runtime mirror relationship.

This runtime distribution uses the root `AGENTS.md` as the project-ready file to
copy into user repositories.

## Full lifecycle default: 9 Skills + 6 Agents

The default runtime profile keeps all four playbook stages first-class:

```text
Idea    -> no1-founder-stage-diagnosis, no1-idea-validation, no1-customer-discovery
MVP     -> no1-mvp-scope, no1-ai-coding-context, no1-pmf-feedback-loop
Launch  -> no1-launch-readiness, no1-founder-bottleneck-audit, no1-pmf-feedback-loop
Scale   -> no1-scale-moat-system, no1-founder-bottleneck-audit, no1-launch-readiness
Review  -> no1_reviewer agent across all stages
```

Runtime inventory:

```text
.agents/skills/
  no1-founder-stage-diagnosis/
  no1-idea-validation/
  no1-customer-discovery/
  no1-mvp-scope/
  no1-ai-coding-context/
  no1-pmf-feedback-loop/
  no1-founder-bottleneck-audit/
  no1-launch-readiness/
  no1-scale-moat-system/

.codex/agents/
  no1-founder-orchestrator.toml
  no1-idea-validator.toml
  no1-mvp-architect.toml
  no1-launch-operator.toml
  no1-scale-operator.toml
  no1_reviewer.toml
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

### ZIP install, recommended

The simplest install path works the same on Windows and macOS:

1. Download the ZIP from GitHub, or use a release ZIP.
2. Extract it.
3. Copy the pack contents into the target project root.
4. Start a new Codex session from the target project root.

If using GitHub's automatic `Download ZIP`, GitHub usually wraps the files in a
top-level directory. Open that directory and copy its contents into the target
project root.

If using a release ZIP that has the pack files directly at the archive root, it
can be extracted directly into the target project directory.

Full install should place these at the target root:

```text
AGENTS.md
.agents/
.codex/
assets/
docs/
examples/
MANIFEST.md
README.md
README_CN.md
```

This may overwrite files with the same names in the target project. Back up or
merge first if needed.

### macOS / Linux command line, optional

Most users do not need this. Use it only if you prefer Terminal and already have
the pack downloaded locally.

From inside the extracted pack directory:

```bash
TARGET="/absolute/path/to/target-project"

mkdir -p "$TARGET"
rsync -av --exclude ".git/" ./ "$TARGET"/
```

Replace `TARGET` with the real target project path.

### Runtime-only install

Use this when the target project only needs Codex-visible runtime files:

```bash
PACK="/absolute/path/to/ai-native-founder-skill-pack"

mkdir -p .agents/skills .agents/shared .codex/agents

cp -R "$PACK/.agents/skills/." .agents/skills/
cp -R "$PACK/.agents/shared/." .agents/shared/
cp -R "$PACK/.codex/agents/." .codex/agents/
cp "$PACK/.codex/config.toml" .codex/config.toml
cp "$PACK/AGENTS.md" AGENTS.md
```

Why copy `shared/`? The skills reference common material through paths like `../../shared/no1/references/lifecycle-stage-gates.md`. If only `skills/` is copied, the skills still work from embedded instructions but lose access to templates, references, and scripts.

## Slim starter profile, optional

Only use this if you deliberately want a smaller starter runtime:

```bash
rm -rf .agents/skills/no1-launch-readiness
rm -rf .agents/skills/no1-scale-moat-system
rm -f .codex/agents/no1-scale-operator.toml
```

This is no longer the default because Launch and Scale are core stages in the playbook.

## Global mode

Global mode is optional. Prefer project-local install unless you intentionally
want this pack available across many Codex projects.

```bash
PACK="/absolute/path/to/ai-native-founder-skill-pack"

mkdir -p ~/.agents/skills ~/.agents/shared ~/.codex/agents

cp -R "$PACK/.agents/skills/." ~/.agents/skills/
cp -R "$PACK/.agents/shared/." ~/.agents/shared/
cp -R "$PACK/.codex/agents/." ~/.codex/agents/
cp "$PACK/.codex/config.toml" ~/.codex/config.toml
```

## Verify

Ask Codex:

```text
List the available AI Native Founder skills and agents you can see. Then summarize the AGENTS.md rules you loaded.
```

Run scripts:

```bash
python .agents/shared/no1/scripts/stage_gate_check.py examples/no1/sample-evidence.json
python .agents/shared/no1/scripts/pmf_signal_score.py examples/no1/sample-pmf-metrics.json
```

## When to restart Codex

Restart or open a new session if newly copied skills, agents, config, or AGENTS.md rules are not visible.
