---
name: customer-discovery
description: "设计客户发现访谈：访谈对象、非诱导问题、追问、访谈后分析和批量综合；trigger: customer discovery, user interview, 用户访谈, 访谈脚本, outreach。不做销售话术伪验证。"
---

# Customer Discovery

Use this skill to plan, run, and synthesize real human conversations for startup validation.

## Trigger when

- The user asks who to interview, what to ask, or how to analyze interviews.
- The user wants a customer discovery script or interview plan.
- The user has interview notes and needs synthesis.
- The user wants outreach structure for discovery interviews.

## Do not use when

- The user wants a sales pitch instead of discovery.
- The user asks for a survey when qualitative learning is still required.
- The user is asking for feature implementation.

## Inputs

- Hypothesis.
- Target persona or segment.
- Number of interviews planned/completed.
- Existing notes or transcripts, if any.
- Constraints: geography, industry, role, company size, regulated context.

## Workflow

1. Define the interview target profile precisely.
2. Identify who not to interview because they are too far from the problem.
3. Draft past-behavior questions in a logical order.
4. Remove leading, future-facing, overly broad, or socially desirable questions.
5. Add follow-up probes for vague answers or deflections.
6. If multiple personas exist, create separate question sets.
7. After interviews, synthesize support, challenge, surprises, repeated language, and segment differences.
8. After every five interviews, recommend whether to continue, narrow segment, pivot, or prototype.

## Shared resources

- `../../shared/templates/customer-discovery-script.md`
- `../../shared/references/validation-and-research.md`

## Output format

```markdown
## Interview Target Profile
...

## Interview Script
...

## Follow-up Probes
...

## Post-interview Debrief Template
...

## Batch Synthesis Plan
...
```

## Guardrails

- Ask about what people did, not what they think they would do.
- Do not count compliments as evidence.
- Do not combine buyer and user interviews unless their incentives are the same.
- If all evidence supports the hypothesis, explicitly check for confirmation bias.
