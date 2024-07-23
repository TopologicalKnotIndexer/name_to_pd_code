# 给定一个复合扭结的名字，获取他的 PD_CODE
# 复合扭结的名字为由若干个都好隔开的素扭结的名字

import re
from get_prime_knot_pd_code_by_name import get_prime_knot_pd_code_by_name
from solve_connected_sum            import solve_connected_sum

# 根据扭结的名字获取扭结的 PD_CODE
def get_knot_pd_code_by_name(composite_knot_name:str) -> list[list]:
    knotnames = [name.strip() for name in composite_knot_name.split(",")]
    for knotname in knotnames: # 合法性检查
        assert re.match(r"^(m|)K\d+(a|n)\d+$", knotname) is not None
    pd_code_list = [get_prime_knot_pd_code_by_name(knotname) for knotname in knotnames]
    for i in range(1, len(pd_code_list)): # 把所有 pd_code 都和第一个 pd_code 做连通和
        pd_code_list[0] = solve_connected_sum(pd_code_list[0], pd_code_list[i])
    return pd_code_list[0]

if __name__ == "__main__":
    print(get_knot_pd_code_by_name("K3a1,mK3a1"))