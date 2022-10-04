import cv2
import numpy as np
from bacord import * 

def Num(frame):   
    
    ret, img_th = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY_INV)
    contours, hierachy= cv2.findContours(img_th.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        
    
    rects = [cv2.boundingRect(each) for each in contours]
        #print(rects)
    tmp = [w*h for (x,y,w,h) in rects]
    tmp.sort()
    print(tmp)
    rects = [(x,y,w,h) for (x,y,w,h) in rects if ((w*h>100)and(w*h<800))]
    print(rects)
    for rect in rects:
    # Draw the rectangles
        x0 = rect[0]
        y0 = rect[1]
        x = rect[0] + rect[1]
        y = rect[1] + rect[3]
        w = x - x0
        h = y - y0
        cv2.rectangle(img_blur, (x0, y0), 
                  (x, y), (0, 255, 0), 5)
    cv2.imshow('blur',img_blur)
    roi = img_gray[y0:y0+h, x0:x0+w]
    cv2.imshow('crop',roi)
    if r == 0:
        res = decode(roi)
        print(res)
        return res
        r = 1
    cv2.waitKey(1)

camera = cv2.VideoCapture(0)
camera.set(3,160) 
camera.set(4,120)
while( camera.isOpened() ):
    ret, frame = camera.read()
    frame = cv2.flip(frame,-1)
    Num(frame)
   
    cv2.waitKey(1)

cv2.destroyAllWindows()
