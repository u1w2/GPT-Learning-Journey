# 日常运行协议｜Cursor 单 Agent

日常训练不再在 ChatGPT 与 Cursor 之间切换。

```text
          ┌─────────────┐
          │    User     │
          │  架构判断    │
          └──────┬──────┘
                 │
           独立回答 / 决策
                 │
                 ▼
          ┌─────────────┐
          │   Cursor    │
          │ 教练 + 执行  │
          │ + Git 证据   │
          └──────┬──────┘
                 │
          出题 / 追问 / Review
          代码 / 测试 / 实验
          CURRENT / Session / ADR
                 │
                 ▼
          ┌─────────────┐
          │  GitHub     │
          │ 成长证据库   │
          └─────────────┘
```

## 分工

- User：独立思考、架构决策、解释为什么。
- Cursor：出题、追问、Review、写代码、跑实验、更新 Learner State、commit / push。
- ChatGPT：可选外援。默认不参与。需要第二意见或故意被另一个模型攻击时再用。

## 标准流程

```text
Cursor 读取 CURRENT
 ↓
出题 / 恢复当前任务
 ↓
User 独立回答
 ↓
Cursor Review / 追问
 ↓
需要实现时，按用户设计落地
 ↓
实验
 ↓
更新 CURRENT / Session / ADR
 ↓
git commit
```

## 禁止误解

“Cursor 全干了”不等于“Cursor 替用户答题”。

全干的是流程：状态、Git、追问、执行。
不能全干的是判断：现在必须定什么、为什么、代价是什么。
