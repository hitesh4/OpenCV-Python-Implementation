import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('1.jpg')
rows,cols,ch = img.shape

ptin = np.float32([[50,50],[200,50],[50,200]])
ptout = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(ptin,ptout)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
