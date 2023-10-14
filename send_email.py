import smtplib
import re

def get_message():
    subject = input('Enter a subject: ')
    body = input('Enter a message: ')
    message = f"Subject: {subject}\n\n{body}"
    return message

def mail_valid(mail_adress):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(pattern, mail_adress):
        return True
    return False

def send_message(sender_mail,sender_password,reciever_mail,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_mail,sender_password)
    server.sendmail(sender_mail,reciever_mail,message)    
    

def main():
    sender_mail = "vera.aleksanyan.1@gmail.com"
    sender_password = "pmuyetzrjwfaoegr"
    reciever_mail = input("Enter an reciever mail adress: ")
    if mail_valid(reciever_mail) == True:
        message = get_message()
        send_message(sender_mail,sender_password,reciever_mail,message)
    else:
        print("This mail is not definted:( ")

main()
    
