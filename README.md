## Hi there 👋
🧾 Sales and Inventory Management System

A console-based Sales and Inventory Management System built using Python and MySQL.
Is project ka use Admin aur Customer dono kar sakte hain inventory manage karne aur purchase karne ke liye.

🚀 Features
🔐 Admin Panel

Admin login system

New products add karna

Product price update karna

Product delete karna

Stock display karna

Admin password change karna

🛒 Customer Panel

Items purchase karna

Payment amount dekhna

Available products list dekhna

🛠️ Technologies Used

Python 3

MySQL Database

mysql-connector-python

🗄️ Database Structure

Database ka naam: sales_manage

Tables:

login

username

password

stock

pcode

pname

quantity

price

purchase

odate

name

pcode

amount

⚙️ Installation & Setup
1️⃣ Requirements Install Karein
pip install mysql-connector-python

2️⃣ MySQL Setup

MySQL server running hona chahiye

Username aur password code me update karein:

mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345"
)

3️⃣ Project Run Karein
python main.py

🔑 Default Login Credentials
Username: usernamr
Password: pass_


⚠️ First login ke baad password change karna recommended hai.

📌 How It Works

Program start hote hi database aur tables automatically create ho jaate hain

Admin inventory manage karta hai

Customer items purchase karta hai

Stock quantity auto-update hoti hai

Purchase record database me save hota hai

⚠️ Important Notes

Ye project learning purpose ke liye best hai

SQL queries me string concatenation use hui hai (production ke liye unsafe)

Future improvement ke liye:

SQL Injection protection

GUI (Tkinter / Web App)

Proper billing system

Multiple customers support

🌟 Future Enhancements (Optional)

Login system with encryption

Invoice generation

Reports & analytics

Role-based authentication

Web-based version (Flask/Django)

📄 License

This project is open-source and free to use for educational purposes.
