"""
列表的操作方法:
    1.index函数
    index函数用于返回所匹配的元素的索引, 该函数的第一个参数是待查找的对象,
    第二个参数是查找的起始范围, 第三个参数是查找的结束范围.

    2.reverse函数:
        reverse函数用于讲列表反向排列

"""

a = ['hello', 'world', 'hello', 'python']
r = a.index('hello') #仅仅只会匹配第一次
print(r)

r2 = a.index('hello', 1, 3)
print(r2) #返还的是在list内的下标而不是对应指定区间的下标

a.reverse()
print(a)