# ADR-0001｜日常训练由 Cursor 单 Agent 执行，ChatGPT 改为可选外援

## Status

Accepted

## Problem

双 Agent 要求用户在 ChatGPT 与 Cursor 之间来回粘贴。ChatGPT 不能把状态写入 GitHub，导致“成长大脑”和“成长证据”断开。交接成本高于训练收益。

## Context

初始化时把职责拆成：ChatGPT 出题 / Review，Cursor 执行工程与 Git。实际使用中，用户立刻碰到两个问题：

1. 不知道下一句该对谁说。
2. ChatGPT 不会自动把 CURRENT.md 写进仓库。

真实约束是：日常训练必须发生在能读写 Git 的环境里。

## Constraints

- 学习者只有一条愿意持续使用的对话入口。
- 状态必须进入 Git，否则新对话会重新开始。
- 不能因此让 AI 代替学习者做架构判断。

## Options

1. 维持 ChatGPT + Cursor 双 Agent，靠人工粘贴同步。
2. 日常全部交给 Cursor：出题、追问、Review、写仓库、提交；ChatGPT 仅在需要第二意见时使用。
3. 让 Cursor 连题目一起答掉，用户只看结论。

## Decision

选择方案 2。

日常只对 Cursor 说话。Cursor 同时承担教练、出题人、Reviewer、工程执行和 Git 维护。ChatGPT 降为可选外援，不参与默认闭环。

## Trade-offs

得到：一条对话、状态自动进 Git、减少协议空转。
放弃：两个模型互相制衡的默认流程。

## Risks

- Cursor 可能既出题又执行，容易滑向“直接给答案”。
- 缺少第二个模型时，Review 盲区可能变大。

## Consequences

- `CURRENT.md` 由 Cursor 在每个有意义节点更新并 commit。
- 角色文件的默认执行方改为 Cursor。
- 用户仍然必须独立回答架构题。

## Validation

下一轮用户直接在 Cursor 中回答 API Question 1，完成后仓库出现对应 Session / CURRENT 更新，且没有把标准答案写进文档。

## Limitations

如果后续发现 Cursor 的 Review 明显偏软、或用户需要故意被另一个模型攻击，再把 ChatGPT 请回来做 Red Team / 第二面试官。没有这个证据前，不恢复双 Agent 日常流程。
