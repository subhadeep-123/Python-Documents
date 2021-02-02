from tkinter import *

# Root widget
root = Tk()

# Creating a Labe Widget
myLabel1 = Label(root, text='Hello World').grid(row=0, column=0)
myLabel2 = Label(root, text="My Name is Subhadeep Banerjee").grid(
    row=1, column=1)
 
# Packing it onto the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

root.mainloop()
