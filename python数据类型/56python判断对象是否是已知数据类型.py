"""
    isinstance()用来判断一个对象是否是一个已知的类型
        isinstance()函数的返回值是布尔型,
        若对象的类型是已知的类型, 那么就返回True, 否则返回False

 语法如下:
    isinstance(对象, 对象类型)
    int(整数) float(浮点数) bool(布尔值) ... ...
"""

a = 123
print(isinstance(a, (int, float, str)))

b = 123.68
c = True
d = 'abc123我爱你'
