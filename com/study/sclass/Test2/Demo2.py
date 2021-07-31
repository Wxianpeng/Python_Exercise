# !/usr/bin/env python
# -*-coding:utf-8 -*-
# encoding = gbk
# coding=gbk
import requests

# 模拟浏览器发送http请求
# 伪造http请求
url = 'https://thispersondoesnotexist.com/image'

# 发送http请求
response = requests.get(url)
# encoding=gbk
print(response.content)
