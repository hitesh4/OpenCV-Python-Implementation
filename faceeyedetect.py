import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture("D:/test/The Newsroom Season 1 to 3 Mp4 720p/Season 1/The Newsroom S01E01.mp4")
i = 0
while(cap.isOpened()):
	i=i+1;
	ret, frame = cap.read();
	if ret == True:
		framegray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(framegray, 1.3, 5)
		j =0
		for (x,y,w,h) in faces:
			j=j+1;
			frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
			roi_color = frame[y:y+h, x:x+w]
			cv2.imwrite("Data/face"+str(i)+str(j)+".jpg",roi_color);
		cv2.imshow('f',frame)
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break
	else:
		break	
		
cap.release()
cv2.destroyAllWindows()				

