import os
import subprocess
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
# 检查本地 latest.md
latest_path = os.path.join(work_dir, "articles", "latest.md")
with open(latest_path, 'r', encoding='utf-8') as f:
    local_content = f.read()
if "按时间发布" in local_content:
    print("✅ 本地 latest.md 是新排版")
else:
    print("⚠️ 本地 latest.md 是旧排版，需要重新运行脚本")
    # 重新运行脚本
    import sys
    sys.path.insert(0, work_dir)
    if 'scripts.update_article_index' in sys.modules:
        del sys.modules['scripts.update_article_index']
    from scripts.update_article_index import main
    main()
# 检查本地脚本
script_path = os.path.join(work_dir, "scripts", "update_article_index.py")
with open(script_path, 'r', encoding='utf-8') as f:
    script_content = f.read()
if "按时间和主题规整排版" in script_content:
    print("✅ 本地脚本已更新")
else:
    print("⚠️ 本地脚本未更新")
# 重新 add, commit, push
print("\n🔄 重新提交...")
subprocess.run(['git', 'remote', 'set-url', 'origin', 'git@github.com:maxim-top/growai-gitbook-44-1783069873.git'],
    capture_output=True, text=True, cwd=work_dir)
subprocess.run(['git', 'add', '.'], capture_output=True, text=True, cwd=work_dir)
result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True, cwd=work_dir)
print(f"未提交文件:\n{result.stdout}")
result = subprocess.run(
    ['git', 'commit', '-m', 'Fix latest.md layout: organize by date and topic'],
    capture_output=True, text=True, cwd=work_dir
)
print(result.stdout)
if result.stderr:
    print(f"  {result.stderr}")
result = subprocess.run(['git', 'push', 'origin', 'master'], capture_output=True, text=True, cwd=work_dir, timeout=30)
print(result.stdout)
if result.stderr:
    print(f"  {result.stderr}")
if result.returncode == 0:
    print("✅ 推送成功！")
# 恢复 HTTPS
subprocess.run(
    ['git', 'remote', 'set-url', 'origin', 'https://github.com/maxim-top/growai-gitbook-44-1783069873.git'],
    capture_output=True, text=True, cwd=work_dir
)
# 获取 commit
result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True, cwd=work_dir)
short_hash = result.stdout.strip()
print(f"\n📋 Commit: {short_hash}")