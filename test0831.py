print("不能摆烂")
print("Hello world")
print("Hello world")
print("不能摆烂")
print("\n\n\n")

#定义变量
money = 50
print("钱包出门时候的金额",money, "元")

#变量发生变化
money -= 10

#打印变量改变后的值
print("钱包剩余金额",money, "元")
print("\n\n\n")

"""
数据类型
"""
#使用print直接输出类型信息
print(type("加油不摆烂"))

#使用变量存储type()语句的结果
string_type = type("加油不摆烂")
int_type = type(3.14)
print(string_type)
print(int_type)

#查看变量的类型
name = "张三"
name_type = type(name)
print("name的类型是", name_type)

"""
数据类型转换

字符串不是都能转数字
整形和浮点型可以互相转换
浮点数转整数 向下取整
"""
#将数字类型转换为字符换
num_str = str(11)
print(type(num_str), num_str)

float_str = str(3.14)
print(type(num_str), float_str)

#将字符串转数字
str_int = int("11")
print(type(str_int), str_int)

str_float = float("3.14")
print(type(str_float), str_float)

#浮点数转整数
float_int = int(3.89)
print(type(float_int), float_int)


"""
运算符
"""
#**  指数 a**b a的b次方
print("3**4 =", 3**4)

"""
字符串的三种定义  
转义字符

print函数使用默认的分隔符' '，  sep=''
"""
str_1 = '不能摆烂'
str_2 = "不能摆烂"
str_3 = """
顶
摆烂不合适
不能摆
低
"""
print("\n", str_1, "\n", str_2, "\n", str_3, "\n", sep='')

#双引号包括的字符串
name = '"不能摆烂"'
print(name)
#单引号包裹的字符串
name = "'不能摆烂'"
print(name)
#使用转义字符 \ 接触引号的效果
name = "\"不能摆烂\""
print(name)

"""
字符串拼接

字符串不能和数字用"+"进行拼接
"""
# 字符串字面量之间的拼接  , sep=''
print("好好学习" + "天天向上")
print("好好学习", "天天向上")
print("好好学习", "天天向上", sep='')

#字符串字面量和字符串变量的拼接
name = "香菱"
pet = "锅巴"
number = 1
print(name +"的魔神宠物是" + pet + "，" + pet + "有" + str(number) + "个板凳那么高")


"""
字符串格式化
%s %d %f

"m.n"控制数据的宽度和精度
m控制宽度  n控制精度

开始格式f"内容{变量}" 快速格式化不支持精度控制

"""
name = "原神"
time = 10
message = "我玩%s%s个月了" % (name, time)
message2 = f"我玩{name}{time}个月了"
print(message)
print(message2)

number = 3.1415926
message = "圆周率是%.2f" % number
message2 = "圆周率是%5.2f" % number
print(message)
print(message2)

