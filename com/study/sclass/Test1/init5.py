import random

player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
enemy_list = ['【狂血敌人】', '【森林敌人】', '【光明敌人】', '【独行敌人】', '【格斗敌人】', '【枪弹敌人】']

players = random.sample(player_list, 3)
enemies = random.sample(enemy_list, 3)

player_info = {}
enemy_info = {}


# 随机生成两种属性
def born_role():
    life = random.randint(100, 180)
    attack = random.randint(30, 50)
    return life, attack


# 给角色赋予随机属性，并展示角色信息。
def show_role():
    for i in range(3):
        player_info[players[i]] = born_role()
    # 这里要给敌人角色信息的字典添加键值对

    print('----------------- 角色信息 -----------------')
    # 展示我方的3个角色
    print('你的人物：')
    for i in range(3):
        print('%s  血量：%d  攻击：%d' % (players[i], player_info[players[i]][0], player_info[players[i]][1]))
    print('--------------------------------------------')

    # 展示敌方3个角色，也是一个循环
    for i in range(3):
        enemy_info[enemies[i]] = born_role()

    print('----------------- 敌人信息 -----------------')  # 展示我方的3个角色
    print('电脑敌人：')
    for i in range(3):
        pass
        print('%s  血量：%d  攻击：%d' % (enemies[i], enemy_info[enemies[i]][0], enemy_info[enemies[i]][1]))


show_role()
