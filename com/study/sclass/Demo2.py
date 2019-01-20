import time

# 提示：（1）为宝石数量赋值（数量可为0-3任意数字）
# （2）条件1：如果宝石数量>=6，显示你拥有了毁灭宇宙的力量
# （3）条件2：如果3<宝石数量<=5，显示红女巫需要亲手毁掉幻视额头上的心灵宝石
# （4）条件3：如果是其它情况，显示需要惊奇队长逆转未来

stoneNumber = 4
# 为宝石数量赋值
if stoneNumber >= 6:
    # 条件：如果你拥有的宝石数量大于等于6个
    print('你拥有了毁灭宇宙的力量')
    # 结果：显示‘就拥有了毁灭宇宙的力量’的结果
elif 3 < stoneNumber <= 5:
    # 条件：如果想让宝石数量停留在4至5个
    print('红女巫需要亲手毁掉幻视额头上的心灵宝石')
else:
    # 条件：当赋值不满足if和elif条件时，执行else下的命令，宝石数量在3个以下
    print('需要惊奇队长逆转未来')
    # 结果：显示‘需要惊奇队长逆转未来’的结果

# region 打印英雄消失
print('一切都化为虚无')
time.sleep(1.5)
print('一切都化为尘埃')
time.sleep(1.5)

print('他们就这样随风消散')
time.sleep(1.5)

print('冬兵')
time.sleep(1.5)

print('格鲁特')
time.sleep(1.5)

print('红女巫')
time.sleep(1.5)

print('黑豹')
time.sleep(1.5)

print('猎鹰')
time.sleep(1.5)

print('星爵')
time.sleep(1.5)

print('奇异博士')
time.sleep(1.5)

print('蜘蛛侠')
time.sleep(1.5)

print('可你只要稍一回忆，似乎还能听见蜘蛛侠彼得·帕克说：')
time.sleep(2)

print("I don't wanna go, Mr Stark.")
time.sleep(2)
print("I'm sorry……")
# endregion

#   （1）把彼得·帕克26分的历史成绩赋值到变量historyscore；
#   （2）用if…else写最基础判断条件如果historyscore>=60时，打印你已经及格，否则，打印不及格；
#   （3）用print()输出程序结束。

#  其中，额外条件1：当历史成绩大于80分，显示结果你很优秀；额外条件2：当历史成绩在60到80分之间，显示结果：你只是一般般。
# 额外条件1：当历史成绩小于60，同时还小于30时，输出结果学渣；额外条件2：当历史成绩小于60，但大于等于30时，输出结果还能抢救一下。

historyScore = 10
if historyScore >= 60:
    print('你已经及格')
    if historyScore > 80:
        print("你狠优秀")
    else:
        print("你只是一般般。")
else:
    if historyScore > 30:
        print('还能抢救一下')
    else:
        print('学渣')

print("打印结束")
