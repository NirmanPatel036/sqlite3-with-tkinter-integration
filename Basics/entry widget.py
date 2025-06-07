from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5, fg='#000000', bg='white')
e.pack()
#e.insert(0, 'Enter Your Name: ')

def myClick():
    hello = 'Hello, ' + e.get() + '!'
    myLabel = Label(root, text=hello)
    myLabel.pack()
    
myButton = Button(root, text='Click Me', command = myClick, fg='#000000', bg='white')
#myButton1 = Button(root, text='Use Me', state=DISABLED)
myButton.pack()
#myButton1.pack()

root.mainloop()


