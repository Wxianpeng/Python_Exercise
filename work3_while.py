import random

# 打印三角形
# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print("*", end="")
#
#         j += 1
#     print("")
#     i += 1
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")

        j += 1
    print("")
    i += 1


# 打印乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        # \t  一个table 键
        print("%d*%d=%d\t" % (j, i, i * j), end="")
        j += 1
    print("")
    i += 1
# 猜拳
# player = int(input("请输入0剪刀 1石头 2 布\n"))
# computer = int(random.randint(0, 2))
#
# if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
#     print("恭喜你赢了，电脑出了%d" % (computer))
# elif player == computer:
#     print("平局，电脑出了%d" % (computer))
# else:
#     print("输了，电脑出了%d" % (computer))
