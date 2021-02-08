from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


btn = Button(root, text='Click Me!', command=slide).pack()
root.mainloop()
