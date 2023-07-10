"""
元组:
    1.元组也是一种数据容器,使用小括号"()"表示, 其使用场景与列表相似,
      这意味着能使用列表的地方, 基本上都能使用元组, 包括列表推导式\ 切片等操作.
      元组与列表的唯一区别是元组不可变
    2.元组的元素类型可以不统一
"""

t = ('hello', 66, -20, 3.66, [10, 20, 30])
print(t[1:40])