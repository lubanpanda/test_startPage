import pytest
'''
添加上级目录，原因pytest和pycharm运行环境不一致。
'''
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

with open('./logs/runlog.log', "r+") as f:
    f.truncate()  # 清空文件
