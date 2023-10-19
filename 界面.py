import socket
import threading
# 导入SQLite驱动:
import sqlite3
sem=threading.Semaphore(1)
IP=""
port=40000
def create_db():
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在，会自动在当前目录创建:
    conn = sqlite3.connect('test.db')
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

    try:
        cursor.execute('create table data1 (id varchar(20), temp varchar(20),humi varchar(20),tt varchar(40))')
    except Exception as e:
        print(e)
    # 继续执行一条SQL语句，插入一条记录:
    # cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)

    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()
    #创建另外一个表
    conn = sqlite3.connect('test.db')
    # 创建一个Cursor:
    cursor = conn.cursor()
    # 执行一条SQL语句，创建user表:
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

    try:
        cursor.execute('CREATE TABLE light2 (id varchar(20), led varchar(20),duoji varchar(20),fm varchar(20) )')
    except Exception as e:
        print(e)
    # 继续执行一条SQL语句，插入一条记录:
    # cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

    # 通过rowcount获得插入的行数:
    print(cursor.rowcount)

    # 关闭Cursor:
    cursor.close()
    # 提交事务:
    conn.commit()
    # 关闭Connection:
    conn.close()

def handle(ip_port,new_client):
        print("客户端的ip和端口号是：" , ip_port)
        # 5.接收数据
            #收发消息使用新返回的套接字
        rece_data = new_client.recv(1024)
        if rece_data:
            rece_data = rece_data.decode('utf-8')
            print("接收到的数据是",rece_data)
            # 6.发送数据
            result=rece_data.split(";")
            if(result[0]=="command=client1"):
                t=result[1].split("=")[1]#获取客户端发来的时间
                temperature=result[2].split("=")[1]#获取客户端发来的温度
                humi=result[3].split("=")[1]#获取客户端发来的湿度
                id=result[4].split("=")[1]#获取客户端发来的设备ID
                #print("here",t,temperature,humi,id)
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                cursor.execute('insert into data1 (id, temp,humi,tt) values (%s, %s,%s,"%s")' % (id, temperature, humi, t))
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=client1;\r\n"
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC1":
                d=result[1].split("=")[1]#获取设备编号
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC1;device=%s;temperature=%s"%(d,a[0][1])
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC2":
                d=result[1].split("=")[1]#获取设备编号
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC2;device=%s;temperature=%s"%(d,a[0][2])
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if (result[0] == "command=client2"):
                id = result[1].split("=")[1]  # 获取客户端发来的设备ID
                # print("here",t,temperature,humi,id)
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                cursor.execute('select * from light where id=%s' % (id,))
                a=cursor.fetchall()
                print("light",a)
                #a[0][0]为设备ID，a[0][1]为LED状态
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=client2;device=%s;light=%s"%(id,a[0][1])
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC3":
                d=result[1].split("=")[1]#获取设备编号
                light="on"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC3;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC4":
                d=result[1].split("=")[1]#获取设备编号
                light="off"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC4;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC5":
                d=result[1].split("=")[1]#获取设备编号
                light="off1"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC4;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC6":
                d=result[1].split("=")[1]#获取设备编号
                light="on1"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC3;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC5":
                d=result[1].split("=")[1]#获取设备编号
                light="off2"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC4;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC7":
                d=result[1].split("=")[1]#获取设备编号
                light="on2"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC3;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC8":
                d=result[1].split("=")[1]#获取设备编号
                light="off3"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC4;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
            if result[0]=="command=PC6":
                d=result[1].split("=")[1]#获取设备编号
                light="on3"
                sem.acquire()
                conn = sqlite3.connect('test.db')
                cursor = conn.cursor()
                #cursor.execute('select * from data1 where id=%s order by tt desc limit 1 ;' % (d,))
                cursor.execute("update light set led='%s' where id='%s'"%(light,d))
                #a = cursor.fetchall()
                #a[0][1]为温度a[0][2]为湿度a[0][0]为设备ID，a[0][3]为时间
                cursor.close()
                conn.commit()
                conn.close()
                sem.release()
                send_content = "command=PC3;device=%s;light=%s"%(d,light)
                send_data = send_content.encode('utf-8')
                new_client.send(send_data)
                new_client.close()
        else:
            print("客户端下线了",ip_port)


if __name__ == '__main__':
    # 1.创建服务端套接字
        # socket.AF_INET表示IPv4类型
        # SOCK_STREAM表示tcp
    create_db()#创建数据库
    tcp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        #端口复用 服务端退出端口立即释放
        #socket.SOL_SOCKET 表示当前套接字
        #socket._RetAddress 复用选项
        #True 确定复用
    # 2.绑定端口号
        # 第一个参数表示ip地址，一般不用置顶 表示本机的任何一个ip
        #第二个参数表示端口号
    tcp_server_socket.bind((IP,port))
    # 3.设置监听
        # 128:表示最大等待建立链接的个数
    tcp_server_socket.listen(128)
    # 4.等待客户端的连接请求
        #每次客户端和服务器建立连接成功都会返回一个新的套接字
    while   True:
        new_client , ip_port = tcp_server_socket.accept()
        sub_thresd = threading.Thread(target=handle,args=(ip_port,new_client))
        sub_thresd.start()


    # 7.关闭套接字
    tcp_server_socket.close()


