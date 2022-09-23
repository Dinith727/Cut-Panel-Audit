import sys
import cv2
import json
import numpy as np
team = {}
team['gbrurl']="../GBR/one.GBR"
with open('parameters.json', 'w') as f:
    json.dump(team, f)

f = open('parameters.json')
openparams = json.load(f)
# print("Parameters from File",openparams['gbrurl'])


f = open(openparams['gbrurl'], "r",encoding='unicode_escape') #reads the GBR file from the directory
alldata = f.read()#assign to all data variable

arrayall = alldata.split('*')#Splits the All Data bt * and stores in a array
# print(arrayall)

linearray=[]
allarray=[]
Nvalue=""
Ndetected=False

#Get Length and Width of Marker=------------------------------------------------
def getGBRdata():
    arrayReturn=[]
    LengthWidth=arrayall[5];
    LandWArray=LengthWidth.split('/')
    print(LandWArray)

    MarkerLength=LandWArray[1]
    MarkerWidth=LandWArray[2]

    MarkerLength = MarkerLength[:-2]
    MarkerLength=MarkerLength[2:]

    arrayReturn.append(round(float(MarkerLength)*25.4,0))

    MarkerWidth=MarkerWidth[:-2]
    MarkerWidth=MarkerWidth[2:]

    arrayReturn.append(round(float(MarkerWidth)*25.4,0))
    return arrayReturn
#Get Length and Width of Marker----------------------------------------------------

for elements in arrayall:

    stripstring = elements.strip(' \n\t')


    if stripstring.startswith('N'):
        # print("Start Drawing Lines:-++++++++++++++++++++++++++++++++++++-")
        # print(elements)
        # print(linearray)
        allarray.append(linearray)
        linearray=[]
        Ndetected=True

    if Ndetected ==True:
        # print("Detected N:--Values")
        # print(stripstring)
        if stripstring.startswith('X'):
            linearray.append(stripstring)#

del allarray[0]
# print(allarray)# Here all arrays contains N1 to Nxxx number of Shapes we can get the N number usig the Array value.
ncounter = 0;
INTALLarray = []
for arrays in allarray:
    # print(arrays)
    ncounter = ncounter + 1
    count = 0
    # print("N number:-:"+str(ncounter))
    INTsubArray = []
    for shapes in arrays:
        # print(shapes)
        count = count + 1
        if count == 1:
            lastwithoutX = shapes.lstrip("X")
            lastcordinat = lastwithoutX.split('Y')
            # print(shapes)
        withoutX = shapes.lstrip("X")
        cordinates = withoutX.split('Y')
        # print(cordinates)
        T4 = [int(x) for x in cordinates]
        #print(T4)
        INTsubArray.append(T4)
    INTALLarray.append(INTsubArray)
img = np.zeros((6000,25000,3), np.uint8)
#print(INTALLarray)

points=np.array(INTALLarray[2])
pts=np.array([points])
cv2.drawContours(img, pts, -1, (0, 225, 0), 10)
half = cv2.resize(img, (0, 0), fx = 0.1, fy = 0.1)

for var in INTALLarray:
    points=np.array(var)
    pts=np.array([points])

    img1 = cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.drawContours(img, pts, -1, (0, 225, 0), 13)
half1 = cv2.resize(img1, (0, 0), fx=0.1, fy=0.1)
cv2.imshow("Stacked Images", half1)

cv2.waitKey(0)
