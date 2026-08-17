# GPT-Learning-Journey

> **AI Native Architect Growth System**
>
> ChatGPT 负责成长教练 / 架构导师 / 出题人 / Reviewer。
> Cursor 负责本地项目、代码、实验、Git 和持续执行。
>
> 目标不是“学完课程”，而是帮助一个已经拥有多年项目经验、但缺少系统架构训练的工程师，通过真实问题、设计、编码、实验、故障、复盘和架构答辩，逐渐成长为能够独立进行系统架构设计的高级工程师 / 架构师。

## 1. 这不是一套课程

本仓库不以“看完知识点”为完成标准，而以 **行为证据 + 项目证据 + 实验结果 + 架构决策** 为核心。

```text
知识
 ↓
场景
 ↓
问题
 ↓
独立思考
 ↓
架构设计
 ↓
实现
 ↓
实验
 ↓
暴露问题
 ↓
定位 Root Cause
 ↓
解决
 ↓
Trade-off
 ↓
ADR
 ↓
Experience Card
 ↓
架构答辩
 ↓
能力评估
 ↓
迁移到新场景
```

**不能把“看过资料”视为掌握。**

## 2. AI 双 Agent 架构

```text
                    用户
                     │
                     ▼
             ┌──────────────┐
             │   ChatGPT    │
             │ Growth Coach │
             └──────┬───────┘
                    │
          任务 / 问题 / Review
                    │
                    ▼
             ┌──────────────┐
             │    Cursor    │
             │ Local Agent  │
             └──────┬───────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Code        Test        Experiment
        │           │           │
        └───────────┼───────────┘
                    ▼
                Git History
                    │
                    ▼
             Experience / ADR
                    │
                    ▼
              能力成长证据
```

### ChatGPT：成长大脑

- Coach：制定成长任务、判断当前能力、找出短板、控制训练难度
- Architect：提出架构问题、提供真实业务场景、要求做架构决策
- Reviewer：审查设计与实现，找出遗漏、过度设计和生产风险
- Red Team：主动攻击当前方案（流量、故障、重复、超时、依赖变慢）
- Interviewer：要求不看文档解释“为什么这样设计”

ChatGPT 不是代码执行器。

### Cursor：工程实验室

- 创建项目、修改代码、运行测试、运行服务、执行实验
- 维护清晰 Git 历史
- 同步 README、CURRENT、Session、ADR、Experience、能力状态
- 提醒遗漏、询问原因、要求补充、要求验证

**Cursor 不允许在用户独立回答之前直接给出架构题的“正确答案”。**

## 3. 跨对话学习协议

`learner/CURRENT.md` 是跨 ChatGPT / Cursor / 新对话恢复成长状态的**唯一入口**。

当用户说：

> **继续 GPT-Learning-Journey**

应优先恢复仓库状态，而不是假设自己记得旧对话：

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
- `CURRENT.md` 只保存当前快照；`learner/sessions/` 保存历史证据。

## 4. Cursor 每次启动必须执行

进入项目后首先读取：

```text
README.md
learner/CURRENT.md
learner/progress.md
learner/capability.md
learner/weak-points.md
learner/mistakes.md
```

然后检查：

```bash
git status
git log --oneline -10
```

最后告诉用户：

```text
当前阶段：
当前任务：
当前项目：
已经完成：
当前短板：
未解决问题：
下一步唯一任务：
```

**不要重新开始课程。**

## 5. 仓库结构

```text
GPT-Learning-Journey/
│
├── README.md
├── AGENTS.md                   # Cursor 启动与职责边界
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
│   └── _template/
├── experience/                 # 问题、模式、Trade-off、经验卡
├── interview/                  # 项目答辩与架构面试迁移
├── tools/                      # 测试、压测、故障注入、检查脚本
├── templates/                  # ADR、Experience、实验等模板
├── learner/                    # 当前学习者状态
│   ├── CURRENT.md              # ★ 跨对话恢复入口
│   └── sessions/               # 学习历史证据
└── ai/                         # AI 角色协议与协作协议
    ├── coach.md
    ├── reviewer.md
    ├── interviewer.md
    ├── red-team.md
    └── protocols/
```

## 6. 能力模型

```text
L0：未知
L1：了解
L2：能够实现
L3：能够独立设计
L4：能够进行 Trade-off
L5：能够处理复杂生产问题
L6：能够指导别人
```

尤其重要：

> **L3 以上必须有项目证据。**

## 7. 架构训练规则

### 约束递增

不要一开始就引入微服务、K8s、Kafka、Redis Cluster、分库分表、Service Mesh。

```text
单体
 ↓
数据库
 ↓
缓存
 ↓
并发
 ↓
消息
 ↓
服务拆分
 ↓
分布式
 ↓
高可用
 ↓
容灾
```

每一步都问：**为什么现在需要？** 如果没有真实约束，不要引入复杂度。

### 主动制造问题

不要只做 CRUD → 测试通过 → 项目结束。必须经历：

```text
正常系统 → 压力 → 故障 → 瓶颈 → 定位 → 解决 → 再次实验
```

### 架构师核心原则

不是“我知道 Redis、Kafka、Kubernetes”。
而是：“当前问题为什么需要它？不用会怎么样？替代方案是什么？引入的代价是什么？”

## 8. Git 是成长黑盒

Git History 本身就是学习证据：

```text
commit
 ↓
问题
 ↓
第一次方案
 ↓
实验
 ↓
发现问题
 ↓
修改
 ↓
再次实验
 ↓
ADR
 ↓
Experience
```

不要为了“干净”而抹掉真实学习过程。

完成有意义的学习节点后：

```bash
git status
git diff
git add .
git commit -m "learn: ..."
```

建议前缀：`learn:` / `feat:` / `test:` / `experiment:` / `docs:`。
不要使用：`update` / `fix` / `test` / `aaa` / `修改`。

## 9. 完成标准

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

## 10. 当前版本

当前仓库已建立完整项目骨架、Learner State、AI 双 Agent 协作协议、模板，以及 Stage 02 System Design / API Design 训练状态。

下一步唯一任务由 `learner/CURRENT.md` 决定。
