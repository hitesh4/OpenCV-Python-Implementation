
#histogram in video not working

import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read();
	if ret == True:
		framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		hist = cv2.calcHist([framegray],[0],None,[256],[0,256])
		hist = hist.ravel()
		print hist.shape
		h1 = framegray.shape[0]
		w1 = framegray.shape[1]
		h2 = hist.shape[0]
		w2 = hist.shape[1]
		vst = np.zeros((h1+h2,(max(w1,w2))),np.uint8)

		vst[:h1,:w1] = framegray
		vst[h1:h1+h2,:w2] = hist

		cv2.imshow('f',vst)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()	

