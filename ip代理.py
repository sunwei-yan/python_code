def get(url,key):
    try:
        import requests
        # 配置代理ip池，可从西刺获取，我这里不用，先注释掉
        # proxies = {'http':'60.168.80.22:3256'}
        # 伪装用户
        header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Host':'www.tianyancha.com',
            'Cookie':'TYCID=7ac4e1708d0811ebb5f3d5b7d6d9508a; ssuid=3646972475; csrfToken=wcUXYBICSWQLy89r05-ElbYT; jsid=https%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-JRGW; bannerFlag=true; CT_TYCID=d7012892dbb348858dbf332a770e0ce9; cloud_token=04236538798743c48dfdb82587b08bd5; creditGuide=1; RTYCID=6b0d1909d8df4572b1e552ba0dd4926e; bdHomeCount=1; searchSessionId=1632625565.85894118; tyc-user-info={%22state%22:%220%22%2C%22vipManager%22:%220%22%2C%22mobile%22:%2215270878905%22}; tyc-user-info-save-time=1632625657685; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTI3MDg3ODkwNSIsImlhdCI6MTYzMjYyNTY1OCwiZXhwIjoxNjY0MTYxNjU4fQ.AW4ebU1XOiSdifOLOoF7Sbfhxyvf3R9BklBgSpcd5UIMP9CYspJFI-Necqd7GnR06y1-3srVimg3nU_bB7vJBA; tyc-user-phone=%255B%252215270878905%2522%255D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215270878905%22%2C%22first_id%22%3A%2217866f93aa328e-05f9d9a8b4b42e-4c3f227c-1327104-17866f93aa4423%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E5%A4%A9%E7%9C%BC%E6%9F%A5%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%7D%2C%22%24device_id%22%3A%2217866f93aa328e-05f9d9a8b4b42e-4c3f227c-1327104-17866f93aa4423%22%7D; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1632578130,1632625425; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1632625976; _ga=GA1.2.920708959.1616635314; _gid=GA1.2.88667156.1632578131',
        }
        # 配置请求数据
        parser = {
            'scheme':'https',
            'host':'www.tianyancha.com',
            'filename':'/search',
            'key':str(key),}
        # 发起请求
        r = requests.get(url, headers=header, params=parser)
        # 需要配置代理ip就用下面一行代码，把上面的注释掉
        # r = requests.get(url,headers=header,params=parser,proxies=proxies)

        if r.status_code == 200:
            print('请求成功')
        else:
            print('请求失败' + str(r.status_code))
        return r.text
    except Exception as e:
        print(e)

def clean(html):
    # 导入包
    from bs4 import BeautifulSoup
    import time
    # 得到开始时间
    start = time.time()
    print('开始清洗数据' )
    soup = BeautifulSoup(html,'lxml')
    # print(soup)
    # 每一页的20条信息都在divs里了
    divs = soup.select('div.result-list > div.search-item')
    # print(len(divs))
    Href = []
    for div in divs:
        # 清洗得到公司名称信息
        company_name = div.select('div.info')[0].text
        # 清洗得到法人信息
        faren = div.select('div.title')[0].text
        # 清洗得到注册资本信息
        zhuceziben = div.select('div.title')[1].text
        # 清洗得到公司成立日期
        chenglidate = div.select('div.title')[2].text
        # 得到公司详情页url
        href = div.select('div.header > a')[0]['href']
        Href.append(href)
        # 清洗省份数据
        # shengfen = div.select('span.site')[0].text
        # 清洗评分数据
        # pingfen = div.select('span.score-num')[0].text
        # 写入数据到文本文档，采取追加写模式
        with open ('公司简介.txt','a+',encoding='utf-8') as f:
            f.write(company_name + ',' + faren + ',' + zhuceziben + ',' + chenglidate + ',' + href + '\n')
    # 关闭文件句柄
    # f.close()
    # 获取结束时间
    end = time.time()
    # 打印所用时间
    print('信息写入完毕,用时{}秒'.format(end-start))
    return Href

# 定义主函数，调用各个函数
def main():
    import time
    key = input('请输入搜索关键词：')
    # key = '苏州教育科技'
    # url = 'https://www.tianyancha.com/search?key=' + str(key)
    # 获取搜索结果前100页，如果反爬通过，是可以爬下来的，可以自行修改页数，我这里是爬前十页示范
    urls = ['https://www.tianyancha.com/search/p{0}?key={1}'.format(i,str(key)) for i in range(1,3)]
    for url in urls:
    # url = 'https://www.tianyancha.com/search/p1?key=%E8%8B%8F%E5%B7%9E%E6%95%99%E8%82%B2%E7%A7%91%E6%8A%80'
        clean(get(url,key))
        time.sleep(3)


if __name__ == '__main__':
    with open('公司简介.txt', 'a+', encoding='utf-8') as f:
        f.write('公司名称' + ',' + '法人' + ',' + '注册资本' + ',' + '成立日期' + ',' + '公司网址' + '\n')
    f.close()
    main()
