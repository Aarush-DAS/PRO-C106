import cv2 

boy=cv2.imread("boy.jpg")
gray=cv2.cvtColor(boy,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces=face_cascade.detectMultiScale(gray)
#print(faces)
#cv2.rectangle(image, start_point, end_point, color,thickness)
for(x,y,w,h) in faces:
    cv2.rectangle(boy,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("display",boy)   
cv2.waitKey(0) 

