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
			mask = np.zeros(framegray.shape,np.uint8)
			im = cv2.drawContours(mask, [c],-1,255,-1)
			pixelpoints = np.transpose(np.nonzero(mask))
			print pixelpoints
		cv2.imshow('frame',im)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()	



