"""
字典的操作方法:
    5 clear函数
        clear函数用于讲字典清空
    6 copy函数
        copy函数用于创建字典的副本, 修改原字典对象, 不会影响其副本
"""

d = {
    "名字": "美女",
    "年龄": "18"
}
d.clear()
print(d)
print(len(d))

d2 = {
    "名字": "美女",
    "年龄": "18"
}
d3 = d2.copy()
del d2["名字"]
print(d2)
print(d3)