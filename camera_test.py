import cv2

camera = cv2.VideoCapture(0)
camera.set(3,160) 
camera.set(4,120)
print(1)
while( camera.isOpened() ):
    ret, frame = camera.read()
    print(2)
    frame = cv2.flip(frame,-1)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()
