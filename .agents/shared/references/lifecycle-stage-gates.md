# Lifecycle Stage Gates

Use stage gates to keep execution from outrunning evidence.

## Idea stage

**Core question:** Is this worth building?

A project is in Idea stage when the founder is still trying to prove that a specific problem exists for a specific person and that the proposed solution addresses the actual problem discovered through validation.

### Exit criteria

Advance to MVP only when the founder can answer yes to all of these:

1. The problem is real, specific, and frequent enough to build around.
2. The target user can be named precisely, including job/persona, context, frequency, severity, and current workaround.
3. The solution addresses the problem revealed by validation, not just the original assumption.
4. There is enough qualitative evidence from real conversations to make building a reasoned decision rather than an act of faith.
5. The strongest disconfirming evidence has been actively sought and documented.

### Failure modes

- Mistaking a prototype for evidence.
- Asking AI to confirm what the founder already believes.
- Building before understanding.
- Scaling execution before validating the problem.

## MVP stage

**Core question:** What exactly should we build first?

A project is in MVP stage when the problem has been validated and the team is now testing whether a small, focused solution creates value for a real, identifiable group of users.

### Exit criteria

Advance to Launch only when there is genuine evidence of product-market fit:

1. A specific user group returns to the product, pays for it, or recommends it.
2. The team has activation, retention, revenue, and referral benchmarks defined before interpreting traction.
3. Day 7 and Day 30 behavior has been observed or explicitly planned.
4. False positives have been identified: signups without activation, revenue without retention, launch spikes without repeat usage.
5. Architecture context, scope boundaries, and session logs exist so AI-generated work does not drift.
6. Security has been reviewed before real users touch the system.

### Failure modes

- False PMF from launch spikes.
- Scope creep because features are easy to generate.
- Agentic technical debt from missing specs and architecture context.
- Insecure AI-generated code shipped to real users.

## Launch stage

**Core question:** Can the product become a repeatable and safe business?

A project is in Launch stage when the product has early traction and the founder must turn it into a production-ready, growth-ready, and operations-ready company.

### Exit criteria

Advance to Scale only when:

1. Growth is repeatable and channel-driven, with defensible CAC, LTV, and payback period assumptions.
2. The product can handle production workloads with hardened infrastructure, reliability, security, and compliance.
3. Operations run without founder bottlenecks; support, triage, sprint planning, reporting, and feedback loops are systematized.

### Failure modes

- Technical debt becomes structural debt.
- Founder stays in every operational loop.
- Security and compliance are treated as optional.
- Expansion into a new market before the original PMF is stable.

## Scale stage

**Core question:** Is this now a sustainable company, not just a successful product?

A project is in Scale stage when it has systematic growth and must mature into an organization that can withstand enterprise, investor, regulator, and acquirer scrutiny.

### Threshold event

Scale is not exited by a single milestone. The company must show that:

1. Growth is systematic and auditable.
2. Governance, compliance, financial controls, and enterprise support are mature.
3. Day-to-day operations can run without the founder directly driving them.
4. The company can answer: if a well-funded incumbent copied the product today, why would users stay?

### Failure modes

- Delegating too much without codified judgment.
- Holding on too long and becoming the bottleneck.
- Lack of enterprise-grade documentation, support, SLAs, and observability.
- No dedicated GTM motion beyond founder-led selling.
- Weak moat: no accumulated domain depth, proprietary workflow context, data flywheel, or integration lock-in.

## Default stage gate output

```markdown
## Stage Gate Result

Current stage: Idea / MVP / Launch / Scale
Confidence: High / Medium / Low
Evidence observed:
- ...
Missing evidence:
- ...
Risks:
- ...
Decision: PASS / HOLD / REVIEW
Next smallest action:
1. ...
```
