
import smtplib
#import imghdr
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Client nou'
msg['From'] = 'pythontest598@gmail.com'
msg['To'] = 'pythontest598@gmail.com'
msg.set_content('Image attached...')
#with open('Capture.JPG', 'rb') as f:
    #file_data = f.read()
    #file_type = imghdr.what(f.name)
    #file_name = f.name
# msg.add_attachment(file_data, maintype='image', subtype=file_type, filename =file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login('pythontest598@gmail.com', 'gvlcfhfgvktgfisf' )

























