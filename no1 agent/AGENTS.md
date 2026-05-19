# AGENTS.md — AI Native Founder Skill Pack Rules

This repository is an AI Native Founder Skill Pack. Treat it as a reusable workflow pack, not as a normal application codebase.

## What this file is

`AGENTS.md` is not a custom agent. It is the durable project instruction file Codex reads before work starts. It defines the stable rules, safety boundaries, stage gates, and expected response shape for this pack.

## Core operating rule

Do not build until the evidence justifies it. Do not scale until operations can survive it. Do not automate judgment before the decision rule is explicit.

## What each layer does

- `skills/`: editable source definitions for reusable workflows.
- `agents/`: editable source definitions for recommended Codex custom agents.
- `shared/`: common references, templates, and deterministic scripts used by skills.
- `templates/`: files users can copy into their own projects.
- `.agents/skills/`: runtime mirror for Codex skill discovery in this pack.
- `.agents/shared/`: runtime shared support so Skills can resolve references/templates/scripts.
- `.codex/agents/`: runtime mirror for project-scoped Codex custom agents.
- `.codex/config.toml`: runtime project-scoped Codex configuration.

When editing this pack, update the source files first, then mirror changes into `.agents/` and `.codex/` so the pack remains directly runnable.

## Stage gates

Always identify the evidence-backed stage before planning work:

1. Idea: prove the problem is real, specific, frequent, and painful enough.
2. MVP: test whether a focused solution creates repeat use, revenue, referral, or strong qualitative pull.
3. Launch: harden product, technical debt, security/compliance, growth, and operations.
4. Scale: build enterprise readiness, delegation, GTM systems, data flywheel, workflow lock-in, and defensible moat.

## Runtime Skills

The default runtime Skill set is the full lifecycle profile:

- `founder-stage-diagnosis`
- `idea-validation`
- `customer-discovery`
- `mvp-scope`
- `ai-coding-context`
- `pmf-feedback-loop`
- `founder-bottleneck-audit`
- `launch-readiness`
- `scale-moat-system`

Do not reduce the runtime to seven Skills unless the user explicitly wants a slim starter profile. Launch and Scale are distinct playbook stages and should remain first-class workflows by default.

Keep each `SKILL.md` short: trigger conditions, non-trigger cases, input requirements, workflow, output shape, references, and prohibitions.

## Runtime Agents

Use the current Codex thread as the main coordinator. Spawn specialist agents only when useful:

- `founder_orchestrator`: stage diagnosis, task routing, and synthesis.
- `idea_validator`: problem validation, customer discovery, competitor threats, and disconfirming evidence.
- `mvp_architect`: MVP scope, architecture context, AI coding session plans, and measurement guardrails.
- `launch_operator`: PMF evidence, launch readiness, product ops, founder bottlenecks, and repeatable growth.
- `scale_operator`: enterprise readiness, GTM system, delegation, data flywheel, workflow lock-in, and moat narrative.
- `reviewer`: adversarial review, stage mismatch, false PMF, scope creep, and missing evidence.

Keep subagent fan-out shallow. Do not build recursive agent chains unless the user explicitly asks for it.

## Safety boundaries

Ask for explicit approval before:

- Modifying source code or project files outside the requested pack edits.
- Installing dependencies.
- Editing config, CI/CD, deployment files, migrations, secrets, `.env`, or databases.
- Running destructive commands.
- Calling production APIs.
- Sending email, CRM updates, customer invites, or support messages.
- Creating paid resources or external automations.

Require backup or reversible state before database, deployment, CI/CD, or bulk-data changes.

## Default response shape for founder-pack work

```markdown
## Stage
...

## Evidence
...

## Decision
PASS / HOLD / REVIEW

## Risks
...

## Next Smallest Action
...

## Approval Needed
Yes / No
```

## Verification

When validating this pack, check:

- Every runtime Skill under `.agents/skills/*/SKILL.md` has `name` and `description` frontmatter.
- Every runtime agent under `.codex/agents/*.toml` has `name`, `description`, and `developer_instructions`.
- `python shared/scripts/stage_gate_check.py examples/sample-evidence.json` runs.
- `python shared/scripts/pmf_signal_score.py examples/sample-pmf-metrics.json` runs.

## Maintenance rule

Keep `skills/` and `.agents/skills/` in sync. Keep `agents/` and `.codex/agents/` in sync. Keep `shared/` and `.agents/shared/` in sync. Keep `templates/AGENTS.md` aligned with this file, while remembering that root `AGENTS.md` is active for this pack and `templates/AGENTS.md` is installable for user projects.
