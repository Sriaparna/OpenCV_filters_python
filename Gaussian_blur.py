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
    # capture each frame of the video
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    kernel = np.ones((5,5), np.uint8)
    # add gaussian blurring to frame
    #frame = cv2.GaussianBlur(frame, (5, 5), 0)
    #another gaussian blur method
    #Gaussian Blur Kernel
    gaussianBlurKernel = np.array(([[1, 2, 1], [2, 4, 2], [1, 2, 1]]), np.float32)/9

    gaussianBlur = cv2.filter2D(src=frame, kernel=gaussianBlurKernel, ddepth=-1)
    out.write(frame.astype('uint8'))
    cv2.imshow("Frame",frame)
    cv2.imshow("GB",gaussianBlur)
    #cv2.waitKey()

    # save video frame
    #out.write(frame)
    # display frame
    #cv2.imshow('Video', frame)
    # press `q` to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#cv2.waitKey()
out.write(frame.astype('uint8'))
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()
