"""
    函数中各种参数排列位置的注意事项
    1. 可变参数, 必须定义在普通参数以及默认值参数的后面
    2. 函数定义时, 二者同时存在, 一定需要将*args放在**kwargs之前
    def abc(普通参数, 默认值参数name = "美女", *参数, **参数):
        pass
"""

def abc(a, name = "美女", *args, **kwargs):
    print(a)
    print(name)
    print(args)     #(1, 2, 3, 4)
    for i in (args):
        print(i)
    print(kwargs)   #{'x': 100, 'y': 200, 'z': 300}
    for key, value in kwargs.items():
        print(key)
        print(value)

abc(100, "少妇", 1, 2, 3, 4, x = 100, y=200, z= 300)