import math
import keyboard
from numpy import double
import pyautogui

y = 360
i = 0

while(1):
    keyboard.wait('a') #键盘监听

    x,y=pyautogui.position()
    print("起始坐标",end='')
    print(x,y)
    keyboard.wait('s') #键盘监听

    z,w=pyautogui.position()
    print("末尾坐标",end='')
    print(z,w)
    l=math.sqrt((x-z)*(x-z)+(y-w)*(y-w))
    L=int(l)
    print("距离",end='')
    print(L)

    print("跳跃")
    pyautogui.mouseDown()
    for i in range(45000):
    
        for j in range(L):
            j=j+1
    i=i+1
    pyautogui.mouseUp()
