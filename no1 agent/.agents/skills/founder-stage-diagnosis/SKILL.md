---
name: founder-stage-diagnosis
description: "判断 AI-native startup 当前处于 Idea, MVP, Launch, or Scale；用于阶段诊断、stage gate、是否该 build/launch/scale、创业阶段判断。不写代码，不修改项目。"
---

# Founder Stage Diagnosis

Use this skill to classify the startup's current lifecycle stage and decide whether it can pass the relevant stage gate.

## Trigger when

- The user asks: "我现在在哪个阶段？", "should we build?", "should we launch?", "should we scale?"
- The task involves Idea / MVP / Launch / Scale diagnosis.
- The user asks for stage gates, go/no-go decisions, or evidence readiness.
- The user wants to know which agent or skill should run next.

## Do not use when

- The user only asks for a normal bug fix, copywriting task, UI tweak, or generic project management answer.
- There is no startup, product, market, MVP, launch, PMF, or scale context.
- The user wants code changes directly; route to planning first.

## Inputs

Ask for or infer:

- One-sentence idea or product.
- Target user and buyer.
- Evidence gathered: interviews, usage, retention, revenue, referrals.
- Current product state: no product, prototype, MVP, production product, scaling product.
- Operations state: founder-led or systematized.
- Constraints: time, budget, team, technical stack, regulation.

## Workflow

1. Identify the claimed stage and the evidence-backed stage. Trust evidence over the founder's claimed stage.
2. Classify the work using this ladder:
   - Idea: proving a real problem exists.
   - MVP: testing whether a focused solution creates value.
   - Launch: turning traction into a production-ready, repeatable business.
   - Scale: making growth, operations, GTM, and moat sustainable without founder day-to-day control.
3. Run the relevant gate using `../../shared/references/lifecycle-stage-gates.md`.
4. If a JSON evidence file exists, run `python ../../shared/scripts/stage_gate_check.py <file>`.
5. Identify missing evidence and the next smallest action.
6. Recommend the next skill or agent.

## Output format

```markdown
## Stage Diagnosis
Current evidence-backed stage:
Claimed stage:
Confidence:

## Evidence
- Supporting evidence:
- Contradicting evidence:

## Gate Result
Decision: PASS / HOLD / REVIEW
Missing evidence:
- ...
Risks:
- ...

## Next Smallest Action
1. ...

## Recommended Skill / Agent
- ...
```

## Guardrails

- Never tell the user to build if the Idea gate is missing target user, frequency, severity, workaround, and real conversations.
- Never call early traffic or signups PMF without retention, revenue, referral, or strong pull evidence.
- Never advance to Launch without production readiness and security/compliance review.
- Never advance to Scale if operations still depend on the founder for support, triage, reporting, or pipeline movement.
