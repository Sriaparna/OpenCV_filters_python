import cv2
import numpy as np

img = cv2.imread("test_1.png") #read

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert

h, s, v = cv2.split(hsv) # split to h s v

limit = v.max () # get max bright in V

hsv_min = np.array((0, 0, limit), np.uint8) # put min and max

hsv_max = np.array((255, 255, limit), np.uint8)

img = cv2.inRange(hsv, hsv_min, hsv_max) # brightness filter

moments = cv2.moments(img, 1) # get moments

x_moment = moments['m01']

y_moment = moments['m10']

area = moments['m00']

x = int(x_moment / area) # x

y = int(y_moment / area) # y

cv2.putText(img, "center_brightness_surface!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,100,100), 2)

cv2.imshow('frame_out', img)


cv2.waitKey (0)

cv2.destroyAllWindows ()