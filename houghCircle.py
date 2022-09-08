import cv2
import numpy as np

def houghCircle(frame):

    frame = cv2.GaussianBlur(frame, (9, 9), 0)
    
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1, 10, param1=60, param2=50, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))

        print(circles)

        for i in circles[0, :]:
            cv2.circle(frame, (i[0], i[1]), i[2], (255, 255, 0), 2)
        cv2.imshow('houghCircle', frame)
        return 1

    else:
        cv2.imshow('houghCircle', frame)
        return 0


camera = cv2.VideoCapture(0)
camera.set(3,160) 
camera.set(4,120)
while( camera.isOpened() ):
    ret, frame = camera.read()
    
    res = houghCircle(frame)
    
    if cv2.waitKey(1) == ord('q'):
            break
        
cv2.destroyAllWindows()
