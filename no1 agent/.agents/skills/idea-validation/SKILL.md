---
name: idea-validation
description: "把创业想法改写成可测试假设，并寻找反证、竞品威胁和 problem-solution fit 证据；trigger: idea validation, startup idea, 反证, problem hypothesis, 是否值得做。不构建产品。"
---

# Idea Validation

Use this skill to pressure-test an AI-native startup idea before building.

## Trigger when

- The user has a startup idea and asks whether it is worth building.
- The user wants problem-solution fit validation.
- The user asks for market research, competitor analysis, TAM/SAM/SOM assumptions, or devil's advocate analysis.
- The user is tempted to build immediately without evidence.

## Do not use when

- The problem has already been validated and the user needs MVP scope.
- The user is asking for coding implementation.
- The user only wants generic brainstorming without a go/no-go decision.

## Inputs

- Raw idea.
- Suspected target user.
- Problem statement.
- Current alternatives or workarounds.
- Known competitors.
- Any interviews, market evidence, or domain experience.

## Workflow

1. Convert the idea into a testable hypothesis:
   - Persona.
   - Problem.
   - Frequency.
   - Severity.
   - Current workaround.
   - Why alternatives fail.
2. Separate observations from testable claims.
3. Create an assumptions table: user, buyer, workflow, willingness to pay, data/integration constraints, timing.
4. Run adversarial validation:
   - Why might this not be a real problem?
   - Why might existing solutions be good enough?
   - Why might the buyer not care?
   - Why might users say yes but not adopt?
5. Map competitor tiers: direct, indirect, adjacent, current workaround, potential acquirer.
6. Design the next validation action: interview, desk research, landing page, concierge test, or lightweight prototype only if evidence supports it.
7. Produce a stage gate conclusion.

## Shared resources

- `../../shared/references/validation-and-research.md`
- `../../shared/templates/idea-stage-brief.md`
- `../../shared/templates/founder-intake.md`

## Output format

```markdown
## Testable Hypothesis
...

## Assumption Map
| Assumption | Evidence | Risk | Test |

## Disconfirming Evidence
- ...

## Competitor / Substitute Threats
- ...

## Validation Plan
1. ...

## Gate Decision
PASS / HOLD / REVIEW
```

## Guardrails

- Do not treat the existence of a prototype as validation.
- Do not inflate market size before the user and problem are specific.
- Do not ask users future-facing questions like "would you use this?" as primary evidence.
- Always include a skeptical case against the idea.
