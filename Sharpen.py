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
    kernel = np.ones((5,5), np.uint8)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(frame, -1, sharpen_kernel)
    out.write(frame.astype('uint8'))
    cv2.imshow('frame',frame)
    cv2.imshow('sharpen', sharpen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
out.write(frame.astype('uint8'))
#cv2.waitKey()
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()
