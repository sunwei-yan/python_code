from time import sleep
import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=Chrome()
result=[]



with open('ybk2.txt','r') as f:
    lst = f.readlines()
    lst = [x.strip() for x in lst]
driver.get("https://www.mosoteach.cn/web/index.php?c=interaction_quiz&m=person_quiz_result&clazz_course_id=BBECB45A-E92A-4DB7-9BB7-DE04E2AEB7A0&id=9A3D6985-81F8-3154-3A05-3BC7EB2948B5&order_item=group")
sleep(15)
s=0
    
for i in range(len(lst)):
    
    driver.get(lst[i])
    sleep(2)
    x=driver.find_elements(By.CSS_SELECTOR,'.t-con')
    f2=open('tk.txt','a+')
    for i in x:
        s=s+1
        q=i.find_element(By.CSS_SELECTOR,'.t-subject.t-item.moso-text.moso-editor').text
        t=i.find_element(By.CSS_SELECTOR,'.t-option.t-item').text
        a=i.find_element(By.CSS_SELECTOR,'.answer-l').text
        f2.write(str(s)+'.'+q+'\n'+t+'\n'+a+'\n')
        dat={
    "bt":s,
    "tm":q,
    "xx":t,
    "dn":a
            }
        result.append(dat)
        print(q,'\n',t,'\n',a)
json_str = json.dumps(result, indent=4,ensure_ascii=False)
# 将JSON格式字符串保存到文件中
with open('output6.json', 'w') as f:
    f.write(json_str)


 