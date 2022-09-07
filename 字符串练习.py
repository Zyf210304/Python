""""
字符串练习
"""

my_str = "Hello hay!"

print(f"字符串{my_str}下标为2的元素{my_str[2]}和倒数第一个元素{my_str[-1]}")

# index方法
value = my_str.index("ll")
print(f"{str}中ll的初始坐标{value}")

# replace 方法
my_str2 = my_str.replace("l", "L")
print(my_str2)

# split方法
my_str = "123 234234 234"
my_str_list = my_str.split(" ")
print(my_str_list)

# strip方法  取出前后空格
my_str = "  asd  123 123asd  asd  "
print(my_str.strip())
my_str = "-+--------asd  123 123asd  asd  "
# 取出前后strip 参数里面的所有字符
print(my_str.strip("-+"))

# 统计字符串某字符出现的次数
print(my_str.count("a"))

# 统计字符串的长度
print(len(my_str))