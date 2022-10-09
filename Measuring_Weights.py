import cv2
import numpy as np
import RPi.GPIO as GPIO
from time import time,sleep
from color import *
from circle import *
from motor import *
from barcode import *
from Img_filter import *

def Measuring():
    camera = cv2.VideoCapture(0)
    camera.set(3,160) 
    camera.set(4,120)

    res = 0
    first = 0
    second = 0
    i = 0
    r = 0
    s = 0
    end = 0
    begin = 0
    r_table = {
        1:{},
        2:{},
        3:{},
        4:{},
        5:{},
        6:{}
    }
    g_table = {
        1:{},
        2:{},
        3:{},
        4:{},
        5:{},
        6:{}
    }
    col = 'r' 
    while( camera.isOpened() ):
        ret, frame = camera.read()
        frame = cv2.flip(frame,-1)
        cv2.imshow('frame',frame)
        res = Circle(frame)
        print(res)
        if res is None:
            motor_go(40)
            continue
        if res == 1:
            motor_stop()
            if s==0:
                first = Num(frame)
                print(first)
                s=1
            else:
                end = time()
                r = 0
                if i == 0:
                    second = Num(frame)
                    if col == 'r':
                        r_table[first] = {second:end-begin}
                    else:
                        g_table[first] = {second:end-begin}
                first = second
        else:                
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if col == 'r':
                frame = redcolor(frame)
            else:
                frame = greencolor(frame)
            frame = frame[72:120, 0:160]    
            cv2.imshow('test',frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('gray',gray)
            blur = cv2.GaussianBlur(gray,(5,5),0)

            ret,thresh1 = cv2.threshold(blur, 10,255,cv2.THRESH_BINARY_INV)
            cv2.imshow('t',thresh1)

            contours,hierarchy = cv2.findContours(thresh1.copy(), 1, cv2.CHAIN_APPROX_NONE)

            if len(contours) > 0:
                c = max(contours, key=cv2.contourArea)
                M = cv2.moments(c)

                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
            if r == 0:
                begin = time()
                r = 1
                if cx >= 95 and cx <= 125:              
                    print("Turn Left!")
                    motor_left(40)
                elif cx >= 39 and cx <= 65:
                    print("Turn Right")
                    motor_right(40)
                else:
                    print("go")
                    motor_go(40)


            if cv2.waitKey(1) == ord('q'):
                break
    #return table
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Measuring()
    GPIO.cleanup()
