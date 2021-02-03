import builtins
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.iconbitmap('assets/icon_test.ico')

img0 = ImageTk.PhotoImage(Image.open('assets/img0.jpg'))
img1 = ImageTk.PhotoImage(Image.open('assets/img1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('assets/img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('assets/img3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('assets/img4.jpg'))

image_list = [img0, img1, img2, img3, img4]
my_label = Label(image=img0)
my_label.grid(row=0, column=0, columnspan=3)


def next(img_num):
    global my_label
    global btn_fwd
    global btn_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    btn_fwd = Button(root, text='>>', command=lambda: next(img_num+1))
    btn_back = Button(root, text='<<', command=lambda: previous(img_num - 1))

    if img_num == 5:
        btn_fwd = Button(root, text='>>', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_fwd.grid(row=1, column=2)


def previous(img_num):
    global my_label
    global btn_fwd
    global btn_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    btn_fwd = Button(root, text='>>', command=lambda: next(img_num+1))
    btn_back = Button(root, text='<<', command=lambda: previous(img_num - 1))
    if img_num == 1:
        btn_back = Button(root, text='<<', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0)
    btn_fwd.grid(row=1, column=2)


btn_back = Button(root, text='<<', command=previous, state=DISABLED)
btn_fwd = Button(root, text='>>', command=lambda: next(2))
btn_exit = Button(root, text='Exit', command=root.quit)

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_fwd.grid(row=1, column=2)
root.mainloop()
