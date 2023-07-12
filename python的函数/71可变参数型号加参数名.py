"""
可变参数:
    *参数: 最常见的变量名是args, 看到该变量名, 一眼就知道变量args指向一个tuple对象
    自动收集所有未匹配的位置参数到一个tuple对象中, 变量名args指向了此tuple对象
"""

def abc(a, *b, c):
    print(a)
    print(b)
    print(c)

abc(100, 200, c = 400)