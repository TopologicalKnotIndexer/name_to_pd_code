# 读取 pd_code_list 中的扭结数据
# 用于获取素扭结的名称
import os
import re
DIRNOW      = os.path.dirname(os.path.abspath(__file__))
PDCODE_FILE = os.path.join(DIRNOW, "pd_code_list", "data", "pd_code_list.txt")
assert os.path.isfile(PDCODE_FILE) # 检查数据文件是否存在

def __get_prime_knot_file_dict() -> dict: # 从文件中读取出扭结名称到 pd_code 的对应关系
    get_pd_code = {}
    for line in open(PDCODE_FILE):
        line = line.strip()
        if line == "" or line[0] == "#": # 跳过空行以及井号开头的行
            continue
        assert re.match(r"^\[K\d+(a|n)\d+\|.*\]$", line) is not None
        lpart, rpart = line[1:-1].split("|")
        lpart = lpart.strip()
        rpart = eval(rpart)
        assert get_pd_code.get(lpart) is None
        get_pd_code[lpart] = rpart # 记录每个扭结的 PD_CODE
    return get_pd_code

def __get_mirror_pd_code(pd_code: list) -> list: # 计算扭结的镜像扭结
    new_pd_code = []
    for a, b, c, d in pd_code: # 修改顺逆时针即可
        new_pd_code.append([a, d, c, b])
    return new_pd_code

def get_prime_knot_pd_code_by_name(knotname: str) -> list: # 给定一个扭结名称，获取其 PD_CODE，可以处理镜像扭结
    knotname = knotname.strip()
    assert re.match(r"^(m|)K\d+(a|n)\d+$", knotname) is not None # 检查扭结名称的合法性
    get_pd_code = __get_prime_knot_file_dict()
    mirror = False
    if knotname[0] == "m": # 去掉 mirror 标记
        knotname = knotname[1:]
        mirror   = True         # 最后需要记得将扭结做镜面反转
    assert get_pd_code.get(knotname) is not None
    pd_code = get_pd_code[knotname]
    if mirror:
        pd_code = __get_mirror_pd_code(pd_code) # 计算镜像扭结的 PD_CODE
    return pd_code

if __name__ == "__main__": # 测试
    print(get_prime_knot_pd_code_by_name("mK3a1"))