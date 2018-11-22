sex = input("请输入性别")
if sex == "男":
    color = input("你白吗？")  # 白  或者 黄
    money = int(input("财产综合"))  # 财产总和
    beautiful = input("你美么？")  # 美或者普通
    if color == "白" and money > 100000 and beautiful == "美":
        # print("%s%d%s" % (color, money, beautiful))
        print("白富美")
    else:
        print("矮矬穷")
else:
    print("判断高富帅的信息在下面......")
