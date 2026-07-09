import requests
print("🔍 详细验证远程文件...")
url = "https://raw.githubusercontent.com/maxim-top/growai-gitbook-44-1783069873/master/articles/latest.md"
resp = requests.get(url, timeout=15)
print(f"状态码: {resp.status_code}")
if resp.status_code == 200:
    content = resp.text
    print(f"内容长度: {len(content)} 字符")
    print(f"内容:")
    print(content)
    print("---")
    if "按时间发布" in content:
        print("✅ 包含「按时间发布」")
    if "按主题分类" in content:
        print("✅ 包含「按主题分类」")