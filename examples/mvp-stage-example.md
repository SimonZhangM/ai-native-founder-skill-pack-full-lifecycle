# MVP Stage Example

## User prompt

```text
我们访谈了 11 个财务经理，8 个每周都在手动核对报销和会计系统。请帮我定义 MVP 范围和 Codex build context。
```

## Recommended flow

1. Run `mvp-scope`.
2. Run `ai-coding-context`.
3. Ask `reviewer` to find scope creep and security gaps.

## Expected output

```markdown
## MVP must do
- Import a small expense CSV.
- Connect or simulate accounting-system records.
- Flag mismatches and explain why.

## MVP must not do
- Full enterprise approvals.
- Payroll integration.
- Multi-country compliance.
```
