import time


# 展示角色
def show_role(player_life, player_attack, enemy_life, enemy_attack):
    print('【玩家】\n血量：%s\n攻击：%s' % (player_life, player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life, enemy_attack))
    print('-----------------------')


# 双方PK
def pk_role(player_life, player_attack, enemy_life, enemy_attack):
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        time.sleep(1)
        print('你发起了攻击，【敌人】剩余血量%s' % enemy_life)
        print('敌人向你发起了攻击，【玩家】剩余血量%s' % player_life)
        print('-----------------------')


# 打印战果
def show_result(player_life, enemy_life):
    if player_life > 0 >= enemy_life:
        print('敌人死翘翘了，这局你赢了')
    elif player_life <= 0 < enemy_life:
        print('悲催，这局敌人把你干掉了！')
    else:
        print('哎呀，这局你和敌人同归于尽了！')
    print('-----------------------')


# （主函数）展开战斗全流程
def main(player_life, player_attack, enemy_life, enemy_attack):
    # 别看这么长，其实就是三个函数，函数1：
    show_role(player_life, player_attack, enemy_life, enemy_attack)
    # 函数2：
    pk_role(player_life, player_attack, enemy_life, enemy_attack)
    # 函数3：
    show_result(player_life, enemy_life)


main(106, 35, 105, 33)
