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
    #  获取玩家 和电脑人物列表:
    for j in range(3):
        player_info[players[j]] = born_role()
        enemy_info[enemies[j]] = born_role()


dict = {}


def order_play():
    for j in range(3):
        order = int(input('你要把' + players[j] + '放在第几位？（请输入数字1,2,3):'))
        dict[order] = players[j]

    print(dict)


show_role()

order_play()

print(players)
