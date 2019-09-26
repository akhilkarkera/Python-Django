########### This file will be used to genrate random ASCII letters####################



import random # inbuild function to genrate random character
import string # Return ASCII letters



class short:

    ticket_size = 5 # Fixed varaiable set (will generate 7 charachtes of random number)

    def __init__(self,ticket_size=None):
        self.ticket_size = ticket_size if ticket_size is not None else 5

    def grant_token(self):
        letter = string.ascii_letters # string.ascii_letters inbuild function in string to generate random letter
        return ''.join(random.choice(letter)for i in range(self.ticket_size)) #generate random letter of 5 letters