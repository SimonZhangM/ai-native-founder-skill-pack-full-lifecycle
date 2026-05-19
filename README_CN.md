# OPC Agent Legion Runtime

根目录是整合版测试区，不是单个 agent 包。

目录分成两个 runtime 相关部分：

```text
no1 agent/    no1 独立单兵包，用户复制其内部内容即可使用
根目录          军团整合测试区，Codex 会直接读取这里的 AGENTS.md、.agents、.codex
```

当前根目录只整合了 no1：Founder Stage-Gate 系统。后续 no2、no3 完成后，应先保持各自独立单兵包，再把命名空间版本整合到根目录。

整合版必须使用命名空间：

```text
.agents/skills/no1-*
.agents/shared/no1/
.codex/agents/no1-*.toml
docs/no1/
examples/no1/
assets/no1/
```

总调度 agent 是：

```text
.codex/agents/commander.toml
```

验证当前 no1 子系统：

```bash
python .agents/shared/no1/scripts/stage_gate_check.py examples/no1/sample-evidence.json
python .agents/shared/no1/scripts/pmf_signal_score.py examples/no1/sample-pmf-metrics.json
```
