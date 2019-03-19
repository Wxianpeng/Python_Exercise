# 为专注于pk_role()函数，将前面代码做了简化，是我们前面已经实现的效果（默认你已经掌握了）。
# 注意代码的缩进、循环和判断条件的设定。

import time

# PK过程，还是有暂停效果比较好！

players = ['【狂血战士】', '【森林箭手】', '【光明骑士】']
enemies = ['【暗黑战士】', '【黑暗弩手】', '【暗夜骑士】']
player_info = {'【狂血战士】': (105, 35), '【森林箭手】': (105, 35), '【光明骑士】': (105, 35)}
enemy_info = {'【暗黑战士】': (105, 35), '【黑暗弩手】': (105, 35), '【暗夜骑士】': (105, 35)}
input('按回车开始简化版游戏：')


# 角色PK
def pk_role():
    round = 1  # 注：round表示局数。
    score = 0
    for i in range(3):  # 一共要打三局 i依次为0,1,2
        player_name = players[i]  # 统一将下面会用到的数据先赋值给变量会更清晰更好管理
        # 提取玩家角色名称
        enemy_name = enemies[i]
        player_life = player_info[players[i]][0]
        # 玩家血量是字典里的值（元组）的第0个元素，以下同理
        player_attack = player_info[players[i]][1]
        enemy_life = enemy_info[enemies[i]][0]
        enemy_attack = enemy_info[enemies[i]][1]

        # 每一局开战前展示战斗信息
        print('\n----------------- 【第%d局】 -----------------' % round)
        print('玩家角色：%s vs 敌方角色：%s ' % (player_name, enemy_name))
        print('%s 血量：%d  攻击：%d' % (player_name, player_life, player_attack))
        print('%s 血量：%d  攻击：%d' % (enemy_name, enemy_life, enemy_attack))
        print('--------------------------------------------')
        input('请按回车键继续。\n')

        # 双方血量都大于零，战斗过程会一直然后互扣血量。
        while player_life > 0 and enemy_life > 0:
            enemy_life = enemy_life - player_attack
            player_life = player_life - enemy_attack
            print('%s发起了攻击，%s剩余血量%d' % (player_name, enemy_name, enemy_life))
            print('%s发起了攻击，%s剩余血量%d' % (enemy_name, player_name, player_life))
            print('--------------------------------------------')
            time.sleep(1)
        else:  # 每局的战果展示，以及对分数score和局数round的影响。
            if player_life > 0 and enemy_life <= 0:
                print('\n敌人死翘翘了，你赢了！')
                score += 1  # 分数变化（1）
            elif player_life <= 0 and enemy_life > 0:
                print('\n悲催，敌人把你干掉了！')
                score += -1  # 分数变化（2）
                # 等价于score = score - 1
            else:
                print('\n哎呀，你和敌人同归于尽了！')
                score += 0  # 分数变化（3）
                # 这行不写也不影响
            round += 1  # 局数+1，直到循环完3局。
    input('\n点击回车，查看比赛的最终结果\n')
    if score > 0:
        print('【最终结果：你赢了！】\n')
    elif score < 0:
        print('【最终结果：你输了！】\n')
    else:
        print('【最终结果：平局！】\n')


pk_role()
