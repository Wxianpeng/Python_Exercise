# 1.print输出多个变量
# print("admin")
# name = "王"
# age = 20
# address = "山东"
# print("姓名是:%s,年龄是%d，地址是%s" % (name, age, age))

#   没有do - while  switch
# if -else  嵌套

# age = 19
# if age > 18:
#     print("我成年了")
# elif age > 30:
#     print("我在 18-30岁之间")
# else:
#     print("我为成年")

# 判断
# 去如果当前用户是男性的话 ,那么 就输入判断女性的要求
# 字符串操作
myStr = "hello word itCast and itCast"

# 1. find

# 从第几位开始找到,找不到返回-1
myStr.find("word")
# 从右边开始寻找
myStr.rfind("itCast")
# 左边寻找
myStr.find("itCast")

# 2.index
# 和find 一样， 找不到会报异常（subString not found）
myStr.index("word")
# 从右边开始寻找
myStr.rindex("itCast")

# 3.count
# 返回字符串的个数,不存在返回0
myStr.count("itCast")

# 4.replace 替换字符串中的数据，远字符串不会改变 （数字  字符串  元组 为不可变类型）

# 替换出现所有出现的word
myStr.replace("word", "WORD")
# 1 表示替换次数
myStr.replace("itCast", "xxx", 1)

# 5.split 分割,
myStr.split(" ")
print(myStr.split(" "))

# 6 capitalize 第一个单词字母大写
myStr.capitalize()

# 7. title 所有单词首字母大写

myStr.title()

# 8. endswith 判断后缀是否合法，返回True\ False
myStr.endswith()
