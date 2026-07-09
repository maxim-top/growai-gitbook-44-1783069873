import subprocess
import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
print("🔄 先 pull 再 push...")
# 切换到 SSH
subprocess.run(
    ['git', 'remote', 'set-url', 'origin', 'git@github.com:maxim-top/growai-gitbook-44-1783069873.git'],
    capture_output=True, text=True, cwd=work_dir
)
# pull
result = subprocess.run(['git', 'pull', 'origin', 'master', '--rebase'], capture_output=True, text=True, cwd=work_dir, timeout=30)
print(result.stdout)
if result.stderr:
    print(f"  {result.stderr}")
# push
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
result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, cwd=work_dir)
full_hash = result.stdout.strip()
print(f"\n📋 Commit: {short_hash} ({full_hash})")
# 验证远程
import requests
print("\n🔍 验证远程文件...")
url = "https://raw.githubusercontent.com/maxim-top/growai-gitbook-44-1783069873/master/articles/latest.md"
resp = requests.get(url, timeout=15)
if resp.status_code == 200:
    content = resp.text
    if "按时间发布" in content and "按主题分类" in content:
        print("✅ 远程 latest.md 已更新为新排版!")
        print(f"\n📄 远程内容预览:")
        print(content[:500])
    else:
        print("⚠️ 可能未更新")