"""
列表的操作方法:
    copy函数
    copy函数用于创建列表的副本
"""
a = ['hello', 'world', 'hello', 'python']
b = a.copy()
del a[0]
print('删除a[0]元素之后, 输出b列表:', b)
