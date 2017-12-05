import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read();
	if ret == True:
		framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		ret1, thresh = cv2.threshold(framegray,127,255,0)
		image,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		framecnt = frame
		im = framecnt
		for c in contours:
			#epsilon = 0.1*cv2.arcLength(c,True)
			#approx = cv2.approxPolyDP(c, epsilon, True)
			#hull = cv2.convexHull(c)
			x,y,w,h = cv2.boundingRect(c)
			framecnt = cv2.rectangle(frame, (x,y),(x+w,y+h), (0,255,0), 3)			
			rect = cv2.minAreaRect(c)
			box = cv2.boxPoints(rect)
			box = np.int0(box)
			im = cv2.drawContours(frame, [box],-1,(0,0,255),2)
			(x,y),radius = cv2.minEnclosingCircle(c)
			center = (int(x),int(y))
			radius = int(radius)
			im = cv2.circle(frame, center, radius, (255,0,0),2)
			print c
			#ellipse = cv2.fitEllipse(c)
			#im = cv2.ellipse(frame, ellipse,(255,68,43),2)
			#framecnt = cv2.drawContours(frame, [hull], -1, (0,255,0), 3)
		cv2.imshow('frame',im)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()	



