nume = input('Care este numele tau? ')
varsta = input('Care este varsta ta? ')
simptome = input('Ce te doare? ')
email_address = input('Scrieti adresa de email sau un numar de telefon! ')
print('Va multumesc si va doresc o zi minunata!')
import smtplib

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:


    smtp.login('pythontest598@gmail.com', 'gvlcfhfgvktgfisf')

    subject = 'Client nou'

    body = nume
    varsta = varsta
    simptome = simptome
    email_address = email_address


    msg = f'Subject: {subject} \n{body},\n{varsta},\n{simptome},\n{email_address}'



    smtp.sendmail('email_address', 'pythontest598@gmail.com', msg)
























