#!/usr/bin/env python3
"""
自动文章索引同步脚本
功能：
1. 扫描 articles/ 目录下所有 .md 文件
2. 排除 README.md, latest.md, index.md, 模板文件
3. 自动提取标题（优先 # 标题，其次文件名）
4. 按日期排序（文件名中的日期或文件修改时间）
5. 生成 articles/latest.md（保留最近 20 篇）
6. 更新 SUMMARY.md 中「博客 → 最新文章」部分
7. 幂等执行，不重复插入，不破坏已有结构
"""
import os
import re
import datetime
from pathlib import Path
# ============ 配置 ============
PROJECT_DIR = Path(__file__).resolve().parent.parent
ARTICLES_DIR = PROJECT_DIR / "articles"
SUMMARY_FILE = PROJECT_DIR / "SUMMARY.md"
LATEST_FILE = ARTICLES_DIR / "latest.md"
MAX_ARTICLES = 20
# 需要排除的文件（不纳入文章列表）
EXCLUDE_FILES = {
    "README.md",
    "latest.md",
    "index.md",
}
# 需要排除的目录名
EXCLUDE_DIRS = {
    "latest",
    ".git",
}
# 文章分类关键词映射
CATEGORY_KEYWORDS = {
    "Agent 开发": ["agent", "智能体"],
    "Workflow": ["workflow", "工作流"],
    "MCP": ["mcp"],
    "RAG": ["rag"],
    "多模态": ["multimodal", "多模态", "视觉", "图片"],
    "LLM": ["llm", "大模型", "deepseek", "qwen", "claude", "gpt"],
    "Prompt Engineering": ["prompt", "提示词"],
}
def scan_articles():
    """
    扫描 articles/ 目录下所有 .md 文件
    返回: [(filename, filepath, title, date, category), ...]
    按日期降序排列
    """
    articles = []
    
    if not ARTICLES_DIR.exists():
        print(f"❌ 目录不存在: {ARTICLES_DIR}")
        return articles
    
    for f in ARTICLES_DIR.iterdir():
        if not f.is_file() or not f.name.endswith('.md'):
            continue
        
        # 排除文件
        if f.name in EXCLUDE_FILES:
            continue
        
        # 读取内容
        content = f.read_text(encoding='utf-8')
        
        # 提取标题
        title = extract_title(content, f.name)
        
        # 提取日期
        date = extract_date(f.name, f)
        
        # 分类
        category = classify_article(title, f.name)
        
        articles.append((f.name, f, title, date, category))
    
    # 按日期降序排序
    articles.sort(key=lambda x: x[3], reverse=True)
    
    return articles
def extract_title(content, filename):
    """从 Markdown 内容中提取标题"""
    # 优先匹配 # 一级标题
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    
    # 如果没有 # 标题，尝试 ## 标题
    match = re.search(r'^##\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    
    # 从文件名生成可读标题
    name = filename.replace('.md', '')
    # 移除日期和ID后缀
    name = re.sub(r'-\d{15,}$', '', name)
    name = re.sub(r'-\d{8}', '', name)
    # 将连字符替换为空格
    name = name.replace('-', ' ').replace('_', ' ')
    # 首字母大写
    return name.strip().title()
def extract_date(filename, filepath):
    """从文件名或文件修改时间提取日期"""
    # 尝试从文件名提取日期 (格式: YYYYMMDD)
    match = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
    if match:
        year, month, day = match.group(1), match.group(2), match.group(3)
        return f"{year}-{month}-{day}"
    
    # 使用文件修改时间
    mtime = os.path.getmtime(filepath)
    dt = datetime.datetime.fromtimestamp(mtime)
    return dt.strftime('%Y-%m-%d')
def classify_article(title, filename):
    """根据标题和文件名对文章进行分类"""
    text = (title + " " + filename).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text:
                return category
    return "其他"
def generate_latest_md(articles):
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
        else:
            # 跳过空分类
            pass
    
    # 页脚
    lines.append("---")
    lines.append("")
    lines.append("*持续更新中，敬请关注*")
    lines.append("*© 2026 AiPy | AI Agent Platform*")
    lines.append("")
    
    return "\n".join(lines)

def update_summary(articles):
    """
    更新 SUMMARY.md 中的「博客 → 最新文章」部分
    幂等操作：先删除旧的「最新文章」子项，再重新插入
    """
    if not SUMMARY_FILE.exists():
        print(f"❌ SUMMARY.md 不存在: {SUMMARY_FILE}")
        return False
    
    content = SUMMARY_FILE.read_text(encoding='utf-8')
    lines = content.split('\n')
    
    # 找到「博客」和「最新文章」所在行
    blog_line_idx = None
    latest_line_idx = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        # 匹配博客行 - 精确匹配 * [博客](articles/latest.md)
        if stripped == '* [博客](articles/latest.md)':
            blog_line_idx = i
        # 匹配最新文章行 - 精确匹配子项
        if stripped == '* [最新文章](articles/latest.md)':
            latest_line_idx = i
    
    if blog_line_idx is None:
        print("⚠️ 未找到「博客」行，跳过 SUMMARY.md 更新")
        return False
    
    # 删除旧的「最新文章」及其子项
    # 从 latest_line_idx 开始删除，直到遇到缩进级别小于或等于的行
    if latest_line_idx is not None:
        # 确定最新文章的缩进级别
        latest_indent = len(lines[latest_line_idx]) - len(lines[latest_line_idx].lstrip())
        
        # 找到删除范围的结束位置
        end_idx = latest_line_idx + 1
        while end_idx < len(lines):
            stripped = lines[end_idx].strip()
            if not stripped:
                end_idx += 1
                continue
            current_indent = len(lines[end_idx]) - len(lines[end_idx].lstrip())
            if current_indent <= latest_indent and stripped.startswith('*'):
                break
            end_idx += 1
        
        # 删除旧内容（保留最新文章行本身，后面会替换）
        del lines[latest_line_idx:end_idx]
    
    # 重新插入最新文章子项
    recent = articles[:MAX_ARTICLES]
    
    # 确定插入位置（在博客行之后）
    insert_idx = blog_line_idx + 1
    
    # 计算缩进（博客行的缩进 + 2空格）
    blog_indent = len(lines[blog_line_idx]) - len(lines[blog_line_idx].lstrip())
    
    # 构建要插入的行
    new_lines = []
    new_lines.append(f"{' ' * (blog_indent + 2)}* [最新文章](articles/latest.md)")
    for filename, _, title, _, _ in recent:
        new_lines.append(f"{' ' * (blog_indent + 4)}* [{title}](articles/{filename})")
    
    # 插入
    for i, line in enumerate(new_lines):
        lines.insert(insert_idx + i, line)
    
    # 写回文件
    SUMMARY_FILE.write_text('\n'.join(lines), encoding='utf-8')
    print(f"✅ SUMMARY.md 已更新，添加了 {len(recent)} 篇最新文章")
    return True
def main():
    """主入口"""
    print("=" * 50)
    print("🔄 自动文章索引同步脚本")
    print("=" * 50)
    
    # 1. 扫描文章
    print("\n📂 扫描 articles/ 目录...")
    articles = scan_articles()
    print(f"   找到 {len(articles)} 篇文章")
    
    if not articles:
        print("   ⚠️ 没有找到文章，跳过")
        return
    
    # 2. 生成 latest.md
    print("\n📝 生成 latest.md...")
    latest_content = generate_latest_md(articles)
    LATEST_FILE.write_text(latest_content, encoding='utf-8')
    print(f"   ✅ latest.md 已生成 ({len(latest_content)} 字符)")
    
    # 3. 更新 SUMMARY.md
    print("\n📑 更新 SUMMARY.md...")
    update_summary(articles)
    
    print("\n" + "=" * 50)
    print("✅ 自动索引同步完成！")
    print(f"   文章总数: {len(articles)}")
    print(f"   最新展示: {min(len(articles), MAX_ARTICLES)} 篇")
    print("=" * 50)
if __name__ == "__main__":
    main()