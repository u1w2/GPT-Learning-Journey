# GPT-Learning-Journey

> **AI Native Architect Growth System**
>
> 从有项目经验的工程师出发，通过 AI 指导、完整项目、问题复现、针对性测试、架构决策、复盘与面试迁移，持续制造真实工程经验，最终形成可迁移的架构能力。

## 1. 这不是一套课程

本仓库不以“看完知识点”为完成标准，而以 **经验形成** 为核心。

```text
知识
 ↓
场景
 ↓
完整项目
 ↓
测试与压力实验
 ↓
主动暴露问题
 ↓
定位与解决
 ↓
Trade-off / Architecture Decision
 ↓
复盘
 ↓
Experience Card
 ↓
面试迁移 / 新项目迁移
 ↓
能力提升
```

## 2. 核心原则

1. **项目优先**：每个核心任务都尽量形成一个完整项目。
2. **问题驱动**：项目必须有可复现的短板、故障或能力边界。
3. **实验验证**：不只“认为系统可以”，而是通过针对性测试证明系统能做到什么。
4. **经验沉淀**：每个项目最终形成问题、解决方案、Trade-off、局限性和经验卡。
5. **能力迁移**：训练用户从历史项目中检索模式，并迁移到新的业务场景。
6. **AI 原生**：AI 既是教练，也是架构师、Reviewer、SRE、面试官和反方评审。
7. **问题驱动成长**：当前项目暴露的能力缺口，可以成为下一阶段学习和新项目的输入。
8. **Private-first / Open-source-ready**：个人 Learner State 默认独立管理，公共课程与模板可以在未来单独开源。
9. **跨对话可恢复**：学习不能依赖某一个 ChatGPT 窗口的上下文；长期状态必须持久化到仓库。

## 3. 跨对话学习协议

`learner/CURRENT.md` 是当前学习状态快照，是新对话恢复学习的第一入口。

当用户在新的 ChatGPT 对话中说：

> **继续 GPT-Learning-Journey**

或：

> **继续我们的成长任务 / 继续我们的学习**

AI 应优先恢复仓库状态，而不是假设自己记得旧对话：

```text
CURRENT.md
    ↓
progress / capability / weak-points / mistakes
    ↓
最近 Session
    ↓
当前 Project
    ↓
最近 Test Lab / Problem / Experience
    ↓
恢复当前任务
    ↓
继续执行
```

恢复时：

- 不重新开始已经完成的内容。
- 优先处理当前未解决问题和能力短板。
- 如果状态文件与项目记录冲突，以最新且有明确完成证据的记录为准，并指出冲突。
- 完成重要学习节点后更新 Learner State。
- `CURRENT.md` 保存当前快照；`learner/sessions/` 保存历史证据。

## 4. 仓库结构

```text
GPT-Learning-Journey/
│
├── README.md
│
├── curriculum/                 # 能力成长路线
│   ├── 01-engineering/
│   ├── 02-system-design/
│   ├── 03-software-architecture/
│   ├── 04-distributed-systems/
│   ├── 05-cloud-native/
│   ├── 06-security/
│   ├── 07-sre/
│   ├── 08-business-architecture/
│   ├── 09-ai-engineering/
│   └── 10-ai-architecture/
│
├── projects/                   # 完整经验制造项目
├── experience/                 # 问题、模式、Trade-off、经验卡
├── interview/                  # 项目答辩与架构面试迁移
├── tools/                      # 测试、压测、故障注入、分析工具
├── templates/                  # 项目、问题、实验、ADR 等模板
├── learner/                    # 当前学习者状态（个人数据）
│   ├── CURRENT.md              # ★ 跨对话恢复入口
│   └── sessions/               # 学习历史证据
└── ai/                         # AI 教练、评审、评估协议
```

## 5. 一个项目必须经历什么

```text
需求 → 业务分析 → 非功能需求 → 架构设计 → 实现
→ Test Lab → 能力边界 → 故障/短板复现 → Root Cause
→ Solution → Trade-off → ADR → Limitations
→ Experience Card → Interview → Pattern Migration
```

### Test Lab

测试不是“让测试通过”，而是通过实验回答：

- 系统能承受多少？
- 哪里先成为瓶颈？
- 哪些故障会发生？
- 故障如何被发现？
- 如何定位？
- 修复后是否真的改善？

测试工具不绑定业务语言。Python 可以作为通用的架构实验与验证语言，但项目可以根据问题选择合适工具。

## 6. AI 在本系统中的角色

AI 不负责替用户“背答案”，而负责推动用户形成自己的判断：

- **Coach**：拆解目标、安排训练、追踪薄弱点
- **Architect**：提出候选架构与 Trade-off
- **Reviewer**：审查代码、设计和文档
- **SRE**：模拟故障与生产事故
- **Red Team**：主动攻击当前设计并寻找边界
- **Interviewer**：围绕真实项目持续追问
- **CTO**：从成本、风险、业务和长期演进角度挑战方案

## 7. 完成标准

“项目完成”不等于“代码跑起来”。至少应回答：

- 我解决了什么问题？
- 为什么这样设计？
- 我遇到过什么问题？
- 如何复现？
- 如何定位？
- 有哪些解决方案？
- 为什么最终选择这个方案？
- 方案有什么代价和局限？
- 如果规模扩大 10 倍怎么办？
- 这个经验可以迁移到哪些场景？

## 8. 当前版本

当前提交建立的是**基础架构、执行规范和跨对话恢复机制**。后续按此结构逐阶段补充完整课程、项目、实验和个人成长状态，不追求一次性堆满内容。