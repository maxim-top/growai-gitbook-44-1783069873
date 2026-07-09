import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
script_path = os.path.join(work_dir, "scripts", "update_article_index.py")
# 读取当前脚本，保留导入和辅助函数，只替换 generate_latest_md
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()
# 找到 generate_latest_md 函数的起始和结束位置
start_marker = "def generate_latest_md(articles):"
end_marker = "\ndef "
func_start = content.find(start_marker)
func_end = content.find(end_marker, func_start + 1)
if func_end == -1:
    func_end = len(content)
print(f"generate_latest_md 函数位置: {func_start} - {func_end}")
# 新的 generate_latest_md 函数
new_func = '''def generate_latest_md(articles):
    """
    生成 latest.md 内容 - 按时间和主题规整排版
    """
    lines = []
    lines.append("# 最新文章")
    lines.append("")
    lines.append("AiPy AI 知识中心持续更新 AI Agent、Workflow、MCP、LLM、RAG、多模态、Prompt Engineering 等技术内容。")
    lines.append("")
    
    # 排除基础页面文档（非文章类）
    article_exclude = {
        "README.md", "latest.md", "index.md",
        "about-aipy.md", "cases.md", "contact.md",
        "what-is-aipy.md", "product-overview.md",
        "agent-development.md", "workflow.md",
        "mcp-development.md", "llm-development.md",
        "prompt-engineering.md", "rag-practice.md",
        "multimodal.md", "api-docs.md",
        "quick-start.md", "best-practices.md",
        "case-customer-service.md", "case-knowledge-base.md",
        "case-office-automation.md",
    }
    
    # 过滤出真正的文章
    real_articles = [(f, fp, t, d, s) for f, fp, t, d, s in articles if f not in article_exclude]
    
    # ========== 第一部分：按日期分区 ==========
    lines.append("## 📅 按时间发布")
    lines.append("")
    
    # 按日期分组
    from collections import OrderedDict
    date_groups = OrderedDict()
    for filename, filepath, title, date_str, _ in real_articles:
        if not date_str:
            date_str = "未分类"
        if date_str not in date_groups:
            date_groups[date_str] = []
        date_groups[date_str].append((filename, title))
    
    for date_str in sorted(date_groups.keys(), reverse=True):
        items = date_groups[date_str]
        lines.append(f"### {date_str}")
        lines.append("")
        for filename, title in items:
            lines.append(f"- [{title}](./{filename})")
        lines.append("")
    
    # ========== 第二部分：按主题分类 ==========
    lines.append("## 📂 按主题分类")
    lines.append("")
    
    # 定义分类关键词映射
    category_keywords = {
        "Agent 开发": ["agent", "智能体"],
        "Workflow 编排": ["workflow", "工作流编排"],
        "MCP 集成": ["mcp", "MCP"],
        "RAG 实践": ["rag", "RAG"],
        "多模态应用": ["多模态", "multimodal", "图片生成", "视觉", "pro"],
        "LLM 与大模型": ["llm", "LLM", "deepseek", "DeepSeek", "大模型", "推理优化"],
        "企业级应用": ["企业版", "企业级", "自动化", "enterprise"],
        "Prompt Engineering": ["prompt", "Prompt"],
    }
    
    categorized = {k: [] for k in category_keywords}
    
    for filename, filepath, title, date_str, _ in real_articles:
        assigned = False
        for category, keywords in category_keywords.items():
            combined = f"{title} {filename}".lower()
            if any(k.lower() in combined for k in keywords):
                categorized[category].append((filename, title))
                assigned = True
                break
        if not assigned:
            if "其他" not in categorized:
                categorized["其他"] = []
            categorized["其他"].append((filename, title))
    
    for category, items in categorized.items():
        if items:
            lines.append(f"### {category}")
            lines.append("")
            for filename, title in items:
                lines.append(f"- [{title}](./{filename})")
            lines.append("")
    
    # 页脚
    lines.append("---")
    lines.append("")
    lines.append("*持续更新中，敬请关注*")
    lines.append("*© 2026 AiPy | AI Agent Platform*")
    lines.append("")
    
    return "\\n".join(lines)
'''
# 替换
new_content = content[:func_start] + new_func + content[func_end:]
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("✅ 脚本 generate_latest_md 函数已替换")
# 验证
with open(script_path, 'r', encoding='utf-8') as f:
    verify = f.read()
if "按时间和主题规整排版" in verify:
    print("✅ 验证通过 - 新函数已写入")
else:
    print("⚠️ 验证失败")