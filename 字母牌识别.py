import cv2
import numpy as np
import ddddocr
flag=0
# 特征库引入
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
face_cascade2=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
face_cascade3=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_upperbody.xml')
cap=cv2.VideoCapture(1,cv2.CAP_DSHOW)
cap.open(0)

while cap.isOpened():
    flag1=6;
    flag2=6;
    # 视频显示
    flag,frame=cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.flip(frame, 1)
    faces=face_cascade.detectMultiScale(frame,1.2,10)
    eye=face_cascade2.detectMultiScale(frame,1.2,10)
    smile=face_cascade3.detectMultiScale(frame,1.2,10)
    img=frame
    #  对识别对象进行框图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 二值化处理
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 获取轮廓
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历轮廓，找到最大的矩形轮廓
    max_area = 0
    max_rect = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_rect = cv2.boundingRect(contour)
            
    # 裁剪图片


    # 获取图片宽度和高度
    height, width = img.shape[:2]

    # 放大图片05
    scale_factor = 1.2
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # 保存放大后的图片
    cropped_img = resized[int(height/3):int(2*height/3), 0:width]
    cv2.imwrite('1010.png', cropped_img)

    ocr=ddddocr.DdddOcr()
    img=open('1010.png','rb')

    img=img.read()
    if(len(ocr.classification(img))==4):
        print(ocr.classification(img))
        break


   
    key_pressed=cv2.waitKey(60)
    
    # 按键检测
    # print("按键监控",key_pressed)
   
   
    
    cv2.imshow('rlsb_tool',frame)
    if key_pressed==27:
        break
    # 释放内存
cap.release()
cv2.destroyAllWindows