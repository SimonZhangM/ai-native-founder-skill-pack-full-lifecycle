# Example Prompts

## Stage diagnosis

```text
请使用 founder-stage-diagnosis 判断我现在处于 Idea / MVP / Launch / Scale 哪个阶段。请输出证据、缺口、风险和下一步最小动作。
```

## Multi-agent Idea workflow

```text
请让 idea_validator agent 做问题验证和客户发现计划，让 reviewer agent 找最强反证，最后由当前线程汇总是否可以进入 MVP。
```

## MVP workflow

```text
请让 mvp_architect agent 使用 mvp-scope 和 ai-coding-context，生成 MVP 边界、架构上下文、第一轮 AI coding session brief。不要写代码。
```

## Launch workflow

```text
请让 launch_operator agent 使用 launch-readiness、pmf-feedback-loop 和 founder-bottleneck-audit，做上线前审计。
```

## Scale workflow

```text
请让 scale_operator agent 使用 scale-moat-system 和 founder-bottleneck-audit，设计企业级支持、GTM 系统、数据飞轮和 workflow lock-in 路线图。
```
