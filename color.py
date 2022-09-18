# b,g,r hsv 값 테스트 해보면서 맞춰야 함

import cv2
import numpy as np

def bluecolor(frame):
  lower = np.array([110,30,30])         
  upper = np.array([130,255,255])

  mask = cv2.inRange(frame, lower, upper)
    
  res = cv2.bitwise_and(frame, frame, mask)

  return res

def greencolor(frame):
       
  lower = np.array([135,65,65])
  upper = np.array([58,166,85])
  
  mask = cv2.inRange(frame, lower, upper)

    
  res = cv2.bitwise_and(frame, frame, mask)

  return res

def redcolor(frame):

  lower = np.array([160,50,50])
  upper = np.array([180,255,255])
  
  mask = cv2.inRange(frame, lower, upper)

  res = cv2.bitwise_and(frame, frame, mask)

  return res

def section(frame):
    lower = np.array([])
    upper = np.array([])

    mask = cv2.inRange(frame, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask)

    return res
