# MANIFEST — AI Native Founder Skill Pack

This manifest describes the current runtime distribution. It does not include
separate source mirrors such as `skills/`, `agents/`, `shared/`, or
`templates/`; the Codex-visible runtime files are the canonical package files.

## Runtime profile

- Skills: 9
- Agents: 6
- Root `AGENTS.md`: yes
- Runtime shared support: yes
- Helper scripts: yes
- Docs/examples/assets: yes

## Runtime files

- `AGENTS.md`
- `.agents/README.md`
- `.agents/skills/*/SKILL.md`
- `.agents/skills/*/examples/example-prompts.md`
- `.agents/shared/references/*.md`
- `.agents/shared/templates/*.md`
- `.agents/shared/scripts/stage_gate_check.py`
- `.agents/shared/scripts/pmf_signal_score.py`
- `.codex/README.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`

## Documentation and examples

- `README.md`
- `README_CN.md`
- `MANIFEST.md`
- `docs/agent-skill-map.md`
- `docs/architecture-map.md`
- `docs/design-principles.md`
- `docs/installation.md`
- `docs/runtime-slim-profile.md`
- `docs/skill-selection-rationale.md`
- `docs/structure-and-agents-md.md`
- `docs/usage-examples.md`
- `examples/example-prompts.md`
- `examples/idea-stage-example.md`
- `examples/mvp-stage-example.md`
- `examples/launch-stage-example.md`
- `examples/scale-stage-example.md`
- `examples/sample-evidence.json`
- `examples/sample-pmf-metrics.json`
- `assets/architecture-map.svg`
- `assets/stage-gates.svg`

## Commercial packaging note

For a marketplace package, do not automatically include every file in this
repository. See `docs/promptbase-packaging.md` for the recommended PromptBase
delivery shape and exclusion list.
