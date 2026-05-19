# Skill Selection Rationale

## Decision

Keep `no1-launch-readiness` and `no1-scale-moat-system` in the default runtime profile.

## Why they stay

The pack is meant to operationalize the full AI-native founder lifecycle, not only the early discovery/MVP loop. The playbook is organized around four stages:

```text
Idea -> MVP -> Launch -> Scale
```

A 7-skill profile covers Idea and MVP well, but Launch and Scale become too compressed:

- `no1-pmf-feedback-loop` can evaluate traction, but it does not fully cover production readiness, technical debt, security/compliance, product management processes, growth-channel economics, and launch gate sequencing.
- `no1-founder-bottleneck-audit` can map founder dependency, but it does not fully cover enterprise readiness, GTM operating system, data flywheel, workflow lock-in, and moat narrative.

Therefore:

```text
no1-launch-readiness    = first-class workflow for turning MVP traction into a launchable business.
no1-scale-moat-system   = first-class workflow for turning a launched product into a defensible company.
```

## Trigger precision

Keeping them as separate Skills improves trigger accuracy:

- User says “上线前检�?/ production readiness / launch readiness�?-> `no1-launch-readiness` should trigger.
- User says “scale / moat / GTM / enterprise readiness / workflow lock-in�?-> `no1-scale-moat-system` should trigger.

If these live only as references, Codex may keep using a broader Skill and miss the stage-specific checklist.

## Scope boundary

They should stay narrow:

- `no1-launch-readiness` should not redo Idea validation or write deployment code.
- `no1-scale-moat-system` should not claim an AI feature is a moat without workflow depth, integration depth, proprietary data loops, or domain knowledge codification.

## Optional slim profile

The 7-skill version remains useful as an onboarding profile. It should be documented as optional, not as the default for this full pack.
