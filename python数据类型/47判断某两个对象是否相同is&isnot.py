"""
    判断某两个对象是否相同, 则是用is和 is not 运算符
    is (是) 判断对象是否相同
    is not (不是) 判断对象是否不同

    数字 / 字符串 / 元组 都是不可变的数据类型 表面一样 完全一样
    列表 / 字典 / 集合  都是可变的数据类型 表面一样 其实不一样 其实不是同一个对象
"""

a = "美女"
b = "python"
print(a is not b)


c = " 111"
d = "111"
print(c is d) #得一模一样

f = [1]
g = [1]
print(f is g) #返回不一样

aa = {"名字": "美女"}
bb = {"名字": "美女"}
print(aa is bb)

ee = (1, 2, 3)
kk = (1, 2, 3)
print(ee is kk)

aaa = {1, 2, 3}
bbb = {1, 2, 3}
print(aaa is bbb)