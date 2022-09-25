from email.message import EmailMessage
from key_password import password
import ssl
import smtplib

# Go over to our gmail account and setup 2 factor authentication
# generate app password

email_sender = 'roqeebakindele@gmail.com'
email_password = password

# this should be the email of the receiver #####
email_receiver = 'abirumar@gmail.com'

# create a function to send the mail

subject = "Don't forget to subscribe"
body = '''
When you watch a video, please subscribe
'''

en = EmailMessage()
en['From'] = email_sender
en['To'] = email_receiver
en.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmaill.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, en.as_string())
