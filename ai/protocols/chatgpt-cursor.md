# ChatGPT ↔ Cursor 协作协议

```text
          ┌─────────────┐
          │  ChatGPT    │
          │  成长大脑    │
          └──────┬──────┘
                 │
           Task / Review
                 │
                 ▼
          ┌─────────────┐
          │   Cursor    │
          │ 工程执行大脑 │
          └──────┬──────┘
                 │
          Code / Test / Git
                 │
                 ▼
          ┌─────────────┐
          │ Repository  │
          │ 真实成长证据 │
          └──────┬──────┘
                 │
          Result / Evidence
                 │
                 ▼
          ┌─────────────┐
          │  ChatGPT    │
          │ Review/升级  │
          └─────────────┘
```

## 分工

ChatGPT 负责：任务、问题、Review、Red Team、面试、能力升级判断。
Cursor 负责：代码、测试、实验、Git、文档维护、状态同步。
User 负责：独立思考、架构决策、解释为什么。

## 标准流程

```text
ChatGPT
 ↓
Question
 ↓
User 独立回答
 ↓
Cursor 执行用户设计
 ↓
实验
 ↓
结果
 ↓
ChatGPT Review
```

## 交接物

ChatGPT → Cursor：

- 当前任务
- 用户已经做出的设计
- 需要执行的实验
- 需要更新的 Learner State

Cursor → ChatGPT：

- Git commit
- 实验结果
- 暴露的问题
- ADR / Experience
- 更新后的 CURRENT.md
