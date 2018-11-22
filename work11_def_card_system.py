# 名字管理系统  函数操作


# 列表
names = []


def card_menu():
    """显示菜单"""
    print("=" * 50 + "\n名字打印系统\n1.添加一个新名字\n2.删除一个新名字\n3.修改一个新名字\n4.查询一个新名字\n5.退出\n" + "=" * 50)


def add_info():
    """增加信息"""
    new_name = input("请输入名字:")
    names.append(new_name)
    print(names)


def del_info():
    """删除信息"""
    del_name = input("请输入要删除的名字:")
    names.remove(del_name)
    print(names)


def update_info():
    """修改信息"""
    print(names)
    upd_name_old = int(input("请输入原名称的下标:"))
    upd_name_new = input("请输入新名称：")
    names[upd_name_old] = upd_name_new
    print(names)


def find_info():
    """查询信息"""
    find_name = input("请输入要查询的名字:")
    print((find_name in names))


def main():
    card_menu()
    """程序的入口"""
    while True:
        num = int(input("请输入序号:"))
        if num == 1:
            add_info()
        elif num == 2:
            del_info()
        elif num == 3:
            update_info()
        elif num == 4:
            find_info()
        elif num == 5:
            print("退出成功！！！")
            break
        else:
            print("输入错误,请重新输入")


# main()


# 不定长参数1  *args 是用 元组保存数据

def sum_nums(a, b, *args):
    result = a + b
    for temp in args:
        # print(temp)
        result += temp

    print("%d+%d+%s=%d" % (a, b, args, result))


# sum_nums(100, 200, 300, 100)


# 不定长参数2 *args 是用 元组保存数据,kwargs用字典保存{"key":"value"}形式

def sum_nums2(a, b, c=11, *args, **kwargs):
    result = a + b + c

    for temp in args:
        # print(temp)
        result += temp

    print("%d+%d+%d+%s=%d" % (a, b, c, args, result))
    print(kwargs)


sum_nums2(11, 22, 44, 26, 16, 56, 45, task=99, done=95)
card_menu()
# 拆包
a = (11, 33, 44, 56)
b = {'age': 20, 'name': '张三'}

sum_nums2(11, 22, 44, *a, **b)
