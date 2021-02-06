from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')

# Different Message Boxes
# showinfo, showwarning, showerror, askquestion, askcancel, askyesno


def popUp():
    messagebox.showinfo("This is my PopUp!", "Hello World")


def yesorno():
    resp = messagebox.askyesno("Hey", "Yes or No")
    Label(root, text=resp).pack()


# Button(root, text="PopUp", command=popUp).pack()
Button(root, text='YesorNo', command=yesorno).pack()
root.mainloop()
