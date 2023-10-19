# 导入seleinum的webdriver接口
from selenium import webdriver
import time
from selenium.webdriver import Chrome
import requests
from selenium.webdriver.common.by import By
# 创建浏览器对象
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')

# chrome_options.add_argument('window-size=1920x1080')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.douyin.com/user/MS4wLjABAAAATej2ZE-Xwj_CUA_goppLgY64E_0wgIT5UL0tb7hMPtc')
# 5秒钟后关闭浏览器
time.sleep(5)
n=0
for i in range(1,180):
    s=driver.find_element(By.XPATH,'//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/ul/li['+str(i)+']/a/p').text
    z=driver.find_element(By.XPATH,'//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/ul/li['+str(i)+']/a/div/span/span').text
    print(i)
    n=n+1;
    ff= open('wenan3.xls','a',encoding="utf-8")
    
    if(n>=5):
        # js="window.scrollBy(0,300)" 
        # driver.execute_script(js)
        driver.find_element(By.XPATH,'//*[@id="douyin-right-container"]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/ul/li['+str(i)+']/a/p')
        time.sleep(2)
        n=0;
       
        



# 关闭打开的文件

    print(s)
    print(n)
    ff.write(s+'\t')
    ff.write(z+'\n')
driver.quit()
ff.close()

