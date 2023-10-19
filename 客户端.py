from socket import *
from unicodedata import name
hostname="DESKTOP-260UTF0" #192.168.1.3
port_num=5021
# print(socket.gethostname())
clientsocket=socket(AF_INET,SOCK_STREAM)
clientsocket.connect((hostname,port_num))
for i in range(1,10):
    messages=input("输入数据")
    clientsocket.send(messages.encode())
    resp=clientsocket.recv(1024).decode()
    print("收到了"+resp)
clientsocket.close()

