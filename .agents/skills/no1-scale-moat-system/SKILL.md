---
name: no1-scale-moat-system
description: "Use when a launched product needs scale readiness, enterprise gaps, GTM systems, data flywheel, workflow lock-in, integration depth, founder dependency, or moat review."
---

# Scale Moat System

Use this skill when a startup is beyond launch and needs to become a scalable, defensible business.

## Trigger when

- The user asks how to scale.
- Growth is flattening, CAC is rising, or pipeline moves only when the founder is involved.
- The user needs enterprise readiness, support infrastructure, GTM system, moat analysis, or workflow lock-in audit.
- The user asks what makes the product defensible.

## Do not use when

- The product has not passed Launch readiness.
- The user only has early traction and no repeatable channel.
- The user wants generic strategy without operational evidence.

## Inputs

- Growth data and channels.
- Enterprise buyer requirements.
- Support and incident process.
- Documentation status.
- Integrations and API surface.
- User behavior data.
- Customer workflows and automations.
- Founder-only responsibilities.

## Workflow

1. Verify Launch exit criteria: repeatable growth, production readiness, operations without founder bottlenecks.
2. Run enterprise readiness gap analysis: docs, SLAs, support playbooks, incident response, observability, security/compliance.
3. Build GTM system map: segmentation, messaging, sales playbook, CRM, pipeline reporting, analyst/investor narrative.
4. Audit founder dependency in GTM and enterprise deals.
5. Map domain expertise moat: edge cases, workflow logic, tests, prompt constraints, integrations.
6. Map data flywheel: behavioral signals, improvement loop, privacy/compliance constraints.
7. Map workflow lock-in: integrations, automations, team workflows, switching cost.
8. Produce a defensibility narrative and 90-day scale plan.

## Shared resources

- `../../shared/no1/templates/scale-moat-map.md`
- `../../shared/no1/templates/scale-bottleneck-map.md`
- `../../shared/no1/references/launch-and-scale-ops.md`

## Output format

```markdown
## Scale Readiness
Decision: PASS / HOLD / REVIEW

## Enterprise Gap Analysis
...

## GTM System
...

## Moat Map
- Domain expertise:
- Data flywheel:
- Workflow lock-in:
- Integrations:

## 90-day Scale Plan
1. ...
```

## Guardrails

- Do not call a product defensible just because it uses AI.
- Do not treat growth as systematic if pipeline depends on founder activity.
- Do not automate high-stakes customer or compliance workflows without explicit decision rules and human escalation.
- Do not claim enterprise readiness without docs, support, incident response, and security/compliance posture.
