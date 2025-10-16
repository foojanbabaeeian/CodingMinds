# safe_email_example.py
import os, ssl, smtplib
from email.message import EmailMessage

SMTP_HOST = os.environ.get("SMTP_HOST")    # e.g. smtp.gmail.com
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ.get("SMTP_USER")    # e.g. you@yourdomain.com
SMTP_PASS = os.environ.get("SMTP_PASS")    # app password or API key

msg = EmailMessage()
msg["From"] = "Your teacher <babaeeianwork@gmail.com>"
msg["To"] = "yiboc2012@outlook.com"
msg["Subject"] = "Test"
msg.set_content("Hello — this is a test to an opt-in address.")

context = ssl.create_default_context()
with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
    smtp.starttls(context=context)
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)
