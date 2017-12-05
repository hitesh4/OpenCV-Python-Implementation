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
			hull = cv2.convexHull(cnt,returnPoints = False)
			defects = cv2.convexityDefects(c,hull)
			for i in xrange(defects.shape[0]):
				s,e,f,d = defects[i,0]
		cv2.imshow('frame',im)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()	



