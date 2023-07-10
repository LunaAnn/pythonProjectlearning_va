"""
python的条件语句:
    if...elif...else...分支语句
"""

a = int(input("请输入你的成绩:"))
if a >= 90:
    print("优秀")
elif a >= 75:
    print("良好")
elif a >= 60:
    print("及格")
else:
    print("不及格")
