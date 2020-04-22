import sys
from config import ALPHABET_SIZE, LOWER_FIRST_DIGIT, UPPER_FIRST_DIGIT
from utils import open_files_decorator
import string


def shift_char(char, shift):
    alphabets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits
    ]
    for alphabet in alphabets:
        if char in alphabet:
            alphabet_len = len(alphabet)
            return alphabet[(alphabet.index(char) + shift + alphabet_len) % alphabet_len]

    return char


def caesar_cipher_encrypt(input_stream, output_stream, shift, decode=False):
    if decode:
        shift *= -1

    while True:
        c = input_stream.read(1)
        if not c:
            break
        shifted_char = shift_char(c, shift)
        output_stream.write(shifted_char)


def vigenere_cipher_encrypt(input_stream, output_stream, key, decode=False):
    key = key.lower()
    key_digits = [ord(i) - ord('a') for i in key if 0 <= ord(i) - ord('a') < ALPHABET_SIZE]
    if decode:
        key_digits = list(map(lambda x: -x + ALPHABET_SIZE, key_digits))

    j = 0
    while True:
        c = input_stream.read(1)
        if not c:
            break

        shift = key_digits[j % len(key_digits)]
        output_stream.write(shift_char(c, shift))
        j += 1


def encode_decode(input_file, output_file, cipher, key, decode=False):
    available_ciphers = ['caesar', 'vigenere']

    if cipher not in available_ciphers:
        raise ValueError(
            'Cipher can be only {}'.format(' or '.join(list(map(lambda x: f'"{x}"', available_ciphers))))
        )

    if cipher == 'caesar':
        try:
            key = int(key)
            if key == 0:
                print('Warning: key is zero. The cipher is unreliable')

        except ValueError:
            raise ValueError('Key must be a number')

        caesar_cipher_encrypt(input_file, output_file, key, decode=decode)

    elif cipher == 'vigenere':
        vigenere_cipher_encrypt(input_file, output_file, key, decode=decode)
