import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
cap = cv2.VideoCapture(0)
cap.set(3, 3840)  # 设置高度
cap.set(4, 3160)  # 设置宽度
detector = HandDetector(detectionCon=0.7,maxHands=1)  # 设置阈值
flag=0;
flag2=0;
flag5=0;
a=0
b=0
c=0
a1=0
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img= cv2.flip(img, 1)
    cv2.imshow("gestureHand", img)
    if hands:
        if(hands[0]['type'])=='Right':
            lmList = hands[0]['lmList']
            print(lmList[12])
            a,b,c=lmList[8]
         
            pyautogui.moveTo((1280-a),b*1.5)
            # print("鼠标在",end="")
            # print(pyautogui.position())
            # print("手在",end="")
            # print(a)
            # print("分辨率是",end="")
            # print (pyautogui.size())
            
            # 1919
            # 1979
            # 1280
            # 720
            # if(a1-a>30):
            #    pyautogui.keyDown('right')
            # if(a-a1>30):
            #        pyautogui.keyDown('left')  
            fingers = detector.fingersUp(hands[0])
            if fingers[2] == 1:
                flag=1
            if(flag==1 and fingers[2] == 0):
                print ("666")
                x,y=pyautogui.position()
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                flag=0
            
            if fingers[3] == 1:
                flag2=1
            if(flag2==1 and fingers[3] == 0):
                print ("666")
                x,y=pyautogui.position()
                for i in range(1,3):
                    pyautogui.mouseDown()
                    pyautogui.mouseUp()
                flag2=0 
            # if fingers[4] == 1:
            #     flag5=1
            # if(flag5==1 and fingers[4] == 0):
            #     print ("666")
            #     x,y=pyautogui.position()
            #     pyautogui.hotkey('alt','a')
                # for i in range(1,5):
                #     pyautogui.mouseDown()
                #     pyautogui.mouseUp()
                # flag5=0 
            
    if 27==cv2.waitKey(1):
        break
    if ord("q")==cv2.waitKey(1):
        print("555")
        
# [{'lmList': [[77, 182, 0], [101, 176, -4], [122, 164, -6], [132, 149, -9], [131, 134, -11], [119, 140, 2], [128, 124, -6], [123, 137, -13], [119, 149, -16], [106, 135, 1], [113, 121, -8], [108, 137, -12], [104, 148, -13], [91, 133, -1], [98, 119, -10], [95, 135, -8], [91, 145, -4], [76, 132, -4], [83, 121, -9], [82, 133, -5], [80, 142, 0]], 'bbox': (76, 119, 56, 63), 'center': (104, 150), 'type': 
# 'Right'}]zzzzzzzzzzz
# 测试区
# 1zzzzzzzz
# 1zxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
# 1xzzzzzzzzzz
# 1zzzzzzzzzzzzzzzzzzz
# 1zzzzzzzz
# 1zxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
# 1xzzzzzzzzzz
# 1zzzzzzzzzzzzzzzzzzz# 1zzzzzzzz
# 1zxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
# 1xzzzzzzzzzz
# 1zzzzzzzzzzzzzzzzzzz# 1zzzzzzzz
# 1zxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
# 1xzzzzzzzzzz
# 1zzzzzzzzzzzzzzzzzzz