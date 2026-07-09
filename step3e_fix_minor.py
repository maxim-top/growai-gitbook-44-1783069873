import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
script_path = os.path.join(work_dir, "scripts", "update_article_index.py")
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()
# 修复：在分类循环中，如果 items 为空则跳过空行
old = """    for category, items in categorized.items():
        if items:
            lines.append(f"### {category}")
            lines.append("")
            for filename, title in items:
                lines.append(f"- [{title}](./{filename})")
            lines.append("")"""
new = """    for category, items in categorized.items():
        if items:
            lines.append(f"### {category}")
            lines.append("")
            for filename, title in items:
                lines.append(f"- [{title}](./{filename})")
            lines.append("")
        else:
            # 跳过空分类
            pass"""
content = content.replace(old, new)
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("✅ 已修复空分类问题")
# 重新运行
import sys
if 'scripts.update_article_index' in sys.modules:
    del sys.modules['scripts.update_article_index']
from scripts.update_article_index import main
main()
# 验证
latest_path = os.path.join(work_dir, "articles", "latest.md")
with open(latest_path, 'r', encoding='utf-8') as f:
    content = f.read()
print("\n" + "=" * 60)
print("📄 最终排版:")
print(content)