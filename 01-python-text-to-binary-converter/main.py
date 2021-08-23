from math import log2

def DecimalToBinary(num, last = 0):

    if num >= 1:
        DecimalToBinary(num // 2, last)
    print(num % 2, end = '')


def to_binary(word):
    """Convert a text into a binary sequence.

    Args:
        text (string): Only a word can be translated at a time at this point(It could be improved).add()
    """
    char_lst = [i for i in set(word)]
    char_lst.sort()
    nb_char = len(char_lst)
    nb_bits = log2(nb_char).__ceil__()
    possibilities = 2**nb_bits

    print("There is {} characters in this string, so each character will be encode in {} bits \n which give us the possibility of coding {} characters.".format(nb_char, nb_bits, possibilities))

    conversion = {}
    for i, char in enumerate(char_lst):
        binary = DecimalToBinary(i)
        conversion[char] = binary
    return conversion


print(to_binary('ABRACADABRAA'))