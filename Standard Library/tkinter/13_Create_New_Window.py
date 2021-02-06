import builtins
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')


def open():
    global img
    top = Toplevel()
    top.title("Second Window")
    top.iconbitmap('assets/icon_test.ico')
    img = ImageTk.PhotoImage(Image.open('assets/img0.jpg'))
    my_label = Label(top, image=img).pack()
    btn = Button(top, text='Close Window', command=top.destroy).pack()


btn = Button(root, text='Open Second Window', command=open).pack()

root.mainloop()
