import requests
import openpyxl
from lxml import etree
url="http://www.kaom.net/jgw_text8.php"
header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
resp=requests.get(url=url,headers=header)
html=etree.HTML(resp.text)
print(resp.text)
