import cv2
import numpy as np

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('1.jpg')
rows,cols,channel = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
