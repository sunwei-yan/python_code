import json
import time
import requests
def _get_roomid_(web_url):
    params = {
        'url': web_url, 
        'token': '320721'
        }
    res = (json.loads(requests.post(url='http://49.235.82.99:8081/get_roomid', data=params).text))
    print(res)
    room_id_ = res['room_id']
    return room_id_


def _get_danmu_(roo_mid):
    params = {
        'room_id': roo_mid, 
        'cursor': '', 
        'internal_ext': '', 
        'token': '320721'
        }
    while True:
        res = requests.post(url='http://49.235.82.99:8081/get_danmu', data=params).text
        res = json.loads(res)
        params['cursor'] = res['cursor']
        params['internal_ext'] = res['fetchInterval']
        for message in res['messagelist']:
            print(message)
        time.sleep(1)  # 一定要休息1s


# 替换直播地址即可
if __name__ == '__main__':
    url = 'https://live.douyin.com/204869389381'
    room_id = _get_roomid_(url)
    _get_danmu_(roo_mid=7192258244294101760)