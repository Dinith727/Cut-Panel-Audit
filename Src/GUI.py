import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

bgcol = '#D5D6EA'

master = tk.Tk()
master.title("Cut Panel Audit")
master.configure(bg=bgcol)
width= master.winfo_screenwidth()
height= master.winfo_screenheight()
#setting tkinter window size
master.geometry("%dx%d" % (width, height))


tk.Label(master, text="Sales order Number : " ,bg=bgcol).place(x=10, y=20)
tk.Label(master, text="Docket Number : ").place(x=10, y=50)
tk.Label(master, text="Cut Number : ").place(x=10, y=80)
tk.Label(master, text="Size : ").place(x=10, y=110)
tk.Label(master, text="Style : ").place(x=10, y=140)
tk.Label(master, text="Panel Number : ").place(x=10, y=170)
tk.Label(master, text="Location : ").place(x=10, y=200)
tk.Label(master, text="Results : ").place(x=10, y=370)





e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)

tk.Label(master, text="Original panel", font='Helvetica 10 bold').place(x=375, y=5)
tk.Label(master, text="Testing panel").place(x=675, y=5)
# Read the Image

hy = "../Cut Panels/14.png"
image = Image.open(hy)
image1 = Image.open("../Cut Panels/14.png")
# Resize the image using resize() method
resize_image = image.resize((250, 300))
resize_image1 = image1.resize((250, 300))

img = ImageTk.PhotoImage(resize_image)
img1 = ImageTk.PhotoImage(resize_image1)

# create label and add resize image
label1 = tk.Label(image=img)
label1.image = img
label1.place(x=300, y=35)

label1 = tk.Label(image=img1)
label1.image = img1
label1.place(x=600, y=35)

e1.place(x=140, y=25)
e2.place(x=140, y=55)
e3.place(x=140, y=85)
e4.place(x=140, y=115)
e5.place(x=140, y=145)
e6.place(x=140, y=175)
e7.place(x=140, y=205)


def search_for_file_path():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfile(parent=master, initialdir=currdir, title='Please select a directory')
    filepath = os.path.abspath(tempdir.name)
    global hy
    hy = str(filepath.replace("\\", '/' ))
    image = Image.open(hy)
    resize_image = image.resize((250, 300))
    img = ImageTk.PhotoImage(resize_image)
    label1 = tk.Label(image=img)
    label1.image = img
    label1.place(x=300, y=35)
    tk.Label(master, text=filepath.replace("\\", '/' )).place(x=10, y=600)
    print(filepath)
    return tempdir


B = tk.Button(master, text ="Select Original File", command = search_for_file_path ,bg='#d9165a', fg='white', font='Helvetica 10 bold', borderwidth=0)
B.place(x=600, y=385)
C = tk.Button(master, text ="Select Testing Panel", command = search_for_file_path)
C.place(x=400, y=385)
D = tk.Button(master, text ="Test", width=10, command = search_for_file_path)
D.place(x=200, y=385)


master.mainloop()