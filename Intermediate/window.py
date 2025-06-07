from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Window')
root.geometry("50x50")

def open():
    global my_img
    top = Toplevel()
    top.title("Image")
    my_img = ImageTk.PhotoImage(Image.open("S:/Python/11th Python/TKinter/Sample Pics/Hydrangeas.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close", command=top.destroy).pack()
    
btn = Button(root, text="Open Image", command=open)
btn.grid(row=0, column=0, padx=(20,0), pady=(13,0))
root.mainloop()