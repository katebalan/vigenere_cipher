# Encryption and decryption for vigenere cipher
from vigenera_cipher import *
from vigenera_hack import *

# key = 'key'.upper()
# info = 'silence is not empty, it is full of answers'

key = input("Please enter key: ").upper()

with open('normal_text.txt', 'r') as text_document:
    info = text_document.read()

text_document.close()

encrypt_msg = encrypt_vigenera(info, key)

text_document = open('encrypted_text.txt', 'w')
text_document.write(encrypt_msg)
text_document.close()


with open('encrypted_text.txt', 'r') as text_document:
    info = text_document.read()

text_document.close()

decrypt_msg = decrypt_vigenera(info, key)

text_document = open('decrypted_text.txt', 'w')
text_document.write(decrypt_msg)
text_document.close()

key_length = hack_key_length(encrypt_msg)
print(key_length)
