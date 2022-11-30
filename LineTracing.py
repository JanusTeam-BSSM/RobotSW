import cv2
import numpy as np
import RPi.GPIO as GPIO
from pylibdmtx.pylibdmtx import decode
from color import *
from motor import *


def detection_Rect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cont in contours:
        approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
        vtc = len(approx)

        if vtc == 4:
            return 1
        else:
            return 0

def Tracing(frame):
    frame = frame[60:120, 0:160]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = redcolor(frame)  
    cv2.imshow('test',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    ret,thresh1 = cv2.threshold(blur, 10,255,cv2.THRESH_BINARY)
    cv2.imshow('t',thresh1)

    mask = cv2.erode(thresh1, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cv2.imshow('mask',mask)
    
    contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)
            
    if len(contours) > 0:
        print(1)
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        
        if cx >= 95 and cx <= 125:              
            print("Turn Left!")
            motor_left(40)
        elif cx >= 39 and cx <= 65:
            print("Turn Right")
            motor_right(40)
        else:
           print("go")
           motor_go(40)

def LineTracing(Appdata):
    camera = cv2.VideoCapture(0)
    camera.set(3,160) 
    camera.set(4,120)
    while( camera.isOpened() ):
        ret, frame = camera.read()
        frame = cv2.flip(frame,-1)
        cv2.imshow('frame',frame)
        
        if(detection_Rect(frame)):
            res = decode(frame)
            print(1)
            if res is not None:
                if res == Appdata:
                    print("end")
                    motor_stop()
                                    
        else:
            Tracing(frame)
            

                
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()
        
if __name__ == '__main__':
    LineTracing(Appdata=?)