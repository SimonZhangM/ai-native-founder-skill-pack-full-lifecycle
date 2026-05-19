# MANIFEST - OPC Agent Legion Runtime

This manifest describes the integrated root runtime, not the standalone `no1 agent/` package and not the finished outputs in `product/`.

## Top-Level Parts

- `product/`: finished marketplace and sales packages.
- `no1 agent/`: standalone no1 package, directly installable by copying its contents into a user project.
- Root runtime: integrated test runtime for the combined agent legion.

## Root Runtime Files

- `AGENTS.md`
- `README.md`
- `README_CN.md`
- `MANIFEST.md`
- `.agents/README.md`
- `.agents/skills/no1-*/SKILL.md`
- `.agents/skills/no1-*/examples/example-prompts.md`
- `.agents/shared/no1/references/*.md`
- `.agents/shared/no1/templates/*.md`
- `.agents/shared/no1/scripts/stage_gate_check.py`
- `.agents/shared/no1/scripts/pmf_signal_score.py`
- `.codex/README.md`
- `.codex/config.toml`
- `.codex/agents/commander.toml`
- `.codex/agents/no1-*.toml`
- `docs/legion-architecture.md`
- `docs/no1/*.md`
- `examples/no1/*.md`
- `examples/no1/*.json`
- `assets/no1/*.svg`

## Current Counts

- Integrated subsystems: 1
- Commander agents: 1
- no1 skills: 9
- no1 specialist agents: 6
- no1 helper scripts: 2

## Runtime Verification

```bash
python .agents/shared/no1/scripts/stage_gate_check.py examples/no1/sample-evidence.json
python .agents/shared/no1/scripts/pmf_signal_score.py examples/no1/sample-pmf-metrics.json
```
