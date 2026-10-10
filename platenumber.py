import cv2 as cv
import numpy as np
import os

haar=cv.CascadeClassifier(r"C:\Users\pirat\Downloads\haarcascade_russian_plate_number.xml")

testimage=cv.imread(r"C:\Users\pirat\Desktop\New folder\imag865785es.jpg",0)
plates=haar.detectMultiScale(testimage,1.2,4)
for (x,y,w,h) in plates:
    cv.rectangle(testimage,(x,y),(x+w,y+h),(255,0,0),2)
cv.imshow("testimage",testimage)
cv.waitKey(0)
cv.destroyAllWindows()