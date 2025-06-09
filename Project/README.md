# Curative Pharmacy Management System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite&logoColor=white)
![PIL](https://img.shields.io/badge/Image-Pillow-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A comprehensive pharmacy management system built with Python's Tkinter GUI framework. This application provides a complete solution for pharmacy operations including user registration, authentication, medicine catalog browsing, shopping cart management, and billing.

## Features

### 🔐 User Management
- **User Registration**: New customers can create accounts with personal details
- **Secure Login**: Username and password authentication
- **User Profile Storage**: SQLite database integration for user data

### 💊 Medicine Catalog
- **Categorized Medicines**: Organized by medical conditions
  - Fever medications
  - Cough & Cold remedies
  - Headache relief
  - Acidity treatments
  - Diabetes management
  - Blood pressure medications
- **Real-time Pricing**: Updated medicine prices and availability

### 🛒 Shopping Experience
- **Interactive Cart**: Add, remove, and modify medicine quantities
- **Real-time Total Calculation**: Automatic price computation
- **Medicine Selection**: Choose quantities with user-friendly spinboxes

### 🧾 Billing System
- **Professional Bills**: Formatted receipts with customer details
- **Order History**: Database storage of all transactions
- **Bill Export**: Save bills as text files for record-keeping
- **Order Confirmation**: Secure transaction processing

## Installation

### Prerequisites

Ensure you have Python 3.7 or higher installed on your system.

### Required Dependencies

Install the required packages using pip:

```bash
pip install pillow
```

**Note**: `tkinter` and `sqlite3` are included with standard Python installations.

### Setup

1. **Clone or download** the project files
2. **Place the logo image** at the specified path:
   ```
   /Users/nirmanpatel36/Documents/Python/11th Python/TKinter/Project/logo.png
   ```
   Or update the image path in `main.py` to match your logo location
3. **Run the application**:
   ```bash
   python main.py
   ```

## Usage

### Getting Started

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **New Users**
   - Click "Register" to create a new account
   - Fill in all required personal information
   - Submit the registration form

3. **Existing Users**
   - Click "Login" 
   - Enter your username and password
   - Access the medicine shop

### Shopping Process

1. **Browse Categories**: Select from available medicine categories
2. **Choose Medicines**: View medicines with prices and select quantities
3. **Manage Cart**: Review selected items and modify as needed
4. **Checkout**: Generate bill and confirm your order
5. **Save Receipt**: Print or save your bill for records

## Database Schema

The application uses SQLite with two main tables:

### Users Table
- `id` (Primary Key)
- `name`, `surname`
- `username` (Unique)
- `email`, `address`, `phone_no`
- `password`

### Orders Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `order_date`, `total_amount`
- `items` (Order details)

## File Structure

```
project/
├── main.py             # Main application file
├── user.db             # SQLite database (user input dependent)
├── medicine.db         # SQLite database (medicine record)
├── logo.png            # Application logo
└── bill_*.txt          # Generated bill files
```

## Technical Specifications

- **GUI Framework**: Tkinter with custom styling
- **Database**: SQLite for local data storage
- **Image Processing**: Pillow (PIL) for logo display
- **Architecture**: Object-oriented design with class-based structure
- **Error Handling**: Comprehensive exception handling for database operations

## Key Components

### CurativePharmacy Class
- **Database Management**: User and order data handling
- **GUI Management**: Window creation and event handling
- **Business Logic**: Shopping cart and billing operations

### Window Management
- **Main Window**: Welcome screen with login/register options
- **Registration Window**: User account creation
- **Login Window**: User authentication
- **Shop Window**: Medicine browsing and cart management
- **Billing Window**: Order confirmation and receipt generation

## Medicine Categories

The system includes the following pre-configured medicine categories:

| Category | Sample Medicines | Price Range |
|----------|-----------------|-------------|
| Fever | Paracetamol, Crocin, Dolo | ₹15-35 |
| Cough & Cold | Benadryl, Vicks, Strepsils | ₹45-95 |
| Headache | Aspirin, Saridon, Combiflam | ₹15-25 |
| Acidity | ENO, Digene, Pantop | ₹35-120 |
| Diabetes | Glucon-D, Diabetrol, Metformin | ₹55-180 |
| Blood Pressure | Telma, Amlodipine, Losartan | ₹65-95 |

## Error Handling

The application includes robust error handling for:
- Database connection issues
- Invalid user inputs
- Missing files or resources
- Authentication failures
- Transaction processing errors

## Security Features

- Password field masking during input
- Input validation for all user data
- SQL injection prevention with parameterized queries
- Session management for logged-in users

## Troubleshooting

### Common Issues

**Logo not displaying**: Update the image path in `main.py` to match your logo location

**Database errors**: Ensure write permissions in the application directory

**GUI not responsive**: Check Python and Tkinter installation

**Missing dependencies**: Install required packages using pip

## License

This project is open source and available under the MIT License.
