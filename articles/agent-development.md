# Agent 开发指南

本文档介绍如何在 AiPy 平台上开发 AI Agent。

## Agent 基础概念

Agent 是 AiPy 的核心组件，负责执行智能任务。

## 创建 Agent

```python
from aipy import Agent

agent = Agent(
    name="CustomerServiceAgent",
    capabilities=["chat", "search"]
)
```

## Agent 配置

- 名称
- 能力列表
- 模型选择

---

*持续更新中，敬请关注*