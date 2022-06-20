import serial
import cv2
import time

faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
while True:
    ret, img = vid.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        # Display the video with a box around the face
        cv2.imshow('video',img)
    with serial.Serial('COM4', 9600, timeout=1) as arduinoSerial:
        # face present: 1
        # face absent: 0
        data = str(1 if len(faces) > 0 else 0)
        print(f'Data: {data}') 
        # Transmit data serially
        arduinoSerial.write(bytes(data, 'utf-8'))
        time.sleep(0.5)
    # Exit condition
    k = cv2.waitKey(30) & 0xff
    if k == ord('q'): # press 'q' to quit
        break

vid.release()
cv2.destroyAllWindows()