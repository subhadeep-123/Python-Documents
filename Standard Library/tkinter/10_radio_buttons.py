from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Adding Frames to Tkinter')
root.iconbitmap('assets/icon_test.ico')
r = IntVar()
r.set(2)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=r, value=1,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 3", variable=r, value=3,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 4", variable=r, value=4,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 5", variable=r, value=5,
            command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 6", variable=r, value=6,
            command=lambda: clicked(r.get())).pack()

# For string
# Radiobutton(root, text="Option 6", variable=r, value="6").pack()
# r = StringVar()
myLabel = Label(root, text=r.get())
myLabel.pack()

myBtn = Button(root, text="click Me!", command=lambda: clicked(r.get()))
myBtn.pack()
root.mainloop()
