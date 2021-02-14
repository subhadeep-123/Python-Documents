from PIL import Image, ImageTk
import getpass
from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')

root.filename = filedialog.askopenfilename(
    title="Select a File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
root.mainloop()


root = Tk()
root.title("Message Box")
root.iconbitmap('assets/icon_test.ico')


def open():
    global img
    top = Toplevel()
    top.title("Second Window")
    top.iconbitmap(filename)
    img = ImageTk.PhotoImage(Image.open())
    my_label = Label(top, image=img).pack()
    btn = Button(top, text='Close Window', command=top.destroy).pack()


username = getpass.getuser()
filename = filedialog.askopenfilename(title="Selec an Image", filetype=(
    ("PNG", "*.png"),
    ("JPEG", "*.jpg"),
    ("JPEG", "*.jpeg")),
    initialdir=f"C:/Users/{username}/Desktop"
)


btn = Button(root, text='Open Second Window', command=open).pack()

root.mainloop()
