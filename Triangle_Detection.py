import cv2
import numpy as np

    
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
            return 1

        else : 
            return 0    
