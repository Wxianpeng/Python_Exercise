# 1.一个人在心里想好一个数————这个数字是提前准备好的，可以设置一个变量来保存这个数字。我就设置我的数字为24。

# 2.然后让另一个人猜————所以可以使用input()函数来接收另一个人输入的数字，并用int()转化为整数。

# 3.直到猜对为止————天知道几次才能猜对，所以肯定需要用到循环，并且由于不知道要循环几次，所以适合while循环。

# 4.如果他猜的数比24小就告诉他“太小了”，如果他猜的数比24大就告诉他“太大了”——这里一看“如果……就……”的描述，就知道应该用if...else...写一个条件判断。

while True:
    prisonerA = input("请输入你的选择")
    prisonerB = input("请输入你的选择")

    if prisonerA == "认罪" and prisonerB == "认罪":
        print("各10年")
        continue
    elif prisonerA == "认罪" and prisonerB == "抵赖":
        print("认罪的人判1年，抵赖的人判20年")
        continue
    elif prisonerA == "抵赖" and prisonerB == "认罪":
        print("认罪的人判1年，抵赖的人判20年")
    elif prisonerA == "抵赖" and prisonerB == "抵赖":
        print("两人都抵赖，则各判3年")
        break
