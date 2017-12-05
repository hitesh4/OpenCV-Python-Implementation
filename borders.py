import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('s.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize =5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(221), plt.imshow(img,'gray'),plt.title('original')
plt.xticks([]),plt.yticks([])
plt.subplot(222), plt.imshow(laplacian,'gray'),plt.title('laplacian')
plt.xticks([]),plt.yticks([])
plt.subplot(223), plt.imshow(sobelx,'gray'),plt.title('sobelx')
plt.xticks([]),plt.yticks([])
plt.subplot(224), plt.imshow(sobely,'gray'),plt.title('sobely')
plt.xticks([]),plt.yticks([])

plt.show()
