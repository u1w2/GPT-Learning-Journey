# Project Template

复制本目录创建新项目。项目目标不是 Demo，而是经历设计、实现、实验、故障、决策和复盘。

```text
NNN-name/
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

## 1. 项目目标

说明要获得什么工程/架构经验。

## 2. 场景

业务背景、用户、规模和关键约束。

## 3. 非功能需求

性能、可用性、一致性、安全、成本、可观测性。只写当前真实约束。

## 4. 交付要求

必须完成的系统、文档和实验。

## 5. 必须暴露的问题

至少设计一个可以复现的短板或能力边界。禁止只做 CRUD 后结束。

## 6. Test Lab

明确实验目标、工具、参数、指标、预期和结果。

## 7. 架构决策

记录候选方案、最终选择、放弃方案和 Trade-off。使用 `templates/adr.md`。

## 8. 局限性

诚实记录当前架构无法解决的问题。

## 9. Experience Card

总结问题、原因、方案、代价、适用场景和迁移方式。

## 10. 面试

准备项目介绍、问题案例、架构答辩和追问。

## 11. 完成标准

项目必须能够被解释、复现、验证、质疑和迁移，而不仅仅是运行成功。
