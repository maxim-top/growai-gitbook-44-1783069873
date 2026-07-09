import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
script_path = os.path.join(work_dir, "scripts", "update_article_index.py")
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()
# 修复 update_summary 函数 - 删除旧内容后重新插入时，要正确处理博客行和最新文章行的关系
old = """    # 重新插入最新文章子项
    recent = articles[:MAX_ARTICLES]
    
    # 确定插入位置（在博客行之后）
    insert_idx = blog_line_idx + 1
    
    # 计算缩进（博客行的缩进 + 2空格）
    blog_indent = len(lines[blog_line_idx]) - len(lines[blog_line_idx].lstrip())
    article_indent = blog_indent + 2
    
    # 构建要插入的行
    new_lines = []
    new_lines.append(f"{' ' * blog_indent}* [最新文章](articles/latest.md)")
    for filename, _, title, _, _ in recent:
        new_lines.append(f"{' ' * (blog_indent + 2)}* [{title}](articles/{filename})")
    
    # 插入
    for i, line in enumerate(new_lines):
        lines.insert(insert_idx + i, line)"""
new = """    # 重新插入最新文章子项
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
        lines.insert(insert_idx + i, line)"""
content = content.replace(old, new)
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ 缩进格式已修复")