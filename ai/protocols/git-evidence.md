# Git Evidence｜Git 是成长黑盒

Git 不只是版本控制。最终应能看到：

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

## 规则

- 完成有意义的学习节点后再 commit
- 不要为了“干净”抹掉真实学习过程
- 不要使用 `update` / `fix` / `aaa` / `修改` 这种无信息 commit
- 建议前缀：`learn:` / `feat:` / `test:` / `experiment:` / `docs:`

## 示例

```text
learn: establish api design baseline
feat: implement order api
test: add concurrent order benchmark
experiment: evaluate database indexing
docs: record api compatibility tradeoffs
learn: complete api design review
```

## Cursor 完成节点后

```bash
git status
git diff
git add .
git commit -m "learn: ..."
```
