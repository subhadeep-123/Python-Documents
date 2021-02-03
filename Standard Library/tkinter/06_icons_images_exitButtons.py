from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title('Icons, Images and Exit Buttons')
# Adding Icon
root.iconbitmap('assets/icon_test.ico')


img = ImageTk.PhotoImage(Image.open('assets/girl.jpg'))
my_label = Label(image=img, width=200, height=200)
my_label.pack()

# Exit button
btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_quit.pack()
root.mainloop()
