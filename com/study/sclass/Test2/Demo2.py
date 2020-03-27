# !/usr/bin/env python
# -*-coding:utf-8 -*-
# encoding = gbk
# coding=gbk
import requests

# 模拟浏览器发送http请求
# 伪造http请求
url = 'https://s.taobao.com/search?q=农产品&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
# 发送http请求
response = requests.get(url)
# encoding=gbk
print(response.text)
