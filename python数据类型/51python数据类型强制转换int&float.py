"""
python的数据类型强制转换:
    1.1 强制类型转换
        int(): 可以把其他类型数据转化为整型
        float(): 可以把其他类型数据转化为浮点型

    注意:
        *数字类型之间可以互相转换
        *只有字符串可以转换为数字类型
        *并且字符串中的元素必须为纯数字, 否贼无法转换
    布尔值也是数字
"""

a = 123
r_a = float(a)
print(r_a)

b = 3.67
r_b = int(b) #不遵循四舍五入的
print(r_b) #输出为3


c = True
r_c = int(c)
f_c = float(c)
print(r_c)
print(f_c)

d = False
r_d = int(d)
f_d = float(d)
print(r_d)
print(f_d)

e = "234"
r_e = int(e)
print(r_e)
print(type(r_e))

g = "1234.56"
f_g = float(g)
print(f_g, type(f_g))
r_g = int(f_g)
print(r_g)