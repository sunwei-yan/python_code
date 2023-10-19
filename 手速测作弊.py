import cv2
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=Chrome()
driver.get("https://humanbenchmark.com/tests/reactiontime")
l=[]
sleep(5)
driver.find_element(By.CSS_SELECTOR,'.css-42wpoy.e19owgy79').click()
sleep(1)
while(1):
    s=driver.find_element(By.CSS_SELECTOR,'.css-42wpoy.e19owgy79')
    s.screenshot('6.png')
    q=cv2.imread('6.png')
    if(q[0][0][0]==98):
        driver.find_element(By.CSS_SELECTOR,'.css-42wpoy.e19owgy79').click()
        break
sleep(10)
