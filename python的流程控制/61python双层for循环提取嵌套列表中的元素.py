"""
    python的双层for循环 if判断
    isinstance() 用来判断一个对象是否是一个已知的类型
"""

a = [1, 2, 3, [10, 20, 30], [50, 60, 70]]

for i in a:
    print(i)
    #判断, 满足条件 是否为列表

    if isinstance(i, list):
        #提取工作 列表中的数据
        for x in i:
            print(x)
