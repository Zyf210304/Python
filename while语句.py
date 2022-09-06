"""
while 条件:
    循环体
"""

# sum = 0
# i = 0
# while i < 100:
#     print("i = ", i)
#     i += 1
#     sum += i
#
# print(str(sum))

number_x = 1
while number_x < 10:
    number_y = 1
    while number_y <= number_x:
        if number_x == number_y:
            str = "%d * %d = %d" % (number_x, number_y, number_x * number_y)
            print(str)
        else:
            str = "%d * %d = %d\t" % (number_x, number_y, number_x * number_y)
            print(str, end='')
        number_y += 1
    number_x += 1

""""
for 循环只有 for -in 
"""
str = "itheima is a brand if itcast"
number = 0
for chart in str:
    if chart == "a":
        number += 1

print(f"总共{number}个a")

import random
sum = 10000
for x in range(1, 21):

    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{x},绩效{num}, 低于5，不发工资，下一位")
        continue
    else:
        sum -= 1000
        print(f"向员工{x}发放工资1000元，账户余额{sum}元")

    if sum == 0:
      print("工资发放完毕，下月领取吧")
      break
