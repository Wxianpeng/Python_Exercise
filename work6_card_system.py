# 名字管理系统

print("=" * 50 + "\n名字打印系统\n1.添加一个新名字\n2.删除一个新名字\n3.修改一个新名字\n4.查询一个新名字\n5.退出\n" + "=" * 50)

# 列表
names = []
while True:
    num = int(input("请输入序号:"))
    if num == 1:
        new_name = input("请输入名字:")
        names.append(new_name)
        print(names)
    elif num == 2:
        del_name = input("请输入要删除的名字:")
        names.remove(del_name)
        print(names)
    elif num == 3:
        print(names)
        upd_name_old = int(input("请输入原名称的下标:"))
        upd_name_new = input("请输入新名称：")
        names[upd_name_old] = upd_name_new
        print(names)
    elif num == 4:
        find_name = input("请输入要查询的名字:")
        print((find_name in names))
    elif num == 5:
        print("退出成功！！！")
        break
    else:
        print("输入错误,请重新输入")
