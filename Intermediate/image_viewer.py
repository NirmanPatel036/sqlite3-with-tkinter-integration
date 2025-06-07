from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()

root.title("Nature Viewer")

img1 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Hydrangeas.jpg"))  
img2 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Chrysanthemum.jpg"))  
img3 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Jellyfish.jpg"))  
img4 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Desert.jpg"))  
img5 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Koala.jpg"))  
img6 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Lighthouse.jpg"))  
img7 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Penguins.jpg"))  
img8 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Sample Pics/Tulips.jpg"))  

img_list = [img1, img2, img3, img4, img5, img6, img7, img8]

status = Label(root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image = img_list[image_number-1])
    
    button_forward = Button(root, text='>>', command=lambda : forward(image_number+1) )
    button_back = Button(root, text='<<', command=lambda : back(image_number-1) )
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    if image_number == 8:
        button_forward = Button(root, text='>>', state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    
def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image = img_list[image_number-1])
    
    button_forward = Button(root, text='>>', command=lambda : forward(image_number+1) )
    button_back = Button(root, text='<<', command=lambda : back(image_number-1) )
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update Status Bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


        
button_back = Button(root, text='<<', command=back, state=DISABLED)
button_forward = Button(root, text='>>', command=lambda : forward(2) )
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)

button_quit = Button(root,text="Exit",height=2,width=13,command=root.destroy)
button_quit.grid(row=1, column=1, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


root.mainloop() 
