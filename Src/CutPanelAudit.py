import numpy as np
import cv2
from StackImage import stackImages
from ShapeComparison import comparison
from SQL import record_data

# declaring the paths
path1 = '../Cut Panels/1.png'
path2 = '../Cut Panels/2.png'

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

# dilating the edges
kernel = np.ones((5, 5), np.uint8)
dilation1 = cv2.dilate(imgCanny1, kernel, iterations=3)
dilation2 = cv2.dilate(imgCanny2, kernel, iterations=3)

# finding contours
contours1, hierarchy = cv2.findContours(dilation1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt1 = contours1[0]
contours2, hierarchy = cv2.findContours(dilation2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt2 = contours2[0]

# calculating area
area1 = cv2.contourArea(cnt1)
area2 = cv2.contourArea(cnt2)

# rounding area values to 2 decimal points
area1_float = "{:.2f}".format(area1)
area2_float = "{:.2f}".format(area2)

# calculating perimeter
peri1 = cv2.arcLength(cnt1, True)
peri2 = cv2.arcLength(cnt2, True)

# rounding perimeter values to 2 decimal points
peri1_float = "{:.2f}".format(peri1)
peri2_float = "{:.2f}".format(peri2)

# calculating the absolute value of the area difference
areaDiff = area1 - area2
areaDiff_float = "{:.2f}".format(areaDiff)

# calculating the absolute value of the perimeter difference
periDiff = peri1 - peri2
periDiff_float = "{:.2f}".format(periDiff)

# calculating the deviation ratio of area
adevratio = abs(areaDiff/area1)*100
adevratio_float = "{:.2f}".format(adevratio)

# calculating the deviation ratio of perimeter
pdevratio = abs(periDiff/peri1)*100
pdevratio_float = "{:.2f}".format(pdevratio)

# drawing contours
cv2.drawContours(imgContour1, cnt1, -1, (0, 225, 0), 30)
cv2.drawContours(imgContour2, cnt2, -1, (0, 225, 0), 30)

# calling the shapeMatch function
shaperesult = (1-(cv2.matchShapes(cnt1, cnt2, 1, 0.0)))*100
shaperesult_float = "{:.2f}".format(shaperesult)

# calling the comparison function from ShapeComparison.py
shrinkage, result, shape = comparison(areaDiff, periDiff, shaperesult)

# printing values
print("Area Of The Original Panel : ", area1_float)
print("Area Of Tested Panel : ", area2_float)
print("Difference Of Area : ", areaDiff_float)
print("Deviation Ratio Of Area : ", adevratio_float, "%")
print("\n")
print("Perimeter Of The Original Panel : ", peri1_float)
print("Perimeter Of Tested Panel : ", peri2_float)
print("Difference Of Perimeter : ", periDiff_float)
print("Deviation Ratio Of Perimeter : ", pdevratio_float, "%")
print("\n")
print("Panel is ", shaperesult_float, "% matching with the original panel")
print("Shape : ", shape)
print("Shrinkage : ", shrinkage)
print("Result : ", result)
record_data(adevratio_float, pdevratio_float)

# declaring an array and calling the stackImage Function in StackImage.py
imgStack = stackImages(0.1, ([img1, dilation1, imgContour1], [img2, dilation2, imgContour2]))

# displaying the stack
cv2.imshow("Stack", imgStack)

# added a wait key
cv2.waitKey(0)