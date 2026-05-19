# Agent / Skill Map

## Conceptual map

```text
founder_orchestrator
  -> founder-stage-diagnosis
  -> routes to specialist agents
  -> integrates results

idea_validator
  -> idea-validation
  -> customer-discovery
  -> reviewer for counterarguments

mvp_architect
  -> mvp-scope
  -> ai-coding-context
  -> pmf-feedback-loop

launch_operator
  -> pmf-feedback-loop
  -> launch-readiness
  -> founder-bottleneck-audit

scale_operator
  -> scale-moat-system
  -> founder-bottleneck-audit
  -> launch-readiness, when scale depends on unresolved launch gaps

reviewer
  -> adversarial review across all stages
```

## Skill inventory

| Skill | Job | Typical stage | Output |
|---|---|---|---|
| `founder-stage-diagnosis` | Determine Idea/MVP/Launch/Scale | All | Stage gate result |
| `idea-validation` | Hypothesis and disconfirming evidence | Idea | Validation brief |
| `customer-discovery` | Interview design and synthesis | Idea/MVP | Interview script and synthesis |
| `mvp-scope` | MVP boundaries and feature gates | MVP | MVP scope |
| `ai-coding-context` | AGENTS.md/CODEX.md/session context | MVP/Launch | Coding context and session log |
| `pmf-feedback-loop` | Interpret traction and PMF signal | MVP/Launch | PMF brief |
| `founder-bottleneck-audit` | Remove founder as ops bottleneck | Launch/Scale | Bottleneck map |
| `launch-readiness` | Production and business launch audit | Launch | Launch readiness report |
| `scale-moat-system` | Enterprise, GTM, data flywheel, moat and lock-in | Scale | Scale moat map |

## Recommended agent fan-out

Keep fan-out shallow:

```text
Parent thread
  -> idea_validator
  -> reviewer
Parent integrates.
```

Avoid:

```text
Parent -> agent -> agent -> agent
```

Use `reviewer` late in the flow to challenge optimistic conclusions.
