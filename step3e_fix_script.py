import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
script_path = os.path.join(work_dir, "scripts", "update_article_index.py")
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()
# 修复博客行匹配逻辑
old = """    for i, line in enumerate(lines):
        stripped = line.strip()
        # 匹配博客行
        if '* [博客]' in stripped and 'articles/latest.md' not in stripped:
            blog_line_idx = i
        # 匹配最新文章行
        if '* [最新文章](articles/latest.md)' in stripped or '* [最新文章]' in stripped:
            latest_line_idx = i"""
new = """    for i, line in enumerate(lines):
        stripped = line.strip()
        # 匹配博客行 - 精确匹配 * [博客](articles/latest.md)
        if stripped == '* [博客](articles/latest.md)':
            blog_line_idx = i
        # 匹配最新文章行 - 精确匹配子项
        if stripped == '* [最新文章](articles/latest.md)':
            latest_line_idx = i"""
content = content.replace(old, new)
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ 脚本已修复")