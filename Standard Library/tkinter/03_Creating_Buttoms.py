from tkinter import *

root = Tk()


def myClick():
    mylabel = Label(root, text="I am clicked a Button")
    mylabel.pack()


# btn = Button(root, text="Click Me", padx=15, pady=10,
#              fg='red', activebackground='yellow',
#              bg='green', command=click(), state=DISABLED)

btn = Button(root, text="Click Me", command=myClick)
btn.pack()
root.mainloop()
