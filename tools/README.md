# Tools｜验证与实验工具

工具服务于问题验证，不反过来成为学习目标。

## 仓库检查

初始化或每次重要节点后运行：

```bash
python3 tools/check_structure.py
```

## 使用原则

```text
发现问题
→ 定义假设
→ 选择最合适的工具
→ 设计实验
→ 采集结果
→ 分析瓶颈
→ 形成 Problem
→ 修复
→ 再实验
```

## 工具类别

- API / Functional Testing
- Load / Stress Testing
- Benchmarking
- Concurrency Testing
- Failure Injection
- Network Testing
- Database Testing
- Log / Metrics Analysis
- Security Testing
- AI Evaluation

当前阶段还没有可运行业务系统，因此先保证仓库结构检查可用。进入项目后，再按问题选择压测和故障工具。
