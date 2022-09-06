"""
函数定义

def 函数名(传入参数):
    函数体
    return 返回值
"""


def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}长度为{count}")


str1 = "1231245asd"
my_len(str1)


def add(a, b):
    """
    add 求和函数
    :param a: 形参a相加的其中一个数字
    :param b: 形参b相加的另一个数字
    :return: 返回两者的和
    """
    result = a + b
    return result


print(add(1, 2))

# 在函数内修改全局变量
num = 200


def test_a():
    print(f"text_a:{num}")


def test_b():
    num = 500
    print(f"text_b:{num}")


def test_c():
    global  num #设置内部变量为全局变量
    num = 500
    print(f"text_b:{num}")


test_a()
test_b()
print(num)
test_c()
print(num)
