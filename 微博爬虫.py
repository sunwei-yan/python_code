from asyncio.windows_events import NULL
import profile
from time import sleep

from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from sqlalchemy import null

driver=Chrome()

driver.get("https://weibo.com/newlogin?tabtype=search&openLoginLayer=0&url=")


sleep(10)
print(6666)
s=driver.find_element(By.CSS_SELECTOR,'.woo-box-flex.woo-box-alignCenter.ProfileHeader_h4_gcwJi').text
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
driver.close()    
print(1)
 
