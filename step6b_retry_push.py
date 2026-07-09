import subprocess
import os
import time
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
print("🔄 重试推送...")
for attempt in range(3):
    print(f"\n尝试 {attempt + 1}/3...")
    result = subprocess.run(['git', 'push', 'origin', 'master'], capture_output=True, text=True, cwd=work_dir, timeout=60)
    print(result.stdout)
    if result.stderr:
        print(f"  STDERR: {result.stderr}")
    if result.returncode == 0:
        print("✅ 推送成功！")
        break
    else:
        print(f"  ⚠️ 失败，等待重试...")
        time.sleep(5)