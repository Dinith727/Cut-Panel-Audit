
import cv2
from StackImage import stackImages

# declaring the paths
path1 = '../Cut Panels/blue.png'
path2 = '../Cut Panels/2.4.png'

# reading the images
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# copying the images to draw contours
imgContour1 = img1.copy()
imgContour2 = img2.copy()

# adding a blur
imgBlur1 = cv2.GaussianBlur(img1, (3, 3), 1)
imgBlur2 = cv2.GaussianBlur(img2, (3, 3), 1)

# converting to gray
imgGray1 = cv2.cvtColor(imgBlur1, cv2.COLOR_BGR2GRAY)
imgGray2 = cv2.cvtColor(imgBlur2, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(imgGray1, 100, 225, cv2.THRESH_BINARY_INV)
ret, thresh2 = cv2.threshold(imgGray2, 100, 225, cv2.THRESH_BINARY_INV)

# canny edge detection
imgCanny1 = cv2.Canny(thresh1, 50, 50)
imgCanny2 = cv2.Canny(thresh2, 50, 50)

# finding contours
contours1, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt1 = contours1[0]
contours2, hierarchy = cv2.findContours(imgCanny2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt2 = contours2[0]

# calculating area
area1 = cv2.contourArea(cnt1)
area2 = cv2.contourArea(cnt2)

# calculating perimeter
peri1 = cv2.arcLength(cnt1, True)
peri2 = cv2.arcLength(cnt2, True)

# printing values
print("Area Of Shape 1 : ", area1)
print("Area Of Shape 2 : ", area2)
print("\n")
print("Perimeter Of Shape 1 : ", peri1)
print("Perimeter Of Shape 2 : ", peri2)
print("\n")

# drawing contours
cv2.drawContours(imgContour1, cnt1, -1, (0, 225, 0), 3)
cv2.drawContours(imgContour2, cnt2, -1, (0, 225, 0), 3)

# declaring an array and calling the stackImage Function in StackImage.py
imgStack = stackImages(0.1, ([img1, imgGray1, imgBlur1, imgCanny1, imgContour1], [img2, imgGray2, imgBlur2, imgCanny2, imgContour2]))

# displaying the stack
cv2.imshow("Stack", imgStack)

# added a wait key
cv2.waitKey(0)