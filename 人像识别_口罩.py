# 库引入
import cv2
import numpy as np
flag1=6;
flag2=6;
# 特征库引入
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
face_cascade2=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
face_cascade3=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_upperbody.xml')
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(0)

while cap.isOpened():
    flag1=6;
    flag2=6;
    # 视频显示
    flag,frame=cap.read()
    frame = cv2.flip(frame, 1)
    faces=face_cascade.detectMultiScale(frame,1.2,10)
    eye=face_cascade2.detectMultiScale(frame,1.2,10)
    smile=face_cascade3.detectMultiScale(frame,1.2,10)
    img=frame
    #  对识别对象进行框图
    for(x,y,w,h)in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(15,236,87),2)
        face_area=img[y:y+h,x:x+w]
        cv2.putText(img,'people',(x,y-7),3,1.2,(18,23,233),2,cv2.LINE_AA)
        if(x>0 and y>0):
           
            flag2=1
            print("face",flag2)
    for(x,y,w,h)in eye:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,247,181),2)
        face_area=img[y:y+h,x:x+w]
        cv2.putText(img,'eye',(x,y-7),3,1.2,(255,0,251),2,cv2.LINE_AA)
        if(x>0 and y>0):
                
                flag1=1
                print("eye",flag1)
    for(x,y,w,h)in smile:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,247,181),2)
        face_area=img[y:y+h,x:x+w]
        cv2.putText(img,'body',(x,y-7),3,1.2,(230,0,251),2,cv2.LINE_AA)
    # 逻辑判断
    if(flag1==1 and flag2!=1):
        cv2.putText(img,'find mask',(230,80),3,1.5,(15,236,87),2,cv2.LINE_AA)
    key_pressed=cv2.waitKey(60)
    
    # 按键检测
    # print("按键监控",key_pressed)
   
   
    if key_pressed==48:
        img=cv2.Canny(img,100,200)
        img=np.dstack((img,img,img))
    cv2.imshow('rlsb_tool',img)
    if key_pressed==27:
        break
    # 释放内存
cap.release()
cv2.destroyAllWindows
