import os
import tkinter as tk

import cv2
import numpy as np
from PIL import ImageTk, Image
from tkinter import filedialog
from LabelReturn import getLable
from Filter import filter, filterByName

SizeArray = []

# defining colours
mainbgcol = '#D5D6EA'
buttonbgcol = "#D2042D"
textcol = "white"

# configuring the window
master = tk.Tk()
master.title("Cut Panel Audit")
master.configure(bg=mainbgcol)
width = master.winfo_screenwidth()
height = master.winfo_screenheight()
master.geometry("%dx%d" % (width, height))

# main title
tk.Label(master, text="Cut Panel Audit", font='Helvetica 28 bold', bg=mainbgcol, fg=buttonbgcol).place(x=550, y=50)

# labels of input fields
tk.Label(master, text="-------- Panel Details --------", bg=mainbgcol, font='Helvetica 12 bold').place(x=200, y=110)
tk.Label(master, text="Piece Name : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=185, y=165)
tk.Label(master, text="Piece Size : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=196, y=205)
tk.Label(master, text="Piece Description : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=140, y=245)
tk.Label(master, text="Piece Category : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=157, y=285)
tk.Label(master, text="Bundle ID : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=197, y=325)
tk.Label(master, text="Model Name : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=177, y=365)
tk.Label(master, text="Left/Right : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=197, y=405)
tk.Label(master, text="Shape Similarity : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=101, y=455)
tk.Label(master, text="Shrinkage Status : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=93, y=475)
tk.Label(master, text="Shape Status : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=122, y=495)
tk.Label(master, text="Shape Pass Limit : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=322, y=455)
tk.Label(master, text="Result : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=405, y=475)
tk.Label(master, text="Original Panel", bg=mainbgcol, font='Helvetica 12 bold').place(x=670, y=170)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 12 bold').place(x=1070, y=170)

tk.Label(master, text="---- Perimeter Status ----", bg=mainbgcol, font='Helvetica 10 bold').place(x=120, y=540)
tk.Label(master, text="Original Panel :", bg=mainbgcol, font='Helvetica 10 ').place(x=100, y=560)
tk.Label(master, text="Testing Panel :", bg=mainbgcol, font='Helvetica 10').place(x=102, y=580)
tk.Label(master, text="Difference :", bg=mainbgcol, font='Helvetica 10').place(x=124, y=600)
tk.Label(master, text="Deviation Ratio :", bg=mainbgcol, font='Helvetica 10').place(x=95, y=620)


tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=200, y=560)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=200, y=580)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=200, y=600)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=200, y=620)

tk.Label(master, text="---- Area Status ----", bg=mainbgcol, font='Helvetica 10 bold').place(x=430, y=540)
tk.Label(master, text="Original Panel :", bg=mainbgcol, font='Helvetica 10').place(x=400, y=560)
tk.Label(master, text="Testing Panel :", bg=mainbgcol, font='Helvetica 10').place(x=402, y=580)
tk.Label(master, text="Difference :", bg=mainbgcol, font='Helvetica 10').place(x=424, y=600)
tk.Label(master, text="Deviation Ratio :", bg=mainbgcol, font='Helvetica 10').place(x=395, y=620)

tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=500, y=560)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=500, y=580)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=500, y=600)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 10').place(x=500, y=620)



# defining open image function for the original panel
def openOriginalImage():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfile(parent=master, initialdir='../GBR', title='Please select a directory')
    filepath = os.path.abspath(tempdir.name)
    global hy
    hy = str(filepath.replace("\\", '/' ))
    SizeArray, PnameArray, StyleArray, ModelArray = getLable(hy);

    pnameDuplicateRemoved = []
    sizeDuplicateRemoved = []
    styleDuplicateRemoved = []

    global modelDuplicateRemoved
    modelDuplicateRemoved = []

    [pnameDuplicateRemoved.append(x) for x in PnameArray if x not in pnameDuplicateRemoved]
    [sizeDuplicateRemoved.append(x) for x in SizeArray if x not in sizeDuplicateRemoved]
    [styleDuplicateRemoved.append(x) for x in StyleArray if x not in styleDuplicateRemoved]
    [modelDuplicateRemoved.append(x) for x in ModelArray if x not in modelDuplicateRemoved]


    def callbacklocation(selection):
        global locationval
        locationval = selection

    def callbacksize(selection):
        global sizeval
        sizeval = selection



    def callbackpname(selection):
        global pnameval
        pnameval = selection

    def callbackstyle(selection):
        global styleval
        styleval = selection

    # def callbackmodel(selection):
    #     global modelval
    #     modelval = selection

    variablepname = tk.StringVar(master)
    pname = tk.OptionMenu(master, variablepname, *pnameDuplicateRemoved, command=callbackpname)
    pname.place(x=300, y=164)
    pname.config(width=20)

    variablesize = tk.StringVar(master)
    size = tk.OptionMenu(master, variablesize, *sizeDuplicateRemoved, command=callbacksize)
    size.place(x=300, y=205)
    size.config(width=20)

    # variablestyle = tk.StringVar(master)
    # style = tk.OptionMenu(master, variablestyle, *styleDuplicateRemoved, command=callbackstyle)
    # style.place(x=300, y=285)
    # style.config(width=20)

    # variablemodel = tk.StringVar(master)
    # model = tk.OptionMenu(master, variablemodel, *modelDuplicateRemoved, command=callbackmodel)
    # model.place(x=300, y=325)
    # model.config(width=20)

    # tk.Label(master, text=modelDuplicateRemoved[0], bg=mainbgcol, font='Helvetica 10').place(x=300, y=325)

    # variablelocation = tk.StringVar(master)
    # location = tk.OptionMenu(master, variablelocation, "A", "B", "C", "D", "E", command=callbacklocation)
    # location.place(x=300, y=365)
    # location.config(width=20)

# defining open image function for the testing panel
def openTestingImage():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfile(parent=master, initialdir='../Cut Panels', title='Please select a directory')
    filepath = os.path.abspath(tempdir)
    hy = str(filepath.replace("\\", '/' ))
    image = Image.open(hy)
    resize_image = image.resize((250, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(image=img)
    label1.image = img
    label1.place(x=1000, y=200)

def viewPanel():
    imgpts = filter(hy, sizeval, pnameval, modelDuplicateRemoved[0])
    if imgpts is None:
        tk.Label(master, text="---- No Match Found ----", bg=mainbgcol, fg='red', font='Helvetica 8 bold').place(x=298, y=395)
    else:
        tk.Label(master, text="----  Match Found   ----", bg=mainbgcol, fg='green', font='Helvetica 8 bold').place(x=310, y=395)
        imgp = np.zeros((6000, 25000, 3), np.uint8)
        cv2.drawContours(imgp, imgpts, -1, (0, 225, 0), 10)
        halfc = cv2.resize(imgp, (0, 0), fx=0.1, fy=0.1)

        cv2.imshow("Stacked Images", halfc)

        cv2.waitKey(0)

def filt():
    label = filterByName(hy, sizeval, pnameval, modelDuplicateRemoved[0])
    splitted = label.split(",")
    piece_discription = splitted[9].split("/")
    piece_Category = splitted[11].split("/")
    bundle_ID = splitted[15].split("/")
    model_Name = splitted[17].split("/")
    tk.Label(master, text=piece_discription[0], bg=mainbgcol, font='Helvetica 10').place(x=300, y=247)
    tk.Label(master, text=piece_Category[0], bg=mainbgcol, font='Helvetica 10').place(x=300, y=287)
    tk.Label(master, text=bundle_ID[0], bg=mainbgcol, font='Helvetica 10').place(x=300, y=327)
    tk.Label(master, text=model_Name[0], bg=mainbgcol, font='Helvetica 10').place(x=300, y=367)
    tk.Label(master, text=splitted[19], bg=mainbgcol, font='Helvetica 10').place(x=300, y=407)


# defining buttons to insert original panel, testing panel and comparison
original = tk.Button(master, text ="Select Original Panel", command = openOriginalImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
original.place(x=670, y=530)
show = tk.Button(master, text ="View Panel", command = viewPanel, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
show.place(x=670, y=580)
testing = tk.Button(master, text ="Select Testing Panel", command = openTestingImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
testing.place(x=1070, y=530)
# compare = tk.Button(master, text ="Compare Panels", command = openTestingImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0, width=15)
# compare.place(x=400, y=420)
Filter = tk.Button(master, text ="Import", command = filt, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0, width=15)
Filter.place(x=400, y=420)

# initial image for original panel
image = Image.open('../Resources/insert_image.jpg')
resize_image = image.resize((250, 300))
img = ImageTk.PhotoImage(resize_image)
label1 = tk.Label(image=img)
label1.image = img
label1.place(x=600, y=200)

# initial image for testing panel
image = Image.open('../Resources/insert_image.jpg')
resize_image = image.resize((250, 300))
img = ImageTk.PhotoImage(resize_image)
label1 = tk.Label(image=img)
label1.image = img
label1.place(x=1000, y=200)

master.mainloop()