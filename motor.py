import RPi.GPIO as GPIO

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

def motor_stop():
  GPIO.output(BR_LED, GPIO.LOW)
  GPIO.output(FR_LED, GPIO.LOW)
  GPIO.output(FL_LED, GPIO.LOW)
  GPIO.output(BL_LED, GPIO.LOW)
  L_Motor.ChangeDutyCycle(0)
  R_Motor.ChangeDutyCycle(0)
        
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