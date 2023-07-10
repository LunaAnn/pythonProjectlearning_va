"""
字典的操作方法:
    9 popitem函数
        popitem函数用于从字典中删除最后一项, 并以元组形式返回该项所对应的键和值
    10 setdefault函数
        setdefault函数用于设置键的默认值,
        若在字典中该键已经存在, 则忽略设置; 若不存在, 则添加该键和值
        d.setdefault(键, 值)
"""
d = {
    "名字" : "美女",
    "年龄" : 18
}
r = d.popitem()
print(r)
print(d)

d2 = {
    "名字" : "美女",
    "年龄" : 18
}
d2.setdefault("技能", "python")
print(d2)
d2.setdefault("名字", "小明") #不会添加操作

d3 = {
    "名字" : "美女",
    "名字" : "小明"
}
print(d3) #{'名字': '小明'}字典当遇到相同键的赋值时, 会覆盖前一个值