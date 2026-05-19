# MVP Build Guardrails

## MVP is still evidence gathering

The MVP stage is not about finishing a product. It is about testing whether a small, focused solution creates enough value that a specific user group returns, pays, or recommends it.

## Required artifacts before build

1. MVP scope document.
2. Architecture context document.
3. AI coding session template.
4. Measurement framework.
5. Security review checklist.

## Scope document requirements

- Core user.
- Core problem.
- Core workflow.
- One or two must-have features.
- Explicit non-goals.
- Evidence required to add features.
- What counts as a failed MVP.
- What counts as an iteration trigger.

## Architecture context requirements

- Product goal.
- User and scale assumptions.
- Tech stack.
- Key architectural decisions.
- Dependencies to prefer and avoid.
- Data model assumptions.
- Authentication/session approach.
- API boundaries.
- Testing commands.
- Security assumptions.
- Known tradeoffs.

## AI coding session rules

Each session must include:

- Task.
- Files likely involved.
- Files not to touch.
- Acceptance criteria.
- Test commands.
- Rollback plan.
- Session log entry.

## Security review minimum

Before real users touch the MVP, review:

- Authentication and session handling.
- Authorization and role boundaries.
- Input validation and injection risks.
- Secrets handling.
- API responses and data exposure.
- Dependency vulnerabilities.
- Logging of sensitive data.
- Payment or personal data flows.

AI can help find issues, but it is not a substitute for security tooling or professional review in high-stakes contexts.
