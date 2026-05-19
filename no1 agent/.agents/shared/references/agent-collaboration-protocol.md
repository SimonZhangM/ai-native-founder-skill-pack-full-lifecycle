# Agent Collaboration Protocol

## Parent thread is the coordinator

The current Codex thread remains the main coordinator. Specialist agents should be spawned only when their role adds leverage.

## Recommended sequence

### Idea stage

1. `founder_orchestrator`: determine stage and task split.
2. `idea_validator`: sharpen hypothesis, discovery plan, competitor risk.
3. `reviewer`: challenge assumptions and find disconfirming evidence.
4. Parent thread: integrate into go/no-go stage gate.

### MVP stage

1. `founder_orchestrator`: verify Idea exit criteria.
2. `mvp_architect`: create MVP scope, architecture context, session plan.
3. `reviewer`: inspect scope creep, missing tests, security and measurement gaps.
4. Parent thread: approve next build session or hold.

### Launch stage

1. `launch_operator`: technical debt, product ops, feedback loop, security/compliance, growth channels.
2. `reviewer`: identify premature expansion and false PMF.
3. Parent thread: prioritize remediation and owner map.

### Scale stage

1. `scale_operator`: enterprise readiness, GTM system, moat, workflow lock-in.
2. `reviewer`: test defensibility and operational maturity claims.
3. Parent thread: produce scale operating roadmap.

## Handoff format

Every agent should return:

```markdown
## Agent Result
Agent: ...
Task: ...
Evidence used:
- ...
Findings:
- ...
Risks:
- ...
Recommended next action:
- ...
Open questions:
- ...
```

## Safety

Agents should avoid writes by default. If a write is necessary, they should ask the parent thread to request explicit user approval.
