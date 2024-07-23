# 桥接：https://github.com/TopologicalKnotIndexer/connected_sum
import os
DIRNOW = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.path.join(DIRNOW, "connected_sum", "src") # 子包路径

# ======================================== BEGIN IMPORT FROM PATH ======================================== #
import importlib
import json
import sys
def load_module_from_path(path: str, mod_name: str): # 从指定路径导入一个包
    assert os.path.isdir(path)                       # 路径必须存在
    path         = os.path.abspath(path)             # 获得绝对路径
    old_sys_path = json.loads(json.dumps(sys.path))  # 存档旧的 sys.path
    sys.path     = [path] + sys.path                 # 将新的路径加入 sys.path
    mod          = importlib.import_module(mod_name) # 加载指定的包
    sys.path     = old_sys_path                      # 恢复旧的 sys.path
    return mod
# ======================================== END IMPORT FROM PATH ======================================== #

# 计算扭结连通和
def solve_connected_sum(pd_code1: list, pd_code2: list) -> list:
    return load_module_from_path(SUBDIR, "connected_sum").connected_sum(pd_code1, pd_code2)

if __name__ == "__main__": # 测试
    print(solve_connected_sum(
        [[4, 2, 5, 1], [8, 6, 1, 5], [6, 3, 7, 4], [2, 7, 3, 8]],
        [[1, 5, 2, 4], [3, 9, 4, 8], [5, 1, 6, 10], [7, 3, 8, 2], [9, 7, 10, 6]]
    ))