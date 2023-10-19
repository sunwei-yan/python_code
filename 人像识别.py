import cv2
# import numpy as np
# face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap.open(0)
# while cap.isOpened():
#     flag,frame=cap.read()
#     frame = cv2.flip(frame, 1)
#     faces=face_cascade.detectMultiScale(frame,1.3,2)
#     img=frame
     
#     for(x,y,w,h)in faces:
#         img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,247,181),2)
#         face_area=img[y:y+h,x:x+w]
#         cv2.putText(img,'people',(x,y-7),3,1.2,(255,0,251),2,cv2.LINE_AA)
#     key_pressed=cv2.waitKey(60)
    
    
#     print("123",key_pressed)
#     if key_pressed==48:
#         img=cv2.Canny(img,100,200)
#         img=np.dstack((img,img,img))
#     cv2.imshow('rlsb_tool',img)
#     if key_pressed==27:
#         break
# cap.release()
# cv2.destroyAllWindows
import cv2
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
    
    # 这一步必须有，否则图像无法显示
    
cv2.imwrite('test.jpg',frame)
  

#当一切完成时，释放捕获
cap.release()
print('s')
cv2.destroyAllWindows()
