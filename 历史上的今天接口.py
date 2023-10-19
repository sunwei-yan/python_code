import requests
import json
url='https://www.mxnzp.com/api/history/today?type=0&app_id=rgihdrm0kslojqvm&app_secret=WnhrK251TWlUUThqaVFWbG5OeGQwdz09'
resp=requests.get(url=url)
t=''
s=json.loads(resp.text)
print(s)
for i in range(len((s['data']))):
    t=t+'在'+s['data'][i]['year']+'的今天'+s['data'][i]['title']+'\n'
    
print(t)
