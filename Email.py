# ---------------------------------------------------------------------------- #
#               This is a simple command line app to send emails               #
# ---------------------------------------------------------------------------- #

# ------------ Please take a look at the readme file before using ------------ #

import yagmail
import os
import re

# --------- using regular expressions to validate the email addresses -------- #

valid_email = "^[-!#$%&'*+/0-9=?A-Z^_a-z{|}~](\.?[-!#$%&'*+/0-9=?A-Z^_a-z{|}~])*@[a-zA-Z](-?[a-zA-Z0-9])*(\.[a-zA-Z](-?[a-zA-Z0-9])*)+$"
emailing = True


def check_sender():
    global sender
    global sndr
    while sndr == True:
        sender = input("Please enter your email address.\n")
        match = re.fullmatch(valid_email, sender)   
        if match is None:
            print('Please enter a valid email address.\n')
            continue
        else:
            sndr = False

def check_receiver():
    global receiver
    global rcvr
    while rcvr == True:
        receiver = input("Please enter the email address you wish to send an email to.\n")
        match = re.fullmatch(valid_email, receiver)
        if match is None:
            print('Please enter a valid email address.\n')
            continue
        else:
            rcvr = False   

if __name__ == "__main__":
    while emailing:
        sndr = True
        rcvr = True
        check_sender()
        check_receiver()

        subject = input("Please Input Subject Line:\n")

        print('Please type the contents of the message.\n You may write multiple lines.\n To finish writing please press the ENTER key again while no characters are written.\n')

        # ------- workaround to input function only allowing one line of input ------- #
        contents = []
        while True:
            line = input()
            if line == '':
                break
            else:
                contents.append(line)

        contents = '\n'.join(contents)

    # Make sure you've made an environment variable as your app password to login to your email account.
    # for more information please refer to the readme file.
        yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

        yag.send(to=receiver, subject=subject, contents=contents)

        print("Email Sent")

        another = input("Would you like to send another email? Y/N?")
        if another[0].upper() == 'Y':
            emailing = True
            continue
        else:
            print("Thanks for using my application!")
            break