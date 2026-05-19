# Slim Runtime Profile

Use this profile when you want the runtime tree to match the original 7-skills / 5-agents architecture exactly.

## Keep these skills

```text
no1-founder-stage-diagnosis
no1-idea-validation
no1-customer-discovery
no1-mvp-scope
no1-ai-coding-context
no1-pmf-feedback-loop
no1-founder-bottleneck-audit
```

## Keep these agents

```text
no1-founder-orchestrator.toml
no1-idea-validator.toml
no1-mvp-architect.toml
no1-launch-operator.toml
no1_reviewer.toml
```

## Remove advanced runtime modules

```bash
rm -rf .agents/skills/no1-launch-readiness
rm -rf .agents/skills/no1-scale-moat-system
rm -f .codex/agents/no1-scale-operator.toml
```

The source files can remain under `skills/` and `agents/`; they simply will not be visible to Codex at runtime unless copied back into `.agents/skills/` or `.codex/agents/`.
