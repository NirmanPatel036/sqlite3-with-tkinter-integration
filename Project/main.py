from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import sqlite3
import os
from datetime import datetime

class CurativePharmacy:
    def __init__(self):
        # Initialize database
        self.init_database()
        self.current_user = None
        self.cart = []
        self.create_main_window()
    
    def init_database(self):
        """Initialize the user database"""
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL,
                    phone_no TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
        
        # Create orders table for billing history
        c.execute('''CREATE TABLE IF NOT EXISTS orders(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    order_date TEXT,
                    total_amount REAL,
                    items TEXT,
                    FOREIGN KEY (user_id) REFERENCES user (id)
                )''')
        
        conn.commit()
        conn.close()
    
    def create_main_window(self):
        """Create the main welcome window"""
        self.root = Tk()
        self.root.title('Curative Pharmacy')
        self.root.geometry("680x550")
        self.root.configure(bg='#D9D7F1')
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window(self.root, 680, 550)
        
        # Main frame
        frame = LabelFrame(self.root, text='Welcome', font=("Agency FB", 20, "bold"), 
                          fg='#143F6B', bg='#D9D7F1', borderwidth=10, relief="groove", 
                          padx=100, pady=10)
        frame.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=3)
        
        #Logo
        img1 = ImageTk.PhotoImage(Image.open("/Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Project/logo.png"))
        i=Label(self.root,image=img1,bg='#D9D7F1')
        i.grid(row=0,column=0,pady=20,padx=20,columnspan=3)

        # Buttons
        login_btn = Button(frame, text="Login", font=("Courier New", 15, "bold"), 
                          fg='#143F6B', command=self.open_login)
        login_btn.grid(row=0, column=0, ipadx=140, pady=5)
        
        register_btn = Button(frame, text="Register", font=("Courier New", 15, "bold"), 
                             fg='#143F6B', command=self.open_register)
        register_btn.grid(row=1, column=0, ipadx=124, pady=15)
        
        exit_btn = Button(frame, text="Exit", font=("Courier New", 15, "bold"), 
                         fg='#143F6B', command=self.root.destroy)
        exit_btn.grid(row=2, column=0, ipadx=148, pady=(0, 15))
        
        # Information labels
        info1 = Label(self.root, text="* Login to buy products.", 
                     font=("Courier New", 16, "bold"), fg='blue', bg='#D9D7F1')
        info1.grid(row=2, column=0, sticky=W, padx=59, pady=5)
        
        info2 = Label(self.root, text="* Register if you are new customer.", 
                     font=("Courier New", 16, "bold"), fg='blue', bg='#D9D7F1')
        info2.grid(row=3, column=0, sticky=W, padx=59, pady=5)
        
        tagline = Label(self.root, text="Always to help you.", 
                       font=("Arial", 20, "italic"), fg='#193498', bg='#D9D7F1')
        tagline.grid(row=4, column=0, sticky=W+E, columnspan=3, padx=10, pady=20)
        
        self.root.mainloop()
    
    def center_window(self, window, width, height):
        """Center a window on the screen"""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def open_register(self):
        """Open registration window"""
        self.reg_window = Toplevel(self.root)
        self.reg_window.title('Curative Pharmacy - Register')
        self.reg_window.geometry("700x600")
        self.reg_window.configure(bg='#98BAE7')
        self.reg_window.resizable(False, False)
        self.center_window(self.reg_window, 700, 600)
        
        # Title
        title = Label(self.reg_window, text="Registration Form", 
                     font=("Agency FB", 20, "bold"), fg='#143F6B', bg='#98BAE7')
        title.grid(row=0, column=0, columnspan=2, pady=10)
        
        info = Label(self.reg_window, text="*Fill the following details.", 
                    font=("Agency FB", 15, "bold"), fg='blue', bg='#98BAE7')
        info.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        
        # Create form fields
        fields = [
            ("First Name:", "name"),
            ("Last Name:", "surname"),
            ("Username:", "username"),
            ("Email ID:", "email"),
            ("Complete Address:", "address"),
            ("Phone No.:", "phone_no"),
            ("Password:", "password")
        ]
        
        self.reg_entries = {}
        
        for i, (label_text, field_name) in enumerate(fields):
            label = Label(self.reg_window, text=label_text, 
                         font=("Agency FB", 15, "bold"), fg='#066163', bg='#98BAE7')
            label.grid(row=i+2, column=0, sticky=W, padx=10, pady=5)
            
            if field_name == "password":
                entry = Entry(self.reg_window, show='*', width=40, borderwidth=3, relief="ridge")
            else:
                entry = Entry(self.reg_window, width=40, borderwidth=3, relief="ridge")
            
            entry.grid(row=i+2, column=1, padx=20, pady=5, sticky=W)
            self.reg_entries[field_name] = entry
        
        # Buttons
        submit_btn = Button(self.reg_window, text="Register", 
                           font=("Agency FB", 12, "bold"), fg='#143F6B', 
                           command=self.register_user)
        submit_btn.grid(row=len(fields)+2, column=0, columnspan=2, pady=15, 
                       sticky=W+E, padx=50)
        
        # Status label
        self.reg_status = Label(self.reg_window, text="", fg='#193498', bg='#98BAE7')
        self.reg_status.grid(row=len(fields)+3, column=0, columnspan=2, pady=5)
        
        tagline = Label(self.reg_window, text="Always to help you.", 
                       font=("Arial", 16, "italic"), fg='#193498', bg='#98BAE7')
        tagline.grid(row=len(fields)+4, column=0, columnspan=2, pady=10)
    
    def register_user(self):
        """Register a new user"""
        # Validate inputs
        for field_name, entry in self.reg_entries.items():
            if not entry.get().strip():
                messagebox.showerror("Error", f"Please fill in {field_name.replace('_', ' ')}")
                return
        
        try:
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            
            # Check if username already exists
            c.execute("SELECT * FROM user WHERE username = ?", (self.reg_entries['username'].get(),))
            if c.fetchone():
                messagebox.showerror("Error", "Username already exists!")
                return
            
            # Insert new user
            c.execute('''INSERT INTO user (name, surname, username, email, address, phone_no, password)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                     (self.reg_entries['name'].get(),
                      self.reg_entries['surname'].get(),
                      self.reg_entries['username'].get(),
                      self.reg_entries['email'].get(),
                      self.reg_entries['address'].get(),
                      self.reg_entries['phone_no'].get(),
                      self.reg_entries['password'].get()))
            
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Success", "Registration successful! You can now login.")
            self.reg_window.destroy()
            
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
    
    def open_login(self):
        """Open login window"""
        self.login_window = Toplevel(self.root)
        self.login_window.title('Curative Pharmacy - Login')
        self.login_window.geometry("500x400")
        self.login_window.configure(bg='#98BAE7')
        self.login_window.resizable(False, False)
        self.center_window(self.login_window, 500, 400)
        
        # Title
        title = Label(self.login_window, text="Login to Your Account", 
                     font=("Agency FB", 20, "bold"), fg='#143F6B', bg='#98BAE7')
        title.grid(row=0, column=0, columnspan=2, pady=20)
        
        info = Label(self.login_window, text="*Enter your login details.", 
                    font=("Agency FB", 15, "bold"), fg='blue', bg='#98BAE7')
        info.grid(row=1, column=0, columnspan=2, sticky=W, padx=10, pady=10)
        
        # Username
        username_label = Label(self.login_window, text="Username:", 
                              font=("Agency FB", 15, "bold"), fg='#066163', bg='#98BAE7')
        username_label.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        
        self.username_entry = Entry(self.login_window, width=30, borderwidth=3, relief="ridge")
        self.username_entry.grid(row=2, column=1, padx=20, pady=10)
        
        # Password
        password_label = Label(self.login_window, text="Password:", 
                              font=("Agency FB", 15, "bold"), fg='#066163', bg='#98BAE7')
        password_label.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        
        self.password_entry = Entry(self.login_window, show='*', width=30, 
                                   borderwidth=3, relief="ridge")
        self.password_entry.grid(row=3, column=1, padx=20, pady=10)
        
        # Login button
        login_btn = Button(self.login_window, text="Login", 
                          font=("Agency FB", 12, "bold"), fg='#143F6B', 
                          command=self.login_user)
        login_btn.grid(row=4, column=0, columnspan=2, pady=20, sticky=W+E, padx=50)
        
        # Status label
        self.login_status = Label(self.login_window, text="", fg='red', bg='#98BAE7')
        self.login_status.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Bind Enter key to login
        self.login_window.bind('<Return>', lambda event: self.login_user())
        self.username_entry.focus()
    
    def login_user(self):
        """Authenticate user login"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            self.login_status.config(text="Please enter both username and password", fg='red')
            return
        
        try:
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            
            c.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
            user = c.fetchone()
            
            if user:
                self.current_user = {
                    'id': user[0],
                    'name': user[1],
                    'surname': user[2],
                    'username': user[3],
                    'email': user[4],
                    'address': user[5],
                    'phone_no': user[6]
                }
                self.login_status.config(text="Login successful! Opening shop...", fg='green')
                self.login_window.after(1000, self.open_shop)
            else:
                self.login_status.config(text="Invalid username or password!", fg='red')
            
            conn.close()
            
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
    
    def open_shop(self):
        """Open the medicine shop window"""
        self.login_window.destroy()
        
        self.shop_window = Toplevel(self.root)
        self.shop_window.title('Curative Pharmacy - Medicine Shop')
        self.shop_window.geometry("800x700")
        self.shop_window.configure(bg='#98BAE7')
        self.shop_window.resizable(False, False)
        self.center_window(self.shop_window, 800, 700)
        
        # Welcome message
        welcome = Label(self.shop_window, 
                       text=f"Welcome, {self.current_user['name']} {self.current_user['surname']}!", 
                       font=("Agency FB", 18, "bold"), fg='#143F6B', bg='#98BAE7')
        welcome.grid(row=0, column=0, columnspan=3, pady=10)
        
        info = Label(self.shop_window, text="*Select the problem and choose medicine:", 
                    font=("Agency FB", 15, "bold"), fg='blue', bg='#98BAE7')
        info.grid(row=1, column=0, columnspan=3, sticky=W, padx=10, pady=5)
        
        # Medicine categories and their medicines
        self.medicines = {
            "Fever": [
                ("Paracetamol 500mg", 25),
                ("Crocin Advance", 35),
                ("Dolo 650mg", 30)
            ],
            "Cough & Cold": [
                ("Benadryl Cough Syrup", 85),
                ("Vicks VapoRub", 95),
                ("Strepsils Lozenges", 45)
            ],
            "Headache": [
                ("Aspirin 75mg", 20),
                ("Saridon", 15),
                ("Combiflam", 25)
            ],
            "Acidity": [
                ("ENO Fruit Salt", 35),
                ("Digene Gel", 40),
                ("Pantop 40mg", 120)
            ],
            "Diabetes": [
                ("Glucon-D", 55),
                ("Diabetrol", 180),
                ("Metformin 500mg", 85)
            ],
            "Blood Pressure": [
                ("Telma 40mg", 95),
                ("Amlodipine 5mg", 65),
                ("Losartan 50mg", 75)
            ]
        }
        
        # Create category buttons
        row = 2
        col = 0
        for category in self.medicines.keys():
            btn = Button(self.shop_window, text=category, 
                        font=("Agency FB", 11, "bold"), fg='#143F6B',
                        width=15, height=2,
                        command=lambda cat=category: self.show_medicines(cat))
            btn.grid(row=row, column=col, padx=10, pady=5, sticky=W+E)
            
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Cart section
        cart_frame = LabelFrame(self.shop_window, text="Shopping Cart", 
                               font=("Agency FB", 14, "bold"), fg='#143F6B', bg='#98BAE7')
        cart_frame.grid(row=row+1, column=0, columnspan=3, padx=10, pady=20, sticky=W+E)
        
        # Cart display
        self.cart_display = Text(cart_frame, height=8, width=70, font=("Courier", 10))
        cart_scroll = Scrollbar(cart_frame, orient=VERTICAL, command=self.cart_display.yview)
        self.cart_display.config(yscrollcommand=cart_scroll.set)
        
        self.cart_display.grid(row=0, column=0, padx=10, pady=10)
        cart_scroll.grid(row=0, column=1, sticky=N+S, pady=10)
        
        # Cart buttons
        button_frame = Frame(cart_frame, bg='#98BAE7')
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        clear_cart_btn = Button(button_frame, text="Clear Cart", 
                               font=("Agency FB", 10, "bold"), fg='#143F6B',
                               command=self.clear_cart)
        clear_cart_btn.grid(row=0, column=0, padx=10)
        
        checkout_btn = Button(button_frame, text="Checkout & Bill", 
                             font=("Agency FB", 12, "bold"), fg='black', bg='green',
                             command=self.checkout)
        checkout_btn.grid(row=0, column=1, padx=10)
        
        # Total amount
        self.total_label = Label(cart_frame, text="Total: ₹0.00", 
                                font=("Agency FB", 14, "bold"), fg='#143F6B', bg='#98BAE7')
        self.total_label.grid(row=2, column=0, columnspan=2, pady=5)
        
        self.update_cart_display()
    
    def show_medicines(self, category):
        """Show medicines for selected category"""
        med_window = Toplevel(self.shop_window)
        med_window.title(f'Curative Pharmacy - {category} Medicines')
        med_window.geometry("600x400")
        med_window.configure(bg='#E8F4FD')
        med_window.resizable(False, False)
        self.center_window(med_window, 600, 400)
        
        title = Label(med_window, text=f"{category} Medicines", 
                     font=("Agency FB", 18, "bold"), fg='#143F6B', bg='#E8F4FD')
        title.grid(row=0, column=0, columnspan=4, pady=15)
        
        # Headers
        headers = ["Medicine Name", "Price (₹)", "Quantity", "Add to Cart"]
        for i, header in enumerate(headers):
            label = Label(med_window, text=header, font=("Agency FB", 12, "bold"), 
                         fg='#066163', bg='#E8F4FD')
            label.grid(row=1, column=i, padx=10, pady=5, sticky=W+E)
        
        # Medicine list
        for i, (med_name, price) in enumerate(self.medicines[category]):
            row = i + 2
            
            # Medicine name
            Label(med_window, text=med_name, font=("Agency FB", 11), 
                 fg='black', bg='#E8F4FD').grid(row=row, column=0, padx=10, pady=5, sticky=W)
            
            # Price
            Label(med_window, text=f"₹{price}", font=("Agency FB", 11), 
                 fg='black', bg='#E8F4FD').grid(row=row, column=1, padx=10, pady=5)
            
            # Quantity spinbox
            qty_var = IntVar(value=1)
            qty_spin = Spinbox(med_window, from_=1, to=10, width=5, textvariable=qty_var)
            qty_spin.grid(row=row, column=2, padx=10, pady=5)
            
            # Add to cart button
            add_btn = Button(med_window, text="Add to Cart", 
                           font=("Agency FB", 9, "bold"), fg='black', bg='#4CAF50',
                           command=lambda m=med_name, p=price, q=qty_var: self.add_to_cart(m, p, q.get()))
            add_btn.grid(row=row, column=3, padx=10, pady=5)
    
    def add_to_cart(self, medicine_name, price, quantity):
        """Add medicine to cart"""
        # Check if medicine already in cart
        for item in self.cart:
            if item['name'] == medicine_name:
                item['quantity'] += quantity
                item['total'] = item['quantity'] * item['price']
                break
        else:
            # Add new item to cart
            self.cart.append({
                'name': medicine_name,
                'price': price,
                'quantity': quantity,
                'total': price * quantity
            })
        
        self.update_cart_display()
        messagebox.showinfo("Added to Cart", f"{medicine_name} x{quantity} added to cart!")
    
    def update_cart_display(self):
        """Update the cart display"""
        self.cart_display.delete(1.0, END)
        
        if not self.cart:
            self.cart_display.insert(END, "Your cart is empty")
            self.total_label.config(text="Total: ₹0.00")
            return
        
        self.cart_display.insert(END, f"{'Medicine':<25} {'Qty':<5} {'Price':<8} {'Total':<8}\n")
        self.cart_display.insert(END, "-" * 50 + "\n")
        
        total_amount = 0
        for item in self.cart:
            line = f"{item['name']:<25} {item['quantity']:<5} ₹{item['price']:<7} ₹{item['total']:<7}\n"
            self.cart_display.insert(END, line)
            total_amount += item['total']
        
        self.cart_display.insert(END, "-" * 50 + "\n")
        self.cart_display.insert(END, f"{'TOTAL AMOUNT:':<40} ₹{total_amount}")
        
        self.total_label.config(text=f"Total: ₹{total_amount:.2f}")
    
    def clear_cart(self):
        """Clear the shopping cart"""
        if messagebox.askyesno("Clear Cart", "Are you sure you want to clear the cart?"):
            self.cart = []
            self.update_cart_display()
    
    def checkout(self):
        """Open checkout and billing window"""
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Please add some medicines to cart first!")
            return
        
        self.billing_window = Toplevel(self.shop_window)
        self.billing_window.title('Curative Pharmacy - Bill')
        self.billing_window.geometry("600x700")
        self.billing_window.configure(bg='white')
        self.billing_window.resizable(False, False)
        self.center_window(self.billing_window, 600, 700)
        
        # Bill content
        bill_frame = Frame(self.billing_window, bg='white', relief=RIDGE, bd=2)
        bill_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header = Label(bill_frame, text="CURATIVE PHARMACY", 
                      font=("Arial", 20, "bold"), fg='#143F6B', bg='white')
        header.pack(pady=10)
        
        tagline = Label(bill_frame, text="Always to help you", 
                       font=("Arial", 12, "italic"), fg='#666', bg='white')
        tagline.pack()
        
        # Separator
        Label(bill_frame, text="=" * 60, font=("Courier", 10), bg='white').pack(pady=5)
        
        # Customer info
        customer_frame = Frame(bill_frame, bg='white')
        customer_frame.pack(fill=X, padx=10, pady=5)
        
        Label(customer_frame, text=f"Customer: {self.current_user['name']} {self.current_user['surname']}", 
              font=("Arial", 11), bg='white').pack(anchor=W)
        Label(customer_frame, text=f"Phone: {self.current_user['phone_no']}", 
              font=("Arial", 11), bg='white').pack(anchor=W)
        Label(customer_frame, text=f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M')}", 
              font=("Arial", 11), bg='white').pack(anchor=W)
        
        # Separator
        Label(bill_frame, text="-" * 60, font=("Courier", 10), bg='white').pack(pady=5)
        
        # Bill items
        bill_text = Text(bill_frame, height=15, width=70, font=("Courier", 10), 
                        bg='white', relief=FLAT)
        bill_text.pack(padx=10, pady=5)
        
        # Generate bill content
        bill_content = f"{'ITEM':<30} {'QTY':<5} {'RATE':<10} {'AMOUNT':<10}\n"
        bill_content += "-" * 60 + "\n"
        
        total_amount = 0
        for item in self.cart:
            bill_content += f"{item['name']:<30} {item['quantity']:<5} ₹{item['price']:<9} ₹{item['total']:<9}\n"
            total_amount += item['total']
        
        bill_content += "-" * 60 + "\n"
        bill_content += f"{'TOTAL AMOUNT:':<50} ₹{total_amount}\n"
        bill_content += "=" * 60 + "\n"
        bill_content += "\nThank you for choosing Curative Pharmacy!\n"
        bill_content += "Take care of your health!"
        
        bill_text.insert(1.0, bill_content)
        bill_text.config(state=DISABLED)
        
        # Buttons
        button_frame = Frame(bill_frame, bg='white')
        button_frame.pack(pady=20)
        
        confirm_btn = Button(button_frame, text="Confirm Order", 
                           font=("Arial", 12, "bold"), fg='black', bg='green',
                           command=lambda: self.confirm_order(total_amount))
        confirm_btn.pack(side=LEFT, padx=10)
        
        print_btn = Button(button_frame, text="Print Bill", 
                          font=("Arial", 12, "bold"), fg='black', bg='blue',
                          command=lambda: self.print_bill(bill_content))
        print_btn.pack(side=LEFT, padx=10)
    
    def confirm_order(self, total_amount):
        """Confirm the order and save to database"""
        try:
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            
            # Prepare order items string
            items_str = "; ".join([f"{item['name']} x{item['quantity']}" for item in self.cart])
            
            # Insert order
            c.execute('''INSERT INTO orders (user_id, order_date, total_amount, items)
                        VALUES (?, ?, ?, ?)''',
                     (self.current_user['id'], 
                      datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                      total_amount,
                      items_str))
            
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Order Confirmed", 
                              f"Your order has been confirmed!\nTotal Amount: ₹{total_amount}\nThank you for shopping with us!")
            
            # Clear cart and close windows
            self.cart = []
            self.billing_window.destroy()
            self.shop_window.destroy()
            
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error saving order: {e}")
    
    def print_bill(self, bill_content):
        """Save bill to text file"""
        try:
            filename = f"bill_{self.current_user['username']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write(bill_content)
            messagebox.showinfo("Bill Saved", f"Bill saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save bill: {e}")

if __name__ == "__main__":
    app = CurativePharmacy()