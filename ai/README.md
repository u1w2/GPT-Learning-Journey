# AI｜成长协作层

日常由 Cursor 单 Agent 运行。ChatGPT 是可选外援，不是默认闭环的一部分。

```text
User     = 架构判断
Cursor   = 教练 + 执行 + Git
Git      = 成长黑盒
Experience = 架构经验库
ChatGPT  = 可选第二意见 / Red Team
```

依据：`experience/decisions/ADR-0001-cursor-primary.md`

## 角色文件

| 文件 | 角色 | 默认执行方 |
| --- | --- | --- |
| `coach.md` | 成长教练 | Cursor |
| `reviewer.md` | 设计 / 实现审查 | Cursor |
| `interviewer.md` | 架构答辩 | Cursor |
| `red-team.md` | 主动攻击当前方案 | Cursor |
| `protocols/` | 启动、出题、Git 证据协议 | Cursor |

## 核心原则

1. 日常只对 Cursor 说话，状态由 Cursor 写入 Git。
2. Cursor 不成为“直接告诉答案”的模型。
3. 关键设计、判断、权衡和最终责任必须由学习者承担。
4. 能力提升必须有行为证据、项目证据、实验结果和架构决策。

## 标准闭环

```text
Cursor 读取 CURRENT 并出题
    ↓
User 独立思考与回答
    ↓
Cursor Review / 追问
    ↓
按用户设计执行 / 实验
    ↓
更新 CURRENT 并 git commit
```
