import werobot
import cv2
import requests
import json
import codecs
import random
# 配置
robot = werobot.WeRoBot(token='ysw666')  
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.config["APP_ID"] = "wxc408e977c0186c5c"
robot.config["APP_SECRET"] = "098753a566cecea27f718fe592f1d8d3"
# 菜单设置
client=robot.client
client.create_menu({
    "button":[
        {
            "name":"嵌入学习",
            "sub_button":[
                {
                    "type":"click",
                    "name":"51学习笔记",
                    "key":"51"
                },
                {
                    "type":"click",
                    "name":"32学习笔记",
                    "key":"32"
                },
                {
                    "type":"click",
                    "name":"计算机学习笔记",
                    "key":"IT"
                }
            ]
        },
        {
          "type":"click",
                    "name":"毛概",
                    "key":"history"
        },
        {
            "name":"其他",
            "sub_button":[
                {
                    "type":"click",
                    "name":"历史上的今日",
                    "key":"today"
                },
                {
                    "type":"click",
                    "name":"待开发",
                    "key":"wait"
                },
                {
                   "type":"click",
                    "name":"待开发",
                    "key":"wait"
                }
            ]
        }
    ]})
 
# 回复列表
his="""团队历程
1.好芯勤的前世今生
https://mp.weixin.qq.com/s/G3ME4UoHG_ksp26jUkEPhw"""#团队历程
# 普通回复
@robot.handler            
def echo(message):
    if message.content=='help':
     return "本团队成立的目的首先对于自身层面来讲是通过写学习心得用于巩固知识，与优秀同学做进一步的交流,新来的朋友点击下方菜单进行交流"   
    else:return 'Hello World!'
# 关注回复
@robot.subscribe          
def subscribe(message):
    return '感谢您投身伟大的嵌入式事业中!'
# 图像回复
@robot.image
def img(message):
    return message.img 
#菜单回复
@robot.key_click("history")
def history(message):
    with codecs.open('output.json', 'r', 'gbk') as f:
        json_str = f.read()
# 将JSON格式字符串反序列化为Python对象
    data = json.loads(json_str)
# 使用Python对象进行操作
    i=random.randint(1,352)
    s=data[i]['bt']+data[i]['tm']+'\n'+data[i]['xx']+'\n'+data[i]['dn']
    return s
@robot.key_click("today")
def today(message):
    url='https://www.mxnzp.com/api/history/today?type=0&app_id=rgihdrm0kslojqvm&app_secret=WnhrK251TWlUUThqaVFWbG5OeGQwdz09'
    resp=requests.get(url=url)
    t=''
    s=json.loads(resp.text)
    if(len((s['data']))<5):
        for i in range(len((s['data']))):
            t=t+'在'+s['data'][i]['year']+'的今天'+s['data'][i]['title']+'\n'
        return t
    if(len((s['data']))>=5):
        for i in range(5):
            t=t+'在'+s['data'][i]['year']+'的今天'+s['data'][i]['title']+'\n'
        return t
robot.run()
# print("""123
# 465
#       """)