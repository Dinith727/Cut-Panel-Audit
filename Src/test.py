import cv2
from StackImage import stackImages
image = cv2.imread('../Cut Panels/blue.png')
imgContour = image.copy()
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, im = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy  = cv2.findContours(im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
cv2.drawContours(imgContour, cnt1, -1, (0,255,75), 2)
imgStack = stackImages(0.1([imgContour]))
# displaying the stack
cv2.imshow("Stack", imgStack)

# added a wait key
cv2.waitKey(0)