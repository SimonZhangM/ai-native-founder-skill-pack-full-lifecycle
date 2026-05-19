---
name: no1-pmf-feedback-loop
description: "Use when a founder has usage, retention, revenue, referral, qualitative pull, or feedback data and needs to assess PMF signals, false positives, and next iteration decisions."
---

# PMF Feedback Loop

Use this skill to design and interpret MVP-stage evidence without mistaking early traction for product-market fit.

## Trigger when

- The user asks whether they have PMF.
- The user has early usage, signups, revenue, or feedback and needs interpretation.
- The user wants activation/retention metrics, D7/D30 targets, Sean Ellis test, or false-positive analysis.
- The user has run multiple iterations and may need pivot diagnostics.

## Do not use when

- The product has not reached real users.
- The user only has interview evidence and no solution usage evidence.
- The user wants to scale immediately from launch spike data.

## Inputs

- Target segment.
- Activation definition.
- Active users and sample size.
- Day 7 and Day 30 retention.
- Paid conversion or revenue.
- Referral or recommendation signal.
- Feedback notes.
- Founder intervention level.

## Workflow

1. Define activation before interpreting numbers.
2. Separate vanity metrics from behavior metrics.
3. Check retention, revenue, referral, and pull signals.
4. Identify false positives: signups without activation, launch spike, revenue without retention, incentive-driven use, founder-pushed engagement.
5. If data is available as JSON, run `python ../../shared/no1/scripts/pmf_signal_score.py <metrics.json>`.
6. Segment results: who is responding differently?
7. After three weak iteration cycles, run pivot diagnostic:
   - Wrong segment?
   - Wrong positioning?
   - Product value gap?
   - Return to Idea stage?
8. Recommend continue, adjust, pivot, or return to validation.

## Shared resources

- `../../shared/no1/templates/pmf-feedback-brief.md`
- `../../shared/no1/scripts/pmf_signal_score.py`
- `../../shared/no1/references/lifecycle-stage-gates.md`

## Output format

```markdown
## PMF Signal
Signal strength: Strong / Promising / Weak / None

## Evidence
- Activation:
- Retention:
- Revenue:
- Referral:
- Pull vs push:

## False Positive Risks
- ...

## Decision
Continue / Adjust / Pivot / Return to Idea
```

## Guardrails

- Never declare PMF from signups alone.
- Never declare PMF from one launch spike.
- Never ignore founder intervention level.
- No single metric confirms PMF; require a pattern across multiple cycles.
