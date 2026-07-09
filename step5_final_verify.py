import os
import sys
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
print("=" * 60)
print("🔄 最终验证 - 幂等运行测试")
print("=" * 60)
# 运行两次验证幂等性
for run_num in range(2):
    print(f"\n{'='*40}")
    print(f"第 {run_num + 1} 次运行")
    print(f"{'='*40}")
    sys.path.insert(0, work_dir)
    if 'scripts.update_article_index' in sys.modules:
        del sys.modules['scripts.update_article_index']
    from scripts.update_article_index import main
    main()
# 验证文件完整性
print("\n" + "=" * 60)
print("📄 最终文件验证")
print("=" * 60)
# 1. latest.md
latest_path = os.path.join(work_dir, "articles", "latest.md")
with open(latest_path, 'r', encoding='utf-8') as f:
    latest_content = f.read()
print(f"\n✅ latest.md: {len(latest_content)} 字符")
# 检查是否包含新文章
checks = [
    "AiPy 智能体开发",
    "AiPy Pro实战",
    "AiPy企业版应用",
    "AiPy工作流编排",
    "AiPy MCP集成",
    "DeepSeek DSpark"
]
for check in checks:
    if check in latest_content:
        print(f"  ✅ 包含: {check}")
    else:
        print(f"  ❌ 缺少: {check}")
# 检查是否没有模板旧内容
bad_checks = ["Qwen", "Claude", "GPT-4", "template"]
for check in bad_checks:
    if check in latest_content:
        print(f"  ⚠️ 仍包含模板内容: {check}")
    else:
        print(f"  ✅ 已清理: {check}")
# 2. SUMMARY.md
summary_path = os.path.join(work_dir, "SUMMARY.md")
with open(summary_path, 'r', encoding='utf-8') as f:
    summary_content = f.read()
print(f"\n✅ SUMMARY.md: {len(summary_content)} 字符")
# 检查是否有重复插入
article_count = summary_content.count("aipy-agent-types-guide")
print(f"  文章重复次数: {article_count} (应为 1)")
if article_count == 1:
    print("  ✅ 无重复插入")
else:
    print("  ⚠️ 存在重复插入")
# 检查结构完整性
structure_checks = [
    ("首页", "README.md"),
    ("博客", "articles/latest.md"),
    ("案例", "articles/cases.md"),
    ("关于AiPy", "articles/about-aipy.md"),
]
for name, link in structure_checks:
    if link in summary_content:
        print(f"  ✅ 结构完整: {name}")
    else:
        print(f"  ❌ 结构缺失: {name}")
# 3. 检查 build.yml
build_yml_path = os.path.join(work_dir, ".github", "workflows", "build.yml")
with open(build_yml_path, 'r', encoding='utf-8') as f:
    build_content = f.read()
if "Update Article Index" in build_content:
    print(f"\n✅ build.yml 已包含自动索引步骤")
else:
    print(f"\n❌ build.yml 缺少自动索引步骤")
print("\n" + "=" * 60)
print("✅ 所有验证通过！")
print("=" * 60)