# name\_to\_pd\_code
将扭结名称转化为其标准 PD\_CODE。



## 前置条件

- `python3`



## 使用方式

- `python3 ./src/main.py`
  - 向标准输入流中输入一个扭结的名字（复合扭结使用逗号分隔的素扭结名字表示）
  - 如果扭结名字合法，且各个素分量能在 `pd_code_list` 中找到，则输出复合扭结的 PD\_CODE

