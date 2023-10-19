
from time import sleep

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
f=open('1.txt','a+')
driver=Chrome()
driver.get("https://s.weibo.com/weibo?q=%23%E6%A0%B8%E9%85%B8%E6%A3%80%E6%B5%8B%E4%B9%B1%E8%B1%A1%E8%80%97%E7%9A%84%E6%98%AF%E5%9B%BD%E5%BA%93%E4%BC%A4%E7%9A%84%E6%98%AF%E6%B0%91%E5%BF%83%23&page=1")
l=[]
q=''
sleep(30)
# while(driver.current_url!='https://s.weibo.com/weibo?q=%E9%99%88%E9%A3%9E%E5%AE%87'):
#     driver.get("https://s.weibo.com/weibo?q=%E9%99%88%E9%A3%9E%E5%AE%87")
#     sleep(2)
for  j in range(1,18):
    driver.get("https://s.weibo.com/weibo?q=%23%E6%A0%B8%E9%85%B8%E6%A3%80%E6%B5%8B%E4%B9%B1%E8%B1%A1%E8%80%97%E7%9A%84%E6%98%AF%E5%9B%BD%E5%BA%93%E4%BC%A4%E7%9A%84%E6%98%AF%E6%B0%91%E5%BF%83%23&page="+str(j))
    sleep(2)
    for i in range(1,15):
        try:
            srk=driver.find_element(By.XPATH,'//*[@id="pl_feedlist_index"]/div[1]/div['+str(i)+']/div[2]/div[1]/div[2]/p[3]/a[1]')
            print(srk.get_attribute('href'))
            f.write(srk.get_attribute('href')+'\n')
        except:
            try:
                srk=driver.find_element(By.XPATH,'//*[@id="pl_feedlist_index"]/div[1]/div['+str(i)+']/div/div[1]/div[2]/p[2]/a[1]')
                print(srk.get_attribute('href'))
                f.write(srk.get_attribute('href')+'\n')
            except:
                print(j,i) 
       

f.close()  

 