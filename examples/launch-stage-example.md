# Launch Stage Example

## User prompt

```text
我们有 80 个活跃用户，D30 留存 22%，有 9 个付费客户。准备上线给更多公司用。请做 launch-readiness。
```

## Recommended flow

1. Run `pmf-feedback-loop`.
2. Run `launch-readiness`.
3. Run `founder-bottleneck-audit`.
4. Ask `reviewer` to challenge PMF and production readiness.

## Expected output

```markdown
## Launch Readiness
Decision: REVIEW

## Fix before launch
- Authentication/session handling review.
- Dependency vulnerability scan.
- Support triage process.
- Weekly metrics brief.
```
