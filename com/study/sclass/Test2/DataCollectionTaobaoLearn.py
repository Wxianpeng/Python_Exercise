# !/usr/bin/env python
# -*-coding:utf-8 -*-
from selenium import webdriver
import time
import re
# 导入pymysql模块
import pymysql

# 连接database

# browser = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver_X64.exe')
# 获取数据，解析数据
keyword = input('请输入你想要的商品信息：')
# selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 81
# 报错意思  这个 chromedriver  是81版本的 ，我的浏览器是 80 版本的 ，所以要下载版本一样的。

chrome_driver = r"E:\Python Space\Python_Exercise\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
# 参考链接   https://blog.csdn.net/weixin_43746433/article/details/95237254
# 进入淘宝页面
driver.get('http://www.taobao.com')

# https://s.taobao.com/search?q=%E5%86%9C%E4%BA%A7%E5%93%81&s=44


# 建立数据库连接
connect = pymysql.connect(host="localhost", user="root", password="123456", database="python", charset="utf8")


# 插入数据方法
def increaseData(data):
    # 使用cursor()方法获取操作游标
    cursor = connect.cursor()
    # SQL 插入语句
    sql = "INSERT INTO productInformation(INFO, PRICE, DEAL, PRODUCTNAME, PLACE) VALUES (%s, %s, %s, %s, %s )"
    try:
        # 执行sql语句
        cursor.execute(sql, data)
        # 提交到数据库执行
        connect.commit()
    except:
        # 如果发生错误则回滚
        connect.rollback()


# 寻找商品

def serch():
    driver.find_element_by_id('q').send_keys('农产品')
    # 多属性btn-search tb-bg 均为class的属性 二选一即可
    # driver.find_element_by_class_name('btn-search tb-bg').click()
    # 进入搜索页面
    driver.find_element_by_class_name('btn-search').click()
    # 等待10秒钟进行扫码
    time.sleep(10)
    # 拿到商品的总页码数
    token = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile('\d+').search(token).group(0))
    return token


# 翻页
def next_page():
    token = serch()
    num = 0
    while num != token - 1:
        driver.get('https://s.taobao.com/search?q={}&s={}'.format(keyword, 44 * num))
        driver.implicitly_wait(10)
        num += 1
        drop_down()
        get_product()


# 下滑
def drop_down():
    for x in range(1, 11, 2):
        time.sleep(0.5)
        j = x / 10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight *%f' % j
        driver.execute_script(js)


# 获取数据
def get_product():
    list = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for li in list:
        info = li.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        price = li.find_element_by_xpath('.//a[@class="J_ClickStat"]').get_attribute('trace-price') + '元'
        deal = li.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        name = li.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        place = li.find_element_by_xpath('.//div[@class="location"]').text

        # 拿到数据,插入数据库
        increaseData([info, price, deal, name, place])
        # 涉及写操作要注意提交


if __name__ == '__main__':
    next_page()

# 数据持久化（写数据库、写文件）
# csv 文件 文本的格式，可以用excel打开
# f = open('淘宝农产品爬取结果.csv', 'w', encoding='utf-8')
# # 写表头
# f.write('名称,价格,购买人数,店铺名称,地区\n')
# for item in list:
#     temp = {
#         'info': item['title'],
#         'price': item['view_price'],
#         'deal': item['view_sales'],
#         'name': item['nick'],
#         'place': item['item_loc']
#     }
#     f.write('{info},{price},{deal},{name},{isTmall},{place}\n'.format(**temp))
#
# f.close()
