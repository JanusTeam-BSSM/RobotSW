import cv2
import numpy as np

def bluecolor(frame):
  while(1):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # BGR을 HSV로 변환해줌

    lower_blue = np.array([100,100,120])          # 파랑색 범위
    upper_blue = np.array([150,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    return res

def greencolor(frame):
  while(1):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_green = np.array([50, 150, 50])        # 초록색 범위
    upper_green = np.array([80, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)    # 흰색 영역에 초록색 마스크를 씌워줌.

    return res

def redcolor(frame):
  while(1):
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150, 50, 50])        # 빨강색 범위
    upper_red = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res2 = cv2.bitwise_and(frame, frame, mask=mask)    # 흰색 영역에 빨강색 마스크를 씌워줌.

    return res

