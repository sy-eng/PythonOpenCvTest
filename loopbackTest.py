import cv2
from myV4L2Lib import *

READ_DEVICE = 0
WRITE_DEVICE_NAME = "/dev/video7"

capture = cv2.VideoCapture(READ_DEVICE)

capture.set(cv2.CAP_PROP_AUTOFOCUS, 0.0)
#print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
writeFile = V4L2Write(WRITE_DEVICE_NAME, int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)), v4l2.V4L2_PIX_FMT_RGB24)

while(True):
	ret, frame = capture.read()
	
	#windowsize = (800, 600)
	#frame = cv2.resize(frame, windowsize)
	grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(grayImage,(7,7), 1.5, 1.5)
	canny = cv2.Canny(blur, 0, 15, 3)
	colorImage = cv2.cvtColor(canny, cv2.COLOR_GRAY2RGB)
	cv2.imshow('frame', colorImage)
	
#	writeData(write_fd, result.data, result.cols * result.rows * 3);
#	writeFile.writeData(colorImage);
#	writeFile.writeData(frame);
	writeFile.writeData(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB));
	
	keyData = cv2.waitKey(1) & 0xff
	if keyData == ord('q'):
		break
	elif keyData == ord('p'):
		focusData = capture.get(cv2.CAP_PROP_FOCUS)
		focusData += 17;
		if focusData > 255:
			focusData = 255
			
		capture.set(cv2.CAP_PROP_FOCUS, focusData)
		print(capture.get(cv2.CAP_PROP_FOCUS))
		
	elif keyData == ord('m'):
		focusData = capture.get(cv2.CAP_PROP_FOCUS)
		focusData -= 17;
		if focusData < 0:
			focusData = 0
			
		capture.set(cv2.CAP_PROP_FOCUS, focusData)
		print(capture.get(cv2.CAP_PROP_FOCUS))
		
	else:
		None
		
writeFile.close()
capture.release()
cv2.destroyAllWindows()

