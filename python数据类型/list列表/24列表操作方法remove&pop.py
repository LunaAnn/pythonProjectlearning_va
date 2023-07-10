"""
列表操作方法:
    1.remove函数
        remove函数用于从列表移除元素
    注意:(执行结果如下, 可以看到, 若列表中有重复元素, remove函数只会移除匹配到的第一个)

    2.pop函数
    pop函数用于移除列表中指定位置的元素, 并返回要移除的元素
    在默认情况下, 移除列表中最后一个元素
"""

a = ['hello', 'world', 'python', 'hello']
a.remove('hello')
print(a) #['world', 'python', 'hello']

a.pop(2) #参数是下标
print(a)

print('输出要移除的数据:', a.pop(0))
print('已经更改后的列表:', a)