from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
def please_giveme_data():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1920x1080')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    location = {
        "latitude": 37.7749,  # 设置纬度
        "longitude": -122.4194  # 设置经度
    }
    chrome_options.add_experimental_option("prefs", {"geolocation": location})
    driver=Chrome(options=chrome_options)
    driver.get("http://www.weather.com.cn/")
    where=driver.find_element(By.XPATH,'//*[@id="cityName"]')
    srk=driver.find_element(By.XPATH,'//*[@id="temp"]')
    weth=driver.find_element(By.XPATH,'//*[@id="sd"]')
    print("""
   ___    _       _             _            __        __                 _     _                   
  / _ \  | |__   | |_    __ _  (_)  _ __     \ \      / /   ___    __ _  | |_  | |__     ___   _ __ 
 | | | | | '_ \  | __|  / _` | | | | '_ \     \ \ /\ / /   / _ \  / _` | | __| | '_ \   / _ \ | '__|
 | |_| | | |_) | | |_  | (_| | | | | | | |     \ V  V /   |  __/ | (_| | | |_  | | | | |  __/ | |   
  \___/  |_.__/   \__|  \__,_| |_| |_| |_|      \_/\_/     \___|  \__,_|  \__| |_| |_|  \___| |_|   
                                                                                                  ysw_v1.0  """)
    return(str(srk.text+where.text+weth.text))
please_giveme_data()
