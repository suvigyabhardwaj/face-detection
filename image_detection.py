import cv2
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("image.jpg")
gray_scale=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_scale,1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (17,3,255), 2)

cv2.imshow("image", img)
cv2.waitKey()
