
import smtplib
from email.mime.text import MIMEText
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email(recipient, subject, body):
    if not EMAIL_USER or not EMAIL_PASS:
        return "Missing email credentials"

    msg = MIMEText(body)
    msg["From"] = EMAIL_USER
    msg["To"] = recipient
    msg["Subject"] = subject

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(EMAIL_USER, recipient, msg.as_string())
    server.quit()
    return True
