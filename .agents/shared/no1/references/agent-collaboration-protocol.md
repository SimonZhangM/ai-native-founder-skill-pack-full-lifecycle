# Agent Collaboration Protocol

## Parent thread is the coordinator

The current Codex thread remains the main coordinator. Specialist agents should be spawned only when their role adds leverage.

## Recommended sequence

### Idea stage

1. `no1_founder_orchestrator`: determine stage and task split.
2. `no1_idea_validator`: sharpen hypothesis, discovery plan, competitor risk.
3. `no1_reviewer`: challenge assumptions and find disconfirming evidence.
4. Parent thread: integrate into go/no-go stage gate.

### MVP stage

1. `no1_founder_orchestrator`: verify Idea exit criteria.
2. `no1_mvp_architect`: create MVP scope, architecture context, session plan.
3. `no1_reviewer`: inspect scope creep, missing tests, security and measurement gaps.
4. Parent thread: approve next build session or hold.

### Launch stage

1. `no1_launch_operator`: technical debt, product ops, feedback loop, security/compliance, growth channels.
2. `no1_reviewer`: identify premature expansion and false PMF.
3. Parent thread: prioritize remediation and owner map.

### Scale stage

1. `no1_scale_operator`: enterprise readiness, GTM system, moat, workflow lock-in.
2. `no1_reviewer`: test defensibility and operational maturity claims.
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
