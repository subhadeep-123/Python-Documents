from tkinter import *

root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')
root.geometry("400x400")


def dostuff():
    my_label = Label(root, text=clicked.get()).pack()


options = ["Monday", "Tuesday",
           "Wednessday", "Thursday",
           "Friday", "Saturday", "Sunday"]
# Drop Down Boxes
clicked = StringVar()
clicked.set("Options")
drop = OptionMenu(root, clicked, *options)
drop.pack()
btn = Button(root, text="Click Me!", command=dostuff).pack()
root.mainloop()
