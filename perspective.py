import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('per.jpg')
rows,cols,ch = img.shape

ptin = np.float32([[100,100],[400,100],[100,250],[400,250]])
ptout = np.float32([[0,0],[300,0],[0,150],[300,150]])
M = cv2.getPerspectiveTransform(ptin,ptout)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
