import os
import re
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
articles_dir = os.path.join(work_dir, "articles")
# 检查新文章的内容结构
new_articles = [
    "aipy-agent-types-guide-168-20260709-2-1-1783572142.md",
    "aipy-pro-multimodal-guide-168-20260709-2-2-1783572237.md",
    "aipy-enterprise-automation-solutions-168-20260709-2-3-1783572301.md",
    "aipy-workflow-multi-agent-collaboration-168-20260709-2-4-1783572354.md",
    "aipy-mcp-integration-best-practices-168-20260709-2-5-1783572416.md",
    "deepseek-dspark-inference-optimization-169-20260706-1-1-1783305743.md",
]
print("📝 检查新文章内容结构...")
for fname in new_articles:
    fpath = os.path.join(articles_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        # 提取标题
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "(无标题)"
        # 提取 description
        desc_match = re.search(r'description:\s*"(.+?)"', content)
        desc = desc_match.group(1)[:80] + "..." if desc_match else "(无摘要)"
        # 提取文件中的日期
        date_match = re.search(r'(\d{4})(\d{2})(\d{2})', fname)
        date_str = f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}" if date_match else "未知"
        print(f"\n📄 {fname}")
        print(f"  标题: {title}")
        print(f"  日期: {date_str}")
        print(f"  摘要: {desc}")
    else:
        print(f"\n❌ {fname} 不存在")