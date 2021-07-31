import requests

import pandas as pd

import xlwings as xw

import json

from selenium import webdriver

import time

pd.set_option('max_rows', 500)

# 1. 初始化 模拟请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# 初始化 Excel 表头

colunms = ['日期', '累计确诊数', '累计死亡数', '累计治愈数', '累计境外输入', '现有重症', '现有疑似', '新增确诊数', '新增死亡数', '新增治愈数',
           '境外输入较昨日新增', '现有重症较昨日新增', '确诊数较昨日新增', '现有疑似较昨日新增', '省份']


def get_cookie(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    cookies = driver.get_cookies()
    driver.quit()
    items = []
    for i in range(len(cookies)):
        cookie_value = cookies[i]
        item = cookie_value['name'] + '=' + cookie_value['value']
        items.append(item)
    cookiestr = '; '.join(a for a in items)
    return cookiestr


#
def get_data(data, info_list):
    info = pd.DataFrame(data)[info_list]
    today_data = pd.DataFrame([i['today'] for i in data])  # 生成today的数据
    today_data.columns = ['today_' + i for i in today_data.columns]  # 修改列名
    total_data = pd.DataFrame([i['total'] for i in data])  # 生成total的数据
    total_data.columns = ['total_' + i for i in total_data.columns]  # 修改列名
    return pd.concat([info, total_data, today_data], axis=1)  # info、today和total横向合并最终得到汇总的数据


def read_url(id, name, writer):
    # 获取数据进行地址拼接
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode=%s' % (id)
    # 网络请求 get
    r = requests.get(url, headers=headers)  # 进行请求
    # 转换json 数据
    data_json = json.loads(r.text)  # 获取json数据
    # 获取dataframe中列名为data、list、date数据
    data_test = get_data(data_json['data']['list'], ['date'])
    # 获取列名
    data_test['name'] = name
    # 讲所有列名替换成colunms列名
    data_test.columns = colunms
    data_test[['日期', '累计确诊数', '累计死亡数', '累计治愈数', '累计境外输入', '现有重症', '现有疑似', '新增确诊数', '新增死亡数', '新增治愈数',
               '省份']].to_excel(excel_writer=writer, index=None, sheet_name='%s.xlsx' % (name))  # 对指定列名数据保存


# 2. json 请求所有数据
url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'
# 使用requests发起请求
r = requests.get(url, headers=headers)

# 2.1 对请求的数据进行json解析
data_json = json.loads(r.text)
# 2.2 取出json中的 data 下的 数据
data = data_json['data']

# 2.3 获取data 下 各个省份名称
data_province = data['areaTree'][2]['children']

# 2.4 获取各个省份更新的时间和colunms字段数据
today_province = get_data(data_province, ['id', 'lastUpdateTime', 'name'])

# 2.5 获取每个省份对应的id和colunms字段
province_dict = {num: name for num, name in zip(today_province['id'], today_province['name'])}
# 2.6 写入数据到excel 表格  并设置保存位置
writer = pd.ExcelWriter('./疫情数据1.xlsx')

# 循环到各个省份的对应的ID
for i in province_dict:

    read_url(i, province_dict[i] + '省', writer)
writer.save()
writer.close()
all_data, hubei_data, sh_data = {}, {}, {}


def get_into_excel():
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    wb = app.books.open('疫情数据1.xlsx')
    ws = wb.sheets['all']
    max_row = ws.api.UsedRange.Rows.count
    ws.range(str(max_row)).value = hubei_data['新增确诊']
    ws.range(str(max_row)).value = hubei_data['新增死亡']
    ws.range(str(max_row)).value = hubei_data['新增治愈']
    ws.range(str(max_row)).value = hubei_data['新增疑似']
    ws.range(str(max_row)).value = hubei_data['累计重症']

    ws.range(str(max_row)).value = all_data['新增疑似']
    ws.range(str(max_row)).value = all_data['累计疑似']
    ws.range(str(max_row)).value = all_data['累计确诊']
    ws.range(str(max_row)).value = all_data['累计重症']
    ws.range(str(max_row)).value = all_data['累计死亡']
    ws.range(str(max_row)).value = all_data['累计治愈']
    ws.range(str(max_row)).value = sh_data['累计排除疑似']
    ws.range(str(max_row)).value = sh_data['累计确诊']
    ws.range(str(max_row)).value = sh_data['累计重症']
    ws.range(str(max_row)).value = sh_data['累计治愈']
    ws.range(str(max_row)).value = sh_data['累计死亡']
    ws.range(str(max_row)).value = sh_data['累计疑似']
    wb.save()
    wb.close()
    app.quit()
