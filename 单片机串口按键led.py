from turtle import width
import serial
from  tkinter import *
from sqlalchemy import asc
wimd=Tk()
wimd.title('LED')
wimd.geometry('461x250')

com = serial.Serial('COM7', 9600)
print (com)

def led1():
        success_bytes = com.write('1'.encode())
        print (success_bytes)
def led2():
        success_bytes = com.write('2'.encode())
        print (success_bytes)   
def led3():
        success_bytes = com.write('3'.encode())
        print (success_bytes)
def led4():
        success_bytes = com.write('4'.encode())
        print (success_bytes)  
def led5():
        success_bytes = com.write('5'.encode())
        print (success_bytes)
def led6():
        success_bytes = com.write('6'.encode())
        print (success_bytes)   
def led7():
        success_bytes = com.write('7'.encode())
        print (success_bytes)
def led8():
        success_bytes = com.write('8'.encode())
        print (success_bytes)  
def led9():
        success_bytes = com.write('9'.encode())
        print (success_bytes)  

bt1=Button(text='LED1_on',command=led1,width=8,height=2)
bt1.place(x=20,y=20)

bt2=Button(text='LED2_on',command=led2,width=8,height=2)
bt2.place(x=100,y=20)
bt3=Button(text='LED3_on',command=led3,width=8,height=2)
bt3.place(x=180,y=20)
bt4=Button(text='LED4_on',command=led4,width=8,height=2)
bt4.place(x=260,y=20) 
bt1=Button(text='LED1_0ff',command=led5,width=8,height=2)
bt1.place(x=20,y=80)
bt2=Button(text='LED2_off',command=led6,width=8,height=2)
bt2.place(x=100,y=80)
bt3=Button(text='LED3_off',command=led7,width=8,height=2)
bt3.place(x=180,y=80)
bt4=Button(text='LED4_off',command=led8,width=8,height=2)
bt4.place(x=260,y=80) 
bt4=Button(text='流水灯',command=led9,width=8,height=2)
bt4.place(x=20,y=140) 
wimd.mainloop()