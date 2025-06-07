from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Resident Details')
root.geometry("450x500")
root.iconbitmap("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Advanced/myicon.ico")
#root.configure(bg='#E8C07D')

#Database

#Create a Database or connect to one
conn = sqlite3.connect("address_book.db")

#create Cursor
csor = conn.cursor()

#Create table

'''
conn.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""")
'''

#Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, padx=20)

#Create Text Boxes Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=10, column=0, padx=20)

#Create the Save Function
def save():
    #Create a Database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    #create Cursor
    csor = conn.cursor()  
    
    record_id = delete_box.get()
    csor.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            state = :state,
            zipcode = :zipcode
            
            WHERE oid = :oid""",
            {
             'first': f_name_editor.get(),
             'last': l_name_editor.get(),
             'address': address_editor.get(),
             'city': city_editor.get(),
             'state': state_editor.get(),
             'zipcode': zipcode_editor.get(),
             'oid': record_id
             })
    
    #Commit changes
    conn.commit()
    
    #Close connection
    conn.close()

#Create a Function to Update a Record
def update():
    editor = Tk()
    editor.title('Update Record')
    editor.geometry("400x400")
    root.iconbitmap("S:/Python/11th Python/TKinter/Advanced/myicon.ico")    
    #editor.configure(bg="#FFFBE7")
    
    #Create global vars
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    #Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)
    
    #Create Text Boxes Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, padx=10, pady=(10,0))
    
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0, padx=10)
    
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0, padx=10)
    
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0, padx=10)
    
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0, padx=10)
    
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0, padx=10)
    
    #Create a Save Button
    save_btn = Button(editor, text="Save Record", command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=(20,0), ipadx=128)
    
    #Create a Database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    #create Cursor
    csor = conn.cursor()
    
    record_id = delete_box.get()
    #Query The Database
    csor.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = csor.fetchall()
    
    #Loop Through Results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])    
    
    
#Create a Function to Delete a Record
def delete():
    #Create a Database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    #create Cursor
    csor = conn.cursor()
    
    #Delete a record
    csor.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    # oid simply refers to the primary key value
    
    delete_box.delete(0, END)
    
    #Commit changes
    conn.commit()
    
    #Close connection
    conn.close()    

#Create a Submit Function for Database
def submit():
    #Create a Database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    #create Cursor
    csor = conn.cursor()
    
    # Insert Into Table
    csor.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  "f_name" : f_name.get(),
                  "l_name" : l_name.get(),
                  "address" : address.get(),
                  "city" : city.get(),
                  "state" : state.get(),
                  "zipcode" : zipcode.get()
              })
    
    #Commit changes
    conn.commit()
    
    #Close connection
    conn.close()
    
    
    #Clear Textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#Create Query Function
def query():
    #Create a Database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    #create Cursor
    csor = conn.cursor()
    
    
    #Query The Database
    csor.execute("SELECT *, oid FROM addresses")
    records = csor.fetchall()
    print(records)
    
    #Loop Through Results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " : " + str(record[2]) + ", " + str(record[3]) + ", " + str(record[4]) + ", " + str(record[5]) + "\n" + "\n"
        
    query_label = Label(root, text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)
    
    #Commit changes
    conn.commit()
    
    #Close connection
    conn.close()    

#Create a Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=(20,0), ipadx=100)

#Create Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=(20,0), ipadx=128)

#Create Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=(20,0), ipadx=128)

#Create an Update Button
update_btn = Button(root, text="Update Record", command=update)
update_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=(20,0), ipadx=126)

#Commit changes
conn.commit()

#Close connection
conn.close()


root.mainloop()
