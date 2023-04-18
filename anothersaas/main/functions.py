import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

def generate_pswd():	
    thepassword=""
    for i in range(30):
                thepassword += secrets.choice(alphabet)
    print(thepassword)
    return thepassword