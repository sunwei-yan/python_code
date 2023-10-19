from socket import *
from unicodedata import name
hostname="10.171.137.38" #192.168.1.3
port_num=23145
# print(socket.gethostname())
for i in range(1,3):
    clientsocket=socket(AF_INET,SOCK_STREAM)
    clientsocket.connect((hostname,port_num))
    messages=input("输入数据")
    clientsocket.send(messages.encode())
    resp=clientsocket.recv(1024).decode()
    print("A:"+resp)
clientsocket.close()


