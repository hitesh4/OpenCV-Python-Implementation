import cv2
import numpy as np

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img = cv2.imread('r.jpg')
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height, length,_ = img.shape
bottom_left = (0, height)                                      # (1)
bottom_right = (length, height)
print height
top_left = (int(length / 2)-50,int(height/1.5))
top_right = (int(length / 2)+50,int(height/1.5))
region = [np.array([bottom_left,top_left,top_right,bottom_right])]  # (2)

mask = np.zeros_like(grayscale_img)                            # (1)
keep_region_color = 255
cv2.fillPoly(mask, region, keep_region_color)                  # (2)
region_selected_image = cv2.bitwise_and(grayscale_img, mask)

kernel_size = 3
blurred =  cv2.GaussianBlur(region_selected_image, (kernel_size, kernel_size), 0)

low_threshold = 150
high_threshold = 300
canny_transformed = cv2.Canny(blurred, low_threshold, high_threshold)

lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=10,
    maxLineGap=100)

Line = namedtuple("Line", "x1 y1 x2 y2")
lines = [Line(*line[0]) for line in lines]

cv2.imshow('image',canny_transformed)
cv2.waitKey(0)