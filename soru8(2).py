import cv2
import numpy as np

image = cv2.imread("red.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)
ret, thresh = cv2.threshold(blur, 200, 255,
                           cv2.THRESH_BINARY_INV)



contours, hierarchies = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


blank = np.zeros(thresh.shape[:2],
                 dtype='uint8')
 
cv2.drawContours(blank, contours, -1,
                (255, 0, 0), 1)
 


for i in contours:
	M = cv2.moments(i)
	if M['m00'] != 0:
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
	print(f"x: {cx} y: {cy}")

