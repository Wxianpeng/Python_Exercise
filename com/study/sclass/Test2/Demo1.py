# encoding = gbk
# coding=gbk

import re
import time
import requests
import pandas as pd
from retrying import retry
from concurrent.futures import ThreadPoolExecutor

start = time.perf_counter()  # 计时-开始

print(start)

# plist 为1-100页的URL的编号num
plist = []
for i in range(1, 101):
    j = 44 * (i - 1)
    plist.append(j)

print(plist)

listno = plist

datatmsp = pd.DataFrame(columns=[])

while True:
    @retry(stop_max_attempt_number=8)  # 设置最大重试次数
    def network_programming(num):
        url = 'https://s.taobao.com/search?q=%E6%B2%99%E5%8F%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180207&ie=utf8&sort=sale-desc&style=list&fs=1&filter_tianmao=tmall&filter=reserve_price%5B500%2C%5D&bcoffset=0&p4ppushleft=%2C44&s=' + str(num)
        web = requests.get(url, headers=headers)
        web.encoding = 'utf-8'

        # print(web.content)
        return web

    #   多线程
    def multithreading():
        number = listno  # 每次爬取未爬取成功的页
        event = []

        with ThreadPoolExecutor(max_workers=10) as executor:
            for result in executor.map(network_programming, number, chunksize=10):
                event.append(result)
        return event


    #   隐藏：修改headers参数
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36(KHTML, like Gecko)  \
            Chrome/55.0.2883.87 Safari/537.36'}

    listpg = []
    event = multithreading()
    for i in event:
        json = re.findall('"auctions":(.*?),"recommendAuctions"', i.text)
        if len(json):
            table = pd.read_json(json[0])
            datatmsp = pd.concat([datatmsp, table], axis=0, ignore_index=True)

            pg = re.findall('"pageNum":(.*?),"p4pbottom_up"', i.text)[0]
            listpg.append(pg)  # 记入每一次爬取成功的页码
    lists = []

    for a in listpg:
        b = 44 * (int(a) - 1)
        lists.append(b)  # 将爬取成功的页码转为url中的num值

    listn = listno

    listno = []  # 将本次爬取失败的页记入列表中 用于循环爬取
    for p in listn:
        if p not in lists:
            listno.append(p)
    if len(listno) == 0:  # 当未爬取页数为0时 终止循环！
        break

datatmsp.to_excel('datatmsp.xls', index=False)  # 导出数据为Excel
end = time.clock()  # 计时-结束
print("爬取完成 用时：", end - start, 's')
