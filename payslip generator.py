import pandas as pd
from fpdf import FPDF
import yagmail
import os

# Load Excel File
df = pd.read_excel("employees.xlsx")
df.columns = df.columns.str.strip()  # Clean up column names

# Standardize columns to prevent typos
df.rename(columns={
    "Employees Id": "Employee ID",
    "Allowance": "Allowances"
}, inplace=True)

# Validate Required Columns
expected_columns = ["Employee ID", "Name", "Email", "Basic Salary", "Allowances", "Deductions"]
for col in expected_columns:
    if col not in df.columns:
        raise KeyError(f"Missing column: {col}")

# Calculate Net Salary
df["Net Salary"] = df["Basic Salary"] + df["Allowances"] - df["Deductions"]

# Email Credentials
SENDER_EMAIL = "yourcompanyemail@gmail.com"     # Replace with your Gmail
SENDER_PASSWORD = "your-app-password"           # Replace with App Password

# Setup yagmail SMTP client
try:
    yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Connected to Gmail SMTP server.")
except Exception as e:
    print(f"❌ Failed to connect: {e}")
    exit()

# PDF Generator Class
class PayslipGenerator:
    def __init__(self, output_dir='payslips'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_payslip(self, employee_data):
        pdf = FPDF(format='A4')
        pdf.add_page()

        # Header
        pdf.set_fill_color(0, 0, 0)
        pdf.rect(0, 0, 210, 30, 'F')
        pdf.set_text_color(212, 175, 55)
        pdf.set_font("Arial", 'BI', 20)
        pdf.set_y(8)
        pdf.cell(0, 10, "The Chic Events", ln=True, align='C')
        pdf.set_font("Arial", 'I', 12)
        pdf.set_text_color(255, 255, 255)
        pdf.set_y(20)
        pdf.cell(0, 10, "Event Management & Planning", ln=True, align='C')

        # Employee Info
        pdf.ln(20)
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Arial", 'B', 13)
        pdf.cell(0, 10, "Employee Details", ln=True)
        pdf.set_font("Arial", '', 11)
        pdf.cell(0, 8, f"Employee ID: {employee_data['Employee ID']}", ln=True)
        pdf.cell(0, 8, f"Name: {employee_data['Name']}", ln=True)
        pdf.cell(0, 8, f"Email: {employee_data['Email']}", ln=True)

        # Salary Info
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 13)
        pdf.cell(0, 10, "Salary Breakdown", ln=True)
        pdf.set_font("Arial", '', 11)
        pdf.cell(0, 8, f"Basic Salary: ${employee_data['Basic Salary']:,.2f}", ln=True)
        pdf.cell(0, 8, f"Allowances: ${employee_data['Allowances']:,.2f}", ln=True)
        pdf.cell(0, 8, f"Deductions: ${employee_data['Deductions']:,.2f}", ln=True)

        # Net Salary Highlight
        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.set_fill_color(230, 230, 250)
        pdf.cell(0, 10, f"Net Salary: ${employee_data['Net Salary']:,.2f}", ln=True, fill=True)

        # Footer
        pdf.set_y(-25)
        pdf.set_font("Arial", 'I', 8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 6, "This payslip is computer-generated and does not require a signature.", ln=True, align='C')
        pdf.cell(0, 6, "© 2025 The Chic Events. All rights reserved.", ln=True, align='C')

        # Save PDF
        filename = f"{employee_data['Employee ID']}_payslip.pdf"
        filepath = os.path.join(self.output_dir, filename)
        pdf.output(filepath)
        return filepath

# Initialize generator
payslip_gen = PayslipGenerator()

# Generate PDFs and send emails
for _, row in df.iterrows():
    try:
        pdf_path = payslip_gen.generate_payslip(row)
        print(f"📨 Sending to {row['Email']}...")

        yag.send(
            to=row["Email"],
            subject="Your Monthly Payslip",
            contents=f"Dear {row['Name']},\n\nPlease find your payslip attached.\n\nBest regards,\nThe Chic Events HR",
            attachments=pdf_path
        )
        print(f"✅ Sent to {row['Email']}")

    except Exception as e:
        print(f"❌ Failed to send to {row['Email']}: {e}")

print("🏁 All payslips processed and sent!")
