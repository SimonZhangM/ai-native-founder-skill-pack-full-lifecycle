---
name: launch-readiness
description: "Launch 阶段审计：PMF 证据、技术债、安全合规、生产可靠性、产品管理流程、增长渠道和创始人瓶颈；trigger: launch readiness, 上线前检查, production readiness。"
---

# Launch Readiness

Use this skill when a startup has MVP traction and needs to know whether it is ready to launch, grow, or enter production with real users.

## Trigger when

- The user asks if they are ready to launch.
- The user has MVP traction and wants to harden production readiness.
- The user asks for technical debt, security, compliance, product ops, or growth channel audit.
- The user wants a launch-readiness report.

## Do not use when

- The product has not reached MVP usage yet.
- The user only needs Idea validation or MVP scope.
- The user wants deployment actions before readiness is reviewed.

## Inputs

- PMF evidence.
- Repository or architecture summary.
- Security/compliance constraints.
- Current support and feedback processes.
- Current growth channels and unit economics assumptions.
- Founder operational load.

## Workflow

1. Confirm MVP-stage evidence: activation, retention, revenue/referral, qualitative pull.
2. Check false PMF risks.
3. Audit technical debt: brittle architecture, missing tests, inconsistent AI-generated patterns, missing context files.
4. Audit production readiness: reliability, observability, backups, auth, data handling, incident response.
5. Audit security/compliance: required frameworks, sensitive data, access controls, logs, dependencies.
6. Audit product operations: spec, sprint cadence, bug triage, weekly metrics brief, feedback loop.
7. Audit growth readiness: channel, CAC/LTV/payback assumptions, repeatability.
8. Audit founder bottleneck: support, triage, reporting, planning.
9. Produce launch gate decision and remediation sequence.

## Shared resources

- `../../shared/templates/launch-readiness-report.md`
- `../../shared/references/launch-and-scale-ops.md`
- `../../shared/references/mvp-build-guardrails.md`

## Output format

```markdown
## Launch Readiness
Decision: PASS / HOLD / REVIEW
Highest-risk area:

## Findings
- PMF:
- Technical debt:
- Security/compliance:
- Product ops:
- Growth:
- Founder bottleneck:

## Remediation Sequence
1. Fix before launch:
2. Next sprint:
3. Acceptable current debt:
```

## Guardrails

- Never recommend production launch with unresolved auth, data exposure, secrets, or payment risks.
- Never treat AI security scan as compliance certification.
- Never recommend expansion to a new market if current segment PMF is unclear.
- Require explicit approval before running commands that modify code or systems.
