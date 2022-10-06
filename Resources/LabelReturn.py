def getLable(filepath):
    f = open(filepath, "r", encoding='unicode_escape')  # reads the GBR file from the directory
    alldata = f.read()  # assign to all data variable
    arrayall = alldata.split('*')  # Splits All the Data bt * and stores in an array
    NewlineArray = arrayall[-2].split('\n')
    del NewlineArray[0]
    del NewlineArray[0]
    del NewlineArray[0]

    # print(NewlineArray)
    lastItem = ""
    LItem =False
    ArrayPostions=[]
    stringmake=""

    SizeArray = []
    PnameArray = []
    StyleArray = []
    ModelArray = []

    for items in NewlineArray:
        if items.startswith('L'):
            LItem = True
            stringmake =stringmake[1:]
            ArrayPostions.append(stringmake);
            stringmake=""
        if LItem:
            stringmake=stringmake+"/"+items

    i = 0
    for x in ArrayPostions:
        splitted = x.split(",")

        if i > 14:

            size = splitted[13].split("/")
            pname = splitted[7].split("/")
            style = splitted[11].split("/")
            model = splitted[17].split("/")

            SizeArray.append(size[0]);
            PnameArray.append(pname[0]);
            StyleArray.append(style[0]);
            ModelArray.append(model[0]);
        i += 1

    return SizeArray, PnameArray, StyleArray, ModelArray
