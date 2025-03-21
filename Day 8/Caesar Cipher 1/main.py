from random import random
from uu import encode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_key = []
#cipher = ""
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(text_to_encrypt):
    cipher = ""
    create_cipher_key(shift)
    print(alphabet)
    print(cipher_key)
    print(f'cipher = {cipher}')
    marker = len(text_to_encrypt)
    print(f'Marker: {marker}')
    for i in text_to_encrypt:
        if i == ' ':
            cipher += " "
        else:
            cipher += cipher_key[alphabet.index(i)]
    print(f'cipher = {cipher}')

def decrypt(text_to_decrypt):
    cipher = ""
    create_cipher_key(shift)
    print(alphabet)
    print(cipher_key)
    print(f'cipher = {cipher}')
    marker = len(text_to_decrypt)
    print(f'Marker: {marker}')
    for i in text_to_decrypt:
        if i == ' ':
            cipher += " "
        else:
            cipher += alphabet[cipher_key.index(i)]
        # print(f'{i}  = {cipher_key[i]}')
    print(f'cipher = {cipher}')
def create_cipher_key(offset):
    marker =len(alphabet)
    j = 0
    for i in range(0, marker -1):
        while j + offset < marker:
            cipher_key.append(alphabet[i + offset])
            i += 1
            j += 1
    for k in range(0, offset):
        cipher_key.append(alphabet[k])
if direction.lower() == 'encode':
    encrypt(text)
else:
    decrypt(text)


# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
#Most of the code above (create_cipher_key, majority of for loop in encrypt/decrypt) could have bee replace with the
# following for loop in the encrypt/decrypt functions:
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
##ChatGPT can easily explain how it works


#Built into create_cipher_key function
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

