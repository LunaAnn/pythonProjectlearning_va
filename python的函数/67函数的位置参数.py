"""
函数的参数
    python函数的参数具有灵活性, 其定义的方法可以接受各种形式的参数,
  也可以简化函数调用方法的代码.
    0. 函数中的pass关键字   保持代码结构完整性
    1. 位置参数
        在对函数进行调用饿时候, 有及格位置参数就需要传递几个参数,
        否则会出发异常. 并且, 传入参数与函数参数列表是意义对象的
    2. 默认参数
    3. 可选参数
    4. 可变参数与关键字参数
"""

def abc(a , b):
    print(a + b)

abc("我爱你", "美女 ") #传入的参数可以使任何的数据类型
                     #注意 : 函数, 先定义函数, 再调用