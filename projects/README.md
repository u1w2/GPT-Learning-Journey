# Projects｜经验制造项目

项目是本系统最重要的学习单元。一个项目的目标不是“做出 Demo”，而是让学习者亲自经历需求、设计、实现、测试、故障、解决、权衡和复盘。

## 标准生命周期

```text
需求 → 业务分析 → NFR → 架构 → 实现
→ Test Lab → 能力上限 → 问题复现
→ Root Cause → Solution → Trade-off
→ ADR → Limitations → Experience Card
→ Interview → Pattern Migration
```

## 标准项目结构

```text
001-example/
├── README.md
├── requirements/
├── architecture/
├── implementation/
├── test-lab/
├── problems/
├── solutions/
├── trade-offs/
├── decisions/
├── limitations/
├── experience/
├── interview/
└── retrospective/
```

## 强制要求

- 至少一个可复现问题或能力边界。
- 至少一个针对性测试实验。
- 记录问题如何发现、定位和解决。
- 记录没有采用的方案及原因。
- 记录当前方案的局限。
- 形成可用于面试的项目案例。
- 形成可以迁移到新场景的架构模式。
