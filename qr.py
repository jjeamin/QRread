import cv2
from pyzbar import pyzbar

cam = cv2.VideoCapture(-1)

while(True):
	ret, frame = cam.read()
	barcodes = pyzbar.decode(frame)
	
	for barcode in barcodes:
		(x,y,w,h) = barcode.rect
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
		
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		text = "["+barcodeType+"]( value = " + barcodeData + ")"
		cv2.putText(frame,text,(x+w/2,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)

		print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

	cv2.imshow('image',frame)
	
	k = cv2.waitKey(10) & 0xFF
	if k == 27:
		break

cam.release()
cv2.destroyAllWindows()
