import cv2
import numpy as np

img = cv2.imread('1.jpg')
print img.shape
cv2.namedWindow('Hist', cv2.WINDOW_NORMAL)
hist = cv2.calcHist([img], [0], None, [256], [0,255])

print hist.shape
print '---'
print hist
print enumerate(hist)
blank= np.zeros((256,256))
for x,y in enumerate(hist):
	print x,y
	cv2.line(blank,(x,0),(x,y),(255,255,255))

cv2.imshow('Hist',blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
