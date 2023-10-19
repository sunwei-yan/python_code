import requests
import json
t2=''
import time
with open('t41.txt','r') as f:
    lst = f.readlines()
    lst = [x.strip() for x in lst]
while(1):
    url="https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid=24847869"

    header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    resp=requests.get(url=url,headers=header)
    s=json.loads(resp.text)
    t1=s["data"]["room"][-1]['text']
 

    if(t2!=t1):
        print(s["data"]["room"][-1]['nickname']+"    :     "+s["data"]["room"][-1]['text'])
        t2=t1
        try:
            print(lst[int(s["data"]["room"][-1]['text'])])
        except:
            print("?")
    time.sleep(1)
  
