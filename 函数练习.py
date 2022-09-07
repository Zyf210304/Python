"""
ATM 模拟函数
"""

user_name = "周杰伦"
sum = 5000000

name = input('请输入您的姓名')


def tips():
    print(f"{name}, 您好，欢迎使用ATM\n查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")


def title(title):
    print(f"-------------------{title}-------------------")


if name == user_name:
    use = True
    while use:
        tips()
        command = int(input('请输入指令'))
        if command == 1:
            title("查询余额")
            print(f"{name},您好，您的余额剩余:{sum}元")
        elif command == 2:
            title("存款")
            count = int(input('请输入您的存款金额'))
            if count >= 0:
                sum += count
                print(f"{name},您好，您的余额剩余:{sum}元")
            else:
                print("充值金额错误")
        elif command == 3:
            title("取款")
            count = int(input('请输入您的取款金额'))
            if count <= sum:
                sum -= count
                print(f"{name},您好，您的余额剩余:{sum}元")
            else:
                print("金额不足")
        else:
            title("退出")
            use = False
else:
    print("未查询到这个账号")
