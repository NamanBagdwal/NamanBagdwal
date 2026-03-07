**Sales and Inventory Management System**


**Overview**

The Sales and Inventory Management System is a console-based application developed using Python and MySQL. This project helps manage product inventory, track sales, and handle customer purchases efficiently. It provides separate functionalities for Admin and Customer, enabling smooth management of stock and transactions.

The system automatically creates the required database and tables, making it easy to set up and run.

**Features**

**Admin Features**

Secure Admin Login System
Add New Products to inventory
Update Product Prices
Delete Products from stock
View All Available Items
Change Admin Password
Logout Option

**Customer Features**

View Available Products
Add Items to Bucket
Automatic Bill Calculation
Payment Amount Display
Real-time Stock Update after Purchase

**Technologies Used**

Programming Language: Python
Database: MySQL
Library: mysql-connector-python

**Database Structure**

The system automatically creates the following tables:
login – Stores admin username and password
stock – Stores product code, name, quantity, and price
purchase – Stores purchase records with date, customer name, product code, and amount

**How to Run the Project**

Install Python and MySQL on your system.
Install the required library:
pip install mysql-connector-python
Update the MySQL username and password in the script if needed.
Run the Python file:
python project.py
Follow the menu options to use Admin or Customer functionalities.

**Default Login**

Username: usernamr
Password: pass_

**Future Improvements**

GUI interface using Tkinter or PyQt
Online payment integration
Better authentication system
Product search and filtering
Sales report generation
Automatic Bill Calculation
