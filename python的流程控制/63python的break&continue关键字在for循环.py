"""
    break 语句可以跳出for 和 while的循环体/
    continue 语句被用来跳过当前循环块中的剩余语句, 然后继续进行下一轮循环.
"""

# for i in "python":
#     if i == "t":
#         break
#     print(i)
#
#
# for a in "python":
#     continue
#     print(a)
#     print("我爱你")

for i in "python":
    if i == "t":
        continue
    print("当前的字母是:", i)