import requests
import json
from http import server
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
url="https://weibo.com/ajax/statuses/hot_band"
n=0;
t=''
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
resp=requests.get(url=url,headers=header)
s=json.loads(resp.text)
for i in range(0,50):
    if(s["data"]['band_list'][i]['label_name']=='热' or s["data"]['band_list'][i]['label_name']=='爆' or s["data"]['band_list'][i]['label_name']=='沸'):
        n=n+1
        t=t+s["data"]['band_list'][i]['note']+'\t'+s["data"]['band_list'][i]['label_name']+'\n'
        t=t+'\n'
        # print(s["data"]['band_list'][i]['note'])
        # print(s["data"]['band_list'][i]['label_name'])
      
t=t+"当前热搜一共有"+str(n)+"个热点"
print(t)
# print("当前热搜一共有"+str(n)+"个热点")
msg=MIMEText(t,'plain','utf-8')
msg['From']=formataddr(["热搜助手","pythontest2481@126.com"])
msg['Subject']="微博热搜"
msg['to'] = '543477641@qq.com'
server = smtplib.SMTP_SSL('smtp.126.com')
server.login("pythontest2481@126.com","PHBGOLPROTJQXFHF")
server.sendmail("pythontest2481@126.com","543477641@qq.com",msg.as_string())
server.quit()