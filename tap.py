import cv2
import numpy as np

img = cv2.imread('1.jpg');
board = img[1200:1500,100:400]
img[200:500,1100:1400] = board
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img[:,:,2] = 0
cv2.imshow('image',img)
cv2.waitKey(0)
