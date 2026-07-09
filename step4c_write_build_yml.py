import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
build_yml_path = os.path.join(work_dir, ".github", "workflows", "build.yml")
with open(build_yml_path, 'r', encoding='utf-8') as f:
    content = f.read()
# 在 "Install GitBook Deps" 和 "Build GitBook" 之间插入
old = "    - name: Install GitBook Deps\n      run: |\n        cd ${{ github.workspace }}\n        gitbook install\n\n    - name: Build GitBook"
new = "    - name: Install GitBook Deps\n      run: |\n        cd ${{ github.workspace }}\n        gitbook install\n\n    - name: Update Article Index\n      run: |\n        cd ${{ github.workspace }}\n        python scripts/update_article_index.py\n\n    - name: Build GitBook"
if old in content:
    content = content.replace(old, new)
    with open(build_yml_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ 已添加自动索引步骤到 build.yml")
else:
    print("⚠️ 未找到，尝试另一种匹配...")
    # 读取并逐行处理
    lines = content.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(line)
        if 'gitbook install' in line and i + 1 < len(lines):
            # 检查下一行是否是 Build GitBook
            if 'Build GitBook' in lines[i + 1] or 'Build GitBook' in lines[i + 2]:
                # 插入自动索引步骤
                indent = line[:len(line) - len(line.lstrip())]
                new_lines.append('')
                new_lines.append(f'{indent}- name: Update Article Index')
                new_lines.append(f'{indent}  run: |')
                new_lines.append(f'{indent}    cd ${{{{ github.workspace }}}}')
                new_lines.append(f'{indent}    python scripts/update_article_index.py')
    content = '\n'.join(new_lines)
    with open(build_yml_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ 已通过逐行方式添加")
# 验证
with open(build_yml_path, 'r', encoding='utf-8') as f:
    print(f.read())