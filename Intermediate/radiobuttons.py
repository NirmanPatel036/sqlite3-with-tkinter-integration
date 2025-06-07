from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Radio Buttons')
root.geometry("200x200")
#r = IntVar()
#r.set("2")

MODES = {
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Babycorn","Babycorn")
}

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack()
    
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
