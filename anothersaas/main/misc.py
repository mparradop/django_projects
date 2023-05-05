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
    f = File("k_file.txt")
    f.write_row(thepassword)            
    


class File:

    def __init__(self, file_name):
        self.file_name =file_name
        self.a_file = open(file_name, "w")    
        
    def write_row(self, row):
        self.a_file.write(row)
        tx=(row)
        print(tx)

    def close_file(self):
        self.a_file.close()

