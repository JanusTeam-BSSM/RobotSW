import cv2
import numpy as np

def Direction_Check(approx):
  # approx의 y 좌표 값의 차를 구함 
  a = approx[0,1]-approx[1,1]
  b = approx[0,1]-approx[2,1]
  c = approx[1,1]-approx[2,1]
  # 차가 가장 작은 것들의 y 좌표를 제외하고 남은 하나를 찾음 
  if a <= b and a <= c: res = 2
  elif b <= a and b <= c: res = 1
  else: res = 0
  # 삼각형의 방향이 어딘지 판별 
  if approx[res,1] < approx[(res+1)%3,1]: res = 1 # 1: front | 2: back
  else: res = 2

  return res 

def Triangle_Detection(frame):
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    _, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) #이진화
    
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 외곽선 검출, EXTERNAL로 바깥 외곽선만 도출
    
    # 외곽선 좌표 받아오기
    for pts in contours:
        if cv2.contourArea(pts) < 400: # contourArea() 면적 반환 / 노이즈 제거, 너무 작으면 무시
            continue
        
        # 근사화 
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
        
        # 근사화 결과 점 갯수
        vtc = len(approx)
        
        if vtc == 3:
          Direction_Check(approx)
          return res

        else : 
            return 0    
             
img = cv2.imread('./img.png')
Triangle_Detection(img)
