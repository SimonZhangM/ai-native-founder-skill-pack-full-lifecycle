# AI Native Founder Skill Pack

[中文说明](README_CN.md)

A Codex-ready workflow pack for founders building AI-native startups.

This pack turns startup discussion into structured founder workflows: diagnose
the current stage, identify the evidence gap, choose the right next action, and
only then decide whether to validate, build, launch, automate, or scale.

## What This Pack Is For

AI tools make it easier to ship software, but that also makes it easier to build
the wrong thing faster. This pack helps a founder keep the work stage-gated:

- Idea: prove the problem is real, specific, frequent, and painful.
- MVP: test whether a focused solution creates repeat use, revenue, referral, or
  strong qualitative pull.
- Launch: harden PMF evidence, product operations, reliability, security, and
  growth loops.
- Scale: build enterprise readiness, delegation, GTM systems, data loops,
  workflow lock-in, and defensible moat.

The core rule is:

```text
Do not build until evidence justifies it.
Do not scale until operations can survive it.
Do not automate judgment before the decision rule is explicit.
```

## Who It Is For

This pack is useful for:

- Solo founders and small teams building AI-native products.
- Founders using Codex, Claude Code, or other agentic coding tools.
- Early operators who need repeatable workflows for validation, MVP planning,
  PMF review, launch readiness, and scale preparation.
- Technical founders who want a forcing function against scope creep and
  premature building.
- Non-technical founders who want AI agents to help structure the startup
  process without replacing founder judgment.

It is not meant to be a generic prompt collection, a fundraising guide, or a
substitute for customer conversations.

## Source And Inspiration

This repository is inspired by Anthropic / Claude's official article
[The founder's playbook: Building an AI-native startup](https://claude.com/blog/the-founders-playbook),
published on May 14, 2026.

That playbook reframes the startup lifecycle for AI-native companies across
Idea, MVP, Launch, and Scale. This repository adapts that lifecycle into a
Codex-ready runtime pack: project instructions, Skills, custom Agents, shared
templates, deterministic scripts, and examples.

This is an independent workflow pack. It is not an official Anthropic product.

## Current Repository Structure

This repository is packaged in Codex runtime form:

```text
.
|-- AGENTS.md              # project rules Codex reads for this pack
|-- README.md
|-- README_CN.md
|-- MANIFEST.md
|-- .agents/
|   |-- skills/            # Codex-visible runtime Skills
|   `-- shared/            # shared references, templates, and scripts
|-- .codex/
|   |-- config.toml
|   `-- agents/            # project-scoped Codex custom agents
|-- docs/
|-- examples/
`-- assets/
```

`AGENTS.md` is the durable project instruction file. It is not a custom agent.
It tells Codex how this pack should operate: keep stage gates, separate evidence
from assumptions, protect safety boundaries, and route work through the right
founder workflow.

## How To Use It

Open Codex from the repository root:

```bash
codex
```

Start with the coordinator:

```text
Use founder_orchestrator to diagnose whether this startup is at Idea, MVP,
Launch, or Scale. Separate evidence, assumptions, risks, and the next smallest
action.
```

A good founder intake prompt includes:

```text
Product idea:
Target user and buyer:
Current product state:
Evidence gathered:
Usage, retention, revenue, or referral data:
Current bottleneck:
Constraints:
```

The expected flow is:

```text
Current thread
  -> founder_orchestrator for stage diagnosis and routing
  -> specialist agent or Skill for focused work
  -> reviewer for adversarial challenge when needed
  -> current thread integrates the final decision
```

## Skills

| Skill | Purpose |
|---|---|
| `founder-stage-diagnosis` | Diagnose the evidence-backed stage and gate readiness. |
| `idea-validation` | Convert an idea into testable hypotheses and disconfirming evidence. |
| `customer-discovery` | Design interview targets, questions, probes, and synthesis. |
| `mvp-scope` | Define MVP boundaries, non-goals, and feature gates. |
| `ai-coding-context` | Produce AI coding context, architecture notes, and session logs. |
| `pmf-feedback-loop` | Interpret activation, retention, revenue, referral, and PMF signals. |
| `founder-bottleneck-audit` | Identify work to stop, delegate, automate, or keep founder-led. |
| `launch-readiness` | Audit PMF evidence, production readiness, security, ops, and growth. |
| `scale-moat-system` | Assess enterprise readiness, GTM systems, data loops, lock-in, and moat. |

## Agents

| Agent | Use when |
|---|---|
| `founder_orchestrator` | You need stage diagnosis, routing, or final synthesis. |
| `idea_validator` | You need problem validation, customer discovery, or competitor threats. |
| `mvp_architect` | You need MVP scope, measurement guardrails, or coding-session context. |
| `launch_operator` | You need PMF review, launch readiness, product ops, or growth channels. |
| `scale_operator` | You need enterprise readiness, GTM systems, delegation, or moat analysis. |
| `reviewer` | You need an adversarial check for weak evidence, false PMF, or stage mismatch. |

## Common Prompts

Idea validation:

```text
Use idea_validator to turn this idea into testable hypotheses, identify the
strongest disconfirming evidence, and design a customer discovery script. Then
use reviewer to challenge the result.
```

MVP planning:

```text
Use mvp_architect to define the MVP scope, explicit non-goals, acceptance
criteria, measurement plan, and first AI coding session context. Do not write
code yet.
```

PMF review:

```text
Use pmf-feedback-loop to evaluate these activation, retention, revenue,
referral, and Sean Ellis signals. Call out false positives and missing evidence.
```

Launch readiness:

```text
Use launch_operator to audit PMF evidence, production readiness, technical debt,
security/compliance, product operations, growth channels, and founder
bottlenecks. Return PASS, HOLD, or REVIEW.
```

Scale and moat:

```text
Use scale_operator to audit enterprise readiness, GTM systems, delegation,
workflow lock-in, proprietary data loops, and defensible moat. Use reviewer to
challenge the moat narrative.
```

## Install Into Another Project

Copy the runtime pack into the target repository:

```bash
mkdir -p .agents .codex
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/.agents/skills .agents/skills
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/.agents/shared .agents/shared
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/.codex/agents .codex/agents
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/.codex/config.toml .codex/config.toml
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/AGENTS.md AGENTS.md
```

Open a new Codex session from the target project after copying so the project
rules, Skills, and Agents are visible.

## Verify

Ask Codex:

```text
List the AI Native Founder skills and custom agents you can see. Then summarize
the AGENTS.md rules you loaded.
```

Run the deterministic helper scripts:

```bash
python .agents/shared/scripts/stage_gate_check.py examples/sample-evidence.json
python .agents/shared/scripts/pmf_signal_score.py examples/sample-pmf-metrics.json
```

Expected result: both commands print structured output and a short summary.

## Documentation

- `docs/agent-skill-map.md` explains how agents and skills fit together.
- `docs/design-principles.md` documents the operating principles behind the pack.
- `docs/installation.md` covers installation shapes and runtime details.
- `docs/usage-examples.md` provides example prompts for common founder workflows.
- `examples/` contains sample stage outputs and JSON inputs for the helper scripts.
