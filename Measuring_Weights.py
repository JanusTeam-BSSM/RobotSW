import cv2
import numpy as np
from time import time,sleep
from color import *
from Triangle_Detection import *
from motor import *

def main():
    camera = cv2.VideoCapture(0)
    camera.set(3,160) 
    camera.set(4,120)

    res = 0
    tim = 0
    begin = 0
    end = 0
    time_table = []
    i = 0;
    while( camera.isOpened() ):
        ret, frame = camera.read()
        frame = cv2.flip(frame,-1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = Triangle_Detection(frame)
        print(res)
        if res is None:
            motor_go(40)
            continue
        if res > 0:
            img = redcolor(frame)
            if (img[50,50] != [0,0,0]).any():
                end = time()
                time_table.append(end-begin)
                sleep(1)
                motor_stop()
                
        else:
            frame = redcolor(frame)
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
                if tim == 0: 
                    begin = time()
                    tim = 1
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

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    GPIO.cleanup()
