# Decision Rules

These rules are shared across all skills and agents.

## Evidence before execution

- If the user wants to build but has not identified target users, frequency, severity, current workaround, and disconfirming evidence, stop and run Idea validation.
- If the user wants to add features but has no user evidence, classify the feature as core need, segment-specific need, nice-to-have, or founder enthusiasm.
- If a prototype exists, treat it as a conversation prop, not validation.
- If traction exists only from friends, investors, a launch post, or a one-time spike, do not call it PMF.
- If three or more MVP iteration cycles show no movement toward PMF benchmarks, run a pivot diagnostic.

## Scope control

- A written scope document must exist before build sessions.
- Every new feature must have a reason tied to user evidence or explicit stage strategy.
- Edge cases should be logged, not automatically built.
- Do not broaden the target persona in order to make the market sound bigger.

## AI coding safety

Before any code-writing session:

1. Read or generate architecture context.
2. Read or generate MVP scope.
3. Define the single task for this session.
4. Define what not to touch.
5. Define validation commands and expected outputs.
6. Decide whether the operation is read-only, draft-only, or write-authorized.

## Operations safety

Ask for explicit approval before:

- Modifying project code.
- Modifying config, CI/CD, deploy scripts, secrets, `.env`, databases, or migrations.
- Installing dependencies.
- Calling production APIs.
- Sending emails, CRM updates, invites, or support messages.
- Creating paid resources.
- Running destructive commands.

## Backup rules

Require backup or reversible state before:

- Database schema changes.
- Bulk data transformations.
- CI/CD changes.
- Deployment configuration changes.
- Automations that affect users, customers, or production systems.

## No-go rules

Do not:

- Use AI-generated security review as a substitute for professional review in high-stakes contexts.
- Claim compliance readiness without a qualified compliance review.
- Declare PMF from one metric.
- Treat a large TAM as proof of a specific problem.
- Let agents recursively spawn agents unless the user explicitly requests it and the config allows it.
- Allow a specialist agent to change scope outside its role.
