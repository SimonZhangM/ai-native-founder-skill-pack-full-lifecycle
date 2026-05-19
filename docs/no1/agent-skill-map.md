# Agent / Skill Map

## Conceptual map

```text
no1_founder_orchestrator
  -> no1-founder-stage-diagnosis
  -> routes to specialist agents
  -> integrates results

no1_idea_validator
  -> no1-idea-validation
  -> no1-customer-discovery
  -> no1_reviewer for counterarguments

no1_mvp_architect
  -> no1-mvp-scope
  -> no1-ai-coding-context
  -> no1-pmf-feedback-loop

no1_launch_operator
  -> no1-pmf-feedback-loop
  -> no1-launch-readiness
  -> no1-founder-bottleneck-audit

no1_scale_operator
  -> no1-scale-moat-system
  -> no1-founder-bottleneck-audit
  -> no1-launch-readiness, when scale depends on unresolved launch gaps

no1_reviewer
  -> adversarial review across all stages
```

## Skill inventory

| Skill | Job | Typical stage | Output |
|---|---|---|---|
| `no1-founder-stage-diagnosis` | Determine Idea/MVP/Launch/Scale | All | Stage gate result |
| `no1-idea-validation` | Hypothesis and disconfirming evidence | Idea | Validation brief |
| `no1-customer-discovery` | Interview design and synthesis | Idea/MVP | Interview script and synthesis |
| `no1-mvp-scope` | MVP boundaries and feature gates | MVP | MVP scope |
| `no1-ai-coding-context` | AGENTS.md/CODEX.md/session context | MVP/Launch | Coding context and session log |
| `no1-pmf-feedback-loop` | Interpret traction and PMF signal | MVP/Launch | PMF brief |
| `no1-founder-bottleneck-audit` | Remove founder as ops bottleneck | Launch/Scale | Bottleneck map |
| `no1-launch-readiness` | Production and business launch audit | Launch | Launch readiness report |
| `no1-scale-moat-system` | Enterprise, GTM, data flywheel, moat and lock-in | Scale | Scale moat map |

## Recommended agent fan-out

Keep fan-out shallow:

```text
Parent thread
  -> no1_idea_validator
  -> no1_reviewer
Parent integrates.
```

Avoid:

```text
Parent -> agent -> agent -> agent
```

Use `no1_reviewer` late in the flow to challenge optimistic conclusions.
