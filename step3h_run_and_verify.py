import os
import sys
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
# 先备份当前 SUMMARY.md 并清理旧内容
summary_path = os.path.join(work_dir, "SUMMARY.md")
with open(summary_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
# 找到 articles 子目录部分的起始位置
articles_section_start = None
for i, line in enumerate(lines):
    if line.strip().startswith('* [articles]') or line.strip().startswith('* [最新]'):
        if articles_section_start is None:
            articles_section_start = i
# 保留博客行之前的内容 + 博客行本身，删除 articles 子目录部分
if articles_section_start:
    # 找到博客行
    blog_line = None
    for i, line in enumerate(lines):
        if line.strip() == '* [博客](articles/latest.md)':
            blog_line = i
            break
    # 保留博客行及之前的内容
    new_lines = lines[:blog_line + 1]
    # 添加案例和关于部分
    cases_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('* [案例]'):
            cases_start = i
            break
    if cases_start:
        new_lines.extend(lines[cases_start:])
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("✅ 已清理 SUMMARY.md 中的 articles 子目录重复内容")
# 现在运行脚本
sys.path.insert(0, work_dir)
if 'scripts.update_article_index' in sys.modules:
    del sys.modules['scripts.update_article_index']
from scripts.update_article_index import main
main()
# 验证最终结果
print("\n" + "=" * 60)
print("📄 最终 SUMMARY.md:")
with open(summary_path, 'r', encoding='utf-8') as f:
    print(f.read())
print("\n📄 最终 latest.md:")
latest_path = os.path.join(work_dir, "articles", "latest.md")
with open(latest_path, 'r', encoding='utf-8') as f:
    print(f.read())