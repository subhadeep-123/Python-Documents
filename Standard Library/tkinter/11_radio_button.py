from tkinter import *

root = Tk()
root.title('Adding Frames to Tkinter')
root.iconbitmap('assets/icon_test.ico')


MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Mushroom", "Mushroom"),
    ("Cheese", "Cheese"),
    ("Onions", "Onions")
]

Pizza = StringVar()
Pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=Pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myBtn = Button(root, text="click Me!", command=lambda: clicked(Pizza.get()))
myBtn.pack()
root.mainloop()
