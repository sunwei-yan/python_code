from turtle import width
import serial
from  tkinter import *
from sqlalchemy import asc
wimd=Tk()
wimd.title('车')
wimd.geometry('461x250')



def led1():
        com = serial.Serial('COM5', 9600)
        print (com)

        success_bytes = com.write('a'.encode())
        print (success_bytes)

def led5():
        com = serial.Serial('COM5', 9600)
        print (com)

        success_bytes = com.write('b'.encode())
        print (success_bytes)


bt1=Button(text='前进',command=led1,width=8,height=2)
bt1.place(x=20,y=20)

# bt2=Button(text='LED2_on',command=led2,width=8,height=2)
# bt2.place(x=100,y=20)
# bt3=Button(text='LED3_on',command=led3,width=8,height=2)
# bt3.place(x=180,y=20)
# bt4=Button(text='LED4_on',command=led4,width=8,height=2)
# bt4.place(x=260,y=20) 
bt1=Button(text='后退',command=led5,width=8,height=2)
bt1.place(x=20,y=80)
# bt2=Button(text='LED2_off',command=led6,width=8,height=2)
# bt2.place(x=100,y=80)
# bt3=Button(text='LED3_off',command=led7,width=8,height=2)
# bt3.place(x=180,y=80)
# bt4=Button(text='LED4_off',command=led8,width=8,height=2)
# bt4.place(x=260,y=80) 
# bt4=Button(text='流水灯',command=led9,width=8,height=2)
# bt4.place(x=20,y=140) 
wimd.mainloop()