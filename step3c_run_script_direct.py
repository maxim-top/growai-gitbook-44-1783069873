import os
import sys
import re
import datetime
from pathlib import Path
# 设置工作目录
work_dir = r"D:\实习aipy\流量平台搭建\growai-gitbook"
os.chdir(work_dir)
sys.path.insert(0, work_dir)
# 导入脚本
from scripts.update_article_index import main
main()