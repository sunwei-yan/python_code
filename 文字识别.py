
# import pynput
from PIL import ImageGrab




def sb():
    t.delete(1.0, 'end') 
    imge=ImageGrab.grabclipboard()
    imge.save('02.png')
    #保存
    # from aip import AipOcr
    # APP_ID = '26179233'
    # API_KEY = 'M8s3SZIzRKMoy23t1DAioZAE'
    # SECRET_KEY = 'L7EAE9gGCImPsObBWed6YRbrXrVqfr6j'
    # # (不轻易用)
    # client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # fp=open('02.png', 'rb')

    # pic = fp.read()



    # text = client.basicGeneral(pic)

    # for i in text['words_result']:
    #     t.insert('insert',i['words'])
    import requests
    password='8907'
    url = "http://www.iinside.cn:7001/api_req"
    filePath='02.png'
    data={
        'password':password,
        'reqmode':'ocr_pp'
    }

    files=[('image_ocr_pp',('wx.PNG',open(filePath,'rb'),'application/octet-stream'))]
    headers = {}
    response = requests.post( url, headers=headers, data=data, files=files)
    x=response.text
    t.insert('insert',x[19:-3])

        
    # files=[('image_ocr_pp',('wx.PNG',open(filePath,'rb'),'application/octet-stream'))]
    # headers = {}
    # response = requests.post( url, headers=headers, data=data, files=files)
    # x=response.text
  
    # t.insert('insert',x[19:-3])
# 123456789123456789
    
def cs():
    t.delete(1.0,'end')
    t.insert('insert',"2.5. Entry&Text输入框与文本框") 
# 界面
import tkinter 
window=tkinter.Tk()
window.title("家庭财务发票识别")
window.geometry('300x600')
l=tkinter.Label(window,text='截取发票图片并文字识别',font=(20),bg='yellow')
l2=tkinter.Label(window,text='先截图，后点击按钮识别',font=(20),bg='red')
l3=tkinter.Label(window,text='21计科人工智能颜孙炜制',font=(20),bg='blue')
l.place(x=30,y=50,width=250,height=50)
l2.place(x=20,y=500,width=250,height=50)
l3.place(x=20,y=540,width=250,height=50)
b=tkinter.Button(window,text='开始识别'
,bg='pink',
width=15,height=2,command=sb)
b.place(x=85,y=120)
t = tkinter.Text(window, 
                 state='normal',  # 有disabled、normal 两个状态值，默认为normal
                 width=35, height=20
                 )
t.place(x=20,y=200)







window.mainloop()