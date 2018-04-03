# TODO hack: not finished
# https://habrahabr.ru/post/103055/
# https://habrahabr.ru/post/221485/


ALPH_SIZE = 26


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


encrypt_msg = "cmjorao mq xsr oqndc, gd mq pyjv sd krqgipc"
devide = "\n***********\n"
print(devide)
hack_key_length(encrypt_msg)
