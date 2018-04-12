# TODO hack: not finished
# https://habrahabr.ru/post/103055/
# https://habrahabr.ru/post/221485/
import operator

ALPH_SIZE = 26
devide = "\n***********\n"


# Return info as array of letters
# without any other symbols
def only_letters(info):
    info = list(info)
    normal_info = []

    for i in range(len(info)):
        if info[i].isalpha():
            normal_info.append(info[i])

    return normal_info


# Make information shift to one character to left
def shift_left(shift):
    shift_list = shift
    shift_symbol = shift_list[0]

    for i in range(len(shift) - 1):
        shift_list[i] = shift_list[i + 1]

    shift_list[len(shift) - 1] = shift_symbol
    return shift_list


def find_best_key(length_key_array):
    analize_keys = {}

    for i in range(len(length_key_array) - 1):
        analize_keys[length_key_array[i]] = 0
        for j in range(i + 1, len(length_key_array)):
            if length_key_array[j] % length_key_array[i] == 0:
                analize_keys[length_key_array[i]] += 1

    best_key = max(analize_keys.items(), key=operator.itemgetter(1))[0]
    return best_key


def hack_key_length(encoded_info):
    result = only_letters(encoded_info)
    shift = only_letters(encoded_info)

    compare_elements = {}
    length_key_array = []
    average = 0

    for j in range(ALPH_SIZE):
        shift = shift_left(shift)
        count = 0

        for i in range(len(result)):
            if result[i] == shift[i]:
                count += 1

        compare_elements[j] = count/len(result)
        average += compare_elements[j]
        # print(compare_elements[j])

    average = average/ALPH_SIZE

    for j in range(ALPH_SIZE):
        if compare_elements[j] > average * 1.06:
            length_key_array.append(j + 1)

    # TODO: if user wants, check for other length
    print(length_key_array)
    return find_best_key(length_key_array)
