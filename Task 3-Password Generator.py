import random
print("HELLO,HERE'S YOUR PASSWORD GENERATOR")
print("Let's Begin")
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "@!$%^&*#()?."

use_letters = True
use_digits = True
use_symbols = True

all_characters = ""

if use_letters:
    all_characters += letters
if use_digits:
    all_characters += digits
if use_symbols:
    all_characters += symbols 

while True:
    password_len = int(input("Enter preferable length of your password: "))
    password_count = int(input("How many passwords would you like to make: "))
    
    for _ in range(password_count):
        password = " ".join(random.sample(all_characters, password_len))
        print(password)
