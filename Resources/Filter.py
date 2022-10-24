import cv2
import json
import numpy as np
def filter(file,sizein, pnamein, modelin ):
    team = {}
    team['gbrurl']= file
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

    i = 0
    for x in ArrayPostions:
        splitted = x.split(",")
        j = -1
        if len(splitted) > 17:
            size = splitted[13].split("/")
            pname = splitted[7].split("/")

            model = splitted[17].split("/")
            if ((sizein == size[0]) and (pnamein == pname[0]) and (modelin == model[0])):
                j = i
                break;
        i += 1

    if j == -1:
        return None

    points = np.array(INTALLarray[j])
    pts = np.array([points])

    return pts

def filterByName(file, sizein, pnamein, modelin ):
    def filter(fileim,k):
        f = open(fileim, "r", encoding='unicode_escape')  # reads the GBR file from the directory
        alldata = f.read()  # assign to all data variable
        # print(alldata)
        arrayall = alldata.split('*')  # Splits All the Data bt * and stores in an array
        # print(arrayall[-2])
        NewlineArray = []
        NewlineArray = arrayall[-2].split('\n')
        del NewlineArray[0]
        del NewlineArray[0]
        del NewlineArray[0]

        # print(NewlineArray)
        lastItem = ""
        LItem = False
        ArrayPostions = []
        stringmake = ""

        for items in NewlineArray:
            if items.startswith('L'):
                LItem = True
                stringmake = stringmake[1:]
                ArrayPostions.append(stringmake);
                # print(stringmake)
                stringmake = ""
            if LItem:
                stringmake = stringmake + "/" + items

        return (ArrayPostions[k])


    team = {}
    team['gbrurl']= file
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

    i = 0
    for x in ArrayPostions:
        splitted = x.split(",")
        j = -1
        if len(splitted) > 17:
            size = splitted[13].split("/")
            pname = splitted[7].split("/")
            model = splitted[17].split("/")
            if ((sizein == size[0]) and (pnamein == pname[0]) and (modelin == model[0])):
                j = i
                break;
        i += 1

    if j == -1:
        return None

    label = filter(file, j)

    return label