import cv2 as cv
import easyocr
carvid = cv.VideoCapture(r"C:\Users\pirat\Desktop\New folder\.vscode\cars\carss.mp4")
numberplate=cv.CascadeClassifier(r"C:\Users\pirat\Downloads\haarcascade_russian_plate_number.xml")
while True:
    ret,frame=carvid.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    plates=numberplate.detectMultiScale(gray,1.2,4)#
    for (x,y,w,h) in plates:
        resultimg=cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv.imshow("Video",frame)
    if cv.waitKey(33) == 112:
        break
cv.destroyAllWindows()
cv.imwrite(r"C:\Users\pirat\Desktop\New folder\.vscode\cars\resultimg.jpg",resultimg)
reader = easyocr.Reader(['en'])
results = reader.readtext(r"C:\Users\pirat\Desktop\New folder\.vscode\cars\resultimg.jpg", detail=0)
print(results)