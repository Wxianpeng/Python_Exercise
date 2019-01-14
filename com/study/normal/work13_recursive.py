# 阶乘求和
def get_sums(num):
    if num > 1:
        return num * get_sums(num - 1)
    else:
        return num


print(get_sums(4))

# 递归需要条件下结束，不然内存会死  内存溢出  2018-3-2 17:18:25

