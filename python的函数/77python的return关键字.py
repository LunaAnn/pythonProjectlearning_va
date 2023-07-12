"""
函数的返回值
    python中的函数可以使用return返回数据, 也可以不用return返回, 则默认返回"None
    return 关键字, 用来函数执行的时候, 帮助我们返回我们处理好的结果
"""
def ggb():
    print("hello")
r = ggb()       # 函数调用的返回值, 可以用变量接收
print(r)

def abc(a):
    return a+100

p= abc(900)
print(p)

#用return关键字, 返回多个数据

def zzz(n, m, b):
    return n+ 100, m+200, b+ 300
qq = zzz(100, 200, 300)
print(qq)       #返回的是一个元组数据类型(200, 400, 600)
print(type(qq))

l, k, j = qq
print(l)
print(k)
print(j)