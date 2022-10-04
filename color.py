import cv2
import numpy as np

def bluecolor(frame):

  lower = np.array([])          # 파랑색 범위
  upper = np.array([])
  
  img_mask = cv2.inRange(frame, lower, upper)
  res = cv2.bitwise_and(frame, frame, mask=img_mask)
  
  return res

def greencolor(frame):
      
  lower = np.array([])
  upper = np.array([])
  
  img_mask = cv2.inRange(frame, lower, upper)
  res = cv2.bitwise_and(frame, frame, mask=img_mask)

  return res

def redcolor(frame):
  
  lower = np.array([0, 0, 60])
  upper = np.array([40,40,255])
  
  img_mask = cv2.inRange(frame, lower, upper)  
  res = cv2.bitwise_and(frame, frame, mask=img_mask)

  return res
  
def sectioncolor(frame):
    
  lower = np.array([])
  upper = np.array([])
  
  img_mask = cv2.inRange(frame, lower, upper)
  res = cv2.bitwise_and(frame, frame, mask=img_mask)

  return res

def Numcolor(frame):
    lower = np.array([0,0,0])
    upper = np.array([255,40,40])
    
    img_mask = cv2.inRange(frame, lower, upper)
    res = cv2.bitwise_and(frame,frame,mask=img_mask)
    return res