from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title('Opener')

def opener():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="S:/Python/11th Python/TKinter/Sample Pics", title="Select A File", filetypes=(("jpg files", "*.jpg") , ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=my_img).pack()
    btn2 = Button(root, text="Close", command=root.destroy).pack()
    
my_btn = Button(root, text="Open File", command=opener).pack()

root.mainloop()