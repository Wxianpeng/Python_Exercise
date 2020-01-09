# bytes转字符串方式一
# b = b'u\xacb\x82\xe6\xb2\xb9\xa9\xf2\xb9\xa9\xf2\xb9\xa9'
#
# string = str(b, 'utf8')
# print(string)

# bytes转字符串方式二
# b = b'u\xe9\x80\x86\xe7\x81\xab'
# string = b.decode()  # 第一参数默认utf8，第二参数默认strict
# print(string)
#
# # bytes转字符串方式三
# b = b'\xe9\x80\x86\xe7\x81\xab'
# string = b.decode('utf-8', 'ignore')  # 忽略非法字符，用strict会抛出异常
# print(string)
# # bytes转字符串方式四
#
# b = b'\xe9\x80\x86\xe7\x81\xab'
# string = b.decode('utf-8', 'replace')  # 用？取代非法字符
# print(string)


# 字符串转bytes方式一
str1 = '10086'
b = bytes(str1, encoding='utf-8')
print(b)
