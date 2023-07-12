"""
    python的函数返回函数
        1. 函数里面嵌套函数
        2. 函数返回函数
"""

def abc():
    def xyz():
        return [1, 2, 3]
    return xyz

r = abc()  #r接收的是一个函数  xyz这个函数
r2 = r()
print(r2)