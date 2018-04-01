# Encryption and decryption for vigenere cipher
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


key = 'key'.upper()
info = 'silence is not empty, it is full of answers'
devide = "\n***********\n"

encrypt_msg = encrypt_vigenera('silence is not empty, it is full of answers', key)
print(encrypt_msg)
# print(decrypt_vigenera('ACE DF?swf', key))


def shift_left(shift):
    shift_list = shift
    shift_symbol = shift_list[0]

    for i in range(len(shift) - 1):
        shift_list[i] = shift_list[i + 1]

    shift_list[len(shift) - 1] = shift_symbol
    return shift_list


def hack_key_length(encoded_info):
    result = list(encoded_info)
    shift = list(encoded_info)
    compare_elements = {}
    length_key = []

    for j in range(ALPH_SIZE):
        shift = shift_left(shift)
        print("".join(shift))

        for i in range(len(result)):
            # print(result[i])
            # print(shift[i])
            if result[i] == shift[i]:
                if compare_elements.get(j):
                    compare_elements[j] += 1
                else:
                    compare_elements[j] = 1

        print(compare_elements)
        if compare_elements[j] / len(result) > 0.06:
            length_key.append(j + 1)

    print(length_key)

print(devide)
hack_key_length(encrypt_msg)
