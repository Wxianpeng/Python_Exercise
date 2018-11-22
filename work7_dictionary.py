# 字典打印

print("=" * 50 + "\n    名片管理系统\n1.添加一个新的名片\n2.删除一个新的名片\n3.修改一个新的名片\n4.查询一个新的名片\n5.名片列表\n6.退出\n" + "=" * 50)

names = []
# 定义字典 存储名片

while True:
    num = int(input("请输入序号:"))
    if num == 1:
        new_name = input("请输入名字:")
        new_age = int(input("请输入年龄:"))
        name_info = {}
        name_info['name'] = new_name
        name_info['age'] = new_age
        names.append(name_info)
        print(names)
    elif num == 2:
        del_name = input("请输入要删除的名字:")
        for temp in names:
            if temp['name'] == del_name:
                pass

        print(names)
    elif num == 3:
        print(names)
        upd_name_old = int(input("请输入原名称的下标:"))
        print(names)
    elif num == 4:
        find_name = input("请输入要查询的名字:")
        find_flag = 0
        for temp in names:
            if find_name == temp['name']:
                print("=" * 10)
                print("姓名\t年龄")
                print("%s\t%d" % (temp['name'], temp['age']))
                find_flag = 1
                break
        if find_flag == 0:
            print("没有这个人")
    elif num == 5:
        print("姓名\t年龄")
        for temp in names:
            print("%s\t%d" % (temp['name'], temp['age']))

    elif num == 6:
        print("退出成功！！！")
        break
    else:
        print("输入错误,请重新输入")

