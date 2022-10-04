import math
import cv2
from color import *

def Circle(frame):
    #img = redcolor(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cont in contours:
        approx = cv2.approxPolyDP(cont, cv2.arcLength(cont, True) * 0.02, True)
        vtc = len(approx)

        if vtc == 3:
            return 0
        elif vtc == 4:
            return 0
        elif vtc == 5:
            return 0
        else:
            area = cv2.contourArea(cont)
            _, radius = cv2.minEnclosingCircle(cont)
            try:
                ratio = radius * radius * math.pi / area
                if int(ratio) == 1:
                    return 1

            except:
                pass
                
    

