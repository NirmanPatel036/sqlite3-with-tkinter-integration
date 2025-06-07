from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Frame')

frame = LabelFrame(root, text="This is my frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)
#frame.configure(bg="#FFFBE7")

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="... or Here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=0, sticky=W+E)

root.mainloop()
