import requests
import json

    
url="https://api.bilibili.com/x/relation/stat?vmid=351762392&jsonp=jsonp"
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
resp=requests.get(url=url,headers=header)
s=json.loads(resp.text)
print(s['data']['follower'])


