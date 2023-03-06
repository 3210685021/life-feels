import random
# 生成随机年龄
age = random.randint(1, 100)
# 猜年龄游戏
print("猜猜我今年多少岁？")
while True:
    guess = int(input("请输入您猜测的年龄："))
    if guess == age:
        print("恭喜您，猜对了！")
        break
    elif guess < age:
        print("猜小了，请再试一次。")
    else:
        print("猜大了，请再试一次。")