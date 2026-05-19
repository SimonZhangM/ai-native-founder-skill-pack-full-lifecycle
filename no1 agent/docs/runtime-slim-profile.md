# Slim Runtime Profile

Use this profile when you want the runtime tree to match the original 7-skills / 5-agents architecture exactly.

## Keep these skills

```text
founder-stage-diagnosis
idea-validation
customer-discovery
mvp-scope
ai-coding-context
pmf-feedback-loop
founder-bottleneck-audit
```

## Keep these agents

```text
founder-orchestrator.toml
idea-validator.toml
mvp-architect.toml
launch-operator.toml
reviewer.toml
```

## Remove advanced runtime modules

```bash
rm -rf .agents/skills/launch-readiness
rm -rf .agents/skills/scale-moat-system
rm -f .codex/agents/scale-operator.toml
```

The source files can remain under `skills/` and `agents/`; they simply will not be visible to Codex at runtime unless copied back into `.agents/skills/` or `.codex/agents/`.
