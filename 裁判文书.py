
from time import sleep

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# f=open('1.txt','a+')
driver=Chrome()
driver.get("https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=4L13DrbIdEzV6Er1vYtavCRF+bYkv8V5ZLtQ3yRuKLq1rcsuOAVdYZO3qNaLMqsJyA3OipRyG3fXTTUjMP3cAswZTGhhuH4xkoN4w/MsoGNcPnil7g1paM60anwwFbXP")
l=[]
q=''
sleep(30)
# while(driver.current_url!='https://s.weibo.com/weibo?q=%E9%99%88%E9%A3%9E%E5%AE%87'):
#     driver.get("https://s.weibo.com/weibo?q=%E9%99%88%E9%A3%9E%E5%AE%87")
#     sleep(2)
for  j in range(1,18):
    for i in range(100):
        try:
            driver.get("https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=4L13DrbIdEzV6Er1vYtavCRF+bYkv8V5ZLtQ3yRuKLq1rcsuOAVdYZO3qNaLMqsJyA3OipRyG3fXTTUjMP3cAswZTGhhuH4xkoN4w/MsoGNcPnil7g1paM60anwwFbXP")
            sleep(2)
            
                
            srk=driver.find_element(By.XPATH,'//*[@id="_view_1541573883000"]/div/div[1]/div[3]/div['+str(i)+']')
        
            print(srk.text)
            s=srk.text
            for q in range(len(s)):
                if(s[q]=="被"  and s[q+1]=="告" and s[q+2]=="人"):
                    print(s[q+3],end='')
                    print(s[q+4],end='')
                    print(s[q+5],end='')
                if(s[q]=="男"   or s[q]=="女"):
                    print(s[q])
        except:
            print("error")



 