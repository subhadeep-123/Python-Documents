from tkinter import *
import types
from PIL import Image, ImageTk

root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')
root.geometry("400x400")


def show():
    my_label = Label(root, text=var.get()).pack()


var = StringVar()
c = Checkbutton(root, text="Check this box, I dare you!",
                variable=var, onvalue="pizza", offvalue="hamburger")
c.deselect()
c.pack()

btn = Button(root, text="Show Selection", command=show).pack()
root.mainloop()
