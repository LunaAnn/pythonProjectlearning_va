"""
函数的参数
    2. 默认参数
        默认参数是指带有默认值的参数, 在对该函数进行调用的时候,
      可以不必显示传递给该函数. 当不传递值的时候, 函数将使用默认值.

        注意: 默认值只能会执行一次这条规则在默认值为可变对象
            (列表\ 字典以及大多数类的实例)时非常需要
                官方默认参数尽量使用不可变对象!!
                因为可变对象会存储后再后续调用中传递给他的参数
"""
#
# def abc(a = 300, b = 400):
#     print(a+b)
#
# # abc(b = 1000)      #指定一个默认参数进行传值
#
# # abc()              # 为两个默认参数都传入值
#
# # abc(600)           #为第一个默认参数传入值, 另一个默认参数继续使用默认值
#
# # abc()              #省略传入所有参数, 函数会使用默认参数的默认值

# def abc(a, b= []):  #列表是可变对象
#     b.append(a)
#     print(b)
#
# abc(100) #[100]
# abc(200) #期待的是[200]  但是得到的是: [100, 200]

def abc(a, b= None):
    if b is None:
        b = []
    b.append(a)
    print(b)

abc(100)  #[100]
abc(200)