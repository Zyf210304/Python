"""
range 语句
range(num)  从0到num 不到num
range(num1, num2) 从num1 到num2 不包含num2
range(num1, num2, step)   从num1 到num2 不包含num2 每个数字间隔step
"""
for x in range(10):
    print(str(x) + "\t", end='')

print("\n")
for y in range(5, 10):
    print(str(y) + "\t", end='')

print("\n")
for x in range(0, 10, 2):
     print(str(x) + "\t", end='')
