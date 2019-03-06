import random, time

playerVictory = 0
# 存放玩家赢的局数。
enemyVictory = 0
# 存放敌人赢的局数

for i in range(1, 4):

    time.sleep(2)
    print(' \n——————现在是第' + str(i) + '局，ready go!——————')  # 作为局的标记
    # 生成随机属性
    playerBlood = random.randint(100, 150)
    playerAttack = random.randint(30, 50)

    enemyBlood = random.randint(100, 150)
    enemyAttack = random.randint(30, 50)

    print("【玩家】\n血量%d:\n攻击力%d " % (playerBlood, playerAttack))
    print('------------------------')
    time.sleep(1)
    print("【敌人】\n血量%d:\n攻击力%d " % (enemyBlood, enemyAttack))
    print('------------------------')
    while (playerBlood > 0) and (enemyBlood > 0):
        playerBlood = playerBlood - enemyAttack
        enemyBlood = enemyBlood - playerAttack
        print('你发起了攻击，【敌人】剩余血量%d' % enemyBlood)
        print('敌人向你发起了攻击，【玩家】剩余血量%d' % playerBlood)
        print('------------------------')
        time.sleep(1.5)
        # 打印战果
        # 提示1:有三种结果，需要用到多向判断 if...elif...else
        # 提示2:判断条件为双方的血量情况
        # 打印战果
        if playerBlood > 0 >= enemyBlood:
            print('敌人死翘翘了，你赢了')
            playerVictory += 1
        elif playerBlood <= 0 < enemyBlood:
            print('悲催，敌人把你干掉了！')
            enemyVictory += 1
        else:
            print('哎呀，你和敌人同归于尽了！')

time.sleep(2)
if playerVictory > enemyVictory:
    print("玩家赢了")
elif playerVictory<enemyVictory:
    print("敌人赢了")
else:
    print("平局")
