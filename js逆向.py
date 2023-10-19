import requests
url="https://api.kertennet.com/live/translate"


data={ 
      "text":"hello",
      "to":"zn"
}
resp=requests.get(url=url,data=data)
print(resp.text)