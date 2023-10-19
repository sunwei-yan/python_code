import tkinter as tk
import time
import requests
import json
st=1
id=''

with open('t41.txt','r') as f:
    lst = f.readlines()
    lst = [x.strip() for x in lst]

url="https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid="+id

header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
def copy_text():
   full1=0
   full2=0
   global id
   id= input_text.get()
   url="https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid="+id
   global st
   st=1
   t2=''
   while(st==1):
        resp=requests.get(url=url,headers=header)
        s=json.loads(resp.text)
        t1=s["data"]["room"][-1]['text']
    

        if(t2!=t1):
            print(s["data"]["room"][-1]['nickname']+"    :     "+s["data"]["room"][-1]['text'])
            t2=t1
          
            try:
                q=s["data"]["room"][-1]['nickname']+"答案之书给你的答案是:     "+lst[int(s["data"]["room"][-1]['text'])]+'\n'
                display_text.insert(tk.END, q)
                print(lst[int(s["data"]["room"][-1]['text'])])
                if(full1>=7):
                     display_text.delete("1.0","end")
                     full1=0
                full1=full1+1
            except:
                 full2=full2+1
                 w=s["data"]["room"][-1]['nickname']+"    :     "+s["data"]["room"][-1]['text']+'\n'
                 display_text2.insert(tk.END, w)
                 if(full2>=17):
                         display_text2.delete("1.0","end")
                         full2=0
                 
        root.update()
    

def clear_text():
    global st
    
    st=0
    display_text2.delete("1.0","end")
    display_text.delete("1.0","end")
root = tk.Tk()
root.title("b站直播答案之书工具")
root.geometry('720x720')
input_label = tk.Label(root, text="id")
# input_label.grid(row=0, column=0)
input_label.place(x=360,y=10)
input_text = tk.Entry(root)
# input_text.grid(row=1, column=0)
input_text.place(x=300,y=50)
copy_button = tk.Button(root, text="开始", command=copy_text)
# copy_button.grid(row=2, column=0)
copy_button.place(x=360,y=90)
clear_button = tk.Button(root, text="结束", command=clear_text)
# clear_button.grid(row=3, column=0)
clear_button.place(x=360,y=130)
display_label = tk.Label(root, text="答案之书:网抑云b站分云制作")
# display_label.grid(row=4, column=0)
display_label.place(x=300,y=170)
display_text = tk.Text(root, height=50, width=100,font=("Helvetica", 15))
# display_text.grid(row=5, column=0, columnspan=2)
display_text.place(x=0,y=210)
display_text2 = tk.Text(root, height=50, width=100,font=("Helvetica", 10))
# display_text.grid(row=5, column=0, columnspan=2)
display_text2.place(x=0,y=400)
display_label = tk.Label(root, text="答案之书，\n在B站直播间评论区输入1-100\n软件会给出答案",font=("Helvetica",15))
# display_label.grid(row=4, column=0)
display_label.place(x=30,y=60)
root.mainloop()