import subprocess
import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
print("=" * 60)
print("🚀 提交到远程仓库")
print("=" * 60)
# 1. 检查状态
print("\n1️⃣  Git 状态:")
result = subprocess.run(['git', 'status'], capture_output=True, text=True, cwd=work_dir)
print(result.stdout)
# 2. 添加文件
print("\n2️⃣  Git add:")
result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True, cwd=work_dir)
print(f"  返回码: {result.returncode}")
if result.stderr:
    print(f"  STDERR: {result.stderr}")
# 3. 提交
print("\n3️⃣  Git commit:")
result = subprocess.run(
    ['git', 'commit', '-m', 'Add automatic article index sync for GitBook'],
    capture_output=True, text=True, cwd=work_dir
)
print(result.stdout)
if result.stderr:
    print(f"  STDERR: {result.stderr}")
# 4. 推送
print("\n4️⃣  Git push:")
result = subprocess.run(['git', 'push', 'origin', 'master'], capture_output=True, text=True, cwd=work_dir)
print(result.stdout)
if result.stderr:
    print(f"  STDERR: {result.stderr}")
# 5. 获取 commit hash
print("\n5️⃣  Commit Hash:")
result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, cwd=work_dir)
commit_hash = result.stdout.strip()
print(f"  {commit_hash}")
result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True, cwd=work_dir)
print(f"  Short: {result.stdout.strip()}")
print("\n" + "=" * 60)
print("✅ 推送完成！")
print("=" * 60)