#Install opencv

import cv2
d = cv2.QRCodeDetector()
a,b,c = d.detectAndDecode(cv2.imread("quote.jpg"))
print(a)#prints the string stored in the qr code.
