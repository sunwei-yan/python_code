from email import message
from socket import *
import string
from struct import pack
from tkinter import *
from matplotlib.pyplot import connect
from sqlalchemy import modifier
import multiprocessing
global  mess
def tcp():
    seversocket=socket(AF_INET,SOCK_STREAM)
    seversocket.bind((gethostname(),5021))
    print("准备接受信息")
    for i in range(1,10):
        seversocket.listen(10)
        
        consoc,adress=seversocket.accept()
        message = consoc.recv(1024).decode()
        print("客户端:"+message)

        modifmessage=mess.encode()
        consoc.send(modifmessage)
    seversocket.close()
def tk():
    wind=Tk()
    wind.title="123"
    en=Entry()
    en.pack()
    mess=en.get()
   
    wind.mainloop()
if __name__ == '__main__':
       
        tcppro=multiprocessing.Process(target=tcp)
        ttkpro=multiprocessing.Process(target=tk)
        tcppro.start()
        ttkpro.start()
        
#该机作为服务器
# 提供大小写转化
