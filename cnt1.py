import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('cnt.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray, 127,255,0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
print contours
cnt = contours[0]
print cnt
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
img2 = cv2.drawContours(img,approx,-1,(0,255,0),3)
cv2.imshow('image',img2)
cv2.waitKey(0)
