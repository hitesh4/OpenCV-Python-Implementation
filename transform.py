import cv2
import numpy as np

img = cv2.imread('1.jpg')

res = cv2.resize(img, None,fx=5,fy=1,interpolation = cv2.INTER_CUBIC)

cv2.imshow('image',res)
cv2.waitKey(0)
