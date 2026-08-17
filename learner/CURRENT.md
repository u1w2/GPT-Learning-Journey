# CURRENT STATE

> 跨对话恢复成长状态的唯一入口。只保存当前快照，完整历史进入 `learner/sessions/`。日常由 Cursor 更新并写入 Git。
>
> 新窗口第一句：`继续 GPT-Learning-Journey`。连续的是仓库，不是聊天记录。

## Current Stage

Stage 02 · System Design

## Current Phase

API Design

## Current Task

API Question 1：第一阶段为了快速验证，Web、小程序、后台管理端都需要调用 API。API 哪些东西第一阶段就必须确定好，避免后面客户端越来越多以后出现大量兼容和重构？

## Current Project

尚未进入可运行项目。当前仍是架构判断训练，不落代码。

## Status

IN_PROGRESS · 等待学习者独立作答

## Current Goal

把已经具备的业务、数据建模和扩展性直觉，训练成稳定的架构决策方法。总目标是：找到能力边缘，把模糊部分清晰化，再适当扩展，成为能独立做系统架构、并具备 AI 系统设计经验的高级架构全栈师。

## Completed

- 仓库已完成 GPT-Learning-Journey 初始化，并接受 ADR-0001：日常 Cursor 单 Agent。
- 已完成一次当前能力盘点：定位在“高级工程师 → 初级架构师”区间。架构思维已经开始形成，但理论体系、工程化、分布式、可靠性和结构化表达仍需补齐。
- 已讨论 `user → user_order → order` 关联模型，并主动考虑冗余字段、查询压力、数据规模、区域划分、未来分布式以及时间/空间取舍。
- 已进入 API 设计训练，并明确：只回答当前问题，不提前展开后续知识点。

## In Progress

API 设计基础：第一阶段就必须确定的 API 契约与演进边界。

训练规则：先由学习者在 Cursor 中独立作答；Cursor Review 并写入 Git。不直接给正确答案，只可提醒遗漏、询问原因、要求补充和验证。

## Current Capability

见 `learner/capability.md`。

已观察到的优势：

- 能从业务对象和访问关系出发思考数据模型。
- 会主动考虑数据规模增长后的查询压力。
- 已经开始使用时间/空间取舍，而不是只寻找标准答案。
- 能提前考虑未来分布式演进。
- 能把问题从“怎么实现”提升到“以后会不会重构”。

待验证：

- API 契约设计是否完整。
- 兼容性与版本演进是否有系统方法。
- 能否主动纳入错误模型、幂等、分页、鉴权和可观测性。
- 能否用统一框架解释“为什么这样设计”。

## Weak Points

见 `learner/weak-points.md` 与 `learner/defects.md`。

主 Open 缺陷：

- D-001 把未来规模当成当前必做项（R1 将在 API Question 1 探测）
- D-002 把知道技术当成掌握架构（R1 将在 API Question 1 探测）

下一周期必须带回这些缺陷做再次强化，不能只开新课。

1. 架构直觉已经出现，但还没有可重复的架构方法论。
2. 需要把“我觉得以后可能需要”训练成“在什么条件下需要、替代方案是什么、代价是什么”。
3. 结构化架构表达与答辩能力不足。
4. 尚无 L3 以上所需的项目证据。

## Unresolved Problems

- API 第一阶段最小稳定契约应该包含哪些内容？
- 哪些设计应该现在确定，哪些应该刻意延后？
- 如何避免为了“未来扩展”过度设计？

## Latest Learning Result

2026-08-17：补齐项目个人能力评判与跨周期强化。每个项目结束必须留下 capability-review，并把 Open 缺陷带入下一周期做 R2/R3 复测。强化是新情境再判断，不是背名词。当前仍等待 API Question 1 作为 D-001/D-002 的 R1。

## Next Single Task

在 Cursor 中独立完成 API Question 1。这次用来探测主边缘：哪些契约现在必须冻结，哪些必须延后。不要先要标准答案。

## Evidence

- 初始化证据：本仓库目录、协议文件、Git commit
- 运行架构证据：`experience/decisions/ADR-0001-cursor-primary.md`
- 能力盘点证据：`learner/capability.md`、`learner/sessions/2026-08-17-init.md`
- API Question 1 证据：尚无。用户作答后才能记为行为证据

## Last Updated

2026-08-17 · 跨周期强化协议
