from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')

root.filename = filedialog.askopenfilename(
    title="Select a File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
root.mainloop()
