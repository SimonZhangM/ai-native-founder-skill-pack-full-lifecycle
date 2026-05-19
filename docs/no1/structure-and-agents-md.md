# Pack Structure and AGENTS.md

## Why root `AGENTS.md` exists

`AGENTS.md` is not a custom agent. It is the durable instruction file Codex reads before work starts. In this pack, the root file tells Codex how to maintain and use the pack itself: keep stage gates, avoid unsafe edits, and preserve source/runtime mirrors.

## Why `templates/AGENTS.md` also exists

The template is what a user copies into their own project when installing the pack. It is close to the root file, but written from the user's project perspective rather than the pack-maintainer perspective.

## Source directories vs runtime directories

```text
skills/               Source Skill definitions.
agents/               Source custom-agent definitions.
shared/               Source references, templates, scripts.

.agents/skills/       Codex-visible runtime Skills.
.agents/shared/       Runtime shared resources used by the Skills.
.codex/agents/        Codex-visible custom agents.
.codex/config.toml    Project-scoped Codex config.
```

Do not rename the runtime Skills folder to `.skills/`. Current Codex repository Skill discovery uses `.agents/skills/`.

## Default full lifecycle profile

The default profile contains nine Skills because it covers all four stages in the playbook:

```text
no1-founder-stage-diagnosis
no1-idea-validation
no1-customer-discovery
no1-mvp-scope
no1-ai-coding-context
no1-pmf-feedback-loop
no1-founder-bottleneck-audit
no1-launch-readiness
no1-scale-moat-system
```

The last two are not generic add-ons. They keep Launch and Scale from being buried inside `shared/references/launch-and-scale-ops.md` where Codex may not trigger them precisely.

## Optional slim profile

For a small starter pack, remove these from runtime:

```text
no1-launch-readiness
no1-scale-moat-system
no1_scale_operator
```

But for an OPC / AI-native founder system, keep the full profile as the default.
