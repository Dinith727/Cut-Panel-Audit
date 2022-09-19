f = open("../GBR/one.GBR", "r", encoding='unicode_escape')  # reads the GBR file from the directory
alldata = f.read()  # assign to all data variable
# print(alldata)
arrayall = alldata.split('*')  # Splits the All Data bt * and stores in a array
# print(arrayall[-2])
NewlineArray = []
NewlineArray = arrayall[-2].split('\n')
del NewlineArray[0]
del NewlineArray[0]
del NewlineArray[0]

print(NewlineArray)
lastItem = ""
LItem =False
ArrayPostions=[]
stringmake=""
for items in NewlineArray:
    # print("Item")

    if items.startswith('L'):
        LItem = True

        stringmake =stringmake[1:]
        ArrayPostions.append(stringmake);
        print(stringmake)
        stringmake=""
        # print(items)

    if LItem:
        #print("Started L Detecetd")
        stringmake=stringmake+"/"+items


print(ArrayPostions)