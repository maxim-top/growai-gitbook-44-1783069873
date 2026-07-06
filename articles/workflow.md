# Workflow 最佳实践

本文档介绍 AiPy Workflow 的使用方法。

## Workflow 简介

Workflow 用于编排多个 Agent 和工具，实现复杂任务自动化。

## 创建 Workflow

```python
from aipy import Workflow

wf = Workflow(name="DataProcessing")
wf.add_step(agent1)
wf.add_step(agent2)
```

## Workflow 模式

- 顺序执行
- 并行执行
- 条件分支

---

*持续更新中，敬请关注*