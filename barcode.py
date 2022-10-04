import pyzbar.pyzbar as pyzbar  # pip install pyzbar
import numpy as np              # pip install numpy
import cv2                      # pip install opencv-python

# 바코드 탐지하는 엔진 (바코드 및 QR코드 탐지)
def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects

camera = cv2.VideoCapture(0)
camera.set(3,160) 
camera.set(4,120)
while( camera.isOpened() ):
    ret, frame = camera.read()
    frame = cv2.flip(frame,-1)
    decodeObjects = decode(frame)
   
    cv2.waitKey(1)

cv2.destroyAllWindows()
