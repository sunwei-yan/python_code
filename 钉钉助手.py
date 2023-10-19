import json
import requests
def dd_robot():
  HEADERS = {"Content-Type": "application/json;charset=utf-8"}
  # 之前复制的接口地址和token信息
  url = 'https://oapi.dingtalk.com/robot/send?access_token=048209a4701b99c4fb0382a1ffb50f6cf34d279dc82790bd6b6eb4062022b671'
  #content里面要设置关键字
  data_info = {
    "msgtype": "text",
    "isAtAll":True,
    "text": {
    "content": 'ysw:今日全员核酸！'
    },
    "at": {
        "isAtAll":True
    },
    #这是配置需要@的人
     # ,"at": {"atMobiles": ["15xxxxxx06",'18xxxxxx1']}
  }
  value = json.dumps(data_info)
  response = requests.post(url,data=value,headers=HEADERS)
  if response.json()['errmsg']!='ok':
    print(response.text)

if __name__ == '__main__':
    dd_robot()
