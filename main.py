import cv2

video = cv2.VideoCapture("C:\\Users\\pirat\\Desktop\\New folder\\cars.mp4")
classifier = cv2.CascadeClassifier("C:\\Users\\pirat\\Desktop\\New folder\\cars.xml")
while True :
    bval,pixels = video.read()
    gray = cv2.cvtColor(pixels,cv2.COLOR_BGR2GRAY)
    cars = classifier.detectMultiScale(gray,1.1,1)
    for x,y,w,h in cars:
        cv2.rectangle(pixels,(x,y),(x+w,y+h),(0,0,255),5)
    cv2.imshow("Video",pixels)      
    if cv2.waitKey(33) == 112:
        break
cv2.destroyAllWindows()
print(cars)
count = len(cars)
print(count)      