import requests
from lxml import etree
url = 'https://www.zhihu.com/hot'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
}
resp= requests.get(url=url, headers=headers)
html=etree.HTML(resp.text)
print(html)
i=html.xpath("//section[3]/div[2]/a/h2/text()")
print(i)

