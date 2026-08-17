# AI｜成长协作层

AI 是整个成长系统的协作基础设施，而不是附加聊天工具。

本项目采用双 Agent：

```text
ChatGPT = 成长大脑
Cursor  = 工程执行大脑
Git     = 成长黑盒
Experience = 架构经验库
```

## 角色文件

| 文件 | 角色 | 默认执行方 |
| --- | --- | --- |
| `coach.md` | 成长教练 | ChatGPT |
| `reviewer.md` | 设计 / 实现审查 | ChatGPT |
| `interviewer.md` | 架构答辩 | ChatGPT |
| `red-team.md` | 主动攻击当前方案 | ChatGPT |
| `protocols/` | 协作、启动、出题、Git 证据协议 | 双方 |

Architect / CTO 视角评审默认由 ChatGPT 承担，协议见 `protocols/`。

## 核心原则

1. ChatGPT 不成为代码执行器。
2. Cursor 不成为另一个“直接告诉答案的 ChatGPT”。
3. 关键设计、判断、权衡和最终责任必须由学习者承担。
4. 能力提升必须有行为证据、项目证据、实验结果和架构决策。

## 标准闭环

```text
ChatGPT 出题 / 布置任务
    ↓
User 独立思考与回答
    ↓
Cursor 按用户设计执行
    ↓
实验 / 故障 / Git 证据
    ↓
ChatGPT Review / 升级下一任务
```

详细协议见 `ai/protocols/`。
