# Vigenera encryption and decryption


ALPH_SIZE = 26


def encrypt_symbol(letter, key, position, start):
    encrypt_letter = (ord(letter) - start + ord(key[position % len(key)]) - 65) % ALPH_SIZE + start
    return chr(encrypt_letter)


def encrypt_vigenera(info, key):
    encrypt_position = 0
    result = ''
    for i in range(len(info)):
        if info[i].isalpha():
            if ord(info[i]) > 96:
                result += encrypt_symbol(info[i], key, encrypt_position, 97)
            else:
                result += encrypt_symbol(info[i], key, encrypt_position, 65)
            encrypt_position += 1
        else:
            result += info[i]
    return result


def decrypt_symbol(letter, key, position, start):
    encrypt_letter = (ord(letter) - start - (ord(key[position % len(key)]) - 65) + ALPH_SIZE) % ALPH_SIZE + start
    return chr(encrypt_letter)


def decrypt_vigenera(info, key):
    decrypt_position = 0
    result = ''
    for i in range(len(info)):
        if info[i].isalpha():
            if ord(info[i]) > 96:
                result += decrypt_symbol(info[i], key, decrypt_position, 97)
            else:
                result += decrypt_symbol(info[i], key, decrypt_position, 65)
            decrypt_position += 1
        else:
            result += info[i]
    return result
