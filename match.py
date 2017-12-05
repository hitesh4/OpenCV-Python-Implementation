import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

img1 = cv2.imread('a.jpg')
imgray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('b.jpg')
imgray2 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(imgray1, 127,255,0)
ret2,thresh2 = cv2.threshold(imgray2, 127,255,0)

_,contours, hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]

_,contours, hierarchy = cv2.findContours(thresh,2,1)
cnt2 = contours[0]

img2 = cv2.drawContours(img2,[cnt2],0,(0,255,0),3)
cv2.imshow('image',img2)
cv2.waitKey(0)
ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
print ret
