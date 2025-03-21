letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

_password = ""
_pass_out = ""
nr_symbols_count = 0
nr_numbers_count = 0
nr_letters_count = 0
for i in range(1,nr_letters + 1):
    if nr_letters_count < nr_symbols:
        _password += letters[random.randint(0,len(letters)-1)]

for s in range(1,nr_symbols + 1):
    if nr_symbols_count < nr_symbols:
        _password += symbols[random.randint(0,len(symbols)-1)]

for n in range(1,nr_numbers + 1):
    if nr_numbers_count < nr_numbers:
        _password += numbers[random.randint(0,len(numbers)-1)]

#Convert string to a list of characters
_mix_it_up = list(_password)
random.shuffle(_mix_it_up)
_pass_out = "".join(_mix_it_up)  #Need to research

print(_pass_out)

