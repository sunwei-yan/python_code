"""示例代码一：使用 selenium+浏览器 打开百度"""
# 导入seleinum的webdriver接口
from selenium import webdriver
import time
from selenium.webdriver import Chrome
import requests
from selenium.webdriver.common.by import By
import tkinter
# 创建浏览器对象
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')

# chrome_options.add_argument('window-size=1920x1080')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--ignore-certificate-errors')
# window = tkinter.Tk()
# window.title("直播间小工具")
# window.geometry("500x500")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://live.douyin.com/144161826012?cover_type=0&enter_from_merge=web_live&enter_method=web_card&game_name=&is_recommend=1&live_type=game&more_detail=&request_id=20230123213259B20A2159FC6F651985B2&room_id=7191834473904802597&stream_type=vertical&title_type=1&web_live_page=hot_live&web_live_tab=all')
# 5秒钟后关闭浏览器
time.sleep(5)
i=2
while(1):
    
    
    time.sleep(1)
    try:
        driver.find_element(By.XPATH,'//*[@id="_douyin_live_scroll_container_"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div['+str(i)+']/div/span[3]/span')
    except:
        n=0
    else:
        print(driver.find_element(By.XPATH,'//*[@id="_douyin_live_scroll_container_"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div['+str(i)+']/div/span[3]/span').text)
        i=i+1
             
        



# 关闭打开的文件

    
driver.quit()

