import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from Comparison import compare_panels

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
tk.Label(master, text="-------- Panel Details --------", bg=mainbgcol, font='Helvetica 12 bold').place(x=200, y=150)
tk.Label(master, text="Sales order Number : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=120, y=200)
tk.Label(master, text="Docket Number : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=153, y=230)
tk.Label(master, text="Cut Number : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=180, y=260)
tk.Label(master, text="Size : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=239, y=290)
tk.Label(master, text="Style : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=234, y=320)
tk.Label(master, text="Panel Number : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=164, y=350)
tk.Label(master, text="Location : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=205, y=380)
tk.Label(master, text="Shape Similarity : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=101, y=455)
tk.Label(master, text="Shrinkage Status : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=93, y=475)
tk.Label(master, text="Shape Status : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=122, y=495)
tk.Label(master, text="Shape Pass Limit : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=350, y=455)
tk.Label(master, text="Result : ", bg=mainbgcol, font='Helvetica 12 bold').place(x=405, y=475)
tk.Label(master, text="Original Panel", bg=mainbgcol, font='Helvetica 12 bold').place(x=670, y=170)
tk.Label(master, text="Testing Panel", bg=mainbgcol, font='Helvetica 12 bold').place(x=1070, y=170)

tk.Label(master, text="---- Perimeter Status ----", bg=mainbgcol, font='Helvetica 10 bold').place(x=120, y=540)
tk.Label(master, text="Original Panel :", bg=mainbgcol, font='Helvetica 10 ').place(x=100, y=560)
tk.Label(master, text="Testing Panel :", bg=mainbgcol, font='Helvetica 10').place(x=102, y=580)
tk.Label(master, text="Difference :", bg=mainbgcol, font='Helvetica 10').place(x=124, y=600)
tk.Label(master, text="Deviation Ratio :", bg=mainbgcol, font='Helvetica 10').place(x=95, y=620)

tk.Label(master, text="---- Area Status ----", bg=mainbgcol, font='Helvetica 10 bold').place(x=430, y=540)
tk.Label(master, text="Original Panel :", bg=mainbgcol, font='Helvetica 10').place(x=400, y=560)
tk.Label(master, text="Testing Panel :", bg=mainbgcol, font='Helvetica 10').place(x=402, y=580)
tk.Label(master, text="Difference :", bg=mainbgcol, font='Helvetica 10').place(x=424, y=600)
tk.Label(master, text="Deviation Ratio :", bg=mainbgcol, font='Helvetica 10').place(x=395, y=620)

# input fields
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)

# input fields positions
e1.place(x=300, y=205)
e2.place(x=300, y=235)
e3.place(x=300, y=265)
e4.place(x=300, y=295)
e5.place(x=300, y=325)
e6.place(x=300, y=355)
e7.place(x=300, y=385)

# defining open image function for the original panel
def openOriginalImage():
    tempdir = filedialog.askopenfile(parent=master, initialdir='../Cut Panels', title='Please select a directory')
    filepath = os.path.abspath(tempdir.name)
    global ho
    ho = str(filepath.replace("\\", '/' ))
    image = Image.open(ho)
    resize_image = image.resize((250, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(image=img)
    label1.image = img
    label1.place(x=600, y=200)


# defining open image function for the testing panel
def openTestingImage():
    tempdir = filedialog.askopenfile(parent=master, initialdir='../Cut Panels', title='Please select a directory')
    filepath = os.path.abspath(tempdir.name)
    global ht
    ht = str(filepath.replace("\\", '/' ))
    image = Image.open(ht)
    resize_image = image.resize((250, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(image=img)
    label1.image = img
    label1.place(x=1000, y=200)


def compare():

    space1 = '         '
    space2 = '           '

    sales_order_number = e1.get()
    docket_number = e2.get()
    cut_number = e3.get()
    size = e4.get()
    style = e5.get()
    panel_number = e6.get()
    location = e7.get()

    area1_float, area2_float, areaDiff_float, adevratio_float, peri1_float, peri2_float, periDiff_float, pdevratio_float, shaperesult_float, shape_match_limit, shape, shrinkage, result, status = compare_panels(ho, ht, sales_order_number, docket_number, cut_number, size, style, panel_number, location)
    tk.Label(master, text=area1_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=500, y=560)
    tk.Label(master, text=area2_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=500, y=580)
    tk.Label(master, text=areaDiff_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=500, y=600)
    tk.Label(master, text=adevratio_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=500, y=620)

    tk.Label(master, text=peri1_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=200, y=560)
    tk.Label(master, text=peri2_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=200, y=580)
    tk.Label(master, text=periDiff_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=200, y=600)
    tk.Label(master, text=pdevratio_float+space1, bg=mainbgcol, font='Helvetica 10').place(x=200, y=620)

    tk.Label(master, text=status, bg=mainbgcol, font='Helvetica 10', fg='blue').place(x=125, y=650)

    if shrinkage == 'Panel has expanded':
        tk.Label(master, text=shrinkage, bg=mainbgcol, font='Helvetica 11').place(x=240, y=475)
    else:
        tk.Label(master, text=shrinkage + space2, bg=mainbgcol, font='Helvetica 11').place(x=240, y=475)
    tk.Label(master, text=shaperesult_float+space1, bg=mainbgcol, font='Helvetica 11').place(x=240, y=455)
    tk.Label(master, text=shape+space2, bg=mainbgcol, font='Helvetica 11').place(x=240, y=495)
    tk.Label(master, text=shape_match_limit+space1, bg=mainbgcol, font='Helvetica 11').place(x=500, y=456)

    if result == 'Passed':
        rescolour = 'Green'
    else:
        rescolour = 'Red'

    tk.Label(master, text=result+space1, bg=mainbgcol, font='Helvetica 11 bold', fg=rescolour).place(x=470, y=477)

# defining buttons to insert original panel, testing panel and comparison
original = tk.Button(master, text ="Select Original Panel", command = openOriginalImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
original.place(x=670, y=530)
testing = tk.Button(master, text ="Select Testing Panel", command = openTestingImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
testing.place(x=1070, y=530)
compare = tk.Button(master, text ="Compare Panels", command = compare, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0, width=15)
compare.place(x=300, y=420)

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