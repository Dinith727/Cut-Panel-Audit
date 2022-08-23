import tkinter as tk
from PIL import ImageTk,Image

master = tk.Tk()
master.title("CUT")
master.geometry("400x400")
tk.Label(master, text="Sales order Number : ").grid(row=0)
tk.Label(master, text="Docket Number : ").grid(row=1)
tk.Label(master, text="Cut Number : ").grid(row=2)
tk.Label(master, text="Size : ").grid(row=3)
tk.Label(master, text="Style : ").grid(row=4)
tk.Label(master, text="Panel Number : ").grid(row=5)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)


# Read the Image
image = Image.open("../Cut Panels/11.png")

# Resize the image using resize() method
resize_image = image.resize((300,205))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = tk.Label(image=img)
label1.image = img
label1.grid(row=5, column=20)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

master.mainloop()