import cv2

# declaring the paths
path1 = 'Src/11.jpg'
path2 = 'Src/22.jpg'

# reading the images
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

# copying the images to draw contours
imgContour1 = img1.copy()
imgContour2 = img2.copy()

# converting to gray
imgGray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
imgGray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# adding a blur
imgBlur1 = cv2.GaussianBlur(imgGray1, (7, 7), 1)
imgBlur2 = cv2.GaussianBlur(imgGray2, (7, 7), 1)

# canny edge detection
imgCanny1 = cv2.Canny(imgBlur1, 50, 50)
imgCanny2 = cv2.Canny(imgBlur2, 50, 50)

# finding contours
contours1, hierarchy = cv2.findContours(imgCanny1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt1 = contours1[0]
contours2, hierarchy = cv2.findContours(imgCanny2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt2 = contours2[0]

# calculating area
area1 = cv2.contourArea(cnt1)
area2 = cv2.contourArea(cnt2)

# calculating perimeter
peri1 = cv2.arcLength(cnt1, True)
peri2 = cv2.arcLength(cnt2, True)

# comparing with matchShapes function
matShape = cv2.matchShapes(imgCanny1, imgCanny2, 1, 0.0)
matShape_float = "{:.2f}".format(matShape*100)

# printing values
print("Area Of Shape 1 : ", area1)
print("Area Of Shape 2 : ", area2)
print("\n")
print("Perimeter Of Shape 1 : ", peri1)
print("Perimeter Of Shape 2 : ", peri2)
print("\n")
print("Match Shape Result : ", matShape)
print("Match Shape Result : ", matShape_float, "%")

# cv2.imshow("Image 1", img1)
# cv2.imshow("Image 2", img2)

# drawing contours
cv2.drawContours(imgContour1, cnt1, -1, (255, 0, 0), 3)
cv2.drawContours(imgContour2, cnt2, -1, (255, 0, 0), 3)

# displaying images
cv2.imshow("Image 1", imgContour1)
cv2.imshow("Image 2", imgContour2)

cv2.imshow("Image Canny 1", imgCanny1)
cv2.imshow("Image Canny 2", imgCanny2)

# added a wait key
cv2.waitKey(0)