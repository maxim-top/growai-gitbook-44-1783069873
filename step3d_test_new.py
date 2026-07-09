import os
import sys
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
sys.path.insert(0, work_dir)
if 'scripts.update_article_index' in sys.modules:
    del sys.modules['scripts.update_article_index']
from scripts.update_article_index import main
main()
# 验证结果
print("\n" + "=" * 60)
print("📄 新排版 latest.md:")
latest_path = os.path.join(work_dir, "articles", "latest.md")
with open(latest_path, 'r', encoding='utf-8') as f:
    content = f.read()
print(content)
print("=" * 60)
# 检查排版结构
print("\n📊 排版结构分析:")
sections = content.split('## ')
for s in sections:
    if s.strip():
        lines = s.strip().split('\n')
        print(f"  ## {lines[0]} ({len(lines)} 行)")