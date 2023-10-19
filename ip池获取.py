from time import sleep

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from lxml import etree
f=open('ip.txt','a+')
driver=Chrome()
for i in range(1,12):
    sleep(2)
    driver.get("http://www.66ip.cn/"+str(i)+".html")
    for i in range(1,11):
        ip=driver.find_element(By.XPATH,'//*[@id="main"]/div[1]/div[2]/div[1]/table/tbody/tr['+str(i)+']/td[1]')
        port=driver.find_element(By.XPATH,'//*[@id="main"]/div[1]/div[2]/div[1]/table/tbody/tr['+str(i)+']/td[2]')
        f.write(ip.text+port.text)
        url='https://www.123cha.com/domain/'
        proxy = {
            'http': ip.text+':'+port.text
        }
        print(type(proxy))
        s=requests.get(url=url,proxies=proxy)
        print(s)
        html=etree.HTML(s.text)
        xpaths="/html/body/center/div[2]/a/text()"
        biaoti=html.xpath(xpaths)
        
        print(biaoti)

