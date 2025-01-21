# idea for future: create a guessing games with clues 

import random
# To easily check if a character is a letter, digit, or punctuation:
import string

#This all a one long string
chars = " " + string.punctuation + string.digits + string.ascii_letters
#  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

# creating a list based on our string variable
chars = list(chars)

# key = chars:
key = chars.copy()
# it will be authomaticly saved in a key list
# it will be shuffled differently each time we run a program
random.shuffle(key)

#encrypt
plain_text = input("\nEnter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original: {plain_text}")
print(f"Encrypted: {cipher_text}")

#decrypt
cipher_text = input("\nEnter a message to dencrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted: {cipher_text}")
print(f"Original: {plain_text}")

