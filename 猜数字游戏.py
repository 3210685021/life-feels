import random
num_to_guess = random.randint(1, 100)
guess = 0
count = 0
while guess != num_to_guess:
    guess = int(input("请猜一个1到100之间的整数："))
    count += 1
    if guess > num_to_guess:
        print("猜大了，请再试一次！")
    elif guess < num_to_guess:
        print("猜小了，请再试一次！")
    else:
        print("恭喜你！你猜对了！")
        print("你猜了" + str(count) + "次。")