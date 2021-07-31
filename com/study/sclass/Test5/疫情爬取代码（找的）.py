import requests
from bs4 import BeautifulSoup
import datetime
import re
from selenium import webdriver
import time
import xlwings as xw


def get_sh_data(url):
    '''获得上海卫健委的数据'''
    r = requests.get(url=url, headers=sh_headers)
    sh_dict = {}
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    ivs_content = soup.find(name='div', attrs={'id': 'ivs_content', 'class': 'Article_content'})
    new_text = ivs_content.get_text()
    # print(new_text)
    sh_dict['累计排除疑似'] = re.search('已累计排除疑似病例(\d+)例', new_text).group(1)
    sh_dict['累计确诊'] = re.search('发现确诊病例(\d+)例', new_text).group(1)
    style2 = '(\d+)例病情危重，(\d+)例重症，(\d+)例治愈出院，(\d+)例死亡'
    sh_dict['累计重症'] = int(re.search(style2, new_text).group(1)) + int(re.search(style2, new_text).group(2))
    sh_dict['累计治愈'] = re.search(style2, new_text).group(3)
    sh_dict['累计死亡'] = re.search(style2, new_text).group(4)
    sh_dict['累计疑似'] = re.search('尚有(\d+)例疑似病例正在排查中', new_text).group(1)
    return sh_dict


def get_sh_today_news():
    '''获得上海卫健委的新闻'''
    url = r'http://wsjkw.sh.gov.cn/xwfb/index.html'
    r = requests.get(url=url, headers=sh_headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    today_format = datetime.datetime.today().strftime('%Y-%m-%d')
    today_sh_news = soup.find_all(name='span', text=today_format)
    today_counts = len(today_sh_news)
    for i in range(today_counts - 1, -1, -1):
        title = today_sh_news[i].find_previous_sibling(name='a').attrs['title']  # 标题
        href = 'http://wsjkw.sh.gov.cn' + today_sh_news[i].find_previous_sibling(name='a').attrs['href']  # 网址
        if title.startswith('上海新增'):
            # print(title)
            return get_sh_data(href)


def get_all_today_news():
    '''获得国家卫健委的新闻'''
    url = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
    r = requests.get(url, headers=quanguo_headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    today_format = datetime.datetime.today().strftime('%Y-%m-%d')
    latest_news_title = soup.find(name='span', text=today_format).find_previous_sibling(name='a').attrs['title']
    latest_news_href = 'http://www.nhc.gov.cn' + \
                       soup.find(name='span', text=today_format).find_previous_sibling(name='a').attrs['href']
    # print(latest_news_href)
    return get_all_today_data(latest_news_href)



def get_all_today_data(url):
    r = requests.get(url, headers=quanguo_headers)
    all_dict = {}
    hubei_dict = {}
    soup = BeautifulSoup(r.text, 'lxml')
    news = soup.find(name='p').get_text()

    all_dict['新增疑似'] = re.search('新增疑似病例(\d+)例', news).group(1)
    all_dict['累计疑似'] = re.search('现有疑似病例(\d+)例', news).group(1)
    all_dict['累计确诊'] = re.search('累计报告确诊病例(\d+)例', news).group(1)
    all_dict['累计重症'] = re.search('其中重症病例(\d+)例', news).group(1)
    all_dict['累计死亡'] = re.search('累计死亡病例(\d+)例', news).group(1)
    all_dict['累计治愈'] = re.search('累计治愈出院病例(\d+)例', news).group(1)

    hubei_dict['新增疑似'] = re.search('新增疑似病例(\d+)例.*?（武汉(\d+)例', news).group(1)
    hubei_dict['新增确诊'] = re.search('湖北新增确诊病例(\d+)例.*?（武汉(\d+)例', news).group(1)
    hubei_dict['新增死亡'] = re.search('新增死亡病例(\d+)例.*?（武汉(\d+)例', news).group(1)
    hubei_dict['新增治愈'] = re.search('新增治愈出院病例(\d+)例（武汉(\d+)例）', news).group(1)
    hubei_dict['累计重症'] = re.search('其中重症病例(\d+)例.*?（武汉(\d+)例', news).group(1)
    # print(all_dict, hubei_dict)
    return all_dict, hubei_dict


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


def get_into_excel():
    '''把数据贴到excel里'''
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = False

    wb = app.books.open('新型冠状病毒每日数据.xlsx')
    ws = wb.sheets['all']
    max_row = ws.api.UsedRange.Rows.count
    ws.range('C' + str(max_row)).value = hubei_data['新增确诊']
    ws.range('K' + str(max_row)).value = hubei_data['新增死亡']
    ws.range('O' + str(max_row)).value = hubei_data['新增治愈']
    ws.range('S' + str(max_row)).value = hubei_data['新增疑似']
    ws.range('AA' + str(max_row)).value = hubei_data['累计重症']

    ws.range('R' + str(max_row)).value = all_data['新增疑似']
    ws.range('AL' + str(max_row)).value = all_data['累计疑似']
    ws.range('V' + str(max_row)).value = all_data['累计确诊']
    ws.range('Z' + str(max_row)).value = all_data['累计重症']
    ws.range('AD' + str(max_row)).value = all_data['累计死亡']
    ws.range('AH' + str(max_row)).value = all_data['累计治愈']

    ws.range('AN' + str(max_row)).value = sh_data['累计排除疑似']
    ws.range('Y' + str(max_row)).value = sh_data['累计确诊']
    ws.range('AC' + str(max_row)).value = sh_data['累计重症']
    ws.range('AK' + str(max_row)).value = sh_data['累计治愈']
    ws.range('AG' + str(max_row)).value = sh_data['累计死亡']
    ws.range('AM' + str(max_row)).value = sh_data['累计疑似']

    wb.save()
    wb.close()
    app.quit()


if __name__ == "__main__":
    sh_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Cookie': get_cookie('http://wsjkw.sh.gov.cn/xwfb/index.html'),
        # 'Cookie': 'zh_choose=s; zh_choose=s; _gscu_2010802395=80620430ie0po683; yd_cookie=12f170fc-e368-4a662db5220af2d434160e259b2e31585efb; _ydclearance=2cd0a8873fd311efcda1c1aa-05fc-4001-a108-0e86b80b3fee-1580700296; _gscbrs_2010802395=1; _pk_ref.30.0806=%5B%22%22%2C%22%22%2C1580693101%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DDVUbOETLyMZLC5c_V7RJRbAYPvyqaU3f2PCBi2-E6KC2QEFltdrKWGmhgA5NbC3c%26wd%3D%26eqid%3Df38b30250015e1c5000000045e365a8d%22%5D; _pk_ses.30.0806=*; _pk_id.30.0806=35b481da38abb562.1580620431.6.1580694952.1580693101.; _gscs_2010802395=80693100qds57e17|pv:6; AlteonP=ALa1BGHbHKyWUqcNUGRETw$$',
        'Host': 'wsjkw.sh.gov.cn'
    }
    quanguo_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Cookie': 'oHAcoULcWCQb80S=pxzexGFCvyGV4xDkaMHSyjBmzwXn5O4vfCbxFCgMDfcBaKqsFU9FHstqjFY6wJt9; yfx_c_g_u_id_10006654=_ck20020209283417867964364567575; _gscu_2059686908=81579037nbf5xc58; insert_cookie=67313298; yfx_f_l_v_t_10006654=f_t_1580606914774__r_t_1581643181169__v_t_1581678949269__r_c_14; security_session_verify=a2efd6893c3ad08675db9b0f5c365ecf; oHAcoULcWCQb80T=4Ywh2qE8IiJP44ThdpW0fs7Yqi1Hwlh9RhJHrW2WVl536y4eCIgXxGh9M8IuYUqGUCCtBO5kBc2DB6Kewd3naLK_O2bK5W3w3pcqT.uX3asTXxC2SGBqy9eV2DoGB0ZXb4uTPzPGbXebmT6xIYxbAmGbm_kZVX_nUvBL4nkAuFAVvcGLBmXr8nsdEToXztqZUlYnTjn9niwHMcg3th7XhJvFS_tckqRq5bLpvS_IKPuYn2JLraIIejlErBhA5IQhyHXFekNynv5PYgpzu2PguGccrP3c_bcg1MFViQjKVhgs_B22Nv4NxdHdiIk9GdZDZBjQ',
        'Host': 'www.nhc.gov.cn'
    }
    # 一、全国和湖北的数据
    all_data, hubei_data, sh_data = {}, {}, {}
    try:
        all_data, hubei_data = get_all_today_news()
        print('全国数据：{}\n'
              '湖北数据：{}'.format(all_data, hubei_data))
    except:
        print('全国数据未更新')
    # 二、上海的数据
    try:
        sh_data = get_sh_today_news()
        print('上海数据：{}'.format(sh_data))
    except:
        print('上海数据未更新')
    # 三、导出到excel里
    if sh_data != {} and all_data != {}:
        get_into_excel()
        print('Excel刷新成功！')
