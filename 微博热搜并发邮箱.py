# from asyncio.windows_events import NULL
# import profile
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver import Chrome
# import requests
# from selenium.webdriver.common.by import By
# from sqlalchemy import null
# from http import server
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
# chrome_capabilities = {
#     "browserName": "chrome",        # 浏览器名称
#     "version": "",                  # 操作系统版本
#     "platform": "ANY",              # 平台，这里可以是windows、linux、andriod等等
#     "javascriptEnabled": True,      # 是否启用js
# }

# # 配置谷歌浏览器静默启动【后台启动】
# chrome_options = webdriver.ChromeOptions()
# # 初始化谷歌浏览器的配置【必须加上】

# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')


# driver = webdriver.Chrome(
#                           desired_capabilities=chrome_capabilities,
#                           options = chrome_options)


# driver.get("https://weibo.com/newlogin?tabtype=search&openLoginLayer=0&url=")


# sleep(10)
# print(6666)

# n=0
# st=""
# for i in range(1,51):
   
#     s=driver.find_element(By.XPATH,'//div[@data-index="'+str(i)+'"]').text
#     st=st+s
#     n=n+1
#     if(n>4):
#         js="window.scrollBy(0,500)" 
#         driver.execute_script(js)
#         n=0
# print(st)
# msg=MIMEText(st,'html','utf-8')
# msg['From']=formataddr(["热搜助手","pythontest2481@126.com"])
# msg['Subject']="微博热搜"
# server = smtplib.SMTP_SSL('smtp.126.com')
# server.login("pythontest2481@126.com","PHBGOLPROTJQXFHF")
# server.sendmail("pythontest2481@126.com","543477641@qq.com",msg.as_string())
# server.quit()
# driver.close()    
# print(1)

import profile
from time import sleep
from selenium import webdriver
from selenium.webdriver import Chrome
import requests
from selenium.webdriver.common.by import By
import xlwt
from http import server
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# 
chrome_capabilities = {
    "browserName": "chrome",        # 浏览器名称
    "version": "",                  # 操作系统版本
    "platform": "ANY",              # 平台，这里可以是windows、linux、andriod等等
    "javascriptEnabled": True,      # 是否启用js
}

# 配置谷歌浏览器静默启动【后台启动】
chrome_options = webdriver.ChromeOptions()
# 初始化谷歌浏览器的配置【必须加上】
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--disable-dev-shm-usage')




driver = webdriver.Chrome(desired_capabilities=chrome_capabilities,options = chrome_options)


driver.get("https://weibo.com/newlogin?tabtype=search&openLoginLayer=0&url=")


sleep(10)
print(6666)

n=0
st=""
for i in range(1,51):
   
    s=driver.find_element(By.XPATH,'//div[@data-index="'+str(i)+'"]').text
    st=st+s
    n=n+1
    if(n>4):
        js="window.scrollBy(0,500)" 
        driver.execute_script(js)
        
        n=0
print(st)
msg=MIMEText(st,'plain','utf-8')
msg['From']=formataddr(["热搜助手","pythontest2481@126.com"])
msg['Subject']="微博热搜"
msg['to'] = '543477641@qq.com'
server = smtplib.SMTP_SSL('smtp.126.com')
server.login("pythontest2481@126.com","PHBGOLPROTJQXFHF")
server.sendmail("pythontest2481@126.com","543477641@qq.com",msg.as_string())
server.quit()
driver.close()    
print(1)
 

 
