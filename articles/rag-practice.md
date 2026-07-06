# RAG 实践

本文档介绍 RAG (检索增强生成) 的实现方法。

## RAG 架构

1. 文档索引
2. 向量检索
3. 上下文增强
4. 生成回答

## 实现 RAG

```python
from aipy import RAG

rag = RAG(documents=["doc1", "doc2"])
answer = rag.query("问题")
```

---

*持续更新中，敬请关注*