"""
python的数据类型转换:
    1.1 检测数据类型方法:
        type()
    1.2 强制类型转换
        str(): 可以把其他类型数据转化为字符串类型
        注意:所有类型都可以转化为字符串类型
"""

a = "123"
b = 123
c = [1, 2, 3]
d = (1, 2, 3)
e = {1, 2, 3}
f = {
    "名字": "美女",
    "年龄": 18
}
g = True
h = 3.14
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print("========分割线========")
print(type("1,2,3"))
