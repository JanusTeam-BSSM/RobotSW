import cv2
import numpy as np
import pytesseract 

camera = cv2.VideoCapture(0)
camera.set(3,160) 
camera.set(4,120)

res = 0
while( camera.isOpened() ):
    ret, frame = camera.read()
    frame = cv2.flip(frame,-1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    img_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    img_blur_thresh = cv2.adaptiveThreshold( img_blurred,
                                             maxValue=255.0,
                                             adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             thresholdType=cv2.THRESH_BINARY,
                                             blockSize=19,
                                             C=9
                                           )
    text = pytesseract.image_to_string(img_blur_thresh, lang="kor", config="--psm 6 oem 0")
    try:
        if int(text) in [1,2,3,4,5,6,7,8,9]:
           print(text)
    except:
        pass
    cv2.imshow('blur',img_blur_thresh)
    cv2.waitKey(1)
cv2.destroyAllWindows()
 