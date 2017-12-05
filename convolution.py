import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('31.jpg')

kernal = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img,-1,kernal)

plt.subplot(121), plt.imshow(img),plt.title('original')
plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(dst),plt.title('Averaged')
plt.xticks([]),plt.yticks([])
plt.show()
