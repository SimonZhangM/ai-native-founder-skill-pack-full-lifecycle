---
name: no1-founder-bottleneck-audit
description: "Use when founder workload, support, sales, reporting, triage, or customer follow-up depends too much on the founder and needs delegation, automation, documentation, or removal."
---

# Founder Bottleneck Audit

Use this skill when a startup is becoming constrained by the founder personally holding too many workflows, decisions, and operational triggers.

## Trigger when

- The user says they are the bottleneck.
- Support, triage, reporting, sprint planning, or customer follow-up depends on the founder.
- The company is moving from MVP to Launch or Launch to Scale.
- The user wants an automation/delegation map.

## Do not use when

- The startup is still in early Idea validation with no recurring operations.
- The user asks only for productivity tips.
- The task requires changing automations or external systems without approval.

## Inputs

- Recurring tasks.
- Decisions the founder handles.
- Support and product feedback flow.
- Reporting cadence.
- Team roles.
- Tools used: CRM, email, docs, project management, analytics, support, calendar.

## Workflow

1. Inventory every recurring task, decision, report, support workflow, and approval routed through the founder.
2. For each item, ask: what happens if the founder is unavailable for one week?
3. Classify each item:
   - Founder-only judgment.
   - Delegate to human.
   - Automate with AI.
   - Document as process.
   - Stop doing.
4. Define triggers, decision rules, output format, escalation path, and review frequency for automation candidates.
5. Produce a 30-day bottleneck removal plan.
6. Flag any operation requiring external system writes or production access.

## Shared resources

- `../../shared/no1/templates/scale-bottleneck-map.md`
- `../../shared/no1/references/launch-and-scale-ops.md`

## Output format

```markdown
## Bottleneck Map
Founder-only:
- ...
Automate:
- ...
Delegate:
- ...
Document:
- ...
Stop:
- ...

## One-week Absence Test
...

## 30-day Systemization Plan
...
```

## Guardrails

- Do not automate judgment until the decision rule is explicit.
- Do not write to CRM, email, calendar, customer systems, or production workflows without explicit approval.
- Do not remove the founder from decisions that still require founder context; codify context first.
