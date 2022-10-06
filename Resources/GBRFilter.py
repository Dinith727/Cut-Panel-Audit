import cv2
import json
import numpy as np
team = {}
team['gbrurl']="../GBR/CZ9857-BULK-A-42-V2.GBR"
with open('parameters.json', 'w') as f:
    json.dump(team, f)

f = open('parameters.json')
openparams = json.load(f)

# Reading the GBR file from the directory
f = open(openparams['gbrurl'], "r", encoding='unicode_escape')

# assigning data to a variable
alldata = f.read()

# Splits All the Data bt * and stores in an array
arrayall = alldata.split('*')

NewlineArray = []
NewlineArray = arrayall[-2].split('\n')
del NewlineArray[0]
del NewlineArray[0]
del NewlineArray[0]

linearray=[]
allarray=[]
Nvalue=""
Ndetected=False

lastItem = ""
LItem =False
ArrayPostions=[]
stringmake=""


# Get the Length and the Width of the Marker
def getGBRdata():
    arrayReturn = []
    LengthWidth=arrayall[5]
    LandWArray=LengthWidth.split('/')

    MarkerLength=LandWArray[1]
    MarkerWidth=LandWArray[2]

    MarkerLength = MarkerLength[:-2]
    MarkerLength= MarkerLength[2:]

    arrayReturn.append(round(float(MarkerLength)*25.4, 0))

    MarkerWidth=MarkerWidth[:-2]
    MarkerWidth=MarkerWidth[2:]

    arrayReturn.append(round(float(MarkerWidth)*25.4, 0))
    return arrayReturn

for items in NewlineArray:
    if items.startswith('L'):
        LItem = True
        stringmake = stringmake[1:]
        ArrayPostions.append(stringmake)
        # print(stringmake)
        stringmake = ""
    if LItem:
        stringmake=stringmake+"/"+items

for elements in arrayall:
    stripstring = elements.strip(' \n\t')

    if stripstring.startswith('N'):
        allarray.append(linearray)
        linearray=[]
        Ndetected=True

    if Ndetected == True and stripstring.startswith('X'):
        linearray.append(stripstring)

# Here all arrays contains N1 to Nxxx number of Shapes we can get the N number using the Array value.
del allarray[0]
ncounter = 0
INTALLarray = []
for arrays in allarray:
    ncounter = ncounter + 1
    count = 0
    INTsubArray = []
    for shapes in arrays:
        count = count + 1
        if count == 1:
            lastwithoutX = shapes.lstrip("X")
            lastcordinat = lastwithoutX.split('Y')
        withoutX = shapes.lstrip("X")
        cordinates = withoutX.split('Y')
        T4 = [int(x) for x in cordinates]
        INTsubArray.append(T4)
    INTALLarray.append(INTsubArray)


img = np.zeros((6000,25000,3), np.uint8)
imgc = np.zeros((6000,25000,3), np.uint8)

count = 0

for var in INTALLarray:
    points=np.array(var)
    pts=np.array([points])
    point = ArrayPostions[count+14]
    splitted = point.split(",")

    size = splitted[13].split("/")
    pname = splitted[7].split("/")
    style = splitted[11].split("/")
    model = splitted[17].split("/")

    #print(count, "  -  ", pname[0],style[0],size[0],model[0])
    print("No : ",count,", piece Name : ", pname[0],", style : ", style[0],", size : ", size[0],", model : ", model[0])
    #print(count, "  -  ", splitted)
    pointC = str(count)
    img1 = cv2.line(img,(0,0),(511,511),(255,0,0),5)
    M = cv2.moments(pts)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.drawContours(img, pts, -1, (0, 225, 0), 13)
    cv2.putText(img, pointC, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 6, (0, 0, 255), 9)
    count += 1

half1 = cv2.resize(img1, (0, 0), fx=0.1, fy=0.1)
cv2.imshow("Stacked Images", half1)

cv2.waitKey(0)

sizein = input("Please enter the size:\n")
pnamein = input("Please enter the piece name :\n")
stylein = input("Please enter the style:\n")
modelin = input("Please enter the model:\n")

i = 0
j = 0
for x in ArrayPostions:
    splitted = x.split(",")

    if i > 14:

        size = splitted[13].split("/")
        pname = splitted[7].split("/")
        style = splitted[11].split("/")
        model = splitted[17].split("/")
        print(size[0])
        if (sizein in size[0] and pnamein in pname[0] and stylein in style[0] and modelin in model[0]):
            j = i - 14
            break;
    i += 1

points = np.array(INTALLarray[j])
pts = np.array([points])
cv2.drawContours(imgc, pts, -1, (0, 225, 0), 10)
halfc = cv2.resize(imgc, (0, 0), fx = 0.1, fy = 0.1)

cv2.imshow("Stacked Images", halfc)

cv2.waitKey(0)