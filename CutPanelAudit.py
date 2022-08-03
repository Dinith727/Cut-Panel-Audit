
import cv2
from StackImage import stackImages

# declaring the paths
path1 = 'Src/1.2.jpg'

# reading the images
img1 = cv2.imread(path1)

# copying the images to draw contours
imgContour1 = img1.copy()

# converting to gray
imgGray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)

# adding a blur
imgBlur1 = cv2.GaussianBlur(thresh1, (7, 7), 1)

# canny edge detection
imgCanny1 = cv2.Canny(imgBlur1, 0, 0)

# finding contours
contours1, hierarchy = cv2.findContours(imgCanny1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt1 = contours1[0]

# calculating area
area1 = cv2.contourArea(cnt1)

# calculating perimeter
peri1 = cv2.arcLength(cnt1, True)

# printing values
print("Area Of Shape 1 : ", area1)
print("\n")
print("Perimeter Of Shape 1 : ", peri1)
print("\n")

# drawing contours
cv2.drawContours(imgContour1, cnt1, -1, (255, 0, 0), 3)
# declaring an array and calling the stackImage Function in StackImage.py
imgStack = stackImages(0.2, ([img1, imgGray1, imgBlur1, imgCanny1, imgContour1]))

# displaying the stack
cv2.imshow("Stack", imgStack)

# added a wait key
cv2.waitKey(0)