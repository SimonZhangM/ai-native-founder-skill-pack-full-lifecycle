# Usage Examples

## Idea validation with reviewer

```text
我有一个想法：给中小律所做 AI 合同审查。请让 idea_validator agent 先把它变成可测试假设，设计 10 个用户访谈问题，并列出最强反证。然后让 reviewer agent 检查有没有确认偏误。
```

## MVP planning

```text
我们已经访谈了 12 个目标用户，问题频率和痛点都明确。请让 mvp_architect agent 生成 MVP scope、AGENTS.md/CODEX.md 架构上下文、第一轮 AI coding session brief。不要写代码。
```

## PMF interpretation

```text
这是我们过去 30 天的数据：activation 62%，D7 38%，D30 22%，付费 11%，推荐 8%，Sean Ellis very disappointed 43%。请用 pmf-feedback-loop 判断是不是 PMF，并指出假阳性风险。
```

## Launch readiness

```text
请让 launch_operator agent 做 launch-readiness 审计。重点看技术债、安全合规、产品管理流程、增长渠道和创始人瓶颈。最后给出 PASS/HOLD/REVIEW。
```

## Scale moat

```text
我们开始卖给企业客户了，但 pipeline 还是我亲自推。请让 scale_operator agent 做 enterprise readiness + GTM + moat audit，并让 reviewer agent 挑战我们的护城河叙事。
```
