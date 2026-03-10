import smtplib
import time
import re
from email.mime.text import MIMEText

# Function to send OTP via email
# You'll need to specify the email account details and the SMTP server settings

def send_otp(email, otp):
    msg = MIMEText(f'Your OTP is: {otp}')
    msg['Subject'] = 'Your OTP'
    msg['From'] = 'your_email@example.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.send_message(msg)

# Function to detect OTP from Outlook inbox

def detect_otp_from_outlook(email, password):
    # This is a placeholder for the function that connects to Outlook and retrieves the OTP.
    # You would need to use a library like `pywin32` or `exchangelib` to access Outlook emails.
    pass

# Main function to run the account creation process

def main():
    while True:
        email = input('Enter email: ')
        password = input('Enter password: ')
        cookie = input('Enter cookie: ')
        send_otp(email, '123456')  # Placeholder for OTP sent
        print('Please check your email for the OTP.')
        otp = detect_otp_from_outlook(email, password)  # Retrieve OTP from Outlook
        if otp:
            print(f'OTP detected: {otp}')
            # Proceed with verification process using the detected OTP
        else:
            print('No OTP detected. Please try again.')
        time.sleep(5)  # Loop again after 5 seconds

if __name__ == '__main__':
    main()