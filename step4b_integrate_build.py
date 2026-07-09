import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
build_yml_path = os.path.join(work_dir, ".github", "workflows", "build.yml")
with open(build_yml_path, 'r', encoding='utf-8') as f:
    content = f.read()
# 在 "Install GitBook Deps" 和 "Build GitBook" 之间插入自动索引步骤
old = """    - name: Install GitBook Deps
      run: |
        cd ${{ github.workspace }}
        gitbook install
    - name: Build GitBook"""
new = """    - name: Install GitBook Deps
      run: |
        cd ${{ github.workspace }}
        gitbook install
    - name: Update Article Index
      run: |
        cd ${{ github.workspace }}
        python scripts/update_article_index.py
    - name: Build GitBook"""
if old in content:
    content = content.replace(old, new)
    with open(build_yml_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ 已添加自动索引步骤到 build.yml")
else:
    print("⚠️ 未找到匹配位置，手动检查 build.yml")
    print(content)