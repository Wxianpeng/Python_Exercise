# -*- coding:utf-8 -*-
import base64
str1 = 'Q0NHVMKiAAAAAAAAAHsic2VxIjo3LCJjb21tYW5kIjoicGFkU2V0VG9Db250cm9sbGVyIiwidmFsdWUiOiI1cldMNksrVjVwYUg1YTJYIiwicHJvcGVydHlfbmFtZSI6InNlYXJjaCIsIm9ial9pZCI6ImNiZDNmOTMxMTgyNzExZWJhZGU2MzBiNDllOWFiNTAwIiwib2JqX25hbWUiOiJhVzV3ZFhSaWIzZ3gifQ==';


def str_to_hex(s):
    return r"/x" + r'/x'.join([hex(ord(c)).replace('0x', '') for c in s])


# 原始
print("原始")
print(base64.b64decode(str1))


print("="*100)
print("修改编码  ISO-8859-1")
bbs = str(base64.b64decode(str1), "ISO-8859-1")
# 解码
print('base64解码:', bbs)
hexbbs = str_to_hex(bbs)
print('base64解码后转16进制:', hexbbs)

print("="*100)
print("修改编码  utf-8  正确结果")
# 解码方式  utf-8 编码
bbs = str(base64.b64decode(str1), "utf-8")

print('base64解码:', bbs)
hexbbs1 = str_to_hex(bbs)
print('base64解码后转16进制:', hexbbs1)
print("="*100)


