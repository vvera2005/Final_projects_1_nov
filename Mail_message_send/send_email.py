"""This module gets some arguments and sends mail from my google account"""
import subprocess

def install_library(library_name):
    """This is to install a library"""
    try:
        subprocess.check_call(['pip', 'install', library_name])
        print(f"Successfully installed {library_name}.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {library_name}.")

try:
    import smtplib
except ModuleNotFoundError:
    install_library("smtplib")
    import smtplib

try:
    import re
except ModuleNotFoundError:
    install_library("re")
    import re

try:
    import argparse
except ModuleNotFoundError:
    install_library("argparse")
    import argparse

def get_message(subject,fn):
    """Gets the message from file"""
    with open(fn,"r",encoding="utf-8") as f:
        body = f.read()
    message = f"Subject:{subject}\n\n{body}"
    return message

def mail_valid(mail_adress):
    """Checks if mail is valid or not"""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.search(pattern, mail_adress):
        return True
    return False

def send_message(sender_mail,sender_password,receiver_mail,message):
    """sends the message"""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_mail, sender_password)
        server.sendmail(sender_mail, receiver_mail, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()



def main():
    """Main pard when everything is called"""
    parser = argparse.ArgumentParser()
    parser.add_argument("subject", type= str, help="Enter mails subject")
    parser.add_argument("reciever_mail",type = str, help="Enter a reciever email")
    args = parser.parse_args()

    sender_mail = "vera.aleksanyan.1@gmail.com"
    sender_password = "pmuyetzrjwfaoegr"
    if mail_valid(args.reciever_mail) is True:
        message = get_message(args.subject,"my_message.txt")
        send_message(sender_mail,sender_password,args.reciever_mail,message)
    else:
        print("This mail is not definted:( ")

if __name__ == "__main__":
    main()    