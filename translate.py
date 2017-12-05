import cv2
import numpy as np

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('1.jpg')
rows,cols,channel = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
