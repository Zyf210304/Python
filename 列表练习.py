"""
列表
"""
mylist = ["嘻嘻", "哈哈", "嘿嘿"]
# 找到某元素在列表中的下标索引
index = mylist.index("嘻嘻")
print(f"嘿嘿在列表中的位置是{index}")
# 找到某元素在列表中的下标索引 错误
# index = mylist.index("嘻嘻222")
# print(f"嘿嘿在列表中的位置是{index}")

# 列表元素追加
mylist.append("哼哼")
print(mylist)

# 列表尾部追加一批新元素
mylist2 = [1, 2, 3]
mylist.extend(mylist2)
print(mylist)

# 删除列表指定位置元素
del mylist[2]
print(mylist)
ele = mylist.pop(2)     # pop取出元素
print(mylist, ele)

# 删除列表中第一个匹配元素
mylist = [1, 2, 3, 3, 4, 1, 5]
mylist.remove(3)
print(mylist)
mylist.remove(1)
print(mylist)

# 清空列表
mylist.clear()
print(mylist)

# 统计某个元素在列表中的数量
mylist = [1, 2, 3, 3, 4, 1, 5]
print(mylist.count(3))
print(len(mylist))

