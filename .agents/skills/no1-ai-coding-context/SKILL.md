---
name: no1-ai-coding-context
description: "Use when a founder is preparing an AI coding session and needs product context, architecture boundaries, allowed files, validation commands, session logs, or safety guardrails before implementation."
---

# AI Coding Context

Use this skill before agentic coding so each build session operates inside stable architecture, scope, and safety constraints.

## Trigger when

- The user wants Codex, Claude Code, or another coding agent to build MVP work.
- The user asks for `AGENTS.md`, `CODEX.md`, architecture context, session prompts, or build logs.
- The user says AI-generated code is drifting or each session re-explains the project.

## Do not use when

- The user has not defined MVP scope.
- The task is pure market validation or customer discovery.
- The user asks for code changes without approving write access.

## Inputs

- MVP scope.
- Product context.
- Project repository path, if available.
- Tech stack.
- Test commands.
- Files or modules in scope.
- Files or modules out of scope.

## Local discovery

Read-only commands are allowed when the user has a local project:

```bash
pwd
ls
find . -maxdepth 3 -type f | head
rg -n "TODO|FIXME|auth|session|secret|token|api|database" .
git status --short
```

Do not install dependencies, run migrations, deploy, or modify files without explicit approval.

## Workflow

1. Confirm MVP scope exists.
2. Inspect project structure read-only if a project is present.
3. Generate architecture context using `../../shared/no1/templates/architecture-context.md`.
4. Generate build session log using `../../shared/no1/templates/build-session-log.md`.
5. Decide whether context should be written as `AGENTS.md`, `CODEX.md`, both, or a docs file.
6. Define session task, files to touch, files not to touch, validation commands, and rollback.
7. End by asking the user to approve writes before creating files.

## Output format

```markdown
## AI Coding Context Draft
...

## Proposed Files
- AGENTS.md / CODEX.md / docs/architecture.md

## Build Session Brief
Task:
Allowed files:
Forbidden files:
Validation commands:
Approval needed:
```

## Guardrails

- Never let a coding agent infer architecture from scratch if a context file can be created.
- Never combine scope expansion with implementation in the same session.
- Never claim code is secure because it runs.
- Never touch production, secrets, migrations, CI/CD, or deployment files without explicit approval and backup.
