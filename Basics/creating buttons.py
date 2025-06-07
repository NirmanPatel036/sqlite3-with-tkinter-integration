from tkinter import *

root = Tk()

#fg ----> foreground colour
#bg ----> background colour


def myClick():
    myLabel = Label(root, text='Hey, I just clicked a button!')
    myLabel.pack()
    
myButton = Button(root, text='Click Me', command = myClick, fg='green', bg='yellow')
myButton1 = Button(root, text='Use Me', state=DISABLED)
myButton.pack()
myButton1.pack()

root.mainloop()
