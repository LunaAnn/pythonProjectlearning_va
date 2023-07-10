"""
列表的操作方法:
    1.insert方法
        insert函数用于向列表中插入元素
        insert函数的第一个参数是插入的位置, 第二个参数是要插入的对象, 如下

    2.clear函数用于讲列表清空
"""

list_1 = [20, 30, 40, 50]

list_1.insert(2, [1, 2, 3])
print(list_1)

list_1.insert(1, 99)
print(list_1)

list_1.clear()
print(list_1)