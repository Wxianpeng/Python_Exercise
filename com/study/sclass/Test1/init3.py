import random, time

player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']

# 随机选取三个角色
print(random.sample(player_list, 3))

# 由于生成双方角色属性的代码类似，所以在试验期，只考虑我方角色。



player_list = ['【狂血战士】', '【森林箭手】', '【光明骑士】', '【独行剑客】', '【格斗大师】', '【枪弹专家】']
players = random.sample(player_list, 3)  # 从列表里随机选取三个元素
player_life = {}  # 建立空字典，存放我方角色的血量。
player_attack = {}  # 建立空字典，存放我方角色的攻击。

# 循环三次
for player in range(0, 3):
    # 生成角色的属性
    life = random.randint(100, 180)
    attack = random.randint(30, 50)
    player_life[players[player]] = life  # 给空字典添加键值对，角色列表players的第0个元素为键，变量life为值
    player_attack[players[player]] = attack  # 给空字典添加键值对，角色列表players的第0个元素为键，变量attack为值

# 展示我方的角色信息
print('----------------- 角色信息 -----------------')
print('你的人物：')

for player in range(0, 3):
    print('%s  血量：%d  攻击：%d'
          % (players[player], player_life[players[player]], player_attack[players[player]]))
    print('--------------------------------------------')
