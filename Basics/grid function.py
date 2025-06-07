from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text='Hello World!').grid(row=0 ,column=0)
myLabel2= Label(root, text='My name is Nirman Patel.').grid(row=1 ,column=1)

#myLabel1.grid(row=1 ,column=0)
#myLabel2.grid(row=1 ,column=1)

root.mainloop( )
