# #
# # Python  基础
#
#
# # 1. 我的第一个程序
# print('Hello,word')
#
# # 2. 常见字符类型(数据类型和变量)
# n = 123
# f = 16544.445
# s1 = 'hello word'
# s2 = 'hello,\'Adam\''
# s3 = r'hello,"Bart"'
# s4 = r'''hello, Lisa!'''
#
# print(n)
# print(f)
# print(s1)
# print(s2)
# print(s3)
# print(s4)
#
# # 3.   字符串和编码
#
# # ord  将 ‘好’ 转换ASCII码
# print(ord('好'))
# print(ord('好'))
# print(ord('工'))
# print(ord('作'))
# # chr 将 22909 转换为Unicode码
# print(chr(22909))  # %运算符就是用来格式化字符串的。在字符串内部
#
# # %s表示用字符串替换，
# # %d表示用整数替换，
#
# # 有几个%?占位符，
# # 后面就跟几个变量或者值，顺序要对应好。
# # 如果只有一个%?，括号可以省略
#
# # %d	整数
# # %f	浮点数
# # %s	字符串
# # %x	十六进制整数
#
# print('Hello, %s' % 'world')
# weather = '晴天'
# temperature = 25  # ("温度")
# print('Hi, %s, you have $%d.' % ('张三', 1000000))
# print('今天是%s,气温大概为%d度' % (weather, temperature))
#
# # 小明的成绩从去年的72分提升到了今年的85分，
# # 请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
#
# lastScore = 72
#
# nowScore = 85
#
# # %% 输出为百分号   %05.2f 表示 总共有3个数(算小数点)  2位小数
# print('小明成绩高了%05.2f%%' % (((nowScore - lastScore) / lastScore) * 100))  # 5 list(无序) 和 tuple(有序)

# 4.  定义数组list(可变的有序表)  tuple(有序列表叫元组) 一旦初始化就不能修改 没有append()，insert()方法,代码更安全
# names = ['张三', '李四', '王五']
#
# languages = ['python', 'java', ['asp', 'php'], 'scheme']
#
# # 获取数组的长度
# print('数组的长度为%d' % (len(names)))
# # 通过下标获取数组里面的数据
# # print(names[0])
# # print(names[1])
# # print(names[2])
#
# # 还可以用-1做索引，直接获取最后一个元素：
# print(names[-1])
# print(names[-2])
# print(names[-3])
# # list中追加元素到末尾
# names.append("赵六")
#
# # 追加指定位置
# names.insert(1, "小二")
#
# # 便利循环数据
# for name in names:
#     print('当前姓名 :', name)
#
# # 删除指定位置
# names.pop(1)
# # 删除最后一个
# names.pop()
#
# data = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
#
# # 打印Apple:
# print(data[0][0])
# # 打印Python:
# print(data[1][1])
# # 打印Lisa:
# print(data[2][2])

# 5 条件判断

# age = 20
# if age > 30:
#     print('A')
# else:
#     print('B')

# score = 61
#
# if score > 60:
#     print('及格')
# elif score > 70:
#     print('良好')
# elif score > 80:
#     print('优')
# elif score > 90:
#     print('优秀')
#
# birthday = input('birthday:')
#
# birthday = int(birthday)
# if birthday < 2000:
#
#     print('00后')
# else:
#     print('00前')

# 小明身高1 .75，体重80.5kg。
# 请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5 - 25：正常
# 25 - 28：过重
# 28 - 32：肥胖
# 高于32：严重肥胖

# height = 1.75
# weight = 80.5
#
# IBM = weight / (height * height)
#
# print(IBM)
#
# if IBM < 18.5:
#     print('过轻')
# elif (IBM > 18.5) and (IBM <= 25):
#     print('正常')
# elif (IBM > 25) and (IBM <= 28):
#     print('过重')
# elif (IBM > 28) and (IBM <= 32):
#     print('肥胖')
# elif IBM > 32:
#     print('严重肥胖')

# num = 0

# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     num = num + x
#
#     print(num)
#
# for x in range(101):
#     num += x
#     print(num)

# names = ['张三', '李四', '王五']
#
# for name in names:
#     print('hello', name)

#   6使用dict 和 set

# dict  key-value存储方式
# score = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#
# print(score['Bob'])
