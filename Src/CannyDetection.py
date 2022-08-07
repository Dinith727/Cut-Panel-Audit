import cv2
import numpy as np
from StackImage import stackImages


def empty(a):
    pass


path = '../Cut Panels/1.png'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 340)
cv2.createTrackbar("Blur 1", "TrackBars", 0, 10, empty)
cv2.createTrackbar("Blur 2", "TrackBars", 0, 10, empty)
cv2.createTrackbar("Thresh 1", "TrackBars", 0, 10, empty)
cv2.createTrackbar("Thresh 2", "TrackBars", 0, 10, empty)
cv2.createTrackbar("Canny 1", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Canny 2", "TrackBars",225, 255, empty)

while True:
    img = cv2.imread(path)
    imgContour1 = img.copy()

    b1 = cv2.getTrackbarPos("Blur 1", "TrackBars")
    b2 = cv2.getTrackbarPos("Blur 2", "TrackBars")
    t1 = cv2.getTrackbarPos("Thresh 1", "TrackBars")
    t2 = cv2.getTrackbarPos("Thresh 2", "TrackBars")
    c1 = cv2.getTrackbarPos("Canny 1", "TrackBars")
    c2 = cv2.getTrackbarPos("Canny 2", "TrackBars")

    print(b1, b2, t1, t2, c1, c2)

    imgGray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur1 = cv2.GaussianBlur(imgGray1, (b1, b2), 1)
    ret, thresh1 = cv2.threshold(imgGray1, t1, t2, cv2.THRESH_BINARY_INV)
    imgCanny1 = cv2.Canny(thresh1, c1, c2)
    contours1, hierarchy = cv2.findContours(imgCanny1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt1 = contours1[0]
    cv2.drawContours(imgContour1, cnt1, -1, (255, 0, 0), 3)

    imgStack = stackImages(0.15, ([img, imgGray1, thresh1, imgCanny1, imgContour1]))
    cv2.imshow("Stacked Images", imgStack)

    cv2.waitKey(1)