from time import sleep

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=Chrome()
driver.get("https://s.taobao.com/search?fromTmallRedirect=true&tab=mall&q=%E7%94%B7%E9%9E%8B&spm=875.7931836.0.0.5bc14265QsTMMV")
l=[]
sleep(5)
while(driver.current_url!='https://s.taobao.com/search?spm=a21bo.jianhua.201867-main.10.55a711d98yNl9S&q=%E7%94%B7%E8%A3%85'):
    driver.get("https://s.taobao.com/search?spm=a21bo.jianhua.201867-main.10.55a711d98yNl9S&q=%E7%94%B7%E8%A3%85")



sleep(3)
for i in range(1,50):
    try:
        srk=driver.find_element(By.XPATH,'//*[@id="mainsrp-itemlist"]/div/div/div[1]/div['+str(i)+']/div[2]/div[2]')
        print(srk.text)
    except:
       sleep(1) 
sleep(10)
   

 