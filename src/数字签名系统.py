import os
import sys

def resource_path(relative_path):
    """获取资源的绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources')
    return os.path.join(base_path, relative_path) 