import numpy as np
import cv2

cap = cv2.VideoCapture('test.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
	ret, frame = cap.read();
	if ret == True:
		frame = cv2.flip(frame,1)
		out.write(frame)
		cv2.imshow('frame',frame)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()		
