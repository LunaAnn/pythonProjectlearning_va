"""
字典的操作方法:
    3 items函数
        items函数将以列表的形式返回字典中的所有键值对
    4 values函数
        values函数将以列表的形式返回字典中的所有值, 如下
"""

d = {
    "名字": "美女",
    "年龄": "18"
}
r = d.items()
r1 = d.values()
print(r)
print(r1)