import cv2
from pyzbar import pyzbar

cam = cv2.VideoCapture(-1)

while(True):
	ret, frame = cam.read()
	barcodes = pyzbar.decode(frame)
	
	for barcode in barcodes:
		(x,y,w,h) = barcode.rect
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

	cv2.imshow('image',frame)
	
	k = cv2.waitKey(10) & 0xFF
	if k == 27:
		break

cam.release()
cv2.destroyAllWindows()
