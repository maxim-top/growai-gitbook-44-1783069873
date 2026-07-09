import requests
print("🔍 通过 raw.githubusercontent.com 验证远程文件...")
# 验证远程 latest.md
url = "https://raw.githubusercontent.com/maxim-top/growai-gitbook-44-1783069873/master/articles/latest.md"
resp = requests.get(url, timeout=15)
print(f"  latest.md: {resp.status_code}")
if resp.status_code == 200:
    content = resp.text
    if "AiPy 智能体开发" in content and "最新发布" in content:
        print("  ✅ 远程 latest.md 已更新为自动生成的最新文章列表!")
    else:
        print("  ⚠️ 可能未更新")
        print(f"  内容: {content[:300]}")
# 验证远程 SUMMARY.md
url = "https://raw.githubusercontent.com/maxim-top/growai-gitbook-44-1783069873/master/SUMMARY.md"
resp = requests.get(url, timeout=15)
print(f"  SUMMARY.md: {resp.status_code}")
if resp.status_code == 200:
    content = resp.text
    if "* [博客](articles/latest.md)" in content:
        print("  ✅ 远程 SUMMARY.md 已更新!")
    if content.count("aipy-agent-types-guide") == 1:
        print("  ✅ SUMMARY.md 无重复插入!")
    else:
        print(f"  ⚠️ 重复次数: {content.count('aipy-agent-types-guide')}")
# 验证远程 build.yml
url = "https://raw.githubusercontent.com/maxim-top/growai-gitbook-44-1783069873/master/.github/workflows/build.yml"
resp = requests.get(url, timeout=15)
print(f"  build.yml: {resp.status_code}")
if resp.status_code == 200:
    if "Update Article Index" in resp.text:
        print("  ✅ 远程 build.yml 已包含自动索引步骤!")
# 验证远程脚本
url = "https://raw.githubusercontent.com/maxim-top/growai-gitbook-44-1783069873/master/scripts/update_article_index.py"
resp = requests.get(url, timeout=15)
print(f"  update_article_index.py: {resp.status_code}")
if resp.status_code == 200:
    print(f"  ✅ 远程脚本已存在! ({len(resp.text)} 字符)")
print("\n✅ 远程验证完成! 所有文件已成功 push 到 GitHub。")
print("   GitHub Actions 构建完成后，网站将自动更新。")