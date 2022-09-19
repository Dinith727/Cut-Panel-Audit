f = open("../GBR/one.GBR", "r", encoding='unicode_escape')  # reads the GBR file from the directory
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
LItem =False
ArrayPostions=[]
stringmake=""

for items in NewlineArray:
    if items.startswith('L'):
        LItem = True
        stringmake =stringmake[1:]
        ArrayPostions.append(stringmake);
        # print(stringmake)
        stringmake=""
    if LItem:
        stringmake=stringmake+"/"+items


word = '171/A,0,0,1,1/P,0,1,0,0'
i = 0
for x in ArrayPostions:
    if (word in x):
        # print(x)
        print(i)
    i += 1


