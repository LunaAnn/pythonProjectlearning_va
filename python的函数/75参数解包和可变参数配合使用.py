"""
    python的参数解包和可变参数一起使用
    注意: **参数只收集未匹配的关键字参数
"""

# def abc(a, *args):
#     print(a)
#     print(args)
# abc(100, *(1, 2, 3),)


d={
    "名字": "美女",
    "年龄": 18
}
def abc(a, **kwargs):
    print(a)
    print(kwargs)

abc(100, **d)