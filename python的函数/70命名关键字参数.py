"""
函数的参数:
    限定关键字形参(命名关键字参数)
    特点: 必须使用关键字方式传递参数

    限定关键字形参, 当然就是为了限制后面几个参数只能按关键字传递,
    这往往是因为后面几个形参名具有十分明显的含义, 形式写出有利于可读性;
    或者后面几个形参随着版本更迭很可能发生变化,强制关键字形式有利于保证跨版本兼容性
"""
# def abc(a, b, c=600, d):  # 默认参数后面必须也是默认参数
#     print(a + b + c)
# abc(100, c=100, b=200, 300)


def abc(a, b=100, c= 200): # 默认参数后面必须也是默认参数
    print(a)
    print(b)
    print(c)

abc(100, c= 600, b= 700)

def ccd(e, *, g, h):
    print(e)
    print(g)
    print(h)
ccd(100, h=200, g=900)