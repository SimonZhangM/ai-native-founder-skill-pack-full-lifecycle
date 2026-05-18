# AI Native Founder Skill Pack — Full Lifecycle Runtime Edition

> A Codex-ready workflow pack for AI-native founders: **multi Skills + multi Agents + shared support + root AGENTS.md**. It turns the playbook into stage-gated startup execution from Idea → MVP → Launch → Scale.

This pack is intentionally **not** a book summary and not a generic startup advisor. It is a runnable project structure that lets Codex load reusable Skills, spawn focused custom Agents, and follow stable project-level rules.

## Why this edition uses 9 Skills, not 7

The 7-skill version is a good slim profile, but it under-represents the second half of the playbook. The book treats **Launch** and **Scale** as distinct lifecycle stages with their own exit criteria, risks, and operating workflows:

- Launch asks whether the business deserves to grow: repeatable/channel-driven growth, production hardening, security/compliance, product operations, and founder-bottleneck removal.
- Scale asks whether the company can become durable: enterprise readiness, GTM motion, delegation, workflow lock-in, proprietary data loops, and defensible moat.

So this default full-lifecycle edition keeps two dedicated stage Skills active:

```text
launch-readiness
scale-moat-system
```

If you want a minimal starter pack, you can still remove those two runtime Skills and the `scale_operator` agent. But for an OPC / AI-native founder workflow, keeping them is the stronger default.

## Runtime-ready structure

Open Codex from this folder and it can read the active runtime areas immediately:

```text
ai-native-founder-skill-pack-full-lifecycle/
├─ AGENTS.md                         # active project rules for Codex
├─ README.md
├─ MANIFEST.md
│
├─ skills/                           # editable source Skills
├─ agents/                           # editable source custom agents
├─ shared/                           # shared references/templates/scripts
├─ templates/                        # installable AGENTS.md and config template
├─ docs/
├─ examples/
├─ assets/
│
├─ .agents/
│  ├─ skills/                        # Codex-visible runtime Skills
│  │  ├─ founder-stage-diagnosis/
│  │  ├─ idea-validation/
│  │  ├─ customer-discovery/
│  │  ├─ mvp-scope/
│  │  ├─ ai-coding-context/
│  │  ├─ pmf-feedback-loop/
│  │  ├─ founder-bottleneck-audit/
│  │  ├─ launch-readiness/
│  │  └─ scale-moat-system/
│  └─ shared/                        # runtime shared support for Skills
│
└─ .codex/
   ├─ config.toml
   └─ agents/                        # Codex-visible custom agents
      ├─ founder-orchestrator.toml
      ├─ idea-validator.toml
      ├─ mvp-architect.toml
      ├─ launch-operator.toml
      ├─ scale-operator.toml
      └─ reviewer.toml
```

## Layer responsibilities

```text
Current Codex thread = 主控层 / final coordinator
Agents               = 角色层 / specialist operators
Skills               = 方法层 / reusable workflows
Shared               = references, templates, deterministic scripts
AGENTS.md            = project-level rules and safety boundaries
```

## Skills

```text
founder-stage-diagnosis   Diagnose Idea / MVP / Launch / Scale and gate readiness.
idea-validation           Turn a vague idea into a testable hypothesis and adversarial validation plan.
customer-discovery        Design interview targets, questions, probes, and synthesis.
mvp-scope                 Define MVP boundaries and feature-amendment criteria.
ai-coding-context         Generate AGENTS.md / CODEX.md style context, architecture notes, and session logs.
pmf-feedback-loop         Define activation, retention, revenue/referral, false-positive checks, and PMF cadence.
founder-bottleneck-audit  Identify workflows to stop, delegate, automate, or keep with founder judgment.
launch-readiness          Audit PMF evidence, production readiness, technical debt, security/compliance, product ops, and growth.
scale-moat-system         Audit enterprise readiness, GTM system, data flywheel, workflow lock-in, and defensible moat.
```

## Agents

```text
founder_orchestrator  Stage diagnosis, routing, synthesis, final gate decision.
idea_validator        Problem validation, customer discovery, competitor threats, disconfirming evidence.
mvp_architect         MVP scope, architecture context, AI coding session plans, measurement guardrails.
launch_operator       PMF evidence, launch readiness, product ops, growth channels, founder bottlenecks.
scale_operator        Enterprise readiness, GTM system, delegation, data flywheel, workflow lock-in, moat narrative.
reviewer              Adversarial check for missing evidence, false PMF, scope creep, stage mismatch, unsafe actions.
```

## Direct use

From the pack root:

```bash
codex
```

Then ask:

```text
List the AI Native Founder skills and custom agents you can see. Then summarize the AGENTS.md rules you loaded.
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

## Typical prompts

```text
请用 founder_orchestrator 判断我现在处于 Idea / MVP / Launch / Scale 哪个阶段，并给出阶段门结论。
```

```text
请让 idea_validator agent 用 idea-validation 和 customer-discovery skills 处理这个想法，再让 reviewer agent 找反证，最后汇总是否值得进入 MVP。
```

```text
请用 mvp_architect agent 生成 MVP scope、AI coding context、session log 模板。不要写代码，先给我边界和验收标准。
```

```text
请用 launch_operator agent 做 launch-readiness 审计：PMF 证据、技术债、安全合规、产品管理流程、增长渠道和创始人瓶颈。
```

```text
请用 scale_operator agent 做 scale-moat-system 审计：企业级 readiness、GTM、数据飞轮、workflow lock-in 和护城河叙事。
```

## Operating principle

```text
Do not build until evidence justifies it.
Do not scale until operations can survive it.
Do not automate judgment before the judgment is explicit.
```

## Smoke tests

```bash
python shared/scripts/stage_gate_check.py examples/sample-evidence.json
python shared/scripts/pmf_signal_score.py examples/sample-pmf-metrics.json
```

Expected: both scripts print JSON plus a short human-readable summary.
