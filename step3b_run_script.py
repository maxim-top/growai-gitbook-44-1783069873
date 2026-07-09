import subprocess
import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
result = subprocess.run(
    ['python', 'scripts/update_article_index.py'],
    capture_output=True, text=True, cwd=work_dir
)
print(result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)