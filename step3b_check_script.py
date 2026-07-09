import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
script_path = os.path.join(work_dir, "scripts", "update_article_index.py")
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()
# 检查是否包含新函数
if "按时间和主题规整排版" in content:
    print("✅ 脚本已更新为新版本")
else:
    print("⚠️ 脚本仍为旧版本")
# 检查 generate_latest_md 函数
if "def generate_latest_md" in content:
    # 提取函数体
    start = content.find("def generate_latest_md")
    end = content.find("\ndef ", start + 1)
    if end == -1:
        end = len(content)
    func_body = content[start:end]
    print(f"\n📄 generate_latest_md 函数 ({len(func_body)} 字符):")
    print(func_body[:200])
    print("...")
    print(func_body[-200:])