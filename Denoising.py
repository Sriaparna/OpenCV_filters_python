import cv2
#import numpy as np
# create VideoCapture object
cap = cv2.VideoCapture('face-demographics-walking.mp4')
cv2.startWindowThread()
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))
while(True):
    # capture each frame of the video
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    dst = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 15)
    out.write(frame.astype('uint8'))
    cv2.imshow('result',dst)
    cv2.imshow('frame',frame)
    #cv2.waitKey()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#cv2.waitKey()
out.write(frame.astype('uint8'))
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()
