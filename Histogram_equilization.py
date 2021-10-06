import cv2
import numpy as np
# create VideoCapture object
cap = cv2.VideoCapture('face-demographics-walking.mp4')
cv2.startWindowThread()
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# apply histogram equalization
#print("[INFO] performing histogram equalization...")
    equalized = cv2.equalizeHist(gray)
    res=cv2.cvtColor(equalized,cv2.COLOR_GRAY2BGR)
 
    out.write(frame.astype('uint8'))
    cv2.imshow('frame',frame)
    cv2.imshow('Histogram equilization', res)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
out.write(frame.astype('uint8'))
#cv2.waitKey()
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()


