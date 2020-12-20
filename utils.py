from config import alphabets


def get_char_num(char):
    for alphabet in alphabets:
        if char in alphabet:
            return alphabet.index(char)

    return 0


def shift_char(char, shift):
    for alphabet in alphabets:
        if char in alphabet:
            alphabet_len = len(alphabet)
            return alphabet[(alphabet.index(char) + shift) % alphabet_len]

    return char
