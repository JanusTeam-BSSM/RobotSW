import cv2
import numpy as np
import RPi.GPIO as GPIO

from color import *

FL_LED = 26
FR_LED = 16
BL_LED = 20
BR_LED = 21

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24
    
def motor_go(speed):
    GPIO.output(BL_LED, GPIO.LOW)
    GPIO.output(BR_LED, GPIO.LOW)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2,True)#AIN2
    GPIO.output(AIN1,False) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2,True)#BIN2
    GPIO.output(BIN1,False) #BIN1
    GPIO.output(FL_LED, GPIO.HIGH)
    GPIO.output(FR_LED, GPIO.HIGH)
    
    
def motor_right(speed):
    GPIO.output(BL_LED, GPIO.LOW)
    GPIO.output(FL_LED, GPIO.LOW)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2,True)#AIN2
    GPIO.output(AIN1,False) #AIN1
    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2,False)#BIN2
    GPIO.output(BIN1,True) #BIN1
    GPIO.output(BR_LED, GPIO.HIGH)
    GPIO.output(FR_LED, GPIO.HIGH)
    
def motor_left(speed):
    GPIO.output(BR_LED, GPIO.LOW)
    GPIO.output(FR_LED, GPIO.LOW)
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2,False)#AIN2
    GPIO.output(AIN1,True) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2,True)#BIN2
    GPIO.output(BIN1,False) #BIN1
    GPIO.output(BL_LED, GPIO.HIGH)
    GPIO.output(FL_LED, GPIO.HIGH)
        
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(FL_LED,GPIO.OUT)
GPIO.setup(FR_LED,GPIO.OUT)
GPIO.setup(BL_LED,GPIO.OUT)
GPIO.setup(BR_LED,GPIO.OUT)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(PWMA,GPIO.OUT)

GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)

L_Motor= GPIO.PWM(PWMA,100)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,100)
R_Motor.start(0)



def main():
    col = 'b'
    camera = cv2.VideoCapture(0)
    camera.set(3,160) 
    camera.set(4,120)

    while( camera.isOpened() ):
        ret, frame = camera.read()
        frame = cv2.flip(frame,-1)
        cv2.imshow('normal',frame)
        if col == 'b': frame = bluecolor(frame)
        elif col == 'g': frame = greencolor(frame)
        elif col == 'r': frame = redcolor(frame)
        cv2.imshow('color',frame)
        crop_img =frame[60:120, 0:160]
        
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    
        blur = cv2.GaussianBlur(gray,(5,5),0)
        
        ret,thresh1 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV)
        
        mask = cv2.erode(thresh1, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow('mask',mask)
    
        contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)
        
        if len(contours) > 0:
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
        
        if cv2.waitKey(1) == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    GPIO.cleanup()

