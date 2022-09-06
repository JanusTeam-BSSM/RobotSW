import cv2
import numpy as np

def bluecolor(frame):
  while(1):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # BGR을 HSV로 변환해줌

    lower = np.array([110,30,30])          # 파랑색 범위
    upper = np.array([130,255,255])

    mask = cv2.inRange(frame, lower, upper)
    
    res = cv2.bitwise_and(frame, frame, mask)

    return res

def greencolor(frame):
  while(1):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower = np.array([135,65,65])
    upper = np.array([58,166,85])
  
    mask = cv2.inRange(frame, lower, upper)

    
    res = cv2.bitwise_and(frame, frame, mask)

    return res

def redcolor(frame):
  while(1):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # upper boundary RED color range values; Hue (160 - 180)
    lower = np.array([160,50,50])
    upper = np.array([180,255,255])
  
    mask = cv2.inRange(frame, lower, upper)

    
    res = cv2.bitwise_and(frame, frame, mask)

    return res