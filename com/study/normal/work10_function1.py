# 无参函数
def function_buddha():
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")


# 有参函数
def sum_a_b(a, b):
    result = a + b
    print("%d+%d=%d" % (a, b, result))


def get_fahrenheit():
    fahrenheit = 96
    print("当前华氏温度%s" % fahrenheit)
    return fahrenheit


def get_temperature(fahrenheit):
    print("当前摄氏温度%d" % ((fahrenheit - 32) / 1.8))


# 调用函数
# function_buddha()

# 调用有参函数
# num1 = int(input("请输入第一个参数:"))
# num2 = int(input("请输入第二个参数:"))
# sum_a_b(num1, num2)

# 函数调用
# get_temperature(int(get_fahrenheit()))


# 一个函数返回多个值: 可用 列表 字典 元组返回   （默认元组）


# 4种函数 : 1 无参数 无返回值 ; 2无参数，有返回值;3有参数，无返回值;4有参数，有返回值

# 缺省参数:有个变量已经确定,不传递值
def test(a, b, c=520):
    print("%d+%d+%d=%d" % (a, b, c, a + b + c))


# test(100, 200)


