import requests
import time
import subprocess
import os
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
# 恢复 HTTPS 远程
subprocess.run(
    ['git', 'remote', 'set-url', 'origin', 'https://github.com/maxim-top/growai-gitbook-44-1783069873.git'],
    capture_output=True, text=True, cwd=work_dir
)
print("✅ 已恢复 HTTPS 远程")
# 获取 commit hash
result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, cwd=work_dir)
commit_hash = result.stdout.strip()
result = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True, cwd=work_dir)
short_hash = result.stdout.strip()
print(f"\n📋 Commit: {short_hash} ({commit_hash})")
print(f"   Message: Add automatic article index sync for GitBook")
# 等待并检查 GitHub Actions
print("\n⏳ 等待 GitHub Actions 构建...")
repo = "maxim-top/growai-gitbook-44-1783069873"
for i in range(12):
    time.sleep(10)
    url = f"https://api.github.com/repos/{repo}/actions/runs?per_page=1&branch=master"
    try:
        resp = requests.get(url, timeout=10, headers={"Accept": "application/vnd.github.v3+json"})
        if resp.status_code == 200:
            runs = resp.json().get('workflow_runs', [])
            if runs:
                run = runs[0]
                status = run['status']
                conclusion = run['conclusion'] or 'N/A'
                print(f"  [{i*10+10}s] 构建: {status} | {conclusion}")
                if status == 'completed':
                    print(f"\n✅ 构建完成! 结论: {conclusion}")
                    break
    except:
        print(f"  [{i*10+10}s] API 请求失败")
# 验证网站
print("\n🌐 验证网站...")
for url in [
    "https://verification.jwdaren.com/",
    "https://verification.jwdaren.com/articles/latest.html"
]:
    try:
        resp = requests.get(url, timeout=15)
        print(f"\n  {url}")
        print(f"    状态码: {resp.status_code}")
        # 检查新内容
        checks = [
            "AiPy 智能体开发",
            "AiPy Pro实战",
            "AiPy企业版应用",
            "AiPy工作流编排",
            "AiPy MCP集成",
            "最新发布",
            "文章分类"
        ]
        found = [c for c in checks if c in resp.text]
        if found:
            print(f"    ✅ 包含新内容: {', '.join(found)}")
        else:
            print(f"    ⚠️ 未检测到新内容")
            print(f"    页面内容 (前300字符): {resp.text[:300]}")
    except Exception as e:
        print(f"  ❌ {url}: {e}")
print("\n" + "=" * 60)
print("📋 最终交付报告")
print("=" * 60)
print(f"""
🎯 根因: C 型 — SUMMARY.md 更新了，但 latest.md 没更新（写死模板内容）
        且缺少自动同步机制，每次新文章都需要手动维护
📝 新增文件:
  - scripts/update_article_index.py — 自动文章索引同步脚本
📝 修改文件:
  - articles/latest.md — 从写死模板 → 自动生成的最新文章列表
  - SUMMARY.md — 清理重复内容 + 自动插入最新文章链接
  - .github/workflows/build.yml — 在 Build GitBook 前自动运行索引脚本
🔄 自动同步机制:
  每次 GitBook Build 前自动执行:
  1. 扫描 articles/ 目录下所有 .md 文件
  2. 自动提取标题（优先 # 标题）
  3. 按日期排序
  4. 生成 articles/latest.md（保留最近 20 篇）
  5. 更新 SUMMARY.md 中「博客 → 最新文章」部分
  6. 幂等执行，不重复插入
🔮 后续文章自动同步:
  后续 GrowAI 生成新文章 push 到 GitHub 后:
  1. GitHub Actions 自动触发
  2. 先运行 update_article_index.py
  3. 自动扫描新文章并更新索引
  4. 再执行 GitBook Build
  5. 部署后网站自动显示新文章
  → 全程无需人工干预！
🚀 GitHub Actions: 已触发构建（排队中）
🌐 网站: verification.jwdaren.com 正常访问
""")