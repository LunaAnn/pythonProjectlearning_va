"""
python的数据类型强制转换:
    其他类型转数字类型中有一个特殊情况, 就是其他类型转布尔类型.
 bool() 可以把其他类型转为True或False
    1. 容器类型转布尔类型:
        容器类型数据   : 字符串, 列表, 元组, 字典, 集合
        非容器类型数据 : 数字类型, 布尔类型
        容器中为空   --> False
        容器中有元素 --> True
    2. 数字类型转布尔类型:
        int类型中, 0为False, 其他为真
        float类型中, 0.0为False, 其他为真
"""

a = "" #空字符串
b = [] #空列表
c = () #空元组
d = {} #空字典
e = set() #空集合
print(bool(a), bool(b), bool(c), bool(d), bool(e))
print("==========分隔符==========")
f = [123, 11]
print(bool(f))

aa = 0
ff = 0.0
print(bool(aa), bool(ff))