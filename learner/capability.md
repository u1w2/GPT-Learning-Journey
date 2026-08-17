# Capability｜能力矩阵

等级定义：

```text
L0：未知
L1：了解
L2：能够实现
L3：能够独立设计
L4：能够进行 Trade-off
L5：能够处理复杂生产问题
L6：能够指导别人
```

规则：L3 以上必须有项目证据。没有项目证据时，最多记为 L2。

| Domain | Level | Evidence | Notes |
| --- | --- | --- | --- |
| Engineering | L2 | 多年项目实现经验；尚无本仓库项目证据 | 能实现，结构化复盘不足 |
| System Design | L2 | 数据模型讨论；API Question 1 尚未作答 | 当前训练重点 |
| Software Architecture | L1 | 有组件拆分直觉，缺方法论 | 未进入正式训练 |
| Distributed Systems | L1 | 能意识到未来分布式，缺真实约束与实验 | 禁止提前上复杂度 |
| Cloud Native | L0 | 无本仓库证据 | LOCKED |
| Security | L1 | 有基本鉴权意识，未形成安全设计证据 | 待 API 设计中验证 |
| SRE | L0 | 无故障注入 / 可观测性项目证据 | LOCKED |
| Business Architecture | L1 | 能从业务对象出发建模 | 需继续训练 |
| AI Engineering | L0 | 无证据 | LOCKED |
| AI Architecture | L0 | 无证据 | LOCKED |

## 当前判断

学习者处于“高级工程师 → 初级架构师”区间。

已经出现架构直觉，但还不能稳定做到：

```text
看到业务 → 识别对象 / 流程 / 约束 / 风险 → 比较方案 → 选择 → 验证 → 知道何时推翻
```
