""""
if 语句
if的内容
    需要缩进
"""

"""
age = input("请输入年龄")

if int(age) >= 18:
    print("已经成年了")
    print("加油")
else:
    print("年轻人 好好玩")


print(f"时间过得好快啊 已经{age}岁了");
"""

# if int(input("你的身高是多少")) > 120:
#     print("身高超过限制，不可以免费游玩")
#     print("可以根据VIP等级判断是否可以免费")
#
#     if int(input("你的vip的等级是多少")) >=3:
#         print("vip等级达标，可以免费")
#     else:
#         print("游览需要买票10元")
# else:
#     print("欢迎小朋友前来游玩")

import  random
num = random.randint(1, 10)
print(num)

number = int(input("请猜一个数字1-10"))
if number != num:
    if number > num:
        print("数字猜大了")
    else:
        print("数字猜小了")

    number = int(input("请再试输入要菜的数字"))
    if number == num:
        print("猜对了")
    else:
        if number > num:
            print("数字猜大了")
        else:
            print("数字猜小了")
        number = int(input("请再试输入要菜的数字"))
        if number == num:
            print("猜对了")
        else:
            if number > num:
                print("数字猜大了正确数字是" + str(num))
            else:
                print("数字猜小了正确数字是" + str(num))

else:
    print("猜对了")
