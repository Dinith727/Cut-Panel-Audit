import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

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

# input fields
sales_order_number = tk.Entry(master)
docket_number = tk.Entry(master)
cut_number = tk.Entry(master)
size = tk.Entry(master)
style = tk.Entry(master)
panel_number = tk.Entry(master)
location = tk.Entry(master)

# input fields positions
sales_order_number.place(x=300, y=205)
docket_number.place(x=300, y=235)
cut_number.place(x=300, y=265)
size.place(x=300, y=295)
style.place(x=300, y=325)
panel_number.place(x=300, y=355)
location.place(x=300, y=385)

# defining open image function for the original panel
def openOriginalImage():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfile(parent=master, initialdir='../Cut Panels', title='Please select a directory')
    filepath = os.path.abspath(tempdir.name)
    hy = str(filepath.replace("\\", '/' ))
    image = Image.open(hy)
    resize_image = image.resize((250, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(image=img)
    label1.image = img
    label1.place(x=600, y=200)


# defining open image function for the testing panel
def openTestingImage():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfile(parent=master, initialdir='../Cut Panels', title='Please select a directory')
    filepath = os.path.abspath(tempdir.name)
    hy = str(filepath.replace("\\", '/' ))
    image = Image.open(hy)
    resize_image = image.resize((250, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(image=img)
    label1.image = img
    label1.place(x=1000, y=200)


# defining buttons to insert original panel, testing panel and comparison
original = tk.Button(master, text ="Select Original Panel", command = openOriginalImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
original.place(x=670, y=530)
testing = tk.Button(master, text ="Select Testing Panel", command = openTestingImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
testing.place(x=1070, y=530)
compare = tk.Button(master, text ="Compare Panels", command = openTestingImage, bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0, width=15)
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