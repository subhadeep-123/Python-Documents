from tkinter import *
from tkinter.font import BOLD

root = Tk()


def click():
    mylabel = Label(root, text=f"Hello, {a.get()}")
    mylabel.pack()


a = Entry(root, width=30)
a.pack()
a.insert(0, "Enter Your Name")
btn = Button(root, text='Click Me', command=click)
btn.pack()

root.mainloop()
