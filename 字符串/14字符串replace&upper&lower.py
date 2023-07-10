"""
字符串常用方法:
    replace: 替换指定的字符串片段
    参数1: 要替换的字符串片段
    参数2: 替换之后的字符串片段
    参数3: 替换的次数, 从前往后替换(默认替换所有的)

    upper:将小写字母转为大写
    lower:讲大写字母转成小写


"""

s1 = 'python to muzhou'
res = s1.replace('o', 'TT')
print(res)


res1 = s1.replace('o', 'TT', 2)
print(res1)

res2 = res.upper()
print(res2)

res4 = res2.lower()