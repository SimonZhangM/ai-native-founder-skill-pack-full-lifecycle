---
name: no1-mvp-scope
description: "Use when a validated problem needs a narrow MVP scope, explicit non-goals, core user journey, feature gates, activation metric, or scope-creep review."
---

# MVP Scope

Use this skill to define the smallest focused product that tests a validated problem without drifting into feature sprawl.

## Trigger when

- The user asks what to build first.
- The user asks for MVP scope, product requirements, or feature boundaries.
- The user wants to prevent scope creep.
- The user has Idea-stage evidence and is preparing a build session.

## Do not use when

- There is no validated problem or target user.
- The user wants a full roadmap instead of a focused MVP.
- The user asks for code generation before scope is approved.

## Inputs

- Validated problem.
- Target user.
- Evidence from interviews or research.
- Proposed solution.
- Constraints: time, budget, stack, data, security, compliance.

## Workflow

1. Confirm Idea-stage exit criteria. If missing, send the user back to no1-idea-validation or no1-customer-discovery.
2. Define the core user outcome and the single shortest value path.
3. List must-have MVP capabilities.
4. List explicit non-goals.
5. Create feature amendment criteria: what user evidence justifies adding a feature.
6. Define activation, retention, revenue/referral, and false-positive metrics.
7. Produce acceptance criteria for the first build session.
8. Recommend no1-ai-coding-context only after scope is stable.

## Shared resources

- `../../shared/no1/templates/mvp-scope.md`
- `../../shared/no1/references/mvp-build-guardrails.md`

## Output format

```markdown
## MVP Scope
Must do:
- ...
Must not do:
- ...

## Core Journey
...

## Feature Gate
| Feature | Include now? | Evidence required |

## Build Readiness
Ready / Not ready / Review
```

## Guardrails

- Do not include features because they are easy to build.
- Do not broaden the target segment to justify more features.
- Do not use "nice to have" as an MVP requirement.
- Every new feature needs user evidence, safety necessity, or direct activation/retention impact.
