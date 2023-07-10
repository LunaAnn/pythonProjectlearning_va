"""
列表的操作方法:
    sort函数:
        sort函数用于讲列表进行排序
        ASCII码科普
        常见ASCII码的大小规则: 0~9<A~Z<a~z
        !! 只能是同类型的数据
"""

a = ['hello', 'world', 'hw', 'python']
b = [1, 2, 3, 5, 2, 1]
a.sort()
b.sort(reverse=True)
print(a)
print(b)