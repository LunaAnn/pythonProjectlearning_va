"""

字符串的方法:
    split: 制定分割点对字符串进行分割
    参数1: 分割点 (切割的内容会被吞噬)
    参数2: 分割的次数(默认找到所有的分割点进行分割)

    strip: 去除字符串收尾的空格
    s2 = '  python:666  '

"""

s1 = "111ab222ab333ab444"
# 将字符串, 用规定的字符"a"进行分割, 得到一个列长
print(s1.split('a'))

s1 = "111ab222ab333ab444"
print(s1.split('a', 2))

s2 = '     python:666     '
print(s2.strip()) #去除字符串的收尾空格

s3 = '6666python:6666'
print(s3.strip('6'))

s4 = '      python:666      muzhou:777777'
print(s4.replace(' ', ''))
