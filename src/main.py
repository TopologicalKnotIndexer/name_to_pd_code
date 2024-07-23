# 从标准输入输入一个扭结名称
# 如果扭结名称合法则输出这个扭结的 PD_CODE
# 如果扭结名称不合法或者出现了 pd_code_list 中未定义的素扭结分量则报错

import sys
from get_knot_pd_code_by_name import get_knot_pd_code_by_name

def main(): # 获取扭结的 PD_CODE 并输出到标准输出流
    inp = sys.stdin.read().strip()
    print(get_knot_pd_code_by_name(inp))

if __name__ == "__main__":
    main()