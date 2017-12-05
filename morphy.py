import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('n3.jpg')

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT, kernel)

plt.subplot(421),plt.imshow(erosion),plt.title('eroded')
plt.xticks([]),plt.yticks([])
plt.subplot(422),plt.imshow(dilation),plt.title('dilated')
plt.xticks([]),plt.yticks([])
plt.subplot(423),plt.imshow(opening),plt.title('opening')
plt.xticks([]),plt.yticks([])
plt.subplot(424),plt.imshow(closing),plt.title('closing')
plt.xticks([]),plt.yticks([])
plt.subplot(425),plt.imshow(gradient),plt.title('gradient')
plt.xticks([]),plt.yticks([])
plt.subplot(426),plt.imshow(tophat),plt.title('tophat')
plt.xticks([]),plt.yticks([])
plt.subplot(427),plt.imshow(blackhat),plt.title('blackhat')
plt.xticks([]),plt.yticks([])
plt.show()
