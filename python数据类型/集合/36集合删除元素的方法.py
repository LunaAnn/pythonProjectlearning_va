"""
集合删除元素的方法:
    1,remove
    使用remove 删除集合中的元素, 如果有直接删除, 如果没有程序报错
    2,pop
    使用pop 删除是随机删除集合中的元素, 如果集合没有元素程序报错
    3,discard
    使用discard 删除, 如果元素存在直接删除, 如果元素不存在不错任何操作
"""

a = {"python", "学", "美女"}
# a.remove("python")
# print(a) #{'美女', '学'}

a.pop()
print(a)

b = {"1", "2", "3", "4", "5", "6"}
a.discard('9')
print(b)