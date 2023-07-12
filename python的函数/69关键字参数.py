"""
函数的参数
    3. 关键字参数
        函数调用时, 指定参数名称, 称为关键字参数
        (不要和默认参数混淆, 这里是函数调用)

        注意: 函数嗲用时, 关键字参数必须在普通参数的后面
"""


def abc(x, a = 100, b = 200): # 默认参数, 函数定义的时候传参
    print(a + b)

abc(100, a = 200, b = 600)  #关键参数(这里指a = b=)要在普通函数的后面  ##!!关键字参数, 函数调用的时候
