"""示例代码一：使用 selenium+浏览器 打开百度"""

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
driver.get('https://www.douyin.com/user/MS4wLjABAAAAii1EPSTJnHfrMxQCxNONsfC6hWwBOAUsnuTNLc0g1Q-KG16oGkKuAyx48kexFkMn?modal_id=7197326333913861428')
# 5秒钟后关闭浏览器
time.sleep(5)
driver.close()