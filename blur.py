import cv2
import numpy as np
from matplotlib import pyplot as plt

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('n2.jpg')

blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
mblur = cv2.medianBlur(img,5)
bilateral = cv2.bilateralFilter(img,9,75,75)

plt.subplot(321), plt.imshow(img),plt.title('original')
plt.xticks([]),plt.yticks([])
plt.subplot(322), plt.imshow(blur),plt.title('BLur')
plt.xticks([]),plt.yticks([])
plt.subplot(323), plt.imshow(gblur),plt.title('Gblur')
plt.xticks([]),plt.yticks([])
plt.subplot(324), plt.imshow(mblur),plt.title('Mblur')
plt.xticks([]),plt.yticks([])
plt.subplot(325), plt.imshow(bilateral),plt.title('bilateral')
plt.xticks([]),plt.yticks([])
plt.show()
