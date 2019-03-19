import random

player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
players = random.sample(player_list, 3)
player_info = {}


# 随机生成属性，并用return语句保存属性信息
def born_role():
    life = random.randint(100, 180)
    attack = random.randint(30, 50)
    return life, attack


# 给角色生成随机属性，并展示角色信息。
def show_role():
    for i in range(3):
        player_info[players[i]] = born_role()

    # 展示我方的3个角色
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for i in range(3):
        print('%s  血量：%d  攻击：%d' % (players[i], player_info[players[i]][0], player_info[players[i]][1]))
    print('--------------------------------------------')


show_role()
