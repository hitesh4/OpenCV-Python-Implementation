import cv2
import numpy as np

img = cv2.imread('traffic.jpg')
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
