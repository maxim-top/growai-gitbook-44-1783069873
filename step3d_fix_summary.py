import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
summary_path = os.path.join(work_dir, "SUMMARY.md")
with open(summary_path, 'r', encoding='utf-8') as f:
    content = f.read()
print("📄 SUMMARY.md 完整内容:")
print("=" * 60)
for i, line in enumerate(content.split('\n')):
    print(f"{i:3d}: {line}")
print("=" * 60)
# 检查博客行
for i, line in enumerate(content.split('\n')):
    stripped = line.strip()
    if '博客' in stripped or 'latest' in stripped:
        print(f"\n行 {i}: '{line}'")
        print(f"  stripped: '{stripped}'")