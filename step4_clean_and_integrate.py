import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
summary_path = os.path.join(work_dir, "SUMMARY.md")
# 读取当前内容
with open(summary_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"当前行数: {len(lines)}")
# 找到 articles 子目录的起始位置
articles_section_start = None
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('* [articles]') or stripped.startswith('* [最新]'):
        articles_section_start = i
        print(f"articles 子目录起始行: {i} -> '{stripped}'")
        break
# 删除 articles 子目录部分（从 articles_section_start 到文件末尾）
if articles_section_start:
    # 保留到 articles_section_start 之前的内容
    new_lines = lines[:articles_section_start]
    # 确保以换行结尾
    if new_lines and not new_lines[-1].endswith('\n'):
        new_lines[-1] += '\n'
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"✅ 已删除 articles 子目录重复内容（从行 {articles_section_start} 开始）")
    print(f"   新文件行数: {len(new_lines)}")
# 验证清理后的内容
print("\n📄 清理后的 SUMMARY.md:")
with open(summary_path, 'r', encoding='utf-8') as f:
    print(f.read())