==============================
Payslip Generator – The Chic Events
==============================

This Python project automatically generates PDF payslips from an Excel file and sends them to employees via email. It is designed for internal payroll processing at The Chic Events and is part of a bootcamp assignment to reinforce file handling, data processing, PDF generation, and email automation using Python.

------------------------------
Features
------------------------------
- Read employee data from an Excel file (employees.xlsx)
- Calculate net salary: Net Salary = Basic Salary + Allowances - Deductions
- Generate formatted PDF payslips for each employee
- Email each payslip as an attachment using Gmail SMTP
- Log successes and failures for tracking

------------------------------
Technologies Used
------------------------------
- Python 3.x
- pandas – for reading and processing Excel files
- fpdf – for generating PDF documents
- yagmail – for sending emails easily
- logging – for status reporting and error tracking

------------------------------
Project Structure
------------------------------
payslip_generator.py         -> Main script
employees.xlsx               -> Input Excel file
payslips/                    -> Folder where payslip PDFs are saved
README.txt                   -> Project documentation

------------------------------
Prerequisites
------------------------------
Before running the script, make sure you have the following:
1. Python 3.x installed
2. A Gmail account
3. Required Python packages installed

Install packages using pip:
pip install pandas fpdf yagmail

------------------------------
Configuring Email Settings
------------------------------
1. Generate a Gmail App Password:
   - Visit https://myaccount.google.com/apppasswords
   - Choose "Mail" and the device name, then generate
   - Copy the 16-character app password

2. Open payslip_generator.py and set the email credentials:
   SENDER_EMAIL = "your_email@gmail.com"
   SENDER_PASSWORD = "your_app_password"

Do not use your regular Gmail password. Use the app password instead for better security.

------------------------------
How to Run the Script
------------------------------
1. Ensure that employees.xlsx is in the same directory as the script.
2. Open terminal or command prompt.
3. Run the script:

   python payslip_generator.py

4. The script will:
   - Create payslips in the payslips/ folder
   - Email each payslip to the corresponding employee
   - Log the status of each operation in the terminal

------------------------------
Sample employees.xlsx Format
------------------------------
| Employee ID | Name       | Email             | Basic Salary | Allowances | Deductions |
|-------------|------------|-------------------|--------------|------------|-------------|
| EMP001      | Jane Doe   | jane@example.com  | 1200         | 150        | 100         |
| EMP002      | John Smith | john@example.com  | 1300         | 200        | 50          |

Make sure the column names are exactly as shown.

------------------------------
Output
------------------------------
- PDFs named like EMP001_payslip.pdf will be saved in the payslips/ directory
- Each PDF includes:
  - Employee name and ID
  - Basic Salary, Allowances, and Deductions
  - Net Salary
  - Branded layout with header and footer

------------------------------
Security Tip
------------------------------
Do not hardcode your actual Gmail password.
For added security, use environment variables or a .env file to store credentials safely.
You can also ask for help adding dotenv support to your script.

------------------------------
Contact
------------------------------
For any issues or questions, feel free to contact me or open an issue in this repository.
