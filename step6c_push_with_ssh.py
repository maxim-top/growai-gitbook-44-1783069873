import subprocess
import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
# 检查是否有 SSH 远程
result = subprocess.run(['git', 'remote', '-v'], capture_output=True, text=True, cwd=work_dir)
print("当前远程配置:")
print(result.stdout)
# 尝试添加 SSH 远程
result = subprocess.run(
    ['git', 'remote', 'set-url', 'origin', 'git@github.com:maxim-top/growai-gitbook-44-1783069873.git'],
    capture_output=True, text=True, cwd=work_dir
)
print(f"设置 SSH 远程: 返回码={result.returncode}")
if result.stderr:
    print(f"  {result.stderr}")
# 尝试 SSH 推送
print("\n🔄 尝试 SSH 推送...")
result = subprocess.run(['git', 'push', 'origin', 'master'], capture_output=True, text=True, cwd=work_dir, timeout=30)
print(result.stdout)
if result.stderr:
    print(f"  STDERR: {result.stderr}")
if result.returncode == 0:
    print("✅ SSH 推送成功！")
else:
    print("⚠️ SSH 推送也失败了，切换回 HTTPS")
    # 恢复 HTTPS
    subprocess.run(
        ['git', 'remote', 'set-url', 'origin', 'https://github.com/maxim-top/growai-gitbook-44-1783069873.git'],
        capture_output=True, text=True, cwd=work_dir
    )