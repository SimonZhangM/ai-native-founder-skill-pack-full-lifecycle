# Design Principles

## 1. Skills are narrow methods

Each skill solves one repeatable workflow. It should contain triggers, non-triggers, inputs, workflow, output format, and guardrails.

## 2. Agents are roles, not methods

An agent is a specialist operator that chooses and applies skills. Agents should not become broad consultants.

## 3. Current thread is the control plane

The current thread decides when to call agents, integrates their outputs, and protects safety boundaries.

## 4. Shared material prevents duplication

References, templates, and scripts live in `shared/` so every skill can stay compact.

## 5. Descriptions drive triggering

Skill descriptions must front-load key use cases and boundaries because Codex uses name and description to decide when a skill is relevant.

## 6. Scripts are deterministic helpers

Use scripts for checks and scores that should execute the same way each time. Do not encode nuanced strategic judgment entirely as scripts.

## 7. Evidence beats enthusiasm

If the user wants to build, launch, or scale before the evidence supports it, the pack should slow down and run the right stage gate.

## 8. Safety beats speed

Production operations, external systems, secrets, deployment, CI/CD, migrations, and customer-facing actions require explicit approval.

## 9. Reviewer protects objectivity

The no1_reviewer agent exists to catch confirmation bias, false PMF, premature launch, premature scale, and missing safety checks.
