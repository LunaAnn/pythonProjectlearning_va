"""
    python的for循环语句:
        1 遍历字典的 键 和值
        2 range函数的步长
"""

d = {
    "名字" : "美女",
    "年龄" : 19
}

# for a in d:
#     print(a)

print(d.items())

for a in d.items():
    print(a)

# range()函数的步长 range(0, 4) -> 区间 0, 1, 2, 3
# range(0, 6, 2) ->

for i in range(0, 6, 2):
    print(i)