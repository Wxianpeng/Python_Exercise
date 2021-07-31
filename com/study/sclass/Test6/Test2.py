# -*- coding:utf-8 -*-
# 将base64编码/解码包
import base64
# 导入url解码包
from urllib import parse

# 普通中文
s = "你好"
# 带竖线的中文
str1 = '中国|陕西省|西安市|雁塔区|小寨东路|178号'
# base64编码后的样例
example = '5Lit5Zu9fOmZleilv+ecgXzopb/lronluIJ86ZuB5aGU5Yy6fOWwj+WvqOS4nOi3r3wxNzjlj7c='
# 先base64编码，再url编码后的样例
example_new = '5Lit5Zu9fOmZleilv%2BecgXzopb%2FlronluIJ86ZuB5aGU5Yy6fOWwj%2BWvqOS4nOi3r3wxNzjlj7c%3D'
# 场景一：普通中文base64编码后，得到带有b的编码结果
# 将字符为unicode编码转换为utf-8编码
bs = base64.b64encode(s.encode("utf-8"))
# 得到的编码结果前带有b
print('带b的编码结果:', bs)
# 将上面带有b的编码结果解码
bbs = str(base64.b64decode(bs), "utf-8")
# 解码
print('带b的编码结果解码:', bbs)
# 场景二：将带有竖线（可以没有）的中文base64编码后，得到不带b的编码结果
bs = str(base64.b64encode(str1.encode("utf-8")), "utf-8")
# 去掉编码结果前的 b
print('不带b的编码结果:', bs)
# 将上面不带b的编码结果解码
bbs = str(base64.b64decode(bs), "utf-8")
# 解码
print('不带b的编码结果解码:', bbs)
# 场景三：base64编码后的样例的解码
bbs = str(base64.b64decode(example), "utf-8")
print('base64编码后的样例解码:', bbs)  # 解码
# 场景四：先base64编码，再url编码后的样例的解码
str3 = parse.unquote(example_new)  # 解码字符串
print('url解码后：', str3)  # str3=haha哈哈
bbs = str(base64.b64decode(str3), "utf-8")
print('先base64编码，再url编码后的样例的解码：', bbs)  # 解码
