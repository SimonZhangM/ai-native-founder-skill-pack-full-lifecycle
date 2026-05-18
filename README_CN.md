# AI Native Founder Skill Pack 中文版

[English](README.md)

这是一套面向 AI-native 创业者的 Codex 工作流包。

它的目标不是提供一组零散提示词，而是把创业讨论变成可复用的阶段化流程：先判断当前阶段，再找证据缺口，然后决定下一步应该验证、做 MVP、上线、自动化，还是规模化。

## 这套 Pack 是做什么的

AI 工具让产品更容易被做出来，但也会让团队更快做出错误的东西。这套 pack 的核心作用，是让 Codex 在和创始人讨论时始终遵守阶段门：

- Idea：证明问题真实、具体、高频、有痛感。
- MVP：验证一个聚焦方案是否能带来重复使用、收入、推荐或强烈定性拉力。
- Launch：检查 PMF 证据、产品运营、可靠性、安全合规和增长闭环。
- Scale：建立企业级 readiness、授权与委托、GTM 系统、数据飞轮、workflow lock-in 和可防守护城河。

核心原则：

```text
证据不足，不要急着 build。
运营承受不了，不要急着 scale。
判断规则不清楚，不要急着 automate。
```

## 适合谁使用

这套 pack 适合：

- 正在做 AI-native 产品的 solo founder 和小团队。
- 使用 Codex、Claude Code 或其他 agentic coding 工具的创始人。
- 需要把验证、MVP、PMF、上线和规模化流程标准化的早期运营者。
- 想避免 scope creep 和过早写代码的技术创始人。
- 希望用 AI agent 辅助创业判断、但不想让 AI 替代创始人判断的非技术创始人。

它不适合被当成普通提示词合集、融资指南，或用户访谈的替代品。

## 来源

这套 pack 的方法论来源和灵感来自 Anthropic / Claude 官方文章
[The founder's playbook: Building an AI-native startup](https://claude.com/blog/the-founders-playbook)，发布时间是 2026 年 5 月 14 日。

那篇 playbook 把 AI-native 创业拆成四个阶段：Idea、MVP、Launch、Scale，并重新定义了每个阶段的目标、退出标准、常见失败模式和 AI 辅助动作。

本仓库做的是 Codex runtime adaptation：把这套生命周期框架落到 `AGENTS.md`、Skills、Agents、共享模板、脚本和示例里，让 Codex 可以直接按这套流程和创始人协作。

这不是 Anthropic 官方产品。

## 当前本地结构

当前仓库以 Codex runtime 形态组织：

```text
.
|-- AGENTS.md              # Codex 会读取的项目规则
|-- README.md
|-- README_CN.md
|-- MANIFEST.md
|-- .agents/
|   |-- skills/            # Codex 可发现的 runtime Skills
|   `-- shared/            # 共享 references、templates、scripts
|-- .codex/
|   |-- config.toml
|   `-- agents/            # 项目级 Codex custom agents
|-- docs/
|-- examples/
`-- assets/
```

`AGENTS.md` 不是 agent。它是这个 pack 的项目级规则文件，用来告诉 Codex：必须遵守阶段门、区分证据和假设、保护安全边界，并把任务路由到合适的 founder workflow。

## 怎么用

在仓库根目录打开 Codex：

```bash
codex
```

建议第一句从阶段诊断开始：

```text
请用 founder_orchestrator 判断这个创业项目当前处于 Idea、MVP、Launch 还是 Scale。
请区分证据、假设、风险，并给出 next smallest action。
```

更完整的输入可以包含：

```text
产品想法：
目标用户和买单方：
当前产品状态：
已经收集到的证据：
使用、留存、收入或推荐数据：
当前最大瓶颈：
约束条件：
```

推荐工作流：

```text
当前 Codex thread
  -> founder_orchestrator 做阶段诊断和路由
  -> 专门 agent 或 Skill 做聚焦任务
  -> 必要时 reviewer 做反向审查
  -> 当前 thread 汇总最终判断
```

## Skills

| Skill | 用途 |
|---|---|
| `founder-stage-diagnosis` | 判断证据支持的阶段和阶段门结果。 |
| `idea-validation` | 把想法改写成可测试假设，并寻找反证。 |
| `customer-discovery` | 设计访谈对象、问题、追问和访谈后综合。 |
| `mvp-scope` | 定义 MVP 边界、不做什么、功能准入标准。 |
| `ai-coding-context` | 生成 AI 编程上下文、架构说明和 session log。 |
| `pmf-feedback-loop` | 判断 activation、retention、revenue、referral 和 PMF 信号。 |
| `founder-bottleneck-audit` | 判断哪些工作该停止、委托、自动化或保留创始人判断。 |
| `launch-readiness` | 审计 PMF 证据、生产 readiness、安全、运营和增长。 |
| `scale-moat-system` | 审计企业级能力、GTM、数据飞轮、workflow lock-in 和护城河。 |

## Agents

| Agent | 什么时候用 |
|---|---|
| `founder_orchestrator` | 需要阶段诊断、任务路由或最终综合。 |
| `idea_validator` | 需要验证问题、设计用户访谈或分析竞品威胁。 |
| `mvp_architect` | 需要定义 MVP、指标护栏或 AI coding session context。 |
| `launch_operator` | 需要审查 PMF、上线 readiness、产品运营或增长渠道。 |
| `scale_operator` | 需要企业级 readiness、GTM 系统、委托机制或护城河分析。 |
| `reviewer` | 需要反向审查证据不足、伪 PMF、阶段错配或过度乐观。 |

## 常用 Prompt

Idea validation：

```text
请让 idea_validator 把这个想法变成可测试假设，找出最强反证，并设计 customer discovery 访谈脚本。然后让 reviewer 挑战这个结论。
```

MVP planning：

```text
请让 mvp_architect 定义 MVP scope、明确 non-goals、验收标准、指标计划和第一轮 AI coding session context。先不要写代码。
```

PMF review：

```text
请用 pmf-feedback-loop 评估这些 activation、retention、revenue、referral 和 Sean Ellis 数据，指出假阳性风险和缺失证据。
```

Launch readiness：

```text
请让 launch_operator 审计 PMF 证据、生产 readiness、技术债、安全合规、产品运营、增长渠道和创始人瓶颈，最后给出 PASS、HOLD 或 REVIEW。
```

Scale and moat：

```text
请让 scale_operator 审计 enterprise readiness、GTM 系统、委托机制、workflow lock-in、数据飞轮和护城河，并让 reviewer 挑战护城河叙事。
```

## 安装到另一个项目

把 runtime pack 复制到目标仓库：

```bash
mkdir -p .agents .codex
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/.agents/skills .agents/skills
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/.agents/shared .agents/shared
cp -R /path/to/ai-native-founder-skill-pack-full-lifecycle/.codex/agents .codex/agents
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/.codex/config.toml .codex/config.toml
cp /path/to/ai-native-founder-skill-pack-full-lifecycle/AGENTS.md AGENTS.md
```

复制后，在目标项目里重新打开一个 Codex session，让新的项目规则、Skills 和 Agents 生效。

## 验证

先问 Codex：

```text
列出你能看到的 AI Native Founder skills 和 custom agents，然后总结你读取到的 AGENTS.md 规则。
```

再运行脚本：

```bash
python .agents/shared/scripts/stage_gate_check.py examples/sample-evidence.json
python .agents/shared/scripts/pmf_signal_score.py examples/sample-pmf-metrics.json
```

预期结果：两个命令都会输出结构化结果和简短 summary。

## 更多文档

- `docs/agent-skill-map.md`：Agents 和 Skills 如何配合。
- `docs/design-principles.md`：这套 pack 的设计原则。
- `docs/installation.md`：安装形态和 runtime 细节。
- `docs/usage-examples.md`：常见 founder workflow 示例 prompt。
- `examples/`：阶段输出示例和脚本输入 JSON。
