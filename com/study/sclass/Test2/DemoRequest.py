# 爬虫四个步骤
#
# 第0步：获取数据。爬虫程序会根据我们提供的网址，向服务器发起请求，然后返回数据。
#
#
# 第1步：解析数据。爬虫程序会把服务器返回的数据解析成我们能读懂的格式。
#
#
# 第2步：提取数据。爬虫程序再从中提取出我们需要的数据。
#
#
# 第3步：储存数据。爬虫程序把这些有用的数据保存起来，便于你日后的使用和分析。


import requests

# res = requests.get(
#     'https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
# res.encoding = "utf-8"
# statusCode = res.text
# fie = open('Http状态码.txt', 'a+')
# fie.write(statusCode)
# fie.close()

photo = requests.get("https://res.pandateacher.com/2019-01-12-15-29-33.png")
pic=photo.content
image = open("download.png", "wb")
image.write(pic)
image.close()
