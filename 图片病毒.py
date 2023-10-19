import cv2
img = cv2.imread('2.png')
import random

for i in range(1,20):
    cv2.imshow('image'+str(i), img)
    s=random.randint(1,20)
    # 释放窗口
    cv2.moveWindow('image'+str(i), 0+s*50, 0+s*50)
for i in range(1,20):
    cv2.imshow('image2'+str(i), img)
    s=random.randint(1,20)
    # 释放窗口
    cv2.moveWindow('image2'+str(i), 0+s*50, 0)
for i in range(1,20):
    cv2.imshow('image3'+str(i), img)
    s=random.randint(1,20)
    # 释放窗口
    cv2.moveWindow('image3'+str(i), 0, 0+s*50)
# x=500
# y=500
# def delay():
#     for i in range(10000):
#         for j in range(10000):
#             s=0
# def up():
#     global x
#     global y
#     for i in range(1,5):
#         y=y-50
        
#         cv2.imshow('image2', img)
       
#         cv2.moveWindow('image2',x, y)
#         delay()
#         cv2.destroyAllWindows()
# cv2.imshow('image2', img)

# s=random.randint(1,5)
# # if(s==1):
# up()
# if(s==2):
#     down()
# if(s==3):
#     west()
# if(s==4):
#     east()
# for i in range(1,20):
#  cv2.moveWindow('image2'+str(i), 0+*50, 0)
cv2.waitKey(0)
# import win32gui
# import win32con
# import time
# from PIL import Image
# # 读取图片
# image = Image.open('2.png')
# # 获取屏幕大小
# screenWidth = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# screenHeight = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
# # 设置图片初始位置
# x, y = 0, 0
# # 设置图片每次移动的距离
# step = 10
# # 设置图片移动的方向（1表示向右移动，-1表示向左移动）
# direction = 1
# # 获取桌面窗口句柄
# desktop = win32gui.GetDesktopWindow()
# # 循环移动图片
# while True:
#     # 计算图片的新位置
#     x += step * direction
#     # 如果图片已经到达屏幕边缘，则改变移动方向
#     if x <= 0 or x + image.width >= screenWidth:
#         direction *= -1
#     # 更新图片位置
#     win32gui.SetWindowPos(desktop, 0, x, y, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)
#     # 等待一段时间，再进行下一次移动（可以根据需要调整时间）
#     time.sleep(0.1)
