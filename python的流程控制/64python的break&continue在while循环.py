"""
循环中的关键字:
    break 语句中可以跳出 for 和 while 的循环体.
    continue 语句被用来跳过当前循环快中的剩余语句, 然后继续进行下一轮循环.
"""

a = 0
while a < 6:
    a += 1
    if a == 3:
        continue
    # a += 1
    print("我爱你")