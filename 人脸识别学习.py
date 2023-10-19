from ast import While
from sqlite3 import InterfaceError
from turtle import color
import cv2 as cv
from cv2 import waitKey
from cv2 import resize
from numpy import True_
from sqlalchemy import true

def rlsb(img):
    gary=cv.cvtColor(img,cv.COLOR_BGR2BGRA)
    face_detect=cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
    face=face_detect.detectMultiScale(gary,1.09,12)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=6)
    cj=cv.resize(img,dsize=(1200,800))
    cv.imshow('123',cj)
cap=cv.VideoCapture(0)

while True:
    flag,frame=cap.read()
    if not flag:
        break
    rlsb(frame)
    if ord('q')==cv.waitKey(60):
        break
# img=cv.imread("111.jpeg")
# rlsb()

cv.destroyAllWindows()
cap.release()



# 坐标
# x,y,w,h=100,100,100,100
# cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,255),thickness=50,lineType=5)
# cv.circle(img,(500,500),200,color=(255,255,0),thickness=5)
# # xiugai=cv.resize(img,dsize=(200,200))
# cv.imshow('123',img)
# while True:
#     if ord('q')==cv.waitKey(0):
#         break
# # gray_img=cv.cvtColor(img,cv.COLOR_RGB2BGRA)
# # cv.imshow('123',gray_img)
# # cv.imwrite('123.jpg',gray_img)
# # cv.imshow('wife_found_tool',img)
# cv.waitKey(0)
# cv.destroyAllWindows()
