from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
f=open('pl.txt','a+')
j=0
flag=0
driver=Chrome()
driver.get("https://www.douyin.com/video/7198185452522720546")
sleep(30)
# driver.get("https://www.douyin.com/video/7198185452522720546")# //登陆//
# 到最底下
while(flag==0):
    try:
        driver.find_element(By.CSS_SELECTOR,'.BbQpYS5o.HO1_ywVX')
        if(driver.find_element(By.CSS_SELECTOR,'.BbQpYS5o.HO1_ywVX').text=='暂时没有更多评论'):
            flag=1
    except:
        flag=0
    driver.execute_script("window.scrollBy(0,100000)")
    sleep(1)
sleep(5)
for i in range(1,2000):
    try:
            s=driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div/div[1]/div[5]/div/div/div[4]/div['+str(i)+']/div/div[2]/div/p/span/span/span/span/span/span/span').text
            print(s)
            f.write(s+'\n')
            
    except :
        print(i)
        
