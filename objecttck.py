import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
	lower_green = np.array([100,50,50])
	upper_green = np.array([130,255,255])

	mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
	mask2 = cv2.inRange(hsv, lower_green, upper_green)
	res1 = cv2.bitwise_or(mask1,mask2)

	res = cv2.bitwise_and(frame,frame, mask = res1)

	cv2.imshow('frame',frame)
	cv2.imshow('mask1',mask1)
	cv2.imshow('mask2',mask2)
	cv2.imshow('res1',res1)
	cv2.imshow('res',res)

	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break

cv2.destroyAllWindows()		
