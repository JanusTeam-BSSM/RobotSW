# BGR -> HSV 코드  
import cv2
import numpy as np

color = []  # BGR 값 
pixel = np.uint8([[color]]) # 한 픽셀로 구성된 이미지로 변환

hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
print(hsv, 'shape:', hsv.shape )

# 픽셀값만 가져오기 
hsv = hsv[0][0]

print("bgr: ", color)
print("hsv: ", hsv) # lower, upper +- 10