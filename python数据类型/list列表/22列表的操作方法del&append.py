"""
列表的操作方法:
    1.del关键字  删除
    2.append方法
        append函数用于向列表末尾添加元素
"""
a = [1, 2, 3]
# del a # 在计算机当中 a变量定义列表 删除
# print(a)  这里会报错因为 因为a列表已经不存在
del a[1] #删除掉 列表中的指定值
print(a)
a.append(4)
print(a)
