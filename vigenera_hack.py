# TODO hack: not finished
# https://habrahabr.ru/post/103055/
# https://habrahabr.ru/post/221485/


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
    # print(info)
    # print(normal_info)
    return normal_info


# Make information shift to one character to left
def shift_left(shift):
    shift_list = shift
    shift_symbol = shift_list[0]

    for i in range(len(shift) - 1):
        shift_list[i] = shift_list[i + 1]

    shift_list[len(shift) - 1] = shift_symbol
    return shift_list


def hack_key_length(encoded_info):
    result = only_letters(encoded_info)
    shift = only_letters(encoded_info)
    compare_elements = {}
    length_key = []

    for j in range(ALPH_SIZE):
        # print(devide)
        # print(result)
        shift = shift_left(shift)
        # print("".join(shift))
        # print(shift)
        count = 0

        for i in range(len(result)):
            # print(result[i])
            # print(shift[i])
            if result[i] == shift[i]:
                count += 1
                # print(result[i])

        compare_elements[j] = count/len(result)

        print(compare_elements[j])
        if compare_elements[j] > 0.06:
            length_key.append(j + 1)

    print(length_key)


# encrypt_msg = "cmjorao mq xsr oqndc, gd mq pyjv sd krqgipc"
# # print(devide)
# hack_key_length(encrypt_msg)
