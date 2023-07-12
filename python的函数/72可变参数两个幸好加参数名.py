"""
可变参数:
    **参数: 最常见的变量名是kwargs, 看到该变量名, 一眼就知道变量kwargs指向一个dict对象
    自动手机所有未匹配的关键字参数到一个dict对象中, 变量名kwargs指向了此dict对象
"""

def abc(a, **b):
    print(a)
    print(b)   # 指向的是 空字典 {} 键值对

abc(100, x= 200, k= 300)