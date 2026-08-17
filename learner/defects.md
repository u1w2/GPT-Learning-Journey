# Defects｜个人缺陷与跨周期强化队列

这里记录需要再次强化的模糊点和错误。项目结束后，下一周期必须从这里带走 1–2 条一起打。

完整协议见 `ai/protocols/reinforce.md`。卡片模板见 `templates/defect-card.md`。

当前主队列不超过 3 条。

## Open

### D-001 把未来规模当成当前必做项

- Status: Open
- First Seen: 数据模型讨论 / 进入 API Design 之前
- Why It Matters: 这是当前最大的能力边缘。不解决，后面所有“高级”组件都会被提前引入。
- Target Rounds: 3
- Round Log:
  - R1 Probe：API Question 1（尚未作答）
- Next Retest: 必须出现在 API Question 1；若仍 Fuzzy，下一个可运行项目里继续作为强制题
- Close Criteria: 在新场景下能独立区分“现在必须冻结 / 现在必须延后”，并说出代价

### D-002 把知道技术当成掌握架构

- Status: Open
- First Seen: 能力盘点
- Why It Matters: 会把 Redis / MQ / 分布式挂在嘴边，但说不清为什么现在需要。
- Target Rounds: 3
- Round Log:
  - R1 Probe：API Question 1 的 Trade-off 表达（尚未作答）
- Next Retest: API Question 1 先探测；后续每个 ADR 都复测
- Close Criteria: ADR 能写清为什么选、为什么不选、不用会怎样

## Reinforcing

无。

## Closed

无。
