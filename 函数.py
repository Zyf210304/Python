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
    global num  # 设置内部变量为全局变量
    num = 500
    print(f"text_b:{num}")


test_a()
test_b()
print(num)
test_c()
print(num)


# 函数多返回值
def test_return():
    return 1, "Hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)


def user_info(name, age, gender="男"):
    print(f"学生姓名：{name}，年龄是：{age}，性别是：{gender}")


user_info("张三", 18)
user_info(name="李四", age=34)
user_info(age=55, name="王五", gender="女")
user_info("赵六", gender="女", age=15)


# 不定长- 位置不定长， *号
# 不定长定义的形式参数会被作为元组存在 接受不定长数量参数传入
def user_info_args(*args):
    print(f"args参数类型是：{type(args)}，内容是：{args}")


user_info_args(1, 2, 3, "TOM")


# 不定长 关键字不定长 **号
def user_info_kwargs(**kwargs):
    print(f"args参数类型是：{type(kwargs)}，内容是：{kwargs}")


user_info_kwargs(name="TOM", age=15)


def test_func(compute):
    result = compute(1, 2)
    print(result)


# lambda 匿名函数
test_func(lambda x, y: x + y)
